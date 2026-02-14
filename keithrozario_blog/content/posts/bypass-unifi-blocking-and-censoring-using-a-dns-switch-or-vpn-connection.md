+++
title = "Bypass Unifi blocking and censoring using a DNS switch or VPN connection"
slug = "bypass-unifi-blocking-and-censoring-using-a-dns-switch-or-vpn-connection"
date = "2012-03-06T23:43:38"
draft = false
tags = ['SOPA', 'Unifi']
categories = ['Copyright and Censorship', 'Malaysia']
+++

<p style="text-align: justify;">

![](/uploads/2731182967_e784c1f65e.jpg "2731182967_e784c1f65e")

If you're on Unifi you might have noticed that <a title="Unifi sites blocked" href="http://torrentfreak.com/pirate-bay-megaupload-others-blocked-by-government-order-110609/" target="_blank">some sites are blocked</a> and it's due to<a title="Wirawan SKMM censorship" href="http://wirawanweb.com/2011/06/09/mcmc-censoring-the-internet/" target="_blank"> government directives to block these sites. </a> Now that goes against what the Government of Malaysia promised it's stakeholders during the advent of the MsC, in which it promised to not censor the internet. If you remember, somewhere in August 2008, the government issued a similar directive to<a title="Malaysia Today Censor" href="http://en.wikipedia.org/wiki/Malaysia_Today#Censorship_by_the_Malaysian_Communications_and_Multimedia_Commission" target="_blank"> censor Malaysia Today</a>.</p>
<p style="text-align: justify;">So what's a average user to do to bypass these internet blocks. The blocks themselves are issued by the government and issued to all ISPs, fortunately there are a couple of ways to bypass these internet blocks which amount to censorship, and it depends on what kind of mechanism your ISP uses to block it. I'm all for a free internet and here are some ways you can bypass those blocks.<!--more--></p>

<h2>A Domain Name Server (DNS) block</h2>
<p style="text-align: justify;">So let's focus on the simplest mechanism the ISPs use to block the internet, and that's a DNS block. A Domain Name Server (DNS) is a server that works in a similar fashion to a phone directory-- you know that big book of phone numbers the telephone company use to give out.</p>

<h2>What is a DNS?</h2>
<p style="text-align: justify;">So imagine the internet was like your phone network, and every website you wanted to call had a phone number, you may know the websites name like www.google.com or www.keithrozario.com, but in order to actually visit any website you'd need to know it's IP address. A IP address is exactly like a phone number, in that once you have it you could just type it in an visit the website, however if you don't have the websites IP address you'd need to look it up. <strong>A DNS would act as a phone directory, just that in a phone directory you look up a phone number based on a persons name, in a DNS you look up an IP address based on a websites name. </strong>Your browser automatically looks up every link you try to visit via DNS, it's the only way it can find the IP addresses.</p>
<p style="text-align: justify;">A DNS block is simply removing the entry for a particular website from 'a' DNS server and if that server happens to be the DNS Server TM configures on all their customers routers, than the implications can be huge. Essentially TM can redact a persons name out of the telephone directory so that no one looking for that person will be able to connect to them.</p>

<h2 style="text-align: justify;">How do I bypass a DNS block? (Unifi has this)</h2>
<p style="text-align: justify;">Just use another DNS server. In the analogy before, Unifi is trying to block your access by preventing you from looking up phone number in phone directories Unifi has provided to you. What's to stop you from using another publicly available phone directory? The answer: nothing.</p>
<p style="text-align: justify;">All you have to do is to configure your network connection to lookup a separate DNS rather than the one recommended by TM (or Maxis or whoever your ISP is), my favorite is OpenDNS but there are others who prefer Google.</p>
<p style="text-align: justify;">The method is pretty simple, here's a <a title="Change DNS server" href="http://www.plus.net/support/software/dns/changing-dns-windows-8.shtml" target="_blank">step-by-step provided for Windows 8</a>, and <a title="MAC change DNS" href="https://support.apple.com/kb/PH6373?locale=en_US" target="_blank">this one for Macs</a>, here's the <a href="https://support.opendns.com/entries/42848890-Android-Configuration-instructions-for-OpenDNS">Android</a> and <a href="https://support.opendns.com/entries/42419230-iPhone-Configuration-for-OpenDNS">iPhone</a> version as well.</p>
<p style="text-align: justify;">For OpenDNS the settings are:</p>

<pre>DNS Server : <strong>208.67.222.222</strong>
Alternate DNS Server : <strong>208.67.220.220</strong></pre>
<p style="text-align: justify;">If you prefer Google then then:</p>

<pre>DNS Server : <strong>8.8.8.8</strong>
Alternate DNS Server: <strong>8.8.4.4</strong></pre>
On Windows your end result should look something like this:



![](/uploads/TCP_Settings.jpg "TCP_Settings")


