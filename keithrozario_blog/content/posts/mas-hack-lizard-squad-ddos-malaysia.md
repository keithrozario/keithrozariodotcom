+++
title = "What happened in the MAS hack. All questions answered, one question asked."
slug = "mas-hack-lizard-squad-ddos-malaysia"
date = "2015-01-29T23:11:53"
draft = false
categories = ['Malaysia', 'Security &amp; Privacy']
+++



![Real-Life DDOS attack](/uploads/11445766236_d072478f86_o.jpg)



Late in January the Malaysian Airlines website was 'supposedly' hacked by Lizard Squad. You  might remember Lizard Squad as the guys who 'hacked' the XBox and Play Station network over the Christmas holidays, and I'm using a lot of 'quotes' here because Lizard Squad didn't really 'hack' XBox One or Playstation, they merely DDOS-ed the services.
<h2><em>What is DDOS-ed I hear you say?</em></h2>
A DDOS attack is one where you flood a server with so much web traffic, that the server is no longer able to serve content to legitimate customers. Imagine if you got 100 friends, and decided to create some havoc at the McDonalds near your home. You and your friends would line-up at the counter, and you'd place an order for 100 Big Macs, 25 Cokes and 1 Apple Pie... only to cancel your order after the cashier typed in it. The next friend in the que would do the same thing--over and over again. Even though there would be legitimate customers at this McDonalds trying to buy some food, chances are they'd either have to wait a very long time to get their food, or they'd give up entirely.

Essentially you've denied McDonalds their chance to serve their customers--or you've just launched a Denial of Service (DOS) attack--the extra D in DDOS, just stands for distributed.

Real-Life DDOS happen all the time--what do you think the Thai Protestors were doing to Airports in 2008?
<h2><em>But why is this important?</em></h2>
It isn't. DOS attacks are pretty common--but Lizard Squad attacked the Play Station Network,and XBOX with ulterior motives. Even though they claimed to do it in the name of 'security awareness', they only stopped their DDOS attack because Kim Dotcom offered them USD300k worth of services on his Mega website. Kim Dotcom is another controversial character, but to cover him in this article would be too large a digression--so if you want to know more about him, just Google it.

The REAL motive of the Lizard Squad DOS attack became apparent some days later when they started to offer their DDOS attack as a service to paying customers. Essentially you could go online and buy their services to attack a target--maybe a competitor company, a personal blog of someone you don't like, or just about anything. Lizard Squad were hawking their services to anyone with cash.

Some suspected that Lizard Squad were running this large DDOS attack using nothing more than home routers--similar to the ones that UniFi provides and that I demonstrated could be <a title="How I hacked 4 Unifi accounts in under 5 minutes" href="http://www.keithrozario.com/2014/01/hack-unifi-in-5-minutes.html">hacked trivially over an internet connection</a>.

<!--more-->

Now hacking is one thing, but hacking as a service for dodgy customers is another, and the move by Lizard Squad didn't go down well with other hackers, who immediately took notice of their DOS-For-Hire website, and revealed some mistakes Lizard Squad made. Brian Krebs reported that:
<blockquote>In a show of just how little this group knows about actual hacking and coding, the source code for the service appears to have been lifted in its entirety from <strong>titaniumstresser</strong>, another, more established DDoS-for-hire booter service. In fact, these Lizard geniuses are <a title="http://www.ericzhang.me/lizardstresser-user-enumeration/#more-449" href="http://www.ericzhang.me/lizardstresser-user-enumeration/#more-449" target="_blank">so inexperienced</a> at coding that they inadvertently <a title="http://pastebin.com/Gdk9wifY" href="http://pastebin.com/Gdk9wifY" target="_blank">exposed</a> information about all of their 1,700+ registered users (more on this in a moment).</blockquote>
Lizard Squad members were beginning to be arrested across the globe, and it looked like it was over for this group...or so it seemed.

As publicity for their service begin to wane, and people begun forgetting who Lizard Squad were, they struck again. Only this time they didn't perform a DOS attack, but rather went after our very own Airline--MAS. It's worth noting that if you're not from my country, that Malaysians still have an open-wound for all 3 of our aircraft that crashed in 2014, specifically for the victims of MH370, whose relatives are still hoping and praying that their loved ones are still alive. You don't make fun of an open wound like that and hope that people like you...you don't kick a country when it's grieving--that's just not what real hackers do.
<h2><em>So what happened to Malaysian Airlines you ask?

![Malaysian Airlines](/uploads/472739228_9acc811ec4_z-300x200.jpg)

