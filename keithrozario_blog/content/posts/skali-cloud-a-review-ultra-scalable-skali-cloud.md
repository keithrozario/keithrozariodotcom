+++
title = "Skali Cloud: A review ultra-scalable skali Cloud"
date = "2012-06-11T12:57:44"
draft = false
tags = ['Skali']
categories = ['Cloud Computing']
+++

<a href="/uploads/Design-your-perfect-Server.png"><img class="alignleft size-medium wp-image-1952" title="Design your perfect Server" src="/uploads/Design-your-perfect-Server-300x136.png" alt="" width="300" height="136" /></a>A couple of months back, I wrote a small article about the <a title="Design your perfect server with Skali Cloud" href="http://www.keithrozario.com/2012/04/design-your-perfect-server-with-skali-cloud.html">Skali Cloud</a> and how I liked the niche approach they took to cloud computing. Skali offers a very unique ultra-scalable instances that can be attached to physical machines of variable performances and storage space. In normal English, that just means you can actually the processor speed, amount of RAM and even storage space of your machine (<em>ok that wasn't 'normal' English</em>).

In contrast, Amazon and every other cloud offering I know of, offer a specific number of machine types (usually 3 to 8) that come in fixed configurations with respect to processor speed, RAM and storage. The great thing about Skali is that if you have certain applications that would require high processing speed with minimum RAM, you can literally create a physical machine that fit your needs exactly. If you used Amazon for example, you'd have to acquire very large instance types on Amazon and usually pay a high premium for storage and memory that you really don't need. Similarly for applications that don't require high processing speed, but high amounts of memory instead could equally benefit from creating highly customized virtual machines to suit your performance needs.

A couple of weeks back, a commenter on <a title="Design your perfect server with Skali Cloud" href="http://www.keithrozario.com/2012/04/design-your-perfect-server-with-skali-cloud.html" target="_blank">my Skali cloud post</a> and thanked me for the post, that commenter turned out to be <a title="https://twitter.com/tengkufarith" href="https://twitter.com/tengkufarith" target="_blank">Tengku Farith</a>, the founder of Skali. So I wrote back requesting a small trial setup, and within a few days I manage to setup a trial account with Rm200 credit on the Skali cloud. (pretty awesome!) So I manage to wriggle a couple of hours to spend time toying around with the Skali cloud and here's what I found:<!--more-->
<h2>Initial impressions</h2>
<a href="/uploads/Skali_Cloud.png"><img class="size-medium wp-image-2267 alignleft" title="Skali_Cloud" src="/uploads/Skali_Cloud-300x242.png" alt="" width="300" height="242" /></a>The Skali interface is in keeping with their purple theme of Skali and has a nice clean look to it. I'm not sure if most of you would use the interface rather than the API, but the interface does its job fairly well. One cool thing about the interface is it lets you perform a hard stop and hard reset directly from the interface. I was also fairly surprised by the distinction between drive and server, I found it pretty interesting at first, and then I discovered the necessity to  make the distinction even from the interface.

There's a couple of things that make Skali different from other cloud providers, firstly it offers ultra-scalability rather than a cookie-cutter approach to virtual machine specifications. Secondly it actually offers drives (which are distinct from servers) that you can mount on various devices for data persistence across machine of various types, even across different operating systems. Think of these drives as Amazon EBS volumes, but with a highly customize-able storage space.
<h2>Ultra-Scalability</h2>
I'm not sure why Skali took the 'ultra-scalable' approach, but I can imagine a couple of scenarios where this would be worthwhile. For instance, high-end computation on small amounts of data would require a machine with large amounts of processing speed but minimal memory and storage. If you wanted to crack 6 million hashed passwords, you'd just take a 2GB RAM machine with the maximum amount of processing power and just enough storage to see you install and OS and your cracking tools. This would result in a far more efficient machine suited to your needs as opposed to buying very powerful processors that come bundled with high memory and storage you don't need.   <em>(I'm just guessing password cracking is a processing intensive operation) </em>

<img class="alignright  wp-image-2269" title="Configuration_Menu" src="/uploads/Configuration_Menu-300x133.png" alt="" width="400" height="177" />The first thing you do with Skali is to create a server, I think it's more apt to call this a server image similar to an Amazon Machine Image. Once you've got your image ready you can start the server, but now you can have a whole host of configuration tools at your disposal before you kickstart the server, most notably the amount of processing speed, memory and storage. You can click on the image to see a much bigger screen of the Skali configuration options, these include firewall settings, network IP and even VNC password.

While you can't change the configurations on the fly, you can quite easily stop the machine and change the configurations from the GUI before restarting the machine again. You may not like this approach, I don't either, I would have preferred the ability to do something like 'configure next reboot', so that I can set the configuration before hand and only after I'm happy with it, commit it on the next reboot of the server. Saving me precious downtime.

