+++
title = "Maxis Loker: A review"
slug = "maxis-loker-googledrive-dropbox"
date = "2012-06-04T10:27:50"
draft = false
tags = ['Amazon', 'Maxis']
categories = ['Cloud Computing', 'Malaysia']
+++

![](/uploads/MaxisLoker-300x273.jpg "MaxisLoker")As you know, I'm not really happy with Maxis. I was utterly disappointed by their latest S3 launch, I don't think their cloud offerings of ebook portal is anything to shout at, and the if my wifes office would get decent Digi coverage, I'd switch in a heartbeat.

That being said, this is one of the times I think Maxis has done a decent job on their Loker offering. It is quite well executed, and if I do say so myself, getting 25GB of free online storage space when you purchase an S3 from Maxis is quite an enticing offer.
<h2><strong>So what is Loker?</strong></h2>
Loker is a simple online storage area for Maxis customers to store their online files. Free registration comes with 5GB of free storage, which you can upgrade all the way to 25GB of storage space coupled with (as far as I can tell) unlimited downloads and uploads.

It's also important to note that Maxis is offering the full 25GB to anyone who signs up for the Samsung Galaxy S3 package, which to me is a great value adding tool.

The service however, is only available to Maxis customers, and you need a Maxis phone number to register.<!--more-->
<h2><strong>So what is Loker NOT?</strong></h2>
Loker is NOT a <strong>file-sharing</strong>, but more a <strong>file-storing</strong> service. It's not as easy to share your files (although its possible), and even if you do share files, you can only share them with Loker users, i.e. Maxis users.

Loker is also not a CDN-like service for you to store images for your website. You can't link directly to Loker files and have them load on your website.

So if you're looking for file-sharing or CDN, something like Google Drive or Amazon S3 may be your best bet, but definitely not Loker. This isn't a disadvantage to Loker, the service is meant for Maxis users to utilize as a file-storing service so in essence it's designed perfectly for what it's supposed to do.
<h2><strong>So what's so great about Loker?</strong></h2>
One thing I like about loker is that the interface isn't too cluttered, although obviously it lacks the simplicity of Google Drive, the web interface means its better than dropbox in terms of usage.

Also the 5GB free package is pretty generous and while you do get a 2GB free from dropbox (with the ability to add to that for free), I believe 5GB is just right in terms of a free package.

There's also a Downloadable program for your PC that creates a nice Loker folder on your desktop. The folder syncs automatically with the Loker servers allowing you to carry your information to multiple PCs ala Google Drive or Dropbox.

I actually prefer the Loker program as opposed to dropbox or even Google drive because it allows me to Manually sync the files myself, meaning that I'm not kept guessing if the files are synced or not. Syncing on Google Drive via my PC wasn't as easy as I expected and I kept running into 'unsyncable files' for unknown reasons. I believe this is because I tried to sync an .iso file which Google probably blocks, although dropbox synced it without a hitch. <em>FYI, the iso file was a downloaded Ubuntu image, so it's 100% legit.</em>

<strong>Comparison #1: Speed</strong>

I tried uploading a 40MB .flac file to both Maxis Loker and Google Drive, and I must say, Maxis was a tad bit faster, if only a tad bit.

The actual file size was 32MB and it managed to upload in about 1 minute on my unifi connection. Google took about 1 minuter15 seconds. So in terms of speed this is blazingly faster than their ebuuk portal.

I think I've figured out why it's so fast, but that's at the end of this post. Keep reading though.

<strong>Comparison #2: File Size</strong>

No where on the Loker site does it specify a maximum file size, but there is one. I've managed to upload a 150MB file with no problems, but a 300MB video failed instantly. So while the maximum file size for Maxis isn't clearly stated, I believe it's around 150MB to 300MB. Anything bigger than this is surely to fail, so no Blu-ray DVD rips here.

Google and Dropbox of course didn't suffer from the same fate. They gobbled up the 300MB file like it was breakfast.

Googles advertised maximum file size is 10GB, so that's a pretty big file size to be throwing around.

<strong>Comparison #3: Scale</strong>

Maxis lets you scale up to a 25GB package, for Rm25 a month. That's not really cheap, but it's reasonable.

Google lets you scale till the cows come home, while Dropbox takes you to 50GB for just Rm30 (roughly) a month, or 100GB for Rm60 a month.

