+++
title = "Should an IP address be used to Identify someone?"
slug = "ip-address-uniquely-identify-law"
date = "2015-04-29T11:00:29"
draft = false
categories = ['CyberLaw', 'Malaysia']
+++

![How IP addressing works](/uploads/Slide2-1024x576.jpg)Recently a court in Malaysia ruled that the newly amended evidence act could presume an IP address would uniquely identify a user of a network, and in the case of an Internet IP address, enough to tie an IP to the individual subscriber. In other words if the authorities ever found out that 'your' IP address was behind a post, then you'd have to prove it wasn't you rather than they having to prove it was.
<blockquote>In <strong>Tong Seak Kan &amp; Anor v Loke Ah Kin &amp; Anor [2014] 6 CLJ 904</strong>, the Plaintiffs initiated an action for cyberspace defamation against the 1st Defendant.   In tracing the perpetrator, who had posted defamatory statements on two Google Blogspot websites, the Plaintiffs filed an action called <strong>a John Doe action in the Superior Court of California</strong>.   In compliance with the court order, <strong>Google traced the blogs to two IP (Internet Protocol) addresses which were revealed by Telekom Malaysia Bhd to be IP addresses belonging to the 1st Defendant’s account</strong>.
<p style="text-align: right;"><a href="https://www.digitalnewsasia.com/insights/bread-kaya-malaysian-cyberlaw-cases-in-2014" target="_blank">Bread &amp; Kaya: Malaysian cyberlaw cases in 2014</a></p>
</blockquote>
Upon further reading of the post on DigitalNewsAsia, my non-lawyer mind got the feeling it didn't end well for Loke Ah Kin &amp; Anor as the court decided they were guily of defamation based on a flimsy piece of evidence like the IP address of the user who posted blogspot.

I'm uncomfortable that a court of law could find someone guilty based on something as trivial as an IP address, when other courts around the world have ruled that IP addresses are insufficient for this purpose.<!--more-->
<h2>What is an IP address?</h2>
But let's get some technical jargon out of the way. An <a href="https://www.keithrozario.com/2013/10/what-is-ip-address.html">Internet Protocol (IP) address </a>identifies a specific connection on the internet, it's like the phone numbers for internet connected devices. Yes, it is unique, but only to a certain extent, and definitely <span style="text-decoration: underline;">not sufficient</span> to identify an individual on the internet.

IP addresses  also ephemeral. For most internet subscribers, you get a different IP address every time you re-start your home router, go ahead try it, I'll wait.

Done? Notice that everytime you re-start your router your IP address changes, that's because most internet users subscribe to dynamic IP address packages, one where the Internet service provider DOESN'T guarantee you get the keep the same IP address in the same way you get to keep your phone number. Rather you get a new IP address that is only unique for that particular session, and they probably recycle the IP addresses for future sessions of other users. An IP address does not belong to a subscriber, it belongs to the ISP (TM, Maxis, Digi, etc) and the ISP than allocates those addresses to subscribers as they log on.

The most you can say is that an IP address was allocated to a particular user within a fixed time-frame.

With Maxis and possibly other smaller telcos, this gets a bit more complicated, because unlike TM (which has upwards of 9 Million IP addresses in the bank),  Maxis has just a couple hundred thousands, and has to share those limited IP addresses with their millions of subscribers. By using a technique called Network Address Translation (NAT) Maxis can share a limited number of public internet IP addresses among its customers allowing them to have more devices connected than their IP address allocation, thereby circumventing the rule that IP addresses must be unique.The 'downside' is an external service like Google Blogspot would see the same IP address for different Maxis subscribers and be unable to differentiate them. In other words, the IP address as seen from blogspot or Google would be identical for different subscribers.
<h2>But uniqueness only applies to the network</h2>
Still reading? Good, because I need to get a bit technical, but if you're a regular reader you can already see where this is heading.

An IP address of your device has to be unique on the network it's on, but the question is--which network? This may shock you, but your device almost never connects to the internet directly--your router is.

