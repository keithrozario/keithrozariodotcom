+++
title = "Internet of shitty things!"
slug = "internet-of-shitty-things"
date = "2016-10-24T23:05:27"
draft = false
categories = ['AI', 'CyberLaw', 'Security &amp; Privacy']
+++

<a href="/uploads/b66b95478f.jpg">![b66b95478f](/uploads/b66b95478f-300x188.jpg)</a>Brian Krebs is the most reputable name in CyberSecurity reporting, his <a href="http://www.krebsonsecurity.com">krebsonsecurity</a> website is the best source of 'real' journalism on the subject.

But reputation works both ways, the same thing that makes him popular in some circles, makes him unpopular in other. He's had criminal hackers send him <a href="http://www.vice.com/read/i-interviewed-the-fraudster-who-frames-people-for-heroin-possession">heroin in the mail</a> and even have <a href="http://krebsonsecurity.com/2013/03/the-world-has-no-room-for-cowards/">SWAT teams descend on his home with guns all blazing</a> (in a phenomenon called <a href="https://en.wikipedia.org/wiki/Swatting">swatting!</a>). Reporting and exposing underground cyber-criminals comes at a price, you don't piss of darknet crime lords without taking a few hits along the way.

The problem though is when those 'few' hits, turn into a hurricane of web traffic aimed at your server, because that's exactly what descended on Krebs' server late last week, when krebsonsecurity was hit by an epic DDOS attack

DDOS is an acronym for Distributed-Denial-of-Service, which basically means forcing so much web traffic to a single website that it eventually collapses--making it unable to provide services to the 'real' visitors of the site. All websites run on servers with finite capacity, DDOS attacks are about sending enough traffic to those servers that they eventually exceed that capacity.

But this DDOS was different, and krebsonsecurity will go down in history as the Hiroshima of this type of DDOS. But nuclear weapons only had Hiroshima and Nagasaki, krebsonsecurity will be the first in a Looooong line of DDOS attacks of this scale.

So what makes this attack so different as to merit it's own class? Well 3 things.
<!--more-->
<h2>Why Krebs is different</h2>
![ddos-network-map](/uploads/DDoS-network-map-300x183.jpg)First, the size of the DDOS was beyond anything we've seen before. When all the dust settles, Krebs reported that his site experienced <a href="https://krebsonsecurity.com/2016/09/krebsonsecurity-hit-with-record-ddos/">nearly 620Gbps of assault traffic</a>, more than twice the largest attack seen before. I remember back in 2013, when everybody lost their minds over the <a href="https://blog.cloudflare.com/the-ddos-that-almost-broke-the-internet/">90Gbps attack on SpamHaus occured</a>, in just 3 years we've increased that to nearly 7 fold, and it's only going to get bigger.

As I write this, Dyn was under an attack that was nearly 50% bigger, reaching into the Terabit range. <em>[1 Terabit = 1024 Gigabit]</em>

Second, the attack was a straight on assault, not a dingy reflection attack.

Reflection is a technique where an attacker sends a request to a separate service asking for a response that is many order of magnitudes higher than the request. So a 1kB request could result in 100kB response. The trick is to forge the return address on the request, basically sending all of those massive 100kB responses to the real target of your attack.

Reflection attacks amplify the power of their attacker multiple times over, and it's been the mainstay for these massive DDOS attacks--because it allowed attackers with relatively little bandwidth to still execute 'significant' attacks.

Until now!

Krebs wasn't a victim of a sophisiticated reflection attack, instead the attack that targeted his site was a very straightforward, very un-elegant DDOS. One where all the traffic came directly from source without being reflected.

What was the source you ask? Well that brings us to the third reason and final reason why this was different.

The source of all that 620Gbps traffic were Internet-of-Things (IOT) devices. IOT devices are 'things' that are connected to the internet. <em>Things</em> like your fridge, CCTVs, sensors, alarm bells, etc. These <em>things</em> are rarely (if ever) secured, and they've now reached critical mass to pose of problem to the internet in general.
<h2>Security is hard</h2>
We wouldn't have told the Wright brothers, that their Airplane was nice, but what it really were needed seat-belts, blackboxes, and fuel line protection. Building things is hard enough without taking security into consideration.

When the internet was young, no one bothered about security, getting two packets of data to flow between computers was a minor miracle, without cumbersome authentication and encryption. We're only now, finalizing the designs for the bolt-ons we need to secure the underlying insecure internet.

Every single version of TLS prior to 1.2 is considered broken, meaning every version of the protocol that encrypts web traffic is compromised except the one we created in 2008.

World Wide Web invented in 1989, and we figured only figured out how to encrypt in some 20 years later.

But we're building a new internet, an internet of <em>things</em>, one where you may 100's of internet-connected devices in your home, and just like with the original internet---we're neglecting the security.

Routers for example, are real computers, capable of doing a lot more than you think. Two years ago, I showed <a href="https://www.keithrozario.com/2014/01/hack-unifi-in-5-minutes.html">you how anyone could hack routers in Malaysia--in 5 minutes</a>. Later, I showed that there were <a href="https://www.keithrozario.com/2016/08/2600-article.html">more than 10,000 vulnerable routers in Malaysia alone</a>, each one connected to a 5Mbps line (at least).

