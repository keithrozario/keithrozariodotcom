+++
title = "Migrating wordpress to Dreamhost"
date = "2011-12-07T20:44:09"
draft = false
categories = ['Blog']
+++

<a href="http://www.keithrozario.com/2011/12/migrating-wordpress-to-dreamhost.html/3950846568_69a959524f_o" rel="attachment wp-att-1532"><img class="alignleft size-medium wp-image-1532" title="3950846568_69a959524f_o" src="/uploads/3950846568_69a959524f_o-300x300.jpg" alt="" width="300" height="300" /></a>Last week I migrated my blog from Nearlyfreespeech (who are awesome by the way!) to dreamhost (who are also quite awesome in their own way). What prompted the move was that I'm already subscribed to a year of hosting to dreamhost at about $6/mo, while my blog at Nearlyfreespeech is still costing me money, although admittedly not much. So I thought why waste my dreamhost hosting, and instead switch over from Nearlyfreespeech to dreamhost.

Before I start, let's me first explain what I want to do. I want to migrate my blog from nearlyfreespech to dreamhost, in essence I want to change my hosting provider from Nearlyfreespeech to dreamhost. I do <strong>not</strong> want to change my url, I still want readers who type www.keithrozario.com to visit my blog, it's just that the blog is now hosted on a different service provider and will ultimately have a different IP.

I also want to point out that although I already have a parallel blog setup on <a title="Keiths Blog" href="http://blog.keithrozario.com" target="_blank">blog.keithrozario.com</a>, I decided not to migrate because nearlyfreespeech kicks ass in terms of reliability, up-time and speed :).<!--more-->

So how do I do it?

<strong>Step1: Make sure you backup everything</strong>

Backing up wordpress is easy, there's a whole list of plugins that can help you here, but where I'm most interested in is backing them up manually. That way there's a whole lot more control and I'm absolutely sure I backed up everything.

First log onto to your SSH and then tar your wordpress directory. Use the following command <strong>tar -cvf wordpress(backup).tar wordpress</strong>. This will create a separate file wordpress(backup).tar in the directory. Think of a tar as the unix equivalent of zip files. If you ever screw up the wordpress installation you can always fix it by deleting the wordpress directory and untar-ing the wordpress(backup).tar file.

Next backup your database. For this you need to logon to your phpMyadmin (check with your hosting provider on how to do this). Once logged in, go to export and export the database file. To make things simpler, under the options, select the  "<strong>add DROP TABLE</strong>"<strong></strong> option. This will allow you to over-write databases, which prove a lot easier than creating them from scratch.  If everything was done right, you'd be able to download a .xml file, this file actually contains a sequence of SQL statements that contain the entire content of your database.

With this .xml file and the wwordpress(backup).tar file stored under lock and key, you can rest easy knowing you can always re-boot your blog up with little fuss.

<strong>Step2: Setup Dreamhost, Early Prep
</strong>

There's actually a couple of ways to do this, my favorite is to actually create a new wordpress site using the 'one-click install'. So for instance I have a domain registered in dreamhost (www.jomlunch.com) and I created sub-domain called keithrozario.jomlunch.com.

Then I install wordpress using the one-click install.

Finally I create a new database from the "manage database" option. I select a server in this case databases.jomlunch.com, I give my database a name keithswordpress and assigned it a user whose username and password I remember.

This means that there's two things setup, a folder titled keithrozario.jomlunch.com in my sFTP directory (together with the wordpress installation file) AND an empty database with a database server/name/username+password.<em>(you'll need this in step 4)</em>

<strong>Step3: Copy that stuff over</strong>

Now logon to your sFTP folder on Dreamhost. You should see a folder you created in step 2 (as part of the wordpress install). Insider that folder will sit a wordpress folder....DELETE that folder.

Then copy over the wordpress.tar file from step into it. So for me, I copy over the wordpress(backup).tar file and then I un-tar the file with the following command from the terminal tar -xvf wordpress(backup).tar. If you did everything right you'd see a wordpress folder appear, this folder will have all your wordpress files from your previous hosting provider.

Next you need to copy over your wordpress database. To do this, go to the "manage my databases" option in your dreamhost panel. Select the phpMyadmin for the server you installed the database on. Logon with your credentials from step 2. Then go to import, and simply import the .xml file you saved in step 1.

Cool. Now you've got the files and database setup. We're almost there but not quite....

<strong>Step4: Modify install to fit Dreamhost</strong>

One of the biggest problems now is that your wordpress files still think they're on the old hosting provider, (in my case nearlyfreespeech). So we need to modify these settings.

First let's point it to the dreamhost database rather than your old database. So head on over to your wp-config.php file located in your wordpress folder (via sFTP).

<span style="color: #333333;">And modify the following lines in the file:</span>
<blockquote><span style="color: #808080;">/** The name of the database for WordPress */</span>
<span style="color: #808080;">define('DB_NAME', 'keithswordpress');</span> <strong>&lt;- the database name from step 2 &amp; 3</strong>

<span style="color: #808080;">/** MySQL database username */</span>
<span style="color: #808080;">define('DB_USER', 'username');</span> <strong>&lt;- the user name from step 2</strong>

<span style="color: #808080;">/** MySQL database password */</span>
<span style="color: #808080;">define('DB_PASSWORD', 'password'); </span><strong>&lt;-the password from step 2</strong>

