+++
title = "Writing a Wordpress Restoration script"
slug = "writing-a-wordpress-restoration-script"
date = "2017-03-02T21:59:50"
draft = false
categories = ["Keith's Favorite Post", 'Misc', 'Security &amp; Privacy']
+++

WordPress sites get hacked all the time, because the typical WordPress blogger install 100's of shitty plugins and rarely updates their site. On the one hand, it's great that WordPress has empowered so many people to begin blogging without requiring the 'hard' technical skills, on the other it just gives criminals a large number of potential victims.

Two years ago, when I studied the details of phishing attacks that targeted <a href="https://www.keithrozario.com/2014/10/phishing-by-the-bank-maybank-that-is.html">Maybank</a> and <a href="https://www.keithrozario.com/2014/07/rhb-phishing-scam-details-phishing-scam.html">RHB</a>, I found that attackers use compromised WordPress sites to host their phishing content. They'd first hack into a seemingly random WordPress website, host their phishing content there, and then blast out emails to unsuspecting victims with links to pointing back to their hacked bounty. If the hack works they'd get free username and passwords, and if they were ever caught, most evidence would point to the unsuspecting Wordpress site owner.

So if you have a WordPress site (like me), chances are you're in the cross-hairs of hackers already, and securing your site is the responsible thing to do.

In general Wordpress sites should be:
<ul>
 	<li>Updated Automatically</li>
 	<li>Use a minimal number of plugins</li>
 	<li>Use plugins only from reputable publishers</li>
 	<li>Use themes only from reputable publishers--and have only one theme in the install directory</li>
 	<li>Employ strong passwords for the admin &amp; user</li>
 	<li>Have the permissions of the underlying folders set accordingly (i.e.CHMOD them all)</li>
</ul>
But even if you took all precautions to hardened your site, there's always a possibility of it getting hacked. No security is perfect, and you should look into backups--backup often and to a separate location. That way, a compromised site can be rebuilt, even if it were defaced. The last thing you want is to lose your precious design and data, because some one installed a shitty plugin over the weekend.

Today, I'll walk through a short bash script I wrote to backup (and restore) a WordPress installation from scratch. It took me quite a while to write this (partly because I have no experience with Bash scripts), but I thought it would be good to walkthrough the details of the script and what it does.

The full script is available on github <a href="https://github.com/keithrozario/WordpressRestore">here</a>, and the usage instructions will be maintained there. The write-up below describes code the first production release, linked <a href="https://github.com/keithrozario/WordpressRestore/releases/tag/Version1.0.0">here</a>, even though I've since updated the scripts to include some modifications, and as we speak I'm just about the release version 1.2.

So here we go...
<h2>Special Thanks</h2>
The following 3 folks, were greatly influential in the writing of the script, listed in no particular order. No to mention, the wonderful folks at stackoverflow that helped tremendously as well.

Thanks to <a href="https://github.com/andreafabrizi">Andrea Fabrizi</a> for the awesome <a href="https://github.com/andreafabrizi/Dropbox-Uploader">DropboxUploader script</a>
Thanks to <a href="https://gist.github.com/benkulbertis">Ben Kulbertis</a> for the awesome<a href="https://gist.github.com/benkulbertis/fff10759c2391b6618dd/"> Cloudflare update script</a>
Thanks to <a href="https://peteris.rocks">Peteris.Rocks</a> for inspiring me with his <a href="https://peteris.rocks/blog/unattended-installation-of-wordpress-on-ubuntu-server/">Unattended WordPress Installation script</a>
<h2>Pre-Requisites</h2>
As a pre-requisite to all this, I made the following decisions.