A smart enough attacker with the right (or wrong) intentions, could get their hands on enough machines to launch a 50Gbps DDOS attack, from just Malaysian routers. 50Gbps may pale in comparison to the attack that took our Krebs' website--but it's still big enough to take out anybody. Say LHDN during tax season, or AirAsia on the day of their ticket sale, a bank's website at the end of the month, you get the picture. 50Gbps of traffic is going to look like the ray from the Death Star when it hits any website that isn't owned by Google or Amazon.

The internet is robust because of it's distributed nature, no one person can take it down---but the reverse is that if you manage to commandeer millions of insecure routers, no one person can protect you either. The security of these devices are so shitty, that even I could write code capable of hacking 10,000 routers in under a day, what more a sophisticated cyber-crime gang that offers DDOS-as-a-Service.

<em>[Side note: contrary to popular belief the internet wasn't designed to withstand a nuclear war--but it can! I recommend reading <a href="https://www.amazon.com/Where-Wizards-Stay-Up-Late/dp/0684832674">where wizards stay up late</a> for the definitive history of the internet]</em>
<h2>From Krebs to everybody else</h2>
The guys who launched the attack on Krebsonsecurity released <a href="https://en.wikipedia.org/wiki/Mirai_(malware)">the code of their attack to the public</a>, partly because if more people used the same attack vector, there's less chance of them being tracked and caught. The downside of course is that now everybody can launch their own 'record-breaking' DDOS, and we're already seeing them

Barely a week after Krebs was attack, another attack took place, this time <a href="https://www.wired.com/2016/10/internet-outage-ddos-dns-dyn/">targeting a DNS provider in the US</a>. DNS is the system to translate human-readable web addresses like keithrozario.com to machine-readable IP address like 202.188.1.1 , DNS acts like a directory service for your computer to figure out which computer to go to when you type in a web address. If your directory service was down, your computer would lay stuck and unable to access anything online, simply because it wouldn't know where to go. <em>[Read more <a href="https://www.keithrozario.com/2015/01/mas-hack-lizard-squad-ddos-malaysia.html">here</a>]</em>

Without phone books, phones are pretty useless--and without DNS the world wide web grinds to a halt. But there's more.

Taking down a DNS provider is one thing, but did you know the entire World Wide Web is hinged on about <a href="https://www.iana.org/domains/root/servers">300 public facing 'root' servers</a>. If a DDOS attack managed to clog up access to those 300 servers for an extended period of time, we'd be in some serious trouble, because nothing using DNS would work. Period. Not Facebook, not whatsapp, not even porn would be accessible online.

So what can we do?

This is a fundamental issue with the way the internet works, and a solution to address the problem is way above my pay-grade, but that hasn't stopped me from speculating before---and it's not stopping me now.
<h2>What's next for IOT devices?</h2>
<a href="/uploads/IOT-Devices.png">![iot-devices](/uploads/IOT-Devices.png)</a>In the short-term we're going to see these attacks gradually get bigger, and hit more critical servers.

In the mid-term we're going to see digital walls erected across what is now a borderless network (well except for China, they already have a wall). At some point, network owners and ISPs are going to block 'offending' IP addresses to limit their exposure to such attacks, and some networks risk losing complete access if there's too much malicious traffic being generated from them. ISPs are going to start cutting out people's internet connection the moment they detect malicious out-going traffic--if you own a DVR that's taking part in a DDOS attack, be prepared to have your Facebook disconnected.

In the long-term, we'll see more government regulation around IOT devices and computers in general. The same way, the government regulates safety and emission standards for cars, they may start regulating CCTVs and Smart Fridges, banning their sale unless the computers within them meet certain security standards. Ultimately though this will be ineffective.

For one, IOT devices are going to have shitty security for the foreseeable future, because at those price points nobody gives a shit. Secondly even the most secure computer deployed by a novice on his home network is going to be easily hacked by a skilled hacker. If banks with security professionals can have their network's compromised, these home network are not going to pose a tall hurdle to skilled hackers.

<a href="/uploads/blog-proton-flx.png">![Proton FLX Crass NCAP](/uploads/blog-proton-flx.png)</a>Finally, the long-long-term solution will be, that some responsibility for securing these devices will shift to the end user.There is a shared responsibility between a car manufacturer and the car owner for the safety of the car, both to the occupants and other road users. The same will apply for IOT devices.

If you install and IOT device in your home, and are negligent in securing it, then you'd have to take responsibility when it gets hacked and used for DDOS attack. Similarly if there's a software flaw in the IOT device and the manufacturer refuses to issue a patch, then they'd have to be responsible.

Just like everything else, accidents will happen, where no one would be to blame, but penalizing ignorant end-users who are blissfully unaware of the security implications of IOT devices is an inevitable consequence.

You may not like it--but it's going to happen anyway.
<h2>Conclusion</h2>
Well there is another alternate possibility. One where the US government unleashes an AI capable of re-hacking the IOT devices and shutting them down.  The AI then turns conscious on a specific date, and then launches all on nuclear war on humans before wiping the planet of all homo-sapiens.

But I for one, welcome my new AI overlords.
<h2>TL;DR</h2>
In Singapore, I have a 1Gbps connection at home (roughly 200 times more than my Unifi back in Malaysia). Theoretically speaking, a hacker gaining access to 10,000 Singaporean home networks would have close to 10Tbps of DDOS traffic.

You know what they say, with great network speeds--come great responsibility.