<strong>Comparison #4: Price</strong>

Price and scale go hand-in-hand, but if you're looking for a good free service either one of the 3 would suffice if you ask me.

<strong>Comparison #5: Windows Application</strong>

While the PC application across the PCs are almost indistiguishable, I have to give Maxis the thumbs up here. I prefered their version ahead of everyone else, only because they provide the manual sync, and the best reporting while syncing. I know exactly how long the sync will take and which files have been synced. This is important to me, and represents good UI design.

<strong>Comparison #6: File Sharing</strong>

As I mentioned before this isn't a file sharing service. So file sharing is both cumbersome and limited to ONLY Loker users. So it's a good place to store your files and sync them across multiple machines, but not a good place if you'd like to share your wedding photos with relatives overseas.

Google and Dropbox don't suffer from the same limitation.
<h2>Conclusion</h2>
Like I said, I like the Loker service.

It's clean, it's simple, it was design for file-storage and it's a great add-on service from Maxis. It's not a great file-sharing service but there's a tonne of those around.

I'm also unable to review and comment on the Loker iPhone or Android app, particularly since <a title="Samsung Galaxy S3: I don’t have one" href="http://www.keithrozario.com/2012/06/samsung-galaxy-s3-maxis-bad.html">I was denied the chance to book the Galaxy S3 last Friday</a>. So I'd be happy to hear your thoughts if you use the service on your smartphone.
<h2>Why is Maxis Loker so fast?</h2>
Remember when I told you that the Maxis Loker service was faster than even Google drive, I was curious as to how Maxis pulled this off, and was hoping they hosed it on their own cloud, however a simple ping would point you to the answer:

![](/uploads/MaxisLokeronAWS.jpg "MaxisLokeronAWS")

I was actually unaware of this, till I did some more googling, and it appears Maxis Loker is actually running of a <a title="Maxis Launch Loker" href="http://www.sys-con.com/node/2286859" target="_blank">'white-lable' personal cloud solution from a company called Funambol</a>.

Funambol actually offers the entire to Maxis, and Maxis then offers it to it's customer. This is truly SaaS, but more along the lines of B2B2C SaaS, that's Business to Business to Customer SaaS. Quite interesting as I've never been aware such offerings were out there. This allows Companies like Maxis to deploy innovative offerings to their customers, without having to invest too deeply on Capex items like specialist staff or even hardware. Everything is run on a SaaS model by Funambol for Maxis, and Maxis then offers the same SaaS model to customers with a little branding and possibly a little profit margin as well.
<h2>Why Doesn't Maxis host the service on their own cloud?</h2>
I'm not by any means an IT guru, but I do believe that the ping points to an <strong>amazonaws.com</strong> url, this suggest that the Loker service is actually hosted on Amazon Web Services (AWS), which if hosted on the Amazons Singaporean data center, would explain why it's faster than Google.

Here the architecture is a bit clearer, AWS provides the Infrastructure to Funambol, who then provide the Application to Maxis on a SaaS model, till Maxis sells it to their customers via the same SaaS model.

This is interesting is because Maxis have their <a title="Maxis cloud" href="http://www.maxis.com.my/business/cloud/maxis_cloud.asp" target="_blank">own cloud offering</a> and data center in Shah Alam.  So the fact that Maxis chose to use Amazon ahead of their own cloud service is interesting.

Some might say, that's like the CEO of maxis having a 016 Digi number, but that's not the correct or even fair analogy, although its a funny one. It's like the CEO of Perodua been chauffeured in a Audi, while they're both technically cars, you don't expect your CEO to be chauffeured in a compact now do you?

Similarly, while Maxis does offer cloud services, they offer nothing close to what Amazon have in terms of scale OR functionality, so there's no way you could create a cloud storage solution like this for the millions of Maxis customers via the Maxis cloud (or least keep it economically viable).

Maxis don't have a storage solution like Amazons S3, so in order to provide you 25GB for Rm25, Maxis would have to procure their 'Optimum' package which has 160GB of storage for Rm1900 a month. That's not economically viable by a long shot.

I guess the conclusion would be that not all clouds are the same, and the Maxis cloud offering just doesn't fit with either the Loker application itself, or even the 'white-lable' model Maxis and Funambol chose.

What you do you think of the Maxis Loker Package? Does it sound interesting and useful, or just another product from Maxis destined for the trash can?

 