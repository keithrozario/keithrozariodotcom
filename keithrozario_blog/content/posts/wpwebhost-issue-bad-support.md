+++
title = "My Issue with WPWebHost: Bad Support"
slug = "wpwebhost-issue-bad-support"
date = "2014-05-22T08:00:52"
draft = false
tags = ['WPWebHost']
categories = ['Blog', 'Malaysia']
+++

<span style="font-size: 13px;"><a href="/uploads/WPWebHost-Logo.jpg">![WPWebHost-Logo](/uploads/WPWebHost-Logo.jpg)</a></span>

Last weekend I had an issue with my hosting provider, WPWebHost.

I switched to <a title="WPWebHost : WordPress Hosting in Malaysia from Exabytes" href="http://www.keithrozario.com/2012/09/wpwebhost-wordpress-hosting-malaysia-exabyte.html">WPWebHost 2 years ago,</a> and recommended them because they promised wordpress hosting at an affordable rate. Wordpress hosting is where the hosting provider would support wordpress specific features, e.g. help troubleshoot plugin and theme issues, perform nightly backups, and offer 'higher availability' for Wordpress sites. If you're still wondering what Wordpress is, take a look at one of my <a title="What is wordpress?" href="http://www.keithrozario.com/2012/07/what-is-wordpress.html">previous post.</a>

My latest experience with WPWebHost has left me wondering if indeed this was actually Wordpress hosting or just regular hosting in disguise. I'm now wondering if I should stay with them.

Was my server really getting the 99% uptime promised by WPWebHost? <strong>Nope.</strong>
Did I get the Wordpress Specific support that help identify theme and plugin issues? <strong>Nope.</strong>
Does WPWebhost cost more than regular hosting from other providers like GoDaddy, Dreamhost and my previous provider NearlyFreeSpeech? <strong>Yup.</strong>
So why I am still with them? <strong>Read more to find out.</strong>

Below is the full un-redacted transcript of my email correspondence with WPWebhost--I've left out the customer service agents name because I believe they have a right to privacy. However, nearly every time I sent an email, a different rep would respond making the whole conversation very messy and difficult to keep track off. Some emails were left out to simplify the flow.

<!--more-->
<blockquote>Hi There,

I'm from keithrozario.net

My website has been done quiet frequently the past 4-5 days. Would you be
able to check.

Thanks.

Keith</blockquote>

<hr />

 
<blockquote>Dear Keith,

Good day! Please elaborate on your inquiry, do you mean website is showing errors intermittently?

If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>
At this point, I'm wondering what else could I elaborate on, and if WPWebhost are doing nothing more than just reply for the sake of replying.
<blockquote>Yes, intermittently I can't access getting 500 internal server error, or can't find webpage etc.

I have two services that monitor the uptime of the site, here's a snapshot of just today. Too many downtimes, and this is not acceptable.

Regards,
Keith</blockquote>

<hr />

 
<blockquote>Dear Keith,

We have checked and found that your account is hitting the virtual memory limit of the server due to which you will get internal server errors on your sites.

We will suggest you to optimize your scripts and databases by contacting your web-developer. We will also suggest you to un-install any unwanted themes, plugins, modules and components installed for the sites.

Currently we can see that the following links is causing high virtual memory usage for your account:

[whole bunch of links]

If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>

<hr />

 
<blockquote>Hi,

I don't have a web developer, the entire site runs on Wordpress.

Your explanation is unacceptable, I chose WPWebhost because you guys promise Wordpress specific support. If this is a theme/plugin issue, find out which component is having the issue and revert.

I haven't performed any updates on any themes or plugins in the last 5 days, so it can't be anything related to it, but please investigate further and revert.</blockquote>

<hr />

 
<blockquote>Dear Keith,

Kindly allow some time to check on this and get back to you. Your patience is appreciated.

If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>

<hr />

 
<blockquote>Dear Keith,

Sorry for the delay.

I can see your website has hit server virtual memory which we have limit for shared hosting package, each account been assign to 512MB of virtual memory to ensure that all account using same resources under server.

From the previous 3 days log, I could see that sometime your website showing 500 Internal Error is due to hit the maximum of virtual memory and hit the maximum of the CPU usage.

==========================================================

