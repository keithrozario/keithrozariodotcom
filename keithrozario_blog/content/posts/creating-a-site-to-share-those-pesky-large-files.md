+++
title = "Creating a site to share those pesky LARGE files"
date = "2011-06-03T14:24:29"
draft = false
tags = ['Blog Features', 'PHP']
categories = ['Blog']
+++

<a rel="attachment wp-att-825" href="http://www.keithrozario.com/2011/06/creating-a-site-to-share-those-pesky-large-files.html/file_sharing"><img class="alignleft size-thumbnail wp-image-825" title="File_sharing" src="/uploads/File_sharing-150x112.jpg" alt="http://www.flickr.com/photos/kevymckeversons/444514987/sizes/l/in/photostream/" width="166" height="123" /></a>Ever since they took down <a title="Drop.Io" href="http://en.wikipedia.org/wiki/Drop.io" target="_blank">drop.io </a>I've been struggling to find a site where I could share content/files with my developers and service providers. I work for the IT department of a multinational company and sometimes I require to share content with developers and service providers that are not from my company (and therefore don't share access to the intranet). I'm sure many people struggle with this, how do I share those large files with my team?<!--more-->

The short answer is email, email offers the simplest method to share files, but email has a limit, usually to the tune of 5MB. Anything bigger and email just won't cut it.

The next option is services like <a title="Dropbox" href="http://en.wikipedia.org/wiki/Dropbox_%28service%29" target="_blank">dropbox</a> and <a title="You Send it" href="http://en.wikipedia.org/wiki/YouSendIt" target="_blank">yousendit.com</a>, but my company's network provider has already begun blocking these sites. Also, some of them require a registration in order to download, and that's big turn off.

If you're looking for a comparison of these websites, techcrunch has a brilliant round-up <a href="http://techcrunch.com/2009/08/08/16-apps-that-make-sharing-large-files-a-snap/">here. </a>(warning: it is  an old link)

If you're still reading, chances are you've already tried these options. So you're here, wondering what you can do. The solution is quite simple, if you have your own website hosted on a site like dreamhost.com that offers unlimited bandwidth and storage for a fixed monthly sum, why waste that? You can turn your website into a <del>cool </del>AWESOME file sharing utility.

Think of the people you'd impress in the office, as the person who successful manages the office<span style="color: #000000;"> <del>illegal collection of MP3's. </del></span>Repository of informational documents.

The script behind it is super simple, and I'll show you how to configure this with minimal fuss on <a title="Dreamhost" href="http://www.dreamhost.com" target="_blank">Dreamhost</a>. The reason why I'm not having a tutorial for nearlyfreespeech, is that nearlyfreespeech's charges would skyrocket the instant you start using it to transfer Gigabytes of data. That being said, I still love nearlyfreespeech and it's one of the best web host out there for low volume blogs like mine, what I'm about to show you however will eat bandwidth and storage, so it's better to go with a unlimited hosting solution.
<h2><span style="color: #993366;">Step1: Download the scripts</span></h2>
Click <a title="Awesome file up&amp;down loader" href="http://www.keithrozario.com/uploads/awesomefiles.zip">here</a> to download the scripts in zip format.
<h2><span style="color: #993366;">Step2: UNzip the scripts anywhere on your webpage.</span></h2>
For this e.g. I'm unzipping it to a sub-domain of mine, in my other website, jomlunch. <strong>http://socialize.jomlunch.com</strong>
<h2><span style="color: #993366;">Step3: Configure the file(s)</span></h2>
Open the <strong>config.php</strong> file of the folder and change the value for PASSWORD. This password would protect both uploads and downloads.

