+++
title = "TM blocking SarawakReport"
date = "2015-07-19T21:58:36"
draft = false
categories = ['Copyright and Censorship', 'Malaysia']
+++

<a href="/uploads/Makluman-Notification-2015-07-19-21-49-53.png"><img class=" wp-image-5102 aligncenter" src="/uploads/Makluman-Notification-2015-07-19-21-49-53-756x500.png" alt="Website Blocked" width="550" height="364" /></a>Sarawakreport, a website covering sensitive political topics in Malaysia was <a href="http://www.themalaymailonline.com/malaysia/article/sarawak-report-blocked">blocked today by the countries most prominent ISP</a>, Telekom Malaysia (TM).

Internet users using TM's Domain Name Server (DNS) reported that the website was inaccessible, and I've confirmed that is an intentional block by TM.

Here's a quick primer on DNS. The internet works on this marvelous set a rules we've come to call the Internet Protocol. Part of this protocol requires that every server or machine on a network be assigned a unique number to identify itself, this number is called an IP address. An IP address is sort of the phone number of a server, and if you want to communicate with a server you'd need to know that servers phone number.

Now of course the internet is made of billions of websites, and so it comes with its own directory service. Older readers will remember dialing 103 on our local phone lines to talk to an operator to look up someones phone number, this is exactly the same concept. On the internet, this directory service is automatic, and comes with a cool name--Domain Name Server (DNS).

When you type google.com or keithRozario.com on your web-browser, the browser automatically looks up the IP address of the website you requested via a DNS server. And just like how you'd have to memorize 103 in order to call it, your computer is set to request DNS resolutions from a specific DNS server.

For most TM users, this is set to a DNS server with an IP address of 1.9.1.9, you can change this of course, but if you've never knew what a DNS was, chances are you're using TM's server to convert web addresses to IP addresses.

Now you can see the issue, if TM is the sole service that you use to convert website addresses to IP addresses, it has a lot of control. For instance it could block you from accessing porn sites (which it does), and of course it can block you from accessing 'controversial' political blogs like SarawakReport.

How do I know this? You can change the settings on your computer to use alternative DNS servers (Google and OpenDNS run great free services), and these DNS servers convert SarawakReport.org to IP addresses like 104.20.27.161<em> (note that most of the time popular websites have multiple IP addresses, but that's not important for now). </em>However, if you use TM's DNS server, SarawakReport.org converts to 175.139.142.25, which is an IP address owned by TM. This also explains why users who use Proxy servers or different DNS settings will not experience any issues.

[caption id="attachment_5103" align="aligncenter" width="550"]<a href="/uploads/TM-DNS.png"><img class="wp-image-5103" src="/uploads/TM-DNS.png" alt="TM-DNS" width="550" height="121" /></a> TM's DNS server resolving SarawakReport.org to 175.139.142.25[/caption]

Tsk, tsk, tsk.

If you do a reverse DNS lookup, essentially reversing the process of looking IP addresses corresponding to web urls, and instead lookup web-urls corresponding to IP addresses, you find that the same IP address is currently being used by Senyum.my--and that website has a glaring notice on the front page, signalling that the site is blocked for violating Malaysian law , that's the screenshot you see above.

Essentially TM routed all traffic destined for SarawakReport.org to a server they keep up for hosting a 'blocked' notice.

This is just so sad, I really don't know if I should laugh or cry. This method of blocking is so ineffective even a child would be able to bypass it.

For those wishing to access SarawakReport.org, please change your <a href="http://pcsupport.about.com/od/windows7/fl/change-dns-servers-windows-7.htm">DNS server settings in Windows</a>--a more effective way around the issue is to use a VPN, like the one I recommend here. A VPN provides a sure-fire way to bypass all the censorship that local ISPs can put in place.

Here's <a href="https://www.keithrozario.com/2013/09/best-vpn-malaysia-privateinternetaccess.html">my review of a VPN service you can use</a>, and hopefully you use my promo code to send some cash my way :). Even if you don't, it's OK though, I'm still cool.

*Update*

TheStar have confirmed that the <a href="http://www.thestar.com.my/News/Nation/2015/07/19/MCMC-block-sarawak-report/">MCMC has issued the directive to block</a> the website, something quite sad, seeing as how you already know how to circumvent the 'block'.