This is Skalis big selling point, and like all niche selling points it probably only appeals to a small sub section of cloud users. However,  a small sub section of the cloud computing industry is more than enough for any company to thrive.
<h2>What's the deal with Drives?</h2>
<a href="/uploads/Multipledrives.png"><img class="size-medium wp-image-2270 alignleft" title="Multipledrives" src="/uploads/Multipledrives-300x177.png" alt="" width="300" height="177" /></a>While Skali prominently displays their ultra scalable cloud as their main selling point, lurking within their offering is a rather unique and somewhat unknown (at least to me) feature that really excited me.

Skali allows you to create 'drives' on their cloud, similar to an EBS on Amazon, however they call it drives for good reason. Just like Amazon, you can attach multiple drives to a server instance and migrate the drives across multiple instances. The one limitation is that each drive can only be attached to one instance at a time, once again--similar to Amazons EBS.

However, the one cool thing Skali offers that Amazon EBS doesn't (yet!) is that you can grow and shrink the drive directly from the interface, <em>Skali does however warn you about losing data when shrinking drives</em>. The one big drawback here is that you can't do this while the drive is mounted, and I couldn't figure out how to unmount the drive other than stopping the instance it was attached to. I would have preferred the ability to unmount a drive from the interface, grow it and re-attach it without having to start/stop the instance, but I guess this is a technical limitation that Skali can't do much about. You can also copy the drive, but that also requires the instance to be stopped. Drawbacks aside, changing the size of the drive in just one step is a pretty neat feature.

In contrast, the recommended way to do this in Amazon is to create a <strong>new</strong> EBS volume, create a copy of your current EBS volume, and then copy your existing snapshot onto the new volume. I have a strong feeling this is exactly the same approach Skali takes, its just that their interface hides this complexity from the user. Thereby simplifying a multiple step process into just 1 step.

I had some difficulty mounting additional drives on my windows machine, only to find out that drives come un-formatted (duh!). So if you're hoping to mount a drive, make sure you mount it and then format it so that it's visible from the OS. I didn't try moving drives around instances, but I believe based on the format of the drive this shouldn't be a problem.
<h2>Tight VNC</h2>
Amazon offers RDP straight out of the box for windows instances on EC2, Skali doesn't.

Skali recommends you use tight VNC for remote access, and send you a nice starter kit with a PDF on how exactly to go about doing this. I found this a tad bit irritating, because I'm so used to RDP but I can live with it. In the end, if things got really bad, I could just enable RDP connectivity once the instance is up and running.

Of course in some companies they have strict guidelines about installing applications like tight VNC, and requiring the installation of a new application onto your local machine isn't something terribly convenient.

<em>*Upon further thinking, I believe I know why this is the case. Skali actually had a brand new instance of windows installed for me via a CD install onto their virtual machine. Windows doesn't come with RDP natively activated, so I think there in lies the problem. I think this would have been solved if I used the <strong>subscription based</strong> windows instance rather than a <strong>'boot from cd'</strong> one.  So neglect this one.</em>
<h2>API</h2>
Never really tried the API as my knowledge of programming is somewhat limited, but I guess having an API is better than no API.
<h2>Conclusions</h2>
I actually liked my experience with Skali,<a title="Design your perfect server with Skali Cloud" href="http://www.keithrozario.com/2012/04/design-your-perfect-server-with-skali-cloud.html"> although their price could do with a little discounting</a>. The overall feel of the interface was nice, although their beta control panel had some issues shutting down my windows instance, I had to hard shutdown the machine everytime I wanted to turn it off.

However, the main selling point for Skali has always been its ultra-scalability. The trial version of Skali didn't really allow me to utilize the most powerful machine type they had (a whoooping 20Ghz of processing power), I did give multiple configurations a try and it was a fairly simple process. Although I would love to get my hands on a 20Ghz machine, the trial version has limitations on the more expensive machine types, even though your RM200 credit should be able to cover it for a good day or two.

The drive concept was also cool, allowing multiple drives to be mounted on a single instance. This plus the ability to grow and shrink the drive at will was a cool feature to have.

That being said, cloud computing is a price game, and price wise its difficult to see Skali beat Amazon. The fact that they moved into a niche market is good, but at some point the price difference may be too great for any local based company to compete head-to-head with behemoths like Amazon, Google and Microsoft <em>(who have announced their IaaS intentions pretty clearly).</em>

There is one niche I've failed to mention. For legal and fiscal reasons,  certain data can't leave Malaysian shores. So if you run a website collecting credit card or personal data of Malaysian citizens for Malaysia, you may have to ensure that the data collected doesn't leave Malaysia (even for a second). In that case you need a Malaysian cloud provider, and Skali could be just what you're looking for, or you could try Maxis.

Thanks Skali for the trial it was quite a cool experience, and good luck!

<a title="www.skalicloud.com" href="www.skalicloud.com" target="_blank">www.skalicloud.com</a>

&nbsp;