+++
title = "Hosting a Web Page on Amazon S3"
slug = "hosting-web-page-amazon-s3"
date = "2011-10-28T17:46:33"
draft = false
tags = ['Amazon', 'S3']
categories = ['Blog']
+++

<a href="/uploads/amazon_s3_thumb2.jpg">![](/uploads/amazon_s3_thumb2.jpg "amazon_s3_thumb2")</a>Yesterday, I blogged on how to<a title="Sharing Files using Amazon S3" href="http://www.keithrozario.com/2011/10/sharing-files-using-s3.html" target="_blank"> share files on Amazon S3</a>, today I'll show you how you can host a webpage on amazon S3. Now Amazon S3 is a simple storage service, and all it does it store files, but if you store a html file you can change this simple storage service into a webhost.

How does it work? Simple.

If you store a picture file (jpeg for example), and then share a url to everyone. Chances are people will click that URL and it'll open the picture in a browser. However, if you share a html file, then people clicking on that URL will be able to view a web page on their browser and they wouldn't be able to tell the difference, because that's essentially what webhost do anyway, they merely store your html file.<!--more-->

The one drawback of this approach is that, all you get is HTML. No PHP or PERL. In layman terms that means no wordpress, movable type or forums. All you get is a static HTML page that would be difficult to modify. Then again, a lot of web pages don't get updated too often anyway.

So let's get started.

For this example, I'm going to a snapshot of my website on the S3 bucket. First I make a copy of this blog, by saving the page via firefox. On firefox I click save-as, and then save the page as a Web Page (Complete), this saves the entire page and all the corresponding icons/pictures into a html file and a folder with the same name.

Then I upload them onto my S3 bucket. People recommend bucket explorer, but you can also try <a title="Cloud Berry" href="http://www.cloudberry.com" target="_blank">cloudberry</a> who've commented on my blog before. Or you can use the plain ol' web interface (which isn't all that bad either). To use the web interface, simply logon onto your AWS management console, open up the S3 tab, click on your bucket and then select upload. Now be careful, you'll have to upload the web page as a html and a folder with the same name as you've saved it from firefox...otherwise it won't work.

You should end up with something like this:

<a href="/uploads/objects.jpg">![](/uploads/objects.jpg "objects")</a>

So here, I have a htm file and a folder of the same name (but with a <strong>_files</strong> postfix). If you've had a old website in a good old days of HTML you'd recognize this structure.

Now the last step is just to setup the S3 as a website.

Click on the bucket and right-click to select it's properties. Select the website option, then enable the website by clicking Website Enabled. Then enter the name of the htm file as the Index Document (remember this is case-sensitive). And then save it.

<a href="/uploads/Website_Keith.jpg">![](/uploads/Website_Keith.jpg "Website_Keith")</a>

To access the website, simply click on the visit the Endpoint and you're good to go!! Happy Hunting!

*If you get the dreaded <strong>403 Forbidden error on your Amazon S3 bucket page</strong> with a <strong>Code: Access Denied</strong> and <strong>Message: Access Denied</strong>, then it's just a simple matter of making the folder and the file public. Right click on the folder and the file and select the Make Public option:

<a href="/uploads/Make_Public.jpg">![](/uploads/Make_Public.jpg "Make_Public")</a>