+++
title = "Create a torrent file to share with Amazon S3"
slug = "create-torrent-file-amazon-s3"
date = "2011-10-30T17:09:10"
draft = false
tags = ['Amazon', 'Torrent']
categories = ['Blog', 'Cloud Computing', 'Cloud Storage']
+++



![](/uploads/Bittorrent_7.2_Logo.png "Bittorrent_7.2_Logo")

As the final part of my series on stuff you can do with Amazon, I've already blogged about how you can <a title="Sharing Files using Amazon S3" href="http://www.keithrozario.com/2011/10/sharing-files-using-s3.html" target="_blank">share files using amazon S3</a> and <a title="Hosting a Web Page on Amazon S3" href="http://www.keithrozario.com/2011/10/hosting-web-page-amazon-s3.html" target="_blank">hosting a static website on amazon S3</a>. Now as a final part on what you can do with your FREE amazon web services account is to host a torrent file. A torrent file would allow you to share stuff online, and not pay for the full bandwidth cost of doing it, provided your leechers share the burden as well.

The concept is really simple, Amazon S3 can act as a torrent tracker as well as a storage facility, so it's an all in one package that ensures that your torrent is tracking and there will be at least 1 tracker :) <!--more-->

The first step obviously to upload the file and share it , similar to when you share files on S3. Then it's just a matter of entering the url of the file on your browser, but append it with a "?torrent". Then you will immediately begin to download a .torrent file, and your S3 account will immediately track it so you can share the torrent....neat huh?

For example, I've the url of one image file on my s3 bucket is:

<a title="https://s3-ap-southeast-1.amazonaws.com/keithsbucket/Keith_files/5824968661_c6d1de3c43.jpg" href="/uploads/5824968661_c6d1de3c43.jpg">https://s3-ap-southeast-1.amazonaws.com/keithsbucket/Keith_files/5824968661_c6d1de3c43.jpg</a>

To generate the .torrent file, all I need to do is:

<a title="Torrent" href="/uploads/5824968661_c6d1de3c43.jpg?torrent" target="_blank">https://s3-ap-southeast-1.amazonaws.com/keithsbucket/Keith_files/5824968661_c6d1de3c43.jpg<strong><span style="color: #ff0000;">?torrent</span></strong></a>

The<span style="color: #ff0000;"> red-bit</span> of the address is all you need to add. Your web browser should immediately begin to download a .torrent file you can use client to download or share with friends.

So an S3 bucket...more than meets the eye.

 