+++
title = "Creating a wiki on Nearlyfreespeech"
slug = "creating-a-wiki-on-nearlyfreespeech"
date = "2011-05-25T14:51:41"
draft = false
tags = ['Blog Features', 'NearlyFreeSpeech', 'PHP', 'wiki']
categories = ['Blog']
+++

![](/uploads/Mediawiki_setup.jpg "Mediawiki_setup")Wikipedia isn't the only Wiki around. A wiki is a generic term us geeks use to describe <em>"A website that allows collaborative editing of its content and structure by its users"</em>

Now wasn't that a mouthful.

To put it simply, a wiki is a website that contains many articles, and ANYONE can update those articles.

Why do you need a site wiki, well the website gigaom has<a href="http://gigaom.com/collaboration/15-productive-uses-for-a-wiki/"> 15 different uses for a wiki</a>. You can use it for anything from project management to knowledge retention. So having one certainly does score you points with the ladies,...well not really but you get the picture.<!--more-->

More to the point, wikis are a cool tool to have on any website.  Installing wikis are simple and straightforward too, if you've installed your own wordpress, there's no reason to think you can't install your own wiki.

For this example, I'm going to install mediawiki in my nearlyfreespeech website. Mediawiki is the platform that powers wikipedia (so you know they're good), but if you're interested in experimenting, try wikkawiki or a few other free wiki platforms available for download. As usual wikipedia is the first place you should go to search, check out this <a title="Comparison of wiki software" href="http://en.wikipedia.org/wiki/Comparison_of_wiki_software">entry</a> for more info.

So here's how you install it:
<h3><span style="color: #3366ff;">Step 1: Create a Subdomain</span></h3>
Create a subdomain for your website, it doesn't have to be titled 'wiki', but make the name clear it's probably a good sub-domain name. Subdomains help make the site more logically divided. The also let you delete the whole wiki without affecting the site. For more info on setting up subdomains on nearlyfreespeech you can read my earlier post <a title="SubDomains" href="http://www.keithrozario.com/2011/05/sub-domains-on-your-post.html" target="_blank">here</a>.

For this example, I'm going to be using my domain (www.keithrozario.com), and I'll create subdomain (wiki.keithrozario.com).
<h3><span style="color: #3366ff;">Step 2: Download Mediawiki</span></h3>
Sub-domains take time to setup, so while that's being setup, head on over to <a title="Media Wiki Download" href="http://www.mediawiki.org/wiki/Download" target="_blank">www.mediawiki.org</a> to download the latest media wiki. Be sure to download the zip file (it's easier to install).
<h3><span style="color: #3366ff;">Step 3: Copy the mediawiki folder into your main folder via sFTP</span></h3>
![](/uploads/Mediawiki_sftp_download.jpg "Mediawiki_sftp_download")
<h3><span style="color: #3366ff;">Step 4: Unzip the folder using SSH</span></h3>
You'll need to unzip the package, most of us with windows would need to download 7-Zip to unzip this on your PC, and that would be a pain and a chore. A simpler version would be login to your SSH and run the following command

