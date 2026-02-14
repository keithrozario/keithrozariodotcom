+++
title = "The GREAT .my outage of 2018"
slug = "the-great-my-outage-of-2018"
date = "2018-06-23T11:22:30"
draft = false
tags = ['DNSSEC', 'MYNIC']
categories = ['Malaysia', 'Security &amp; Privacy']
+++

[caption id="attachment_6436" align="aligncenter" width="550"]<a href="/uploads/DNSKEY-Fail.jpg">![.my DNSKEY Failure](/uploads/DNSKEY-Fail.jpg)</a> Boy, that's a lot of RED![/caption]

Last week, MyNic suffered a massive outage taking out any website that had a <code>.my</code> domain, including local banks like maybank2u.com.my and even government websites hosted on <code>.gov.my</code>.

Here's a great report on what happened from <a href="https://ianix.com/pub/dnssec-outages/20180615-my/">IANIX.</a> I'm no DNSSEC expert, but here's my laymen reading of what happened:
<ol>
 	<li><code>.my</code> uses DNSSEC</li>
 	<li>Up to <a href="http://dnsviz.net/d/my/Wx5EtQ/dnssec/">11-Jun</a>,<code>.my</code> used a DNSKEY with <code>key tag:25992</code></li>
 	<li>For some reason, this key went missing on the <a href="http://dnsviz.net/d/my/WyNgLA/dnssec/">15-Jun</a>, and was replaced with DNSKEY <code>key tag:63366</code>. Which is still a valid SEP for <code>.my</code></li>
 	<li>Unfortunately, the DS record on root, was still pointing to <code>key tag:25992</code></li>
 	<li>So DNSSEC starting failing</li>
 	<li><a href="http://dnsviz.net/d/my/WyQtVw/dnssec/">15 hours later</a>, instead of correcting the error, someone tried to switch off DNSSEC removing all the signatures (RRSIG)</li>
 	<li>But this didn't work, as the parent zone still had a DS entry that pointed to <code>key tag:25992</code> and hence was still expecting DNSSEC to be turned on.</li>
 	<li><a href="http://dnsviz.net/d/my/WyQtVw/dnssec/">5 hours after that</a>, they added back the missing DNSKEY <code>key tag:25992</code> <em>(oh we found it!)</em>, but added invalid Signatures for all entries -- still failing.</li>
 	<li><a href="http://dnsviz.net/d/my/WySnIA/dnssec/">Only 4 hours</a> after that did they fix it, with the proper DS entry on root for DNSKEY <code>key tag:63366</code>and valid signatures.</li>
 	<li>That's a 24 hour outage on all <code>.my</code> domains.</li>
</ol>
So basically, something broke, they sat on it for 15 hours, then tried a fix, didn't work. Tried something else 5 hours after that, didn't work again! And finally after presumably a lot of praying to the Gods of the Internet and a couple animal sacrifices, managed to fix it after a 24-hour downtime.

I defend my fellow IT practitioners a lot on this blog, but this is a difficult one. Clearly this was the work of someone who didn't know what they were doing, and refused to ask for help, instead tried one failed fix after another which made things worse. As my good friend Mark Twain would say -- <a href="https://www.worldofbuzz.com/watch-this-video-of-a-datuk-hilariously-translating-peribahasa-on-live-tv/">it's like a Mouse trying to fix a pumpkin</a>.

I don't fully understand DNSSEC (it's complicated), but I'm not in charge of a TLD. It's unacceptable that someone could screw up this badly -- and for that screw up to impact so many people, and all we got was a lousy press release.

The point is, it shouldn't take 24 hours to resolve a DNSSEC issue, especially when it's such a critical piece of infrastructure. I've gone through <a href="https://ianix.com/pub/dnssec-outages.html">reports of similar DNSSEC failures</a>, and in most cases recovery takes 1-5 hours. The<code> .nasa.gov</code> TLD had a similar issue, that was resolved in an <a href="https://ianix.com/pub/dnssec-outages/20171007-nasa.gov/">hour</a>, very rarely do we see a 24 hour outage, so what gives?

I look forward to an official report from MyNIC to our spanking new communications ministry, and for that to be shared to the public.<!--more-->
<h2>Resilience on the Internet</h2>
But this does give us an opportunity to talk about resilience on the internet -- because as great as it is, the Internet is <strong>not</strong> 100% reliable.

It's built on lots of infrastructure that we take for granted, and every once in a while, that infrastructure fails. There is no such thing as a 100% uptime, not even with companies like Google or Amazon. In 2017, Amazon messed up their S3 offering, and caused an Internet catastrophe by taking out (at least according to <a href="https://www.theregister.co.uk/2017/03/01/aws_s3_outage/">The Register</a>):
<blockquote>Docker's Registry Hub, Trello, Travis CI, GitHub and GitLab, Quora, Medium, Signal, Slack, Imgur, Twitch.tv, Razer, heaps of publications that stored images and other media in S3, Adobe's cloud, Zendesk, Heroku, Coursera, Bitbucket, Autodesk's cloud, Twilio, Mailchimp, Citrix, Expedia, Flipboard, and Yahoo<i>!</i> Mail (which you probably <a href="https://www.theregister.co.uk/2017/02/16/yahoo_forged_cookie_hack_risk/" target="_blank" rel="noopener">shouldn't be using</a> anyway)</blockquote>
Even after spreading your infrastructure across the globe, in various datacenters, from various cloud providers, you're still reliant on the Internet itself to transport your packets from point A to point B. And that's are just one <a href="https://bgpmon.net/massive-route-leak-cause-internet-slowdown/">BGP screw up away from going down</a>.

And even when the network is working, and the datacenters are fine, there's still a chance you (or your sysadmin)will crash your little house of cards all on your own.

Nothing has 100% uptime -- and there's a balance to be struck between getting as close to 100% and spending that money elsewhere.

<strong>Can I sue MyNIC?</strong>

I'm no lawyer, but I don't think a registrar charges tens of US dollars per year, can't be sued for thousands of dollars in lost revenue, that's just not the way things work. If that were true, every restaurant could sue the Water company when they cut the water supply, and every factory could sue Electric company for lost productivity -- all of that liability is bound to increase the price of the utility, and that's bad for everyone.

But just how do you avoid making the TLD a single point of failure? Maybe you have website <span style="text-decoration: underline;">maybank2u.com.my</span>, but also an app that connects directly or to backup domains. That way, if the TLD falls apart -- you can post a tweet that says, use the app. Having a separate domain that is public (like therealmaybank.com ,will just look like a phishing attempt), but a separate domain that your app can secretly call -- or even just a direct IP connection from your app would smoothen things out.

As long as MYNIC is a single point of failure for all .my domains, the question becomes, do you really want your business to be beholden to them? Or should you try to engineer your way around it by migrating away from .my?
<h3>References:</h3>
<ul>
 	<li><a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">Great high level overview on DNSSEC</a></li>
 	<li><a href="https://tools.ietf.org/html/rfc6781">RFC 6781</a> on Operational DNSSEC (including how long KSKs should last)</li>
</ul>