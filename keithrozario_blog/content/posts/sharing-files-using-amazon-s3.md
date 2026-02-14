+++
title = "Sharing Files using Amazon S3"
slug = "sharing-files-using-amazon-s3"
date = "2011-10-27T15:43:46"
draft = false
tags = ['Amazon', 'S3']
categories = ['Blog', 'Cloud Computing', 'Cloud Storage']
+++

![](/uploads/amazon_s3_thumb2.jpg "amazon_s3_thumb2")There are a couple of ways you can share files on the web for free, for instance you can create a <a title="Creating a site to share those pesky LARGE files" href="http://www.keithrozario.com/2011/06/creating-a-site-to-share-those-pesky-large-files.html">website to share your files</a> (although that depends on whether you have a hosting plan) or you use websites like <a title="Best File Sharing Website" href="http://www.keithrozario.com/2011/09/best-file-sharing-website.html">minus.com</a> to share it (but they have limits to the file size etc etc). For sharing large files like your wedding photos, may require you fork out a bit of cash to truly have unlimited downloads and good connectivity.

If you've got a large 1GB file for example you're hoping to send out to a bunch of friends and colleagues, your best bet may be Amazons Simple Storage Service (S3). The reason why I like S3, is that just like everything else with Amazon it's a pay as you use model, which means there are no monthly fix fees and the moment your files stop becoming the flavor of the month, you'll stop paying bandwidth for it. Plus I'm applying for a job at Amazon and hopefully this scores me some points :)<!--more-->

So before that you need to setup an AWS account, I recently blogged about how you can <a title="WordPress on Amazon Web Services (AWS)" href="http://www.keithrozario.com/2011/10/wordpress-on-aws.html">setup a wordpress site on the Amazon EC2 instance</a>, now it's time to look at the S3 data storage. Now the good news is that the free-tier applies to S3 buckets as well, which means for the first year of your subscription you get <span style="text-decoration: underline;">5GB storage and 15GB bandwidth a month free for one whole year</span>.

So if you just got married and just registered for AWS, chances are you can host your pictures for free!! Trust me that after 1 year, even you may not remember where you left your wedding photos.

So here goes, logon to your AWS management console and click on the S3 tab. Then hit the Create a bucket button. Think of a bucket as physical hard-drive with unlimited space where you can store multiple files and folders. Next you'll be prompted to choose bucket name and region, in this case you'd want to pick a region closest to where you think your data will be downloaded from. So if you've got lots of relatives in Malaysia, you'd pick Singapore, this allows faster transfer of files. This is important as a buckets location cannot be changed later on (at least not for free).

Next, you can begin immediately uploading/downloading files into the bucket. You can even sort this out logically by creating folders.

Once the data is uploaded, you have you to make sure you make the files public, otherwise you'll get a dreaded <strong>403 Forbidden</strong> message when you try to access the files. To do this, simply right-click on the files in the bucket and select 'make public'. By default any file uploaded to S3 is private only to you, so you'll have to modify all files if you want to make them public. The interesting thing though is that you can select on a folder and iteratively make the entire folder public by just making the folder public.

Now if you select the properties of each individual file you can see it's url, something like : <a title="https://s3-ap-southeast-1.amazonaws.com/keithsbucket/Keith+Rozario_files/Flight-Search.jpg" href="/uploads/Flight-Search.jpg">https://s3-ap-southeast-1.amazonaws.com/keithsbucket/Keith+Rozario_files/Flight-Search.jpg</a>

With the url you can share it with your friends/family on the cheap (possibly even free).

Tomorrow, we'll talk about hosting a website on S3 and how I hosted a simple html version of my site on S3 @ <a title="Keith's Bucket Website" href="http://keithsbucket.s3-website-ap-southeast-1.amazonaws.com/index.htm" target="_blank">http://keithsbucket.s3-website-ap-southeast-1.amazonaws.com/index.htm </a>S3 only allows for hosting of static html based sites and not dynamic sites , so no php or perl, which means no wordpress, movable type or forums. But for a lot of purposes a static site is still sufficient.

Finally On Saturday, I'll show you how we can create a torrent file with S3 and run our own torrents, so your family can share the load of sharing your wedding photos. It'll be fun.