![](file:///C:/Users/KEITH-%7E1.ROZ/AppData/Local/Temp/moz-screenshot-2.png)<strong>tar -zxvf *</strong>

<address>*The tar commands unzips the file, and the -zxvf are various options I generally use. The important bit is the *, I use that to unzip ALL files in the directory, but seeing as how there will be only file in the folder (if you followed the instructions), it's good enough. To be doubly sure replace the * at the end of the command to the actually file name of the media wiki downloaded.</address>By then your FTP will look like this:

![](/uploads/Mediawiki_sftp_unzip.jpg "Mediawiki_sftp_unzip")

Before moving to step 7, you'll need to setup your permissions correctly. Login to your SSH again and run the following command from the main prompt:

<strong>chmod 777 wiki/config</strong>

<address>*This command sets the config subfolder to all writable, something that needs to be done for the installation to proceed. We'll reset it back to safer permission once we're done with the install. Another way is to use WinSCP and set the permission by right-clicking the file and modifying permissions</address>
<h3><span style="color: #3366ff;">Step 5: Tidy stuff up (optional)</span></h3>
To make things easier I've renamed the mediawiki1.16-5 to simply 'wiki' and deleted the zip file for tidiness. So in the end what I get is:
<h6>![](/uploads/Mediawiki_sftp_tidied_up.jpg "Mediawiki_sftp_tidied_up")<span style="color: #999999;">*to save yourself a full bunch of trouble, unpack the '/wiki' folder out into the root directory, this will save you on step 11</span></h6>
<h3><span style="color: #3366ff;">Step 6: Create a Database</span></h3>
From your nearlyfreespeech menu, look for the MYSQL options, (it's right next to support), then select your db process (create one if you haven't already). The select 'Create new Database' from the side menu.

Then use a wiki name, I use wikidb and provide a username and password. (Write down the database name and username/password).

Then click create now.
<h3><span style="color: #3366ff;">Step 7 : Logon to the your wiki page and set it up.</span></h3>
Browse to <strong><em>http://wiki.keithrozario.com/wiki </em></strong>and you'll see something like this:\

[caption id="attachment_757" align="aligncenter" width="276"]![](/uploads/Mediawiki_setup.jpg "Mediawiki_setup") Media Wiki setup page[/caption]
<h3><span style="color: #3366ff;">Step 8 : Enter the related info</span></h3>
Most of this is easy, except the DB related stuff. For DB related stuff, use the following:
Firstly go to the mysql option of your nearlyfreespeech control panel. Then look for the name of your mysql instance, an example here:

[caption id="attachment_755" align="aligncenter" width="388"]![](/uploads/Mediawiki_mysql_info.jpg "Mediawiki_mysql_info") Name intentionally blank out and changed to test.db[/caption]
<p style="text-align: center;">Then enter the information into the database information part of the page:</p>

<blockquote>Database host: <strong>localhost</strong>
Database name: <strong>-as from step 6-</strong>
Database username : <strong>-as from step 6-</strong>
Database password: <strong>-as from step 6-</strong>
Superuser account: <strong>(leave unchecked)</strong></blockquote>
<h3><span style="color: #3366ff;">Step 9: Copy the localsettings.php file from the '/wiki/config' folder to the '/wiki' folder.</span></h3>
You'll need to move the Localsettings.php file found in the '/wiki/config' folder out to the '/wiki' folder.
<h3><span style="color: #3366ff;">Step 10: Tidy up permissions</span></h3>
Perform the following commands on the SSH:

<strong>chmod 775 wiki/config</strong>

<strong>chmod 777 wiki/LocalSettings.php</strong>
<h3><span style="color: #3366ff;">Step 11: Redirect traffic from wiki.keithrozario.com to wiki.keithrozario.com/wiki</span></h3>
This was an oversight on my part, but only after installing did I noticed we'd be stuck with a wiki that links all it's articles with<span style="text-decoration: underline;"><span style="color: #3366ff;"> <em>wiki.keithrozario.com/wiki/ArticleName</em></span></span>
<blockquote>RewriteEngine on
RewriteCond %{HTTP_HOST} ^keithrozario\.com$
RewriteRule (.*) http://www.keithrozario.com/$1 [R=301,L]
RewriteRule ^$ wiki [L]</blockquote>
Replace keithrozario.com to the name of your domain.
<h3><span style="color: #3366ff;">You're Done.</span></h3>
Now this post was written for nearlyfreespeech users, who are generally more savvy than your usual web user, but if you're uninitiated to even try this. Dreamhost has a 1-click install that will settle all your problems from step 1-6.

So basically Dreamhost reduces your MediaWiki installation from a 11 (or 10) step process to just 3 steps. Steps 8,9 and 10. That's the difference between Dreamhost and Nearlyfreespeech.

 