Your computer is connected to your router, and is part of a much smaller network we call the Local Area Network or LAN <em>(no it wasn't invented by a Hokkien guy, it's just an unfortunate coincidence). </em>A LAN usually consist of the devices in a home network, like your phone, iPads, laptops...etc. Your IP address on your laptop only has to be unique among the other devices connected in your home. (it's the blue circle in the picture below).

![IP Address LAN/WAN 1](/uploads/Slide12-820x461.jpg)

Your router on the other hand is connected to the outer internet, we call this the Wide Area Network or WAN <em>(describing the network now, not the Chef)</em>. It's the only device in your home directly connected to the internet, and hence the it's the only device that actually needs an <span style="text-decoration: underline;">internet IP address</span>. It's the red circle in the picture above.

Pay close attention, your router is connected the internet, while your device isn't. Your device 'gets' the internet through your router, which acts as a bridge between the WAN and LAN. So your router has an Internet IP address that is unique throughout the internet, while your devices have LAN IP addresses that are only unique to LAN in your home. This is how TM can get away with giving you just one Internet IP address, which you can then share among the hundreds of devices you have in your home.

To an external party like Google, or keithRozario.com <em>(heard it's a great website)</em>, all devices on your network would look to have identical IP addresses, even though individually they have unique LAN IP addresses.

The consequences of this is that if someone were to hack your WiFi (quite trivial for a skilled attacker) they'd get into your LAN, they can then post defamatory statements on your behalf and get you in trouble. And since there really is No bloody way to prove your WiFi was hacked, you'd be holding the proverbial short end of the stick, or to quote a more technical term--being absolutely screwed!

![Slide2](/uploads/Slide22.jpg)

There is no way you would have a 'fair trial', if you had to prove your router was hacked, since there's no technical way prove that, most home routers don't have sufficient logging capability, or diagnostics to even hint of a potential hack, and even if the logs managed to prove that an 'unknown' device logged on at a particular time, what difference would that make? Couldn't you have bought a cheap laptop, connected to the network, post the defamatory article and then throw the laptop away. You see how absurd it is to force a normal person to prove their router was hacked---heck even I couldn't do it, let alone the tech-phobic community.

It's because of this, that <a href="https://www.techdirt.com/articles/20130218/21462222020/yet-another-court-says-ip-addresses-are-not-enough-to-positively-identify-infringers.shtml" target="_blank">multiple court rulings in the US that have stated categorically that IP addresses do not identify a person</a>, with one ruling going so far as saying <a href="https://torrentfreak.com/ip-address-cant-even-identify-a-state-bittorrent-judge-rules-120515/" target="_blank">it can't even be tied to a state</a>, let alone an individual. The question of which state an IP address belongs to is particularly important, as it would define which court had jurisdiction to actually hear the case, less important in Malaysia, where state jurisdiction doesn't quite exist for the evidence act, but it tells you just how unreliable the IP address is as a unique identifier.

But in good ol' Bolehland, apparently these are small issues, who cares if a defendant could never prove the negative, we need these tough laws to curb 'fitnah' and slanderous statements. All of this borders on bat-shit crazy, I can't imagine what's going on in the minds of the supporters of the law.
<h2>PostScript : Hola Unblocker</h2>
About a month after writing this post, news broke out that popular Chrome Extension Hola Unblocker was now literally selling user IPs via their little known VPN luminati.

Hola was a really cool extension that I used to recommend to people to bypass geo-restrictions to watch Netflix. It was first on the list of recommended methods to watch netflix simply because it was free, but there's a downside. Any user that downloaded Hola to watch Netflix was also unwittingly allowing their connection to be 'hijacked' by any other user--thereby allowing someone else to literally spoof your IP without leaving a trace.

So if you were on Hola, I could theoretically log onto Hola, get your connection, post seditious material on your behalf, and leave you having to prove your innocence. Yet another reason why IP addresses are not uniquely identifiable.