define('PASSWORD', '<span style="color: #888888;">Enter your password here</span>'');
<h2><span style="color: #993366;">Step4: Change the permissions of the folders</span></h2>
You need to change the permissions of the <strong>/uploads</strong> folder and the <strong>config.php</strong>. This protects the files from being viewed by nefarious people, you're not fully protecting the files, but protecting them enough for this example. This prevents anyone from just typing in the url of the link and downloading the file, so the only way anyone is going to access the uploaded file is via the php script and that requires a password.

Change the permission for the upload folder to 744

Change the permission for the config.php file to 700
<h2><span style="color: #993366;">Step 5: Modify the php.ini on Dreamhost.</span></h2>
<span style="color: #993366;"><span style="color: #000000;">If you unzip the files correctly, and you browsed to the info.php file with your internet browser, you'll see something like this:</span></span>
<h2><a href="http://socialize.jomlunch.com/info.php"><img class="size-medium wp-image-822  aligncenter" title="PHP_info" src="/uploads/PHP_info-300x246.jpg" alt="" width="300" height="246" />
</a></h2>
<span style="color: #993366;"><span style="color: #000000;">Look for these 2 values:</span></span>
<blockquote>post_max_size = 12M
upload_max_filesize = 7M</blockquote>
Here is where it gets specific for the webhost. The default setting for Dreamhost is just 12MB per upload, this is WAAAY to small. To increase this, you'll need to change these values. Dreamhost has a pretty

simple way to change the php.ini settings
<h2><span style="color: #993366;">Step 5.1 Upgrade your site to PHP5.3</span></h2>
Upgrade your website to PHP5.3

Go to your domains-&gt;Edit the domain and under the web options select <strong>PHP5.3 FAST CGI</strong> from the list

[caption id="attachment_823" align="aligncenter" width="300" caption="Chaging the web-options in Dreamhost"]<a rel="attachment wp-att-823" href="http://www.keithrozario.com/2011/06/creating-a-site-to-share-those-pesky-large-files.html/web_options_php_5-3"><img class="size-medium wp-image-823" title="web_options_php_5.3" src="/uploads/web_options_php_5.3-300x134.jpg" alt="" width="300" height="134" /></a>[/caption]
<h2><span style="color: #993366;">Step 5.2 upload a new php.ini file</span></h2>
This is simpler than it sounds.

In your main folder (the one you see when you logon to sFTP, i.e. root\home\user_name), create a folder called "<span style="color: #ff6600;"><strong>.php</strong></span>" remember the ".".

Then create another folder called "<span style="color: #ff6600;"><strong>5.3</strong></span>" in that, and finally create a file called <span style="color: #ff6600;"><strong>phprc.</strong></span><strong> </strong>At the end you'll the path of the file would be <strong><span style="color: #ff6600;">.php\5.3\phprc</span></strong>

<span style="color: #ff6600;"><span style="color: #000000;"><span style="color: #ff6600;"><span style="color: #000000;">Then just change the contents of the file to the following:</span></span></span></span>
<blockquote><span style="font-size: x-small;"><span style="font-family: georgia,serif;">post_max_size = 128M
upload_max_filesize = 128M</span></span></blockquote>
This overrides the default php setting of Dreamhost. To double check this, view the info.php file again. Sometimes it takes 5-10 minutes for these changes to be reflected so don't get too excited if it doesn't work instantly.
<h2><span style="color: #993366;">Step 6: Give it a test drive.</span></h2>
The scripts should work, if you give it a test drive. If you wish to increase the size to greater than 128MB, you'll also need to change the value of the "MAX_FILE_SIZE" parameter in the index.php file.

Finally you'll be able to see, <strong>Keith's Awesome File Up&amp;Down loader</strong>. The design of the site leaves much to be desired, I'm hoping someone could help me out there.

Preview of the site:
<p style="text-align: center;"><a rel="attachment wp-att-824" href="http://www.keithrozario.com/2011/06/creating-a-site-to-share-those-pesky-large-files.html/keiths_awesome_file_uploader"><img class="size-full wp-image-824 alignnone" style="border: 2px solid blue;" title="Keiths_Awesome_file_uploader" src="/uploads/Keiths_Awesome_file_uploader.jpg" alt="" width="594" height="478" /></a></p>
&nbsp;

If you're still interested, try my awesome file uploader over at <a title="Uploads" href="http://www.keithrozario.com/uploads" target="_blank">www.keithrozario.com/uploads</a>, use 'KEITHisAWESOME'.
<div id="_mcePaste" class="mcePaste" style="position: absolute; left: -10000px; top: 424px; width: 1px; height: 1px; overflow: hidden;"><img src="file:///C:/DOCUME%7E1/Test/LOCALS%7E1/Temp/moz-screenshot.png" alt="" /></div>