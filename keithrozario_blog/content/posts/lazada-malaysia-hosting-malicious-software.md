+++
title = "Google: Lazada.com.my Malaysia is hosting Malware"
slug = "lazada-malaysia-hosting-malicious-software"
date = "2012-08-08T13:57:11"
draft = false
categories = ['Malaysia']
+++

![Lazada Infected by Malware Warning from Google](/uploads/lazada_malware_waning.jpg "lazada_malware_waning")
<h5><em>Lazada.com.my contains malware. Your computer might catch a virus if you visit this site. Google has found malicious software may be installed on your computer if you proceed.</em></h5>
WOW, Lazada Malaysia apparently has been infected with some rather nasty infection. My version of Google Chrome prompted this when I tried to visit the site today. Hope everything is alright over there in Lazada headquarters.

In fact, Google is populating it on their search results as well, must be a rather nasty one:

![](/uploads/Lazada_malware_google_search.png "Lazada_malware_google_search") 

It can get really nasty trying to disinfect a site. Good luck to the guys over at Lazada, what's more worrying if Lazada actually carried credit card and personal data, I wonder if they secured it thoroughly and whether this breach could point to something even more serious over at Lazada headquarters.

We can only wait and see.
<h2><strong>Update 1: Digging deeper</strong></h2>
Further checks on the <a title="Diagnostic page for www.lazada.com.my" href="http://safebrowsing.clients.google.com/safebrowsing/diagnostic?site=http%3A%2F%2Fwww.lazada.com.my%2F&amp;client=googlechrome&amp;hl=en-US" target="_blank">Google Safe Browsing diagnostic report for lazada.com.my reports </a>no malicious software present:
<blockquote>Of the 793 pages we tested on the site over the past 90 days, 0 page(s) resulted in malicious software being downloaded and installed without user consent. The last time Google visited this site was on 2012-08-07, and suspicious content was never found on this site within the past 90 days.</blockquote>
So what could be the issue? Well according to Google and some searches I made, Lazada is hosted on Rackspace servers in Hong Kong, and <a title="Diagnostic page for AS45187 (RACKSPACE)" href="http://safebrowsing.clients.google.com/safebrowsing/diagnostic?site=AS:45187&amp;client=googlechrome&amp;hl=en-US" target="_blank">Google have reported that these Rackspace servers were used to serve up malicious content to users</a>:
<blockquote>Of the 1484 site(s) we tested on this network over the past 90 days, 9 site(s), including, for example, <a href="http://safebrowsing.clients.google.com/safebrowsing/diagnostic?site=chinafpga.com/&amp;client=googlechrome&amp;hl=en-US">chinafpga.com/</a>, <a href="http://safebrowsing.clients.google.com/safebrowsing/diagnostic?site=ourebiz.net/&amp;client=googlechrome&amp;hl=en-US">ourebiz.net/</a>,<a href="http://safebrowsing.clients.google.com/safebrowsing/diagnostic?site=devicewell.cn/&amp;client=googlechrome&amp;hl=en-US">devicewell.cn/</a>, served content that resulted in malicious software being downloaded and installed without user consent.

The last time Google tested a site on this network was on 2012-08-07, and the last time suspicious content was found was on 2012-08-06.</blockquote>
Could it be that Google is wrongly penalizing Lazada just because it shares the same servers as suspected malicious sites?

We'll have to wait and see. This could prove very damaging for a lot of sites hosted on IaaS providers like AWS and Rackspace. Especially if you can get penalize just because you're on the same network as malicious sites.

On a flip side, Firefox users don't see the warning, but the <em>"This site may harm your computer message"</em> still appears on the Google Searches.
<h2><strong>Update 2: Problem resolved</strong></h2>
Ok, the problem seemed to be neither the fact that Lazada was hosted on Rackspace (sorry guys!) or that it had a link to offerstation.com (an infected site).

I'm not entirely sure what the problem is, but it seems to be resolved now. Google has also updated it's safe browsing diagnostic page to reflect the breach. Now a quick check on the<a title="Google Safe Browsing Lazada.com.my" href="http://www.google.com/safebrowsing/diagnostic?site=http://www.lazada.com.my" target="_blank"> Lazada.com.my safe browsing page reveals</a>:
<blockquote><strong>What is the current listing status for www.lazada.com.my?</strong>

This site is not currently listed as suspicious.

Part of this site was listed for suspicious activity 2 time(s) over the past 90 days.

<strong>What happened when Google visited this site?</strong>

Of the 811 pages we tested on the site over the past 90 days, <strong>3 page(s) resulted in malicious software being downloaded and installed without user consent</strong>. The last time Google visited this site was on 2012-08-08, and the last time suspicious content was found on this site was on 2012-08-07.</blockquote>
Whatever it was the problem looks to be resolved. I can't help but wonder what it was...

Would someone from Lazada help me understand what went wrong here?

To view the full Google Safe Browsing Diagnostic page for Lazada.com.my, enlarge the image below:

![Google Safe Browsing diagnostic page for www.lazada.com.my](/uploads/Google-Safe-Browsing-diagnostic-page-for-www.lazada.com_.my_.png "Google Safe Browsing diagnostic page for www.lazada.com.my")