Below are URL which hitting internal server error when memory is full
==========================================================
<strong>1 https://www.google.ru/</strong>
1 http://www.google.com/url?sa=t&amp;source=web&amp;cd=2&amp;ved=<span style="color: #888888;">(<em>url ommitted because too long)</em></span>
2 http://www.google.com.mx/url<span style="color: #888888;"><em>(url ommitted because too long)</em></span>
2 http://www.google.com.np/url<em><span style="color: #888888;">(url ommitted because too long)</span></em>
2 http://www.google.com.sg/search
2 http://www.keithrozario.com/2012/04/kindle-malaysia-buying-ebooks-amazon.html
2 http://www.keithrozario.com/2012/09/port-forwarding-unifi-dlink-dir-615.html
2 http://www.keithrozario.com/2012/09/setting-up-dlink-ddns-unifi-router.html
2 http://www.keithrozario.com/2012/09/wpwebhost-wordpress-hosting-malaysia-exabyte.html
2 http://www.keithrozario.com/2014/01/hack-unifi-in-5-minutes.html
2 http://www.keithrozario.com/tech-evangelist
3 http://www.keithrozario.com/wp-login.php?action=register
4 http://keithrozario.net/wp-login.php
<strong>4 https://www.google.com/</strong>
<strong>4 https://www.google.com.ph/</strong>
4 http://www.keithrozario.com/
4 http://www.keithrozario.com/2012/02/4-ways-to-add-pinterest-pin-it-button-to-wordpress.html
4 http://www.keithrozario.com/2013/04/f-secure-hackathon-malaysia-result.html
4 http://www.keithrozario.com/2013/08/asus-unifi-rt-n12-hp.html
6 http://www.keithrozario.com/2013/08/hack-unifi-default-password.html
7 http://www.keithrozario.com/feed/atom
8 https://www.google.com.my/
10 http://www.keithrozario.com/2012/07/change-unifi-password-wifi-dlink.html
10 www.keithrozario.com/wp-login.php
359
==========================================================

You are advice to perform below step to reduce memory usage for your website.

<strong>1) remove unwanted plugin or module</strong>
<strong> 2) optimized your website plugin (may try to disable plugin to verify if help)</strong>

<strong>If you confirm that your website running on best configuration, you are advice to upgrade your account to next level which is allow more virtue memory to your hosting package.</strong>

To understand the output on screenshot please refer the below, Output:
ID : LVE Id or username
aCPU : Average CPU usage
mCPU : Max CPU usage
lCPU : CPU Limit
aEP : Average Entry Processes
mEP : Max Entry Processes
lEP : maxEntryProc limit
aMEM : Average Memory Usage
mMEM : Max Memory Usage
lMEM : Memory Limit
VMemF : Out Of Memory Faults
MepF : Max Entry processes faults
If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>
At this point of course, I get a bit mad. Not only is he not offering my any help on the plugins or themes which he claims may be my problem, he's advising to upgrade my account. This turns out to be bad advice because the fault was with the server and not with my plugins or themes, had I upgraded I would have been wasting my money. I wonder how many WPWebhost customers may have been 'recommended' to upgrade their account when they didn't have to.

No matter what kind of support you provide, even the most basic technician will know that obviously any issue with my website can't be because of Google. Yet, he proudly puts and tells me<em> "Below are URL which hitting internal server error when memory is full"</em>
<blockquote>Hi,

Thanks for the report, but this doesn't help me. I understand 512MB, but I don't understand how google.com and google.com.ph is in any way impacting my site. How can Google issues trouble me?

Secondly, my website doesn't serve videos or heavy-duty content--videos are all youtube links, and the biggest files I store on the website are photos that are hardly 1MB each in size.

Thirdly, my site gets around 500-600 hits a day, which means only 18,000 hits month. You guys promise 30,000 hits a month for the smaller plan. Why do you recommend me to upgrade when have far less hits than number you suggest.

If you can't help me, please patch me through to your sales manager for me to speak to.

My feeling is something is wrong with your server, I don't know what your architecture is, but the issue is only now impacting me, and I have done nothing to change the site.

Regards,
Keith</blockquote>

<hr />

 
<blockquote>Dear Keith,

Apologize for the extreme delay.

