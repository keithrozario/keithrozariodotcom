+++
title = "Installing Joomla on your Nearlyfreespeech site"
slug = "installing-joomla-on-your-nearlyfreespeech-site"
date = "2011-05-01T00:19:29"
draft = false
tags = ['Joomla']
categories = ['Blog']
+++



![Joomla](/uploads/logo-150x29.png "logo")

 Joomla is a content management system that is customized for building actual sites. Wordpress is similar to Joomla with the exception that it's VERY VERY tailored to blogs. Of course I'm still new to most of this, but you can read up more by searching online:

 

So how do you install Joomla on nearlyfreespeech, surprisingly it's VERY easy. Follow these steps.<!--more-->

<strong>Download Joomla.</strong>

Extract the Joomla and upload it into your root folder or \Joomla folder.

<strong>Create a database.</strong>

From the Nearlyfreespeech Menu:
MySQL - &gt;Click on SQL Process - &gt; CreateDatabase -&gt; <strong>myjoomla</strong> -&gt; ok

<strong>Installation</strong>

Browse to http://www.yoursite.com/Joomla/installation/ (remember sometimes it's case sensitive)

<strong>Some issues with Nearlyfreespeech:</strong>
Configuration.php writeable is 'OFF'.
Create a configuration.php in your joomla folder.
Set to permissions to 777 temporarily.

Enter the database information.
hostname is located in the "How to Access MySQL" box in nearlyfreespeech
enter you admin and password setting
and DB name is what you entered previously. (<strong>myjoomla</strong>)

Next enable ftp, but remove the username and password (for security reasons).
Copy the ftp information from your sites page into the Joomla (under advanced settings).

Click next, and you're good to go.

Delete the installation folder from Joomla. (via sFTP is the best).

Then browse to www.yoursite.com/Joomla and you can view your new Joomla page :)

If you'd like to see a sample, head on over to<a title="Joomla on nearlyfreespeech" href="http://www.keithrozario.com/Joomla"> www.keithrozario.com/Joomla</a>