</em></h2>
MAS was a victim not of a DOS attack, but had its DNS hijacked by Lizard Squad.

DNS stands for Domain Name Server. It's the end-2-end solution that manages to translate website's name to an <a title="What is an IP address" href="http://www.keithrozario.com/2013/10/what-is-ip-address.html">IP addresses</a>. A simple way to think of it is as the telephone book for websites, but instead of giving phone numbers of people--it was giving IP addresses of Websites.

Unlike the phone book though, DNS is a real-time service, and not something printed once a year, and set in stone forever after. If you own a website, like keithrozario.com or MalaysianAirlines.com.my, somewhere in the vast expanse of the internet is a Nameserver that holds the IP address of your website. This NameServer is the official guardian of the most important record your website has--this is where the question "What's the IP address of keithrozario.com" get's answered.

What Lizard Squad did was attack the Domain Registrar of MalaysianAirlines,com who owned the NameServer, and change the IP address to point to a server they owned. A server that held the disgusting picture of "Plane not Found"--and as a side note, I can't believe our local press actually printed that on their websites, do they not care about the feelings of our fellow Malaysians who had love ones on board?

In any case, this wasn't Lizard Squad attacking MAS servers, but rather Lizard Squad attacking the MAS Domain Registrar.

It's like instead of attacking the airport, hackers just change the road-signs so people end up at Pudu Bus Station instead of KLIA--then people who end up at Pudu think KLIA must have been invaded by hoardes of foreign workers....<em>(sorry so racist of me!)</em>
<h2><em>But didn't you see the IMGUR image of emails that Lizard Squad posted--surely data was compromised.</em></h2>
WELLLLLL.....Yes and No.

The domain registrar doesn't just hold the IP address of the website, it will hold the IP addresses (or CNAME records) of your email server as well. When you send an email to me keith[at]keithrozario.com, your mail program looks up the IP address of my mail server @keithrozario.com, in much the same way as your browser looks up the IP address of my website.

If Lizard Squad manage to compromise the Website IP address of the domain--there's nothing to stop them from compromising the email server IP addresses as well.

<span style="color: #ff0000;"><strong>WARNING: HYPOTHETICAL SOLUTION AHEAD--please exercise critical thinking and left brain powers as much as possible</strong></span>

So here's what I think happened. The guys over at Lizard Squad hacked the DNS registrar as MAS claim, then pointed the website IP address to a server they own. No questions there.

In addition, they also re-configured the e-mail entries on the DNS to point to email servers that <strong>they!!</strong> owned. At that point anyone sending an e-mail to MAS 'could' have inadvertently sent that email to Lizard Squad instead. So if you sent an email to MAS...beware who might have your email address now.
<h4><em>The worst part though-----</em></h4>
IF (<span style="color: #ff0000;"><strong>and I stress IF</strong></span>), MAS had external email services like Enrich (or whatever) that sent email through the MAS email servers. Those external services would have needed to login to the MAS email servers---and for a short time, they may have been trying to login to servers hosted by Lizard Squads, because their DNS resolution would have taken them to the Lizard Squad IP.

And because these email protocols don't have 2 way authentication <em>(you authenticate yourself to the server, but you have no way to authenticate if the server is real) </em>, MAS 'may' have given Lizard Squad login credentials to the 'REAL' email servers. And those are like the keys to the kingdom of heaven--and who knows what Lizard Squad might have done with those credentials.

Also, if MAS allows their staff to access email from external sources via public internet (instead of Private VPN connections), these staff might have also handed Lizard Squad their login credentials to the MAS email server.

Of course, all hypothetical.
<h3><em>But I have a question for you...</em></h3>
![We take ourselves WAAAY to seriously](/uploads/images-11.jpg)Where is Pertubuhan Martabat Jalinan Muhibbah Malaysia(MJMM)--you know the guy with the Red Beret who lodges a Police Report every time his backside feels a bit itchy.

I mean if this guy lodges reports over anything and everything, and claims to be the defender of this <strong>'Agama, Bangsa dan Negara'</strong>--where is he when Lizard Squad attacks the website of our National Airline, and insults the memory of victims of a tragedy that Malaysians are still grieving for.

Or is he afraid to lodge a report against someone outside Malaysia that can harm him, and he can't go to his political masters for help and assistance. I always think of him as the Kanye West of NGO's--he's got the most publicity, he's got a full-blown entourage (with girls btw), but ultimately he's the one nobody takes seriously--not even his own kind.