The back ups would be stored in DropBox-- Dropbox has free options (up to 2GB) and has versioning by default.All your backups are versioned and kept for 30 days (not just the latest upload, which gets destroyed if you're hit by malware). Doing this on AWS requires extra work, which I wasn't prepared to do, and AWS has no free tier for S3 storage.

Also, I use CloudFlare to maintain the DNS. It's optional of course, but I needed a DNS provider that had an API, and they were the logical choice. This allowed the script to update your DNS as well.

Finally, the script assumes a standard LAMP stack, i.e. <strong>L</strong>inux (specifically Ubuntu 16.04), <strong>A</strong>pache , <strong>M</strong>ySql and <strong>P</strong>HP. PHP is enforced by Wordpress itself so that's fine.But the 'trend' these days is to have NGINX instead of Apache, and MariaDB instead of MySQL. I kept things in 'classic' mode for now, I may revisit in the future.<!--more-->
<h2>High level setup</h2>
The entire thing (both backup and restore) runs on Bash scripts. There are 5 .sh files, 3 of which are core :
<ul>
 	<li><strong>setup.sh</strong> - first time initialization of the scripts (use this for a site that already has Wordpress installed)</li>
 	<li><strong>backupWP.sh</strong> - backs up the Wordpress Installation (called from a cronjob)</li>
 	<li><strong>restoreWP.sh</strong> - restores Wordpress Installation on a blank machine</li>
</ul>
The remaining 2 non-core files:
<ul>
 	<li><strong>cloudflare.sh</strong> - updates Cloudflare DNS entry</li>
 	<li><strong>functions.sh</strong> - common functions between 3 core files</li>
</ul>
Non-core files are only called from the core scripts, and are used to keep common functions in a single re-usable location.
<h2><span style="text-decoration: underline;">File 1: Setup.sh</span></h2>
Setup.sh takes in 4 command line arguments as defined in the <a href="https://github.com/keithrozario/WordpressRestore/blob/master/README.md">README.md</a> file. I won't repeat here. Once all the usual command-line parameter parsing is done, we get into the meat of things.
<h3>Section 1: Download DropboxUploader</h3>
<a href="https://github.com/andreafabrizi/Dropbox-Uploader">DropboxUploader</a> is a fantastic piece of code that enables upload/download to Dropbox via command line. The first line of my code downloads it and sets it up according.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Download DropboxUploader and Setup</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
GetDropboxUploader <span style="color: #19177c;">$DROPBOXTOKEN</span> <span style="color: #408080; font-style: italic;">#in functions.sh</span>
</pre>
</div>
<h3>Section 2: Setup wpsettings File</h3>
The<em> .wpsettings</em> file is an important configuration file created by the script to store values for future use. Since the back up script should run everyday without user intervention, we need to store the configuration parameters for this setup somewhere on disk, and I used a file called <em>.wpsettings</em> stored in the user folder.

To maintain idempotency, the script first checks for any old <em>.wpsettings</em> file and deletes them before starting. You'll see this often throughout the script to ensure that I can run the script over and over again without any worries.

Once done, I create a <em>.wpsettings</em> file from scratch that stores:
<ul>
 	<li>WPDIR : The WordPress installation directory</li>
 	<li>WPCONFDIR: The Wordpress configuration Directory (the wp-config.php file can be stored somewhere else)</li>
 	<li>DROPBOXPATH: The Path for the DropBoxUploader.</li>
</ul>
The script also creates a an .enckey file, that stores the encryption key. All uploads to dropbox are encrypted before transmission (for added security), and obviously the encrypted key shouldn't be uploaded to Dropbox. This way, even if your Dropbox is compromised, the backup wordpress files have a separate layer of protection afforded by AES-256 encryption.

When you wish to restore you'll need the provide the encryption key to the restoration script.I created the full call (including the encryption key as a command-line argument) and stored it in Lastpass under my encrypted notes. That way, I can simply spin up an instance of Ubuntu on any cloud provider, and run a few lines of code I copied from Lastpass to restore my site.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Setup .wpsettings file</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -f <span style="color: #ba2121;">"$WPSETTINGSFILE"</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"Deleting old $WPSETTINGSFILE (probably from previous installation)"</span>
rm <span style="color: #19177c;">$WPSETTINGSFILE</span>
<span style="color: #008000; font-weight: bold;">fi</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WPDIR=$WPDIR"</span> &gt;&gt; <span style="color: #19177c;">$WPSETTINGSFILE</span> <span style="color: #408080; font-style: italic;">#store wordpress directory in config file</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WPCONFDIR=$WPCONFDIR"</span> &gt;&gt; <span style="color: #19177c;">$WPSETTINGSFILE</span> <span style="color: #408080; font-style: italic;">#store wordpress config (wp-config.php) directory in config file</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"DROPBOXPATH=$DROPBOXPATH"</span> &gt;&gt; <span style="color: #19177c;">$WPSETTINGSFILE</span> <span style="color: #408080; font-style: italic;">#store dropbox uploader path in directory</span>

SetEncKey <span style="color: #19177c;">$ENCKEY</span> <span style="color: #408080; font-style: italic;">#in functions.sh</span>
</pre>
</div>
<h3>Section 3: Setup CRON job</h3>
At the end, a Cronjob is created to ensure backupWP.sh runs are a specified time everyday. For more info on these functions look into functions.sh for SetCronJob
<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Download Backup Script and create CRON job</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>

SetCronJob <span style="color: #408080; font-style: italic;">#in functions.sh</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"Setup Complete"</span>
</pre>
</div>
<h2><span style="text-decoration: underline;">File 2: backupWP.sh</span></h2>
backupWP.sh doesn't take in any command line arguments (how could it? it runs automatically everyday)
<h3>Section 1: Delete previous backups</h3>
To ensure everything is idempotent, again we have check if the backup directory exist. If it does, we delete it and create a new one, ensuring we have a nice and empty backup folder to store our <strong>new</strong> backups in.
<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Download Backup Script and create CRON job</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>

SetCronJob <span style="color: #408080; font-style: italic;">#in functions.sh</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"Setup Complete"</span>
</pre>
</div>
<h3>Section 2: Backup DB</h3>
The following section grabs the data from wp-config.php to access the database. And then makes a .sql backup of the database. Reading the database parameters from the wp-config.php file ensures that I don't have to store the database credentials anywhere else.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># mysqldump the MYSQL Database</span>
<span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n######### Backing Up Mysql Database BEGIN #########\\n"</span>

<span style="color: #19177c;">WPDBNAME</span><span style="color: #666666;">=</span><span style="color: #ba2121;">`</span>cat <span style="color: #19177c;">$WPCONFDIR</span>/wp-config.php | grep DB_NAME | cut -d <span style="color: #bb6622; font-weight: bold;">\'</span> -f 4<span style="color: #ba2121;">`</span>
<span style="color: #19177c;">WPDBUSER</span><span style="color: #666666;">=</span><span style="color: #ba2121;">`</span>cat <span style="color: #19177c;">$WPCONFDIR</span>/wp-config.php | grep DB_USER | cut -d <span style="color: #bb6622; font-weight: bold;">\'</span> -f 4<span style="color: #ba2121;">`</span>
<span style="color: #19177c;">WPDBPASS</span><span style="color: #666666;">=</span><span style="color: #ba2121;">`</span>cat <span style="color: #19177c;">$WPCONFDIR</span>/wp-config.php | grep DB_PASSWORD | cut -d <span style="color: #bb6622; font-weight: bold;">\'</span> -f 4<span style="color: #ba2121;">`</span>

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -z <span style="color: #19177c;">$WPDBNAME</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
    <span style="color: #008000;">echo</span> <span style="color: #ba2121;">"ERROR: unable to extract DB NAME from $WPCONFDIR/wp-config.php"</span>
    <span style="color: #008000;">exit </span>0
<span style="color: #008000; font-weight: bold;">else</span>
    <span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Dumping MYSQL Files"</span>
    mysqldump -u <span style="color: #19177c;">$WPDBUSER</span> -p<span style="color: #19177c;">$WPDBPASS</span> <span style="color: #19177c;">$WPDBNAME</span> | sudo tee <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPSQLFILE</span> &gt; /dev/null
    <span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: MYSQL successfully backed up to $BACKUPPATH/$WPSQLFILE"</span>
<span style="color: #008000; font-weight: bold;">fi</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n#########    END    #########\\n"</span>
</pre>
</div>
<h3>Section 3: Zip WordPress &amp; Apache Directory</h3>
A separate assumption is that Wordpress is installed with Apache, and this part of the script creates two zip files, one for the WordPress installation, and another for the Apache configuration (typically /etc/apache2).

This allows us to copy over SSL certs and apache configuration to restore, on the fly. Later on the script, we grab data from letsencrypt (if it exist).

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Zip $WPDIR folder</span>
<span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n######### Zipping Wordpress BEGIN #########\\n"</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Zipping the $WPDIR to : $BACKUPPATH/$WPZIPFILE"</span>
sudo tar -czf <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPZIPFILE</span> -C <span style="color: #19177c;">$WPDIR</span> . <span style="color: #408080; font-style: italic;">#turn off verbose and don't keep directory structure</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: $WPDIR successfully zipped to $BACKUPPATH/$WPZIPFILE"</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n#########    END    #########\\n"</span>
<span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Copy all Apache Configurations files</span>
<span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n######### Zipping APACHE BEGIN #########\\n"</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Zipping $APACHEDIR"</span>
sudo tar -czf <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$APACHECONFIG</span> -C <span style="color: #19177c;">$APACHEDIR</span> . <span style="color: #408080; font-style: italic;">#turn off verbose and don't keep directory structure</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: $APACHEDIR successfully zipped to $BACKUPPATH/$WPZIPFILE"</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n#########    END    #########\\n"</span>
</pre>
</div>
<h3>Section 4: Encrypt backup files and remove unencrypted ones</h3>
Before uploading to Dropbox, we need to encrypt the files (for security purposes) and delete the unencrypted ones, so that they're not lying around.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Encrypting files before uploading</span>
<span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n######### Encrypting files BEGIN #########\\n"</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"INFO: Encrypting MYSQL FIles"</span>
sudo openssl enc -aes-256-cbc -in <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPSQLFILE</span> -out <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPSQLFILE</span>.enc -k <span style="color: #19177c;">$ENCKEY</span>
sudo rm <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPSQLFILE</span> <span style="color: #408080; font-style: italic;">#remove unencrypted file</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"INFO: Encrypting Wordpress Backup file:"</span>
sudo openssl enc -aes-256-cbc -in <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPZIPFILE</span> -out <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPZIPFILE</span>.enc -k <span style="color: #19177c;">$ENCKEY</span>
sudo rm <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPZIPFILE</span> <span style="color: #408080; font-style: italic;">#remove unencrypted file</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"INFO: Encrypting Apache Configuration"</span>
sudo openssl enc -aes-256-cbc -in <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$APACHECONFIG</span> -out <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$APACHECONFIG</span>.enc -k <span style="color: #19177c;">$ENCKEY</span>
sudo rm <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$APACHECONFIG</span> <span style="color: #408080; font-style: italic;">#remove unencrypted file</span>



<span style="color: #408080; font-style: italic;"># Encrypt wp-config.php file</span>
<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #ba2121;">"$WPCONFDIR"</span> !<span style="color: #666666;">=</span> <span style="color: #ba2121;">"$WPDIR"</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span> <span style="color: #408080; font-style: italic;">#already copied, don't proceed</span>
    <span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Encrypting wp-config.php file in $WPCONFDIR"</span>   
    sudo openssl enc -aes-256-cbc -in <span style="color: #19177c;">$WPCONFDIR</span>/<span style="color: #19177c;">$WPCONFIGFILE</span> -out <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPCONFIGFILE</span>.enc -k <span style="color: #19177c;">$ENCKEY</span>
<span style="color: #008000; font-weight: bold;">else</span>
    <span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: wp-config.php file is in the wordpress directory, no separate zipping necessary"</span>
<span style="color: #008000; font-weight: bold;">fi</span>

sudo openssl enc -aes-256-cbc -in <span style="color: #19177c;">$WPSETTINGSFILE</span> -out <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPSETTINGSFILENAME</span>.enc -k <span style="color: #19177c;">$ENCKEY</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"WARNING: The encryption key in $ENCKEYFILE will not be uploaded to Dropbox"</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"WARNING: Store $ENCKEYFILE in a safe place"</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n#########    END    #########\\n"</span>
</pre>
</div>
<h3>Section 5: Upload to Dropbox</h3>
Finally we use dropbox_uploader.sh (which was downloaded during setup.sh), to upload the files into Dropbox.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Upload to Dropbox</span>
<span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n######### Upload to Dropbox BEGIN #########\\n"</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"INFO: Uploading Files to Dropbox"</span>
sudo <span style="color: #19177c;">$DROPBOXPATH</span>/dropbox_uploader.sh upload <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPSQLFILE</span>.enc /
sudo <span style="color: #19177c;">$DROPBOXPATH</span>/dropbox_uploader.sh upload <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPZIPFILE</span>.enc /
sudo <span style="color: #19177c;">$DROPBOXPATH</span>/dropbox_uploader.sh upload <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$APACHECONFIG</span>.enc /
<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #ba2121;">"$WPCONFDIR"</span> !<span style="color: #666666;">=</span> <span style="color: #ba2121;">"$WPDIR"</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span> <span style="color: #408080; font-style: italic;">#already copied, don't proceed</span>
    sudo <span style="color: #19177c;">$DROPBOXPATH</span>/dropbox_uploader.sh upload <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPCONFIGFILE</span>.enc /
<span style="color: #008000; font-weight: bold;">fi</span>
sudo <span style="color: #19177c;">$DROPBOXPATH</span>/dropbox_uploader.sh upload <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$WPSETTINGSFILENAME</span>.enc /

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n#########    END    #########\\n"</span>
</pre>
</div>
<h3>Section 6: Letsencrypt</h3>
As you can tell, this was a last-minute bolt-on. If you used Letsencrypt to generate your certificates, this part of the script copies across the letsencryt configuration and files to be restored later on.

You might be wondering--why back this up at all? Why not just run letsencrypt during the restoration process, and you'd be right. But as I said, this was a last-minute bolt-on.

Letsencrypt only works if your domain already resolves to the new server. During restoration, you might find yourself waiting 24 hours before the new DNS entry propagates across the internet.--hence copying over letsencrypt gives you the opportunity you set server even before the resolution has been fixed.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Lets Encrypt</span>
<span style="color: #408080; font-style: italic;">#-------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n######### LetsEncrypt BEGIN #########\\n"</span>
<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -d <span style="color: #19177c;">$LETSENCRYPTDIR</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
    <span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"INFO: LetsEncrypt detected, backing up files"</span>
    sudo tar -czf <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$LETSENCRYPTCONFIG</span> -C <span style="color: #19177c;">$LETSENCRYPTDIR</span> .
    <span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"INFO: Encrypting Letsencrypt Configuration"</span>
    sudo openssl enc -aes-256-cbc -in <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$LETSENCRYPTCONFIG</span> -out <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$LETSENCRYPTCONFIG</span>.enc -k <span style="color: #19177c;">$ENCKEY</span>
    sudo rm <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$LETSENCRYPTCONFIG</span> <span style="color: #408080; font-style: italic;">#remove unencrypted file</span>
    <span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"INFO: Uploading Letsencrypt to Dropbox"</span>
    sudo <span style="color: #19177c;">$DROPBOXPATH</span>/dropbox_uploader.sh upload <span style="color: #19177c;">$BACKUPPATH</span>/<span style="color: #19177c;">$LETSENCRYPTCONFIG</span>.enc /
<span style="color: #008000; font-weight: bold;">else</span>
    <span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"LetsEncrypt not found"</span>
<span style="color: #008000; font-weight: bold;">fi</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n#########    END    #########\\n"</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n#########    SCRIPT END    #########\\n"</span>
</pre>
</div>
 
<h2><span style="text-decoration: underline;">File 3: restoreWP.sh</span></h2>
Easily the most complex of the 3 core files is restoreWP.sh. This script is meant to run on a bare Ubuntu 16.04 box, and will build the WordPress Installation from scratch, specifically:
<ul>
 	<li>Update Cloudflare DNS entry to point to the new server (optional)</li>
 	<li>Download the backup files from Dropbox</li>
 	<li>Restore Wordpress files (preserving directory &amp; configuration..passwords etc)</li>
 	<li>Download necessary packages for MySQL</li>
 	<li>Restore Wordpress Database (preserving username, password, db name..etc)</li>
 	<li>Download all necessary packages Apache &amp; PHP</li>
 	<li>Restore Apache configuration (optional) or; Build Apache configuration from scratch</li>
 	<li>Setup backup script (to continue backing up to cloud)</li>
 	<li>Setup a swapfile configuration (1GB)</li>
 	<li>Setup firewall rules for Ubuntu (ports 22,80,443 only)</li>
 	<li>Restore letsencrypt configuration from backup or; Call letsencrypt to get certificates or</li>
</ul>
Everything here has an order for a reason.
<ul>
 	<li>Cloudflare 'should' got first, because DNS propagation takes time. Placing it first is just logical.</li>
 	<li>Download the files from Dropbox before installing packages, because if downloads aren't available, end script now</li>
 	<li>We restore wordpress first, because we need the DB parameters from wp-config file to setup DB</li>
 	<li>Setup DB according to user,database name and password set in previous WP configuration</li>
 	<li>Finally we restore Apache last, because it's the most complicated</li>
 	<li>Once there, we setup backup, swapfile and firewall</li>
 	<li>Only then call letsencrypt because letsencrypt is the only interactive portion
<ul>
 	<li>I chose to use standard letsencrypt call which is interactive (Certbot)</li>
 	<li>but it means I'm not maintaining a custom script for this...more sustainable</li>
</ul>
</li>
</ul>
<h3>Section 0: Main Initialization</h3>
<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Main-Initilization</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### REPO UPDATE #########\\n\\n"</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Updating REPO"</span>
sudo apt-get update &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
<span style="color: #408080; font-style: italic;">#we will upgrade after deletion of unwanted packages</span>
<span style="color: #008000;">export </span><span style="color: #19177c;">DEBIAN_FRONTEND</span><span style="color: #666666;">=</span>noninteractive <span style="color: #408080; font-style: italic;">#Silence all interactions</span>
</pre>
</div>
<h3>Section 1: Update Cloudflare DNS entry</h3>
A quick update on Cloudflare, I placed it at the beginning simply because DNS updates take time to propogate, so putting it upfront seemed to make sense.

What makes less sense though, is that if the script fails later on, the DNS has already been updated. That's a risk worth taking. If you really are worried don't supply the cloudflare credentials and the DNS update won't occur.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># DNS Update with Cloudflare - (done first because it takes time to propagate)</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### CLOUDFLARE UPDATE #########\\n\\n"</span>

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #ba2121;">"$DNSUPDATE"</span> <span style="color: #666666;">=</span> <span style="color: #008000;">true</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
	
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Updating cloudflare record $CFRECORD in zone $CFZONE using credentials $CFEMAIL , $CFKEY "</span>
	./cloudflare.sh --email <span style="color: #19177c;">$CFEMAIL</span> --key <span style="color: #19177c;">$CFKEY</span> --zone <span style="color: #19177c;">$CFZONE</span> --record <span style="color: #19177c;">$CFRECORD</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Removing Cloudflare script"</span>
	rm cloudflare.sh <span style="color: #408080; font-style: italic;">#you only need it once</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: Cloudflare update complete"</span>
	
<span style="color: #008000; font-weight: bold;">else</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WARNING: DNS wasn't updated"</span>
<span style="color: #008000; font-weight: bold;">fi</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### CLOUDFLARE UPDATE END#########"</span>
</pre>
</div>
<h3>Section 2: Remove Previous Installations (Idempotent)</h3>
Just to make sure the server is a blank Ubuntu, we uninstall all the stuff we'll install later on.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Remove previous installations if necessary</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Attempting to delete older packages if they exist -- idempotency"</span>
sudo apt-get --purge -y remove mysql* &gt;&gt;<span style="color: #19177c;">$LOGFILE</span> <span style="color: #408080; font-style: italic;">#remove all mysql packages</span>
sudo apt-get --purge -y remove apache2 &gt;&gt;<span style="color: #19177c;">$LOGFILE</span> 
sudo apt-get --purge -y remove php &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get --purge -y remove libapache2-mod-php &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get --purge -y remove php-mcrypt &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get --purge -y remove php-mysql &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get --purge -y remove python-letsencrypt-apache &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>

sudo apt-get -y autoremove &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get -y autoclean &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Upgrading installed packages"</span> <span style="color: #408080; font-style: italic;">#do this after deletion to avoid upgrading packages set for deletion</span>
<span style="color: #408080; font-style: italic;">#sudo apt-get upgrade &gt;&gt;$LOGFILE #Disabled for now</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### REPO UPDATE COMPLETE #########\\n\\n"</span>
</pre>
</div>
<h3>Section 3: Download files from Dropbox</h3>
Setup DropboxUploader, and then download the backup files from Dropbox.

$WPSETTINGSFILE is downloaded first, because it contains the basic wordpress configuration information, which will be useful later on. You'll notice I use openssl to decrypt the files, because by default all files are encrypted to before being uploaded to Dropbox as part of the backup script.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;">#Setup DropboxUploader</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Downloading from Dropbox #########\\n\\n"</span>

GetDropboxUploader <span style="color: #19177c;">$DROPBOXTOKEN</span> <span style="color: #408080; font-style: italic;">#in functions.sh</span>

<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;">#Download .wpsettings file</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
delFile <span style="color: #19177c;">$WPSETTINGSFILE</span>
delFile <span style="color: #19177c;">$WPSETTINGSFILEDIR</span>/<span style="color: #19177c;">$WPSETTINGSFILE</span> <span style="color: #408080; font-style: italic;">#remove old wpsettings file (if exists)--functions.sh</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Checking if $WPSETTINGSFILE exist on Dropbox"</span>
sudo /var/Dropbox-Uploader/dropbox_uploader.sh download /<span style="color: #19177c;">$WPSETTINGSFILE</span>.enc <span style="color: #408080; font-style: italic;">#wpsettings file</span>

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -f <span style="color: #19177c;">$WPSETTINGSFILE</span>.enc <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: $WPSETTINGSFILE exist, decrypting and loading"</span>
	sudo openssl enc -aes-256-cbc -d -in <span style="color: #19177c;">$WPSETTINGSFILE</span>.enc -out <span style="color: #19177c;">$WPSETTINGSFILEDIR</span>/<span style="color: #19177c;">$WPSETTINGSFILE</span> -k <span style="color: #19177c;">$ENCKEY</span> 
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Loading $WPSETTINGSFILE"</span>
	<span style="color: #008000;">source</span> <span style="color: #ba2121;">"$WPSETTINGSFILEDIR/$WPSETTINGSFILE"</span> 2&gt;/dev/null <span style="color: #408080; font-style: italic;">#file exist, load variables</span>
<span style="color: #008000; font-weight: bold;">else </span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"ERROR: unable to find $WPSETTINGSFILE, check dropbox location to see if the file exists"</span>
	<span style="color: #008000;">exit </span>0
<span style="color: #008000; font-weight: bold;">fi</span>


<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;">#Download files from dropbox</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
delFile <span style="color: #19177c;">$WPSQLFILE</span> <span style="color: #408080; font-style: italic;">#delete files if it exist, functions.sh</span>
delFile <span style="color: #19177c;">$WPZIPFILE</span>
delFile <span style="color: #19177c;">$APACHECONFIG</span>
delFile <span style="color: #19177c;">$LETSENCRYPTCONFIG</span>
delFile <span style="color: #19177c;">$WPCONFIGFILE</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Downloading and decrypting SQL backup file"</span>
sudo /var/Dropbox-Uploader/dropbox_uploader.sh download /<span style="color: #19177c;">$WPSQLFILE</span>.enc <span style="color: #408080; font-style: italic;">#Wordpress.sql file</span>
sudo openssl enc -aes-256-cbc -d -in <span style="color: #19177c;">$WPSQLFILE</span>.enc -out <span style="color: #19177c;">$WPSQLFILE</span> -k <span style="color: #19177c;">$ENCKEY</span> 

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Downloading and decrypting Wordpress zip file"</span>
sudo /var/Dropbox-Uploader/dropbox_uploader.sh download /<span style="color: #19177c;">$WPZIPFILE</span>.enc <span style="color: #408080; font-style: italic;">#zip file with all wordpress contents</span>
sudo openssl enc -aes-256-cbc -d -in <span style="color: #19177c;">$WPZIPFILE</span>.enc -out <span style="color: #19177c;">$WPZIPFILE</span> -k <span style="color: #19177c;">$ENCKEY</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Downloading and decrypting Apache configuration"</span>
sudo /var/Dropbox-Uploader/dropbox_uploader.sh download /<span style="color: #19177c;">$APACHECONFIG</span>.enc <span style="color: #408080; font-style: italic;">#zip file with all wordpress contents</span>
sudo openssl enc -aes-256-cbc -d -in <span style="color: #19177c;">$APACHECONFIG</span>.enc -out <span style="color: #19177c;">$APACHECONFIG</span> -k <span style="color: #19177c;">$ENCKEY</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Downloading and decrypting LetsEncrypt configuration"</span>
sudo /var/Dropbox-Uploader/dropbox_uploader.sh download /<span style="color: #19177c;">$LETSENCRYPTCONFIG</span>.enc <span style="color: #408080; font-style: italic;">#zip file with all wordpress contents</span>
<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -f <span style="color: #19177c;">$LETSENCRYPTCONFIG</span>.enc <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
	sudo openssl enc -aes-256-cbc -d -in <span style="color: #19177c;">$LETSENCRYPTCONFIG</span>.enc -out <span style="color: #19177c;">$LETSENCRYPTCONFIG</span> -k <span style="color: #19177c;">$ENCKEY</span>
<span style="color: #008000; font-weight: bold;">else</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WARNING: Letsencrypt.tar not found"</span>
<span style="color: #008000; font-weight: bold;">fi</span>

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #ba2121;">"$WPDIR"</span> <span style="color: #666666;">=</span> <span style="color: #ba2121;">"$WPCONFDIR"</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: wp-config is in $WPZIPFILE, no further downloads required"</span>
<span style="color: #008000; font-weight: bold;">else</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: wp-config is a separate file, downloading $WPCONFIGFILE from Dropbox"</span>
	sudo /var/Dropbox-Uploader/dropbox_uploader.sh download /<span style="color: #19177c;">$WPCONFIGFILE</span>.enc <span style="color: #408080; font-style: italic;">#encrypted Wp-config.php file</span>
	sudo openssl enc -aes-256-cbc -d -in <span style="color: #19177c;">$WPCONFIGFILE</span>.enc -out <span style="color: #19177c;">$WPCONFIGFILE</span> -k <span style="color: #19177c;">$ENCKEY</span>
<span style="color: #008000; font-weight: bold;">fi</span>

sudo rm *.enc <span style="color: #408080; font-style: italic;">#remove encrypted files after decryption</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Downloaded backup files from Dropbox #########\\n\\n"</span>
</pre>
</div>
<h3>Section 4: Restore Wordpress files</h3>
Extract the Wordpress files into the $WPDIR, which is a variable extracted from the $WPSETTINGSFILE earlier.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Extracting Wordpress Files</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Extracting Wordpress Files #########\\n\\n"</span>

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -d <span style="color: #19177c;">$WPDIR</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WARNING: Removing older version of $WPDIR"</span>
	sudo rm -r <span style="color: #19177c;">$WPDIR</span> <span style="color: #408080; font-style: italic;">#remove current directory (to avoid conflicts)</span>
<span style="color: #008000; font-weight: bold;">else </span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: $WPDIR not found, proceeding to extraction"</span>
<span style="color: #008000; font-weight: bold;">fi</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Extracting $WPDIR"</span>
sudo mkdir -p <span style="color: #19177c;">$WPDIR</span>
sudo tar -xzf <span style="color: #19177c;">$WPZIPFILE</span> -C <span style="color: #19177c;">$WPDIR</span> .

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #ba2121;">"$WPDIR"</span> <span style="color: #666666;">=</span> <span style="color: #ba2121;">"$WPCONFDIR"</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: wp-config file is part of $WPDIR, no further action required"</span>
<span style="color: #008000; font-weight: bold;">else</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: wp-config is a separate file, moving it to $WPCONFDIR"</span>
	sudo mv <span style="color: #19177c;">$WPCONFIGFILE</span> <span style="color: #19177c;">$WPCONFDIR</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: wp-config file moved to $WPCONFDIR"</span>
<span style="color: #008000; font-weight: bold;">fi</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: Wordpress Files extracted"</span>
</pre>
</div>
<h3>Section 5: Download packages for MySQL &amp; Restore database</h3>
Extract Wordpress configuration (database user, database name, database password) from wp-config.php, and then restore the DB based on those variables.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Get DB Parameters from wp-config.php</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Obtaining configuration parameters from wp-config.php"</span>

<span style="color: #19177c;">WPDBNAME</span><span style="color: #666666;">=</span><span style="color: #ba2121;">`</span>cat <span style="color: #19177c;">$WPCONFDIR</span>/<span style="color: #19177c;">$WPCONFIGFILE</span> | grep DB_NAME | cut -d <span style="color: #bb6622; font-weight: bold;">\'</span> -f 4<span style="color: #ba2121;">`</span>
<span style="color: #19177c;">WPDBUSER</span><span style="color: #666666;">=</span><span style="color: #ba2121;">`</span>cat <span style="color: #19177c;">$WPCONFDIR</span>/<span style="color: #19177c;">$WPCONFIGFILE</span> | grep DB_USER | cut -d <span style="color: #bb6622; font-weight: bold;">\'</span> -f 4<span style="color: #ba2121;">`</span>
<span style="color: #19177c;">WPDBPASS</span><span style="color: #666666;">=</span><span style="color: #ba2121;">`</span>cat <span style="color: #19177c;">$WPCONFDIR</span>/<span style="color: #19177c;">$WPCONFIGFILE</span> | grep DB_PASSWORD | cut -d <span style="color: #bb6622; font-weight: bold;">\'</span> -f 4<span style="color: #ba2121;">`</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Wordpress Extractiong Complete #########\\n\\n"</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Install MySQL and Dependencies</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Installing mysql Server #########\\n\\n"</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Installing mysql-server"</span>
sudo -E apt-get -q -y install mysql-server &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>  <span style="color: #408080; font-style: italic;">#non-interactive mysql installation</span>

<span style="color: #408080; font-style: italic;">#Some security cleaning up on mysql-----------------------------------------------------</span>
sudo mysql -u root -e <span style="color: #ba2121;">"DELETE FROM mysql.user WHERE User='';"</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Setting password for root user to $DBPASS"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"UPDATE mysql.user SET authentication_string=PASSWORD('$DBPASS') WHERE User='root';"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"DROP DATABASE IF EXISTS test;"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"FLUSH PRIVILEGES;"</span>

<span style="color: #408080; font-style: italic;">#Create DB for Wordpress with user------------------------------------------------------</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Creating Database with name $WPDBNAME"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"CREATE DATABASE IF NOT EXISTS $WPDBNAME;"</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Granting Permission to $WPDBUSER with password: $WPDBPASS"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"GRANT ALL ON *.* TO '$WPDBUSER'@'localhost' IDENTIFIED BY '$WPDBPASS';"</span>
sudo mysql -u root -e <span style="color: #ba2121;">"FLUSH PRIVILEGES;"</span>

<span style="color: #408080; font-style: italic;">#Setup permission for my.cnf propery----------------------------------------------------</span>
sudo chmod 644 /etc/mysql/my.cnf

<span style="color: #408080; font-style: italic;">#Extract mysqlfiles---------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Loading $WPSQLFILE into database $WPDBNAME"</span>
sudo mysql <span style="color: #19177c;">$WPDBNAME</span> &lt; <span style="color: #19177c;">$WPSQLFILE</span> -u <span style="color: #19177c;">$WPDBUSER</span> -p<span style="color: #19177c;">$WPDBPASS</span> <span style="color: #408080; font-style: italic;">#load .sql file into newly created DB</span>

<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### MYSQL Server Installed #########\\n\\n"</span>
</pre>
</div>
<h3>Section 6: Apache Configuration</h3>
Restore Apache, with 2 options:
<ul>
 	<li>$APRESTORE=1 : Restore apache configuration from backup files</li>
 	<li>$APRESTORE is empty: Script default Apache configuration based on wordpress directory. In this setting no further security is set for apache, you'll have to modify manually later on.</li>
</ul>
<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Basic Apache and PHP Installations</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Installing APACHE &amp; PHP #########\\n\\n"</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Installing Apache2"</span>
sudo apt-get -y install apache2 &gt;&gt;<span style="color: #19177c;">$LOGFILE</span> <span style="color: #408080; font-style: italic;">#non-interactive apache2 install</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: Apache Installed"</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Installing PHP and libapache2-mod-php"</span>
sudo apt-get -y install php &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get -y install libapache2-mod-php &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get -y install php-mcrypt &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
sudo apt-get -y install php-mysql &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: PHP Installed"</span>

<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Loading Apache Configurations</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Stopping Apache Service to load configurations"</span>
sudo service apache2 stop

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #19177c;">$APRESTORE</span> <span style="color: #666666;">=</span> 1 <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>

	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Removing configurations file--to prevent conflicts"</span>
	delDir <span style="color: #19177c;">$APACHEDIR</span>
	sudo mkdir -p <span style="color: #19177c;">$APACHEDIR</span>
	sudo tar -xzf <span style="color: #19177c;">$APACHECONFIG</span> -C <span style="color: #19177c;">$APACHEDIR</span> .

<span style="color: #008000; font-weight: bold;">else</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Setting up Apache default values"</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"### WARNING: Apache config files will not be secured ###"</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"### Consider modifying the config files post-install ###"</span>
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Copying 000-default config for $DOMAIN.conf"</span>
	sudo cp <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DEFAULTAPACHECONF</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#create a temporary Apache Configuration</span>
	
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Updating $DOMAIN.conf"</span>	
	sudo sed -i <span style="color: #ba2121;">"/ServerAdmin*/aServerName $DOMAIN"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#insert ServerName setting</span>
	sudo sed -i <span style="color: #ba2121;">"/ServerAdmin*/aServerAlias $DOMAIN"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#insert ServerAlias setting</span>
	sudo sed -i <span style="color: #ba2121;">"s|\("</span>DocumentRoot<span style="color: #ba2121;">" * *\).*|\1$WPDIR|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#change DocumentRoot to $WPDIR</span>
	sudo sed -i <span style="color: #ba2121;">"/DocumentRoot*/a&lt;Directory $WPDIR&gt;\nAllowOverride All\nOrder allow,deny\nallow from all\n&lt;/Directory&gt;"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf
	sudo sed -i <span style="color: #ba2121;">"/ServerAdmin*/aServerAlias $DOMAIN"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#insert ServerAlias setting</span>
	
	<span style="color: #408080; font-style: italic;">#Format $DOMAIN.conf file</span>
	sudo sed -i <span style="color: #ba2121;">"s|\(^ServerName*\)|$EIGHTSPACES\1|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#tab-ing</span>
	sudo sed -i <span style="color: #ba2121;">"s|\(^ServerAlias*\)|$EIGHTSPACES\1|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#tab-ing</span>
	sudo sed -i <span style="color: #ba2121;">"s|\(^&lt;Directory*\)|$EIGHTSPACES\1|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#tab-ing</span>
	sudo sed -i <span style="color: #ba2121;">"s|\(^AllowOverride*\)|$EIGHTSPACES\1|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#tab-ing</span>
	sudo sed -i <span style="color: #ba2121;">"s|\(^Order*\)|$EIGHTSPACES\1|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#tab-ing</span>
	sudo sed -i <span style="color: #ba2121;">"s|\(^allow*\)|$EIGHTSPACES\1|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#tab-ing</span>
	sudo sed -i <span style="color: #ba2121;">"s|\(^&lt;/Directory*\)|$EIGHTSPACES\1|"</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#tab-ing</span>
	sudo sed -i <span style="color: #ba2121;">'/#.*/ d'</span> <span style="color: #19177c;">$SITESAVAILABLEDIR</span>/<span style="color: #19177c;">$DOMAIN</span>.conf <span style="color: #408080; font-style: italic;">#remove all comments in file (nice &amp; clean!)</span>
	
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Enabling $DOMAIN on Apache"</span>
	sudo a2ensite <span style="color: #19177c;">$DOMAIN</span> &gt;&gt;log.txt
	<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: $DOMAIN enabled, restarting Apache2 service"</span>
<span style="color: #008000; font-weight: bold;">fi</span>

sudo rm <span style="color: #19177c;">$APACHECONFIG</span> <span style="color: #408080; font-style: italic;">#remove downloaded Apache configurations</span>
sudo a2enmod rewrite &gt;&gt;<span style="color: #19177c;">$LOGFILE</span> <span style="color: #408080; font-style: italic;">#enable rewrite for permalinks to work</span>
sudo service apache2 start

<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: LAMP Stack Installed!!"</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### APACHE &amp; PHP INSTALLED #########\\n\\n"</span>
</pre>
</div>
<h3>Section 7: Setup backup script</h3>
Once everything is fine, setup a backup script, and set the cronjob. Also save the encryption key for further backups to Dropbox.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Setup backup script &amp; Cron jobs</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Setting CRON Job, Swap File and Firewall #########\\n\\n"</span>

SetCronJob <span style="color: #408080; font-style: italic;">#from functions.sh</span>
SetEncKey <span style="color: #19177c;">$ENCKEY</span>
<span style="color: #19177c;">ENCKEY</span><span style="color: #666666;">=</span>0 <span style="color: #408080; font-style: italic;">#for security reasons set back to 0</span>
</pre>
</div>
<h3>Section 8: Setup a swapfile</h3>
Some basic things we need to do, to ensure our site stability.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Swap File creation (1GB) thanks to peteris.rocks for this code: http://bit.ly/2kf7KQm</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
sudo swapoff -a <span style="color: #408080; font-style: italic;">#switch of swap -- idempotency</span>
delFile <span style="color: #19177c;">$SWAPFILE</span>
sudo fallocate -l 1G <span style="color: #19177c;">$SWAPFILE</span>
sudo chmod 0600 <span style="color: #19177c;">$SWAPFILE</span>
sudo mkswap <span style="color: #19177c;">$SWAPFILE</span>
sudo swapon <span style="color: #19177c;">$SWAPFILE</span>
<span style="color: #008000;">echo</span> <span style="color: #ba2121;">'/swapfile none swap sw 0 0'</span> | sudo tee -a /etc/fstab
</pre>
</div>
<h3>Section 9: Setup firewall rules</h3>
Setup firewall rules to only allow port 80, port 443 and port 22. You should know what these ports are for.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Setup uncomplicated firewall rules for SSH, Http and Https: http://bit.ly/2kf7KQm</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
<span style="color: #008000;">echo </span>y | sudo ufw <span style="color: #008000;">enable</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### CRON jobs, firewall and swap file COMPLETE #########\\n\\n"</span>
</pre>
</div>
<h3>Section 10: Letsencrypt</h3>
Finally call letsencrypt. I call certbot, which is the default implementation from EFF. However, this part is interactive (requires user input), hence I placed it at the end.

There are 'some' implementations by others that don't require user interaction--but I'd rather use the official implementation, and trust they'd continue updating it.

<!-- HTML generated using hilite.me -->
<div style="background: #f8f8f8; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0; line-height: 125%;"><span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #408080; font-style: italic;"># Lets encrypt</span>
<span style="color: #408080; font-style: italic;">#---------------------------------------------------------------------------------------</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Let's encrypt #########\\n\\n"</span>
<span style="color: #408080; font-style: italic;">#Future Feature to ping $Domain and check if IP=this machine, only then proceed</span>
<span style="color: #408080; font-style: italic;">#While possible to do this automatically, I prefer to use letsencrypt supported script</span>
sudo apt-get -y install python-letsencrypt-apache &gt;&gt;<span style="color: #19177c;">$LOGFILE</span>

<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -z <span style="color: #ba2121;">"$PRODCERT"</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span> <span style="color: #408080; font-style: italic;">#Check for prodcert</span>
	<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #19177c;">$APRESTORE</span> <span style="color: #666666;">=</span> 1 <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
		<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"Let's encrypt not called, attempting to restore from backup"</span>
		<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> -f <span style="color: #19177c;">$LETSENCRYPTCONFIG</span> <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
			<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"GOOD: $LETSENCRYPTCONFIG found. Restoring configuration from backup"</span>
			delDir <span style="color: #19177c;">$LETSENCRYPTDIR</span>
			<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Creating $LETSENCRYPTDIR"</span>
			sudo mkdir <span style="color: #19177c;">$LETSENCRYPTDIR</span>
			<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Extracting Configuration"</span>
			sudo tar -xzf <span style="color: #19177c;">$LETSENCRYPTCONFIG</span> -C <span style="color: #19177c;">$LETSENCRYPTDIR</span> .
		<span style="color: #008000; font-weight: bold;">else</span>
			<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WARNING: Letsencrypt.tar not found, looks like you don't have lets encrypt installed"</span>
		<span style="color: #008000; font-weight: bold;">fi</span>
<span style="color: #008000; font-weight: bold;">	else</span>
		<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WARNING: Apache wasn't restored from Backup, unable to restore Lets Encrypt"</span>
		<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"INFO: Consider installing let's encrypt by using letsencrypt --apache"</span>
		<span style="color: #408080; font-style: italic;">#no point copying over letsencrypt configs if Apache wasn't restored (fresh install)</span>
	<span style="color: #008000; font-weight: bold;">fi</span>
<span style="color: #008000; font-weight: bold;">else</span>
	<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Getting Certs #########"</span>
	
	<span style="color: #666666;">(</span> crontab -l ; <span style="color: #008000;">echo</span> <span style="color: #ba2121;">"0 6 * * * letsencrypt renew"</span> <span style="color: #666666;">)</span> | crontab -
	<span style="color: #666666;">(</span> crontab -l ; <span style="color: #008000;">echo</span> <span style="color: #ba2121;">"0 23 * * * letsencrypt renew"</span> <span style="color: #666666;">)</span> | crontab -
	
	<span style="color: #008000; font-weight: bold;">if</span> <span style="color: #666666;">[</span> <span style="color: #19177c;">$PRODCERT</span> <span style="color: #666666;">=</span> 1 <span style="color: #666666;">]</span>; <span style="color: #008000; font-weight: bold;">then</span>
		<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"WARNING: Obtaining production certs, these are rate-limited so be sure this is a Production server"</span>
		sudo letsencrypt --apache 
	<span style="color: #008000; font-weight: bold;">else</span>
		<span style="color: #008000;">echo</span> <span style="color: #ba2121;">"Obtaining staging certs (for test)"</span>
		sudo letsencrypt --apache --staging
	<span style="color: #008000; font-weight: bold;">fi</span>
<span style="color: #008000; font-weight: bold;">fi</span>
<span style="color: #008000;">echo</span> -e <span style="color: #ba2121;">"\\n\\n######### Let's encrypt COMPLETE #########\\n\\n"</span>
</pre>
</div>