Kindly let me consult my senior for further assistance.

Your patience is much appreciated. Please hold on.

If you have any enquiries, please do not hesitate to contact us. Thank You!

<hr />

 

Dear Keith,

As per checking with my senior engineer, he suggest migrate your hosting to other server. After migrate to other, we will verify if your website will still hit the virtual memory.

Please confirm with us if you wish us to perform the migration.

Awaiting for your reply.</blockquote>

<hr />

 
<blockquote>agreed. I still own the keithrozario.com domain, please let me know the IP address once you've migrated it for me to change the DNS entry.

However you manage the keithrozario.net domain, so you will have to change that.

Regards,
Keith​</blockquote>

<hr />

 
<blockquote>Hello Keith?

We shall schedule on the migration for weekend and will get back to you on this. We appreciate your patience in this regards as we shall update you before and after the migration is done.

If you have any enquiries, please do not hesitate to When can you complete migrating the server?</blockquote>
Regards,
keith

<hr />

 
<blockquote>Dear Keith,

Due to there is some problem to the server, we will continue migration once the server is back to normal.
If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>

<hr />

 
<blockquote>Dear Keith,

We are still working on your account migration process. We will update you once the migration is done.

Meanwhile, we appreciate your patience and understanding.

If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>

<hr />

 
<blockquote>Hi,

Give me a time and date.

Regards,
Keith</blockquote>

<hr />

 
<blockquote>Dear Keith,

Due to server is not stable at the moment. I will delay the migration.

Our migration department will arrange the time and date with you once they resume duty.

Apologize for the issue caused to you.

 </blockquote>

<hr />

 
<blockquote>Dear Keith,

We apologize for the inconvenience caused to you.

The server is normal at the moment. Kindly confirm if we can proceed with the migration now.

If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>

<hr />

 
<blockquote>Dear Keith,

We have proceed to migrate your account to another server (72.18.130.154).

C:\&gt;ping keithrozario.net

Pinging keithrozario.net [72.18.130.154] with 32 bytes of data:
Reply from 72.18.130.154: bytes=32 time=338ms TTL=51
Reply from 72.18.130.154: bytes=32 time=338ms TTL=51
Reply from 72.18.130.154: bytes=32 time=344ms TTL=51
Reply from 72.18.130.154: bytes=32 time=411ms TTL=51

Ping statistics for 72.18.130.154:
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
Minimum = 338ms, Maximum = 411ms, Average = 357ms

Please clear DNS cache of your machine
https://support.exabytes.com.my/KB/a1953/how-to-flush-dns-cache-from-your-computer.aspx

Also add your domain temporarily in the hosts file of your computer to check the website.
https://support.exabytes.com.my/KB/a2877/dns-host-file.aspx

If you have any enquiries, please do not hesitate to contact us. Thank You!</blockquote>

<hr />

 
<blockquote>Dear Keith,

Please be advised that the migration has completed. Kindly note that the cpanel username and password details will remain the same.</blockquote>

<hr />

 
<blockquote>Thanks everything appears fine for now. Will monitor and revert.</blockquote>
Eventually the problem is fixed, but this took a couple of days to resolve.

Honestly, I don't expect much for the USD6.95 I fork out every month, but I expect better service than this. Also, I recommended WPWebhost because I felt the less tech-savvy readers could get straight to blogging without worrying about the details, however on two occasions I was prompted to do my own support, and was wrongly told this was a plugin problem when it was clearly a server issue that was fixed after migration.

I still think these guys are worth the money, <a title="One year of Blogging on Nearlyfreespeech" href="http://www.keithrozario.com/2012/04/one-year-of-blogging-on-nearlyfreespeech.html">Nearlyfreespeech provided no support</a>, but <a title="Nearlyfreespeech, how much does it really cost? Just $3.60" href="http://www.keithrozario.com/2011/09/nearlyfreespeech-cost.html">were really cheap</a>....but I'm re-thinking my recommendation of WPWebhost.

To be fair, they did fix the problem, albeit after some persuasion--and they did earn some of my loyalty when they persevered through a tough migration for me. So I'm sticking with them for now, even if the only reason is that they did a good job 2 years ago.

Rest assured though--that good will won't last forever.