<p style="text-align: justify;">I also have to stress, that changing your DNS server to OpenDNS has benefits above and beyond bypassing Unifis censorship. OpenDNS operates phishtank, which is a crowd-sourced application that signals out phishing websites and then blocks those websites via a DNS block. To a Layman what that means is that once you switch to OpenDNS, it'll offer you some protection, whenever you lookup a domain of a website that it believes to be malicious, you'll get a warning to inform you of the potential dangers.You can read up more<a title="OpenDNS" href="http://www.opendns.com/business-solutions/premium-dns/benefits/" target="_blank"> here</a>.</p>
<p style="text-align: justify;">Also OpenDNS operates a parental control DNS where it blocks access to sites marked as Adult content.</p>
<p style="text-align: justify;">This would easily by pass any DNS block your Internet service provider has set in place, but what if your ISP actually has a more sophisticated blocking mechanism. A DNS block is real kiddie stuff when it comes to online censorship and there should be other means to block users from accessing content and other means for users to bypass those blocking mechanisms.</p>
<span style="color: #888888;"><em>by the way, if you prefer Google over OpenDNS you might want to read<a title="Google vs. OpenDNS" href="http://blog.opendns.com/2009/12/03/opendns-google-dns/" target="_blank"> this</a>.</em></span>
<h2>What if my ISP is smarter than that?</h2>
<p style="text-align: justify;">In short there's a WHOLE lot of stuff your ISP can do that you probably don't know about. So a basic Virtual Private Network (VPN) would be the best option here.</p>
<p style="text-align: justify;">In a VPN setup, what actually happens is that you setup a connection to a private server and then use that server as a proxy for all your connections. This means that as long as your Internet Service Provider doesn't block the IP address of your VPN you can basically roam free. Another good reason to have a VPN is that they're 'usually' encrypted, so that your ISP can't look at what you're looking at, some VPN providers provide encryption so strong it would take a super computer millions of years to crack. While you may not be starting the next revolution or Arab Spring, sometimes it feels a bit uncomfortable especially in Malaysia to know that your ISP could potentially be spying on your personal data, and a good VPN is a solid way to prevent that from happening.</p>
<p style="text-align: justify;">So how do you setup a VPN. Well thankfully there's a free version you can try, and it's called <a title="proxpn" href="http://proxpn.com/" target="_blank">proXPN</a>. proXPN is a fantastic free VPN service that uses end-2-end encryption to keep the baddies and your local ISP out of your business, it utilizes a 2048 bit encryption. On the website, the company claims that:</p>

<blockquote>
<div><strong>With proXPN nobody* can...</strong></div>
<div>
<ul>
	<li>see the websites you visit</li>
	<li>hijack your passwords, credit cards, or banking details</li>
	<li>intercept and spy on your email, IMs, calls, or anything else</li>
	<li>record your web history</li>
	<li>run traces to find out where you live</li>
</ul>
</div></blockquote>
<p style="text-align: justify;">There's a downside however, the free version is throttled to just 100kbps (less than 10% of the slowest Unifi speed), and you need to use a specific application to access the service. The paid version doesn't have throttled speed but has an associated cost. If you're willing to pay for a VPN, consider trying a service called <a href="https://www.privateinternetaccess.com/">privateinternetaccess</a> (my review of it <a title="Best VPN for Malaysians : Privateinternetaccess" href="https://test.keithrozario.com/2013/09/best-vpn-malaysia-privateinternetaccess.html">here</a>), which is just as good and it's cheaper, plus the affiliate program I have with them help provide for this blog. More importantly, I use them as well.</p>
<p style="text-align: justify;">When you use a VPN, no man-in-the-middle like TM can even detect which website you're visiting as ALL your communication is encrypted. Some VPN providers don't protect against DNS-leak, which may cause issues, but private internet access <a href="https://www.privateinternetaccess.com/pages/client-support/">specifically addresses this</a>.</p>

<h2 style="text-align: justify;">BolehVPN : Malaysias Best VPN provider</h2>
<p style="text-align: justify;">If you're looking to support  a local organization, the guys over at <a title="Boleh VPN" href="http://www.bolehvpn.net/" target="_blank">bolehvpn </a>are doing a pretty good job as well. While they don't have a free version to offer, they do have a <span style="text-decoration: underline;">RM5 offering that last 2 days</span>, and depending on your needs that could be good enough. I've used bolehvpn and can vouch for it's quality and service.</p>

<h2 style="text-align: justify;">Conclusion</h2>
<p style="text-align: justify;">The best way around a DNS Block like the one Unifi currently has on some websites, is to just change your DNS settings to OpenDNS or Google.</p>
<p style="text-align: justify;">However, given that you may need extra security a VPN server like proXPN or BolehVPN or Privateinternetaccess would be your best bet to bypass any damn filter your ISP may throw at you, plus it'll keep your internet browsing away from pesky eyes.</p>
<p style="text-align: justify;">Of course this doesn't mean anything if your local Wi-Fi at your home is compromised, so do yourself a favor and <a title="6 Things to do when you have Unifi installed" href="http://sawanila.com/v10/2011/03/6-things-to-do-when-you-got-your-unifi-wireless-router-d-link-dir-615/" target="_blank">read this</a> if you just recently had Unifi installed at your home, and I would add changing DNS server to that list of things to do.</p>
<p style="text-align: justify;">With censorship rearing it's ugly head in Malaysia, I may have to encourage other more drastic measures like using a remote desktop to an Amazon EC2 machine to download sensitive material. For now, happy hunting.</p>
<p style="text-align: justify;"><span style="color: #888888;">picture of roadblock courtesy of : <a href="http://www.flickr.com/photos/simon-james/2731182967/"><span style="color: #888888;">http://www.flickr.com/photos/simon-james/2731182967/</span></a></span></p>