<span style="color: #808080;">/** MySQL hostname */</span>
<span style="color: #808080;">define('DB_HOST', 'databases.jomlunch.com'); </span><strong>&lt;- database server name from step 2</strong></blockquote>
Now your wordpress is pointing to the right database, but that database has the wrong urls. So you'll need to be a bit more specific. So add the following 4 lines to your wp-config file right after the database setup (changing the <strong>bolded black parts</strong> to your site specific values)
<blockquote><span style="color: #808080;">define('WP_SITEURL', '<span style="color: #333333;"><strong>http://keithrozario.jomlunch.com/wordpress</strong></span>');</span>
<span style="color: #808080;">define('WP_HOME', '<span style="color: #333333;"><strong>http://keithrozario.jomlunch.com/wordpress</strong></span>');</span>
<span style="color: #808080;">define('WP_PLUGIN_DIR', '/home<strong><span style="color: #333333;">/username/keithrozario.jomlunch.com/wordpress</span></strong>/wp-content/plugins');</span>
<span style="color: #808080;">define('WP_CONTENT_DIR', '/home<span style="color: #333333;"><strong>/username/keithrozario.jomlunch.com/</strong></span>wordpress/wp-content');</span></blockquote>
WP_SITEURL is the url of the site, and for my example it was keithrozario.jomlunch.com/wordpress (I found that I needed the '/wordpress' because I installed wordpress in the /wordpress folder. We'll change this value once everything is settled.

WP_HOME refers to the actual URL where wordpress resides. This could be different from the url. So for instance this blog on nearlyfreespeech had a <strong>WP_SITEURL</strong> of http://www.keithrozario.com and a <strong>WP_HOME</strong> of http://keithrozario.nfshost.com

WP_PLUGIN_DIR is a the directory for your plugins. For some reason dreamhost automatically thinks your plugins are somewhere else. It may be ok to leave this out, but it's best to put it here. Remember to change the field accordingly.

WP_CONTENT_DIR is the directory for your wp-content directory. If you're using a theme, wordpress will look for the theme files using this variable. If it's wrong, your theme will not load and your site won't even load....I learnt this the very hard way.

Now Wordpress should work. Save the changes and give it a test. Head on over to your domain (in my example it's http://keithrozario.jomlunch.com) and you'll see an exact replica of your blog...HOORAY!!

<strong>Step 5: Made the changes permanent</strong>

Now that everything on the wordpress site is working, let's work on the making the blog run in parallel. So I'm not going to immediately point www.keithrozario.com to my dreamhost wordpress (are you crazy!!), I'm going to point a sub-domain from keithrozario.com to keithrozario.jomlunch.com, make sure that's working correctly and then make the changes.

So here's how.

First I'll have to download a plugin called Search and Replace to wordpress, this plugin allows you to search and replace content throughout wordpress....but be warned it doens't let you revert back.

Once I downloaded the plugin, I'm going to change my previous hosting server http://keithrozario.nfshost.com to my new dreamhost server at http://keithrozario.jomlunch.com. So I use the plugin to change "<strong>keithrozario.nfshost.com</strong>" to "<strong>keithrozario.jomlunch.com</strong>".

Next I'll change my blog url from <strong>www.keithrozario.com</strong> to <strong>blog.keithrozario.com</strong>.So I'll search and replace that as well.

Once this is done you can actually remove the WP_SITEURL and WP_HOME lines from your wp-config.php file, but keep it there for now.

<strong>Step 6: Point your old domain to your new</strong>

Now it gets a bit interesting in dreamhost you can't create CNAME from your old hosting provider to your dreamhost address and hope everything goes hunky dory....ain't going to happen.

We need to create A DNS records, (that's a capital A by the way). And we also need to alert Dreamhost that there will be something pointing to it from your old host. So here's how. For my example, I want to point blog.keithrozario.com (hosted on nearlyfreespeech) to keithrozario.jomlunch.com (hosted on dreamhost).

Here's what you need to do:
<blockquote>Go to the Manage Domains page-

<a href="https://panel.dreamhost.com/index.cgi?tree=domain.manage&amp;" target="_blank">https://panel.dreamhost.com/<wbr>index.cgi?tree=domain.manage&amp;</wbr></a>

Click the Add New Domain / Sub-Domain button.

Domain to host: <a href="http://keithrozario.com/" target="_blank">blog.keithrozario.com</a>
Do you want the www in your URL?  (select as desired)

Web directory: <a href="http://keithsblog.jomlunch.com/" target="_blank">keithrozario.jomlunch.com</a>

Click the "Fully host this domain" button to finish. By doing so, the domains will be set to load the content at
<a href="http://keithsblog.jomlunch.com/" target="_blank">keithrozario.jomlunch.com</a>

When you are finished adding the domains to your plan click the DNS link
under each.  You will find the A record IPs for the domains that way.
Use those for the DNS from the other host.  You should see the domains
loading from your account with us within a few hours after.</blockquote>
That way you can avoid the dreaded <a title="Damn you!! error id: “bad_httpd_conf”" href="http://www.keithrozario.com/2011/12/damn-you-error-id-bad_httpd_conf.html" target="_blank">httpd_conf</a> errors....damn those errors.

<strong>Step 7: Make sure everything is OK.</strong>

In about 1 hour after adding your A DNS entry, you should be able to go to blog.keithrozario.com and see the content of keithrozario.jomlunch.com (you can do this now to see my blog there).

Make sure everything is OK, and you can even do some housekeeping by upgrading your wordpress plugins and wordpress itself, then when everything is really good to go, perform step 6 again for www.keithrozario.com, and you'll be magic!!

I find keeping a parallel blog allowed me to really experiment with a few things, without having to worry about crashing my blog.

So that's it.