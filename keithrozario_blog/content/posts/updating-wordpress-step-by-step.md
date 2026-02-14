+++
title = "Updating Wordpress: Step by Step"
slug = "updating-wordpress-step-by-step"
date = "2011-07-14T11:11:42"
draft = false
tags = ['wordpress']
categories = ['Blog']
+++

![](/uploads/WordPress-Introduction-icon_big-en-150x133.png "WordPress-Introduction-icon_big-en")Updating Wordpress is a pretty important step in keeping your blog safe and secure. Older versions of wordpress (even those just months old) have security flaws/bugs that are public knowledge, what this means if that if you run an older version of wordpress for your blog you're vulnerable to these security bugs unless you upgrade. What's even worse is that the security threats are public knowledge and even a un-skilled hacker could compromise your site. So upgrade to stay secure and get the most out of blogging experience.

So here's how you update your Wordpress. It's actually very simple, and I'm going to use the manually way which should be applicable regardless of which webhost you're on. For this example, I'm using my own blog at www.keithrozario.com which is hosted on NearlyFreeSpeech.<!--more-->

<strong>Step 1: Backup your current blog</strong>

Backing up your blog is easy, but this way of backing up is bullet-proof. The first thing you want to do is export your wordpress content. This is a simple .xml file that can be imported back into wordpress. (File #1)

Next  step is to backup your wordpress directory, it's simply to copy out ALL the content of your wordpress directory for safe keeping. It's either you copy the whole folder via sFTP or a much simpler method is to zip (or tar) your wordpress folder directly from SSH. What this does, is it creates a tar file of your wordpress folder on your webhost. It's a much quicker solution given most webhost have slow sFTP transfer. (File #2)

Finally backup your database via the phpMyAdmin or cPanel. This ensures that all your data is intact. (File #3)

I recommend you download a copy of your current wordpress version from <a title="Wordpress Download" href="http://wordpress.org/download/release-archive/" target="_blank">here</a>, in case you need to restore the blog quickly. (File #4)

At the end of this exercise you should have 4 files.

1) A .xml file from your wordpress export
2) A wordpress.tar file on your webhost
3) A .sql database backup file
4) A wordpressX.X.zip file of your current wordpress version

With these 4 files, you can backup your wordpress even if you wipe out your entire directory.

<strong>Step 2: Download and Install the new wordpress version</strong>

<strong></strong>Next you'll need to download the latest wordpress installation here. Once you've got the wordpress installation, unzip it to your local machine.<strong></strong>

<strong>Step 3: Install wordpress</strong>

So far we've done nothing to your site and you can stop the installation with no issues. Here's where the interesting stuff begins.
<ol>
	<li>Disable ALL wordpress plugin</li>
	<li><strong></strong>Copy AND overwrite all content in the wp-includes and wp-admin folder of your wordpress</li>
	<li>Copy AND overwrite all content in your wordpress root folder (wp-activate.php, wp-app..etc etc)</li>
	<li>Copy AND overwrite all content in your wp-content folder (remember not to delete anythign)</li>
	<li>Logon to your login page (http://www.example.com/wordpress/wp-login.php)</li>
	<li>Follow the steps.</li>
	<li>Enable the plugins (one at a time)</li>
	<li>You're done.</li>
</ol>
For an even more detailed (ALL steps) procedure, read on.

<span style="text-decoration: underline;"><strong>The (slightly more detailed) steps</strong></span>

To be even more detailed, I'm going to need to be specific about the tools I'm using. So if you haven't downloaded these tools, please do:

1) Mozilla firefox version 3.6.18
2) WinSCP
3) Putty SSH portable

Once you've downloaded and installed them. Follow these steps.

1) Logon to your wordpress Admin Panel
2) On the right menu, click on Tools-&gt;Export
3) Select ALL content and download export file (File #1 in .xml)
4) Logon to your FTP/sFTP server via Putty
5) Browse to the directory where you can see your wordpress directory
6) Execute the following command: tar -cvzf wordpress.tar wordpress
7) Step 6 creates a wordpress.tar file in case you need to restore it later (File #2)
8) Logon to your phpMyAdmin panel from your webhost (consult your webhost for details)
9) Follow the steps in this article <a href="http://codex.wordpress.org/Backing_Up_Your_Database">here</a>
10)At the end of step 9 you'll need to download a .sql file (File #3)
11)Browse to the wordpress repository and download your current version of wordpress (File #4)

Congratulations you've successfully backedup your wordpress. From here on in no matter what happens you'll be able to restore your wordpress to exactly as it was from before step1.

12) Unzip the Wordpress Version you plan to install to a folder wordpress_new on your local machine
13) Logon to your sFTP/FTP server via WinSCP.
14) Copy over and overwrite the wp-includes folder from the wordpress_new folder to your FTP.
15) Copy over and overwrite the wp-admin folder from the wordpress_new folder to your FTP.
16) Copy over and overwrite the files in wordpress_new folder (wp-atom,wp-activate.php, wp-app, etc etc)

Congratulations, you've copied the files now.

17) Now logon to your wordpress admin panel and it should redirect you to the page.
18) Follow the steps, update the database and you should be good to go.

<strong>Oh-oh my update didn't work.</strong>

Now if you need to restore wordpress don't worry. The solution is quite simple. First take a deep breath, and make sure you have File #2, File #3 and File #4. If you have them.

1) Browse to the directory where you have your wordpress installation via Putty
2) Execute the following command: rm -r wordpress (deletes the entire wordpress directory)
3) Execute the following command: tar -xvzf wordpress wordpress.tar

What this does it it untars (similar to unzip) the tar file you created in step 6 of the backup procedure above. That's all you need to do if you haven't done step 17 of the procedure above. If you've done step 17, don't worry just follow these steps to restore a database.

4) Go to your phpMyAdmin panel
5) Drop the database (usually it's named wordpress.db something like that)
6) Then import the database from the file you created in step 10 (File #3)
7) Finally logon to your wordpress admin panel and make sure everything is OK.

And there you have it a simple straight forward way to update your wordpress. The key thing to know about Wordpress is that it is basically a collection of files and a database. If you are able to restore the files and database from the same time, you've got nothing to worry about.