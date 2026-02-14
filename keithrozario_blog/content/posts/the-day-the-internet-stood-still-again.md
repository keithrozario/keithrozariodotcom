+++
title = "The day the internet stood still--AGAIN!"
date = "2015-06-17T13:02:04"
draft = false
categories = ['Malaysia', 'WhatisIT']
+++

There was a time when the internet was young, just a little fledgling network, an academic toy used only by computer scientist to try out theoretical concepts. Contrary to popular belief the internet wasn't created to withstand a nuclear war(although it can), instead it was created to address a very serious engineering question--how to connect together different computers with different operating systems and different commands? The answer to that question stumped many brilliant people, in the late 60's and early 70's, computers were Gods of their domain, stand-alone machines with 'slaves' like disk-drives and monitors, if you hooked up a computer to another computer, they wouldn't know what to do--there's a chinese saying about one mountain can only have one dragon, computers in those days were exactly like that.

Solving that issue of having a computers connect to each other, was no trivial task, it took a US Department of Defence project to resolve the issue, culminating in ARPANET. For geeks like me, ARPANET is like the garden of Eden, where it all began, where God said let there be downloads and uploads. But ARPANET was a military funded network, and soon other networks begun to connect into it, and slowly but surely ARPANET faded into oblivion leaving a civilian run Internet behind. The engineering challenges of the day were daunting enough, that no one stopped to think about the possible security challenges, after all the word cyber-crime didn't exist yet, there wasn't an internet to do bad things on. So a lot of the protocols that were designed by the engineers of the day assumed that everyone on the network was playing fair and nice, and that it was a co-operative network of peers. Today, IT architects like myself view the internet as an un-trusted by reliable network, where all sensitive data traversing it should be encrypted. It's a like a super highway full of bandits, and the only way we'd use it, is if we drove tanks.
<h2>E-mail, the killer-app</h2>
Take for instance the very first 'killer-app' for the internet, e-mail. The first iteration of e-mail was built on a protocol meant for transferring files rather than messages, a kind of protocol hack. This was a time when the number of users on the network could be listed by hand on a piece of paper--and everyone trusted each other, hence the protocol never incorporated any form of authentication simply because it wasn't required, the early internet was like the sitcom cheers, everybody really did know your name. Even when e-mail got its own protocol, authentication was never considered an important feature.

Authentication is the act of verifying the identity of a person or machine performing a request, when you call certain call centers, they may authenticate you by asking a series of questions like "what's your mothers maiden name", or "what's your favorite pet". Un-authenticated protocols, allow anyone to either impersonate someone, or just execute any command, and unfortunately is the default standards for many of the older protocols online.

The e-mail we use today, is built on these ancient un-authenticated protocols, with a couple of tweaks here and there, but fundamentally it remains every bit insecure today as it did back then. The only difference is that there are lot more internet users today than in the 70's, and some of those users are criminals, so when you have a widely used insecure protocol, and a criminal element looking to exploit it....you have problems.
<h2>Everything is insecure, now what?</h2>
And that brings us nicely into what happened last week, I must admit I didn't experience the issue as I was at work, but apparently the Telekom Malaysia not just experience catastrophic internet melt-down in Malaysia, it was causing network issues on the internet globally.

The internet is (as the name suggest) an interconnection of different networks. You can think of each Internet Service Provider (ISP) as a node on that network that communicates with other ISPs. All these nodes communicate to each other using the <a href="http://What is" target="_blank">Internet Protocol(IP),</a> and IP works fairly similarly to the way the postal system works. With routing occuring at post-offices throughout the country, and between countries. (hopefully my <a href="https://www.keithrozario.com/2013/09/what-is-it-ip-address.html" target="_blank">previous post</a> will help you understand)

But IP isn't the complete picture, while IP defines how messages get routed from one node to another, it doesn't define how those routing decisions are made. In other words, how does the Post-Office know that letters addressed to the US should be sent to Hong Kong first, before being shipped to the US?

The answer is a totally separate protocol called BGP, which was invented in the 80's, slightly younger than IP or e-mail, but still old enough to be born in a time before security was a major concern on the internet. BGP allows for nodes in the network to communicate with each other, 'advertising' the other nodes they connect to.

IP is a protocol based on routing  by tables, and BGP is the protocol that defines how those routing tables get populated.
<h2>How does it work?</h2>
So for example, imagine if Klang were a country onto itself (some say it already is), and had it's own ISP, Klang Telecommunications (KT). KT is a pretty decent ISP, and has about 2,000 IP addresses assigned to it by IANA, the body in charge of IP addresses.

Unfortunately, KT is a small local ISP and can't build expensive under-sea cables to the internet. Instead it connects to Telekom Malaysia and Maxis for all it's internet traffic. In this case, Telekom Malaysia and Maxis would advertise the KT IP addresses as ones that it connects through directly, and anyone wanting to communicate with KT would route all their traffic to either of them first.

Now Imagine an IP packet on the AT&amp;T network in the US destined for a servers hosted on the KT network, the AT&amp;T would look its BGP tables, and sees that in order to send the data to KT, it would have route the packet to either Maxis or TM. Then it looks internally and discovers that it has a direct connection to TM (single-hop), but needs to go through a Singaporean ISP to connect to Maxis (double-hop). The fastest way to get to KT is through TM, and hence all the routing is from AT&amp;T to TM and finally to Klang.

You can probably see the issue already, if the 'advertising' function of the BGP isn't authenticated, anyone can control network routing, by just claiming to be the nearest node to Facebook, or Youtube, which is exactly what Pakistan did back in 2007. Since all nodes accept the information from all other nodes without question and authentication--a rogue ISP, or even a careless mistake can wreak havoc.
<h2>And now we see the problem</h2>
That's what happened last week, TM advertised that they were the shortest path to a motherload of IP addresses, and a giant node in the US noticed and began routing nearly all its traffic to TM. Predictably, TM just got crushed under the load, ending all traffic not just to TM subscribers, but also for the Americans using that giant node as well. Sort of like, a small phone shop, advertising that they're selling iPhones for one dollar, and then it gets crushed by the sheer number of people cramming into the shop to buy them.

Of course, you may rightfully ask why don't the geeks fix the problem. We have pretty easy solutions for this, unfortunately the pervasiveness of the internet make it very hard to implement any new change. The internet in many cases is a victim of it's own success, no one imagined the internet would be this great when it first started, and we're now reaching the edges of some of the engineering we did in the 60's and 70's. It's a testament to the engineers that we're only now reaching those limits, but the problem is ever present.

Because so many people use the internet, and because so many ISPs are on-board, any change has to be implemented world-wide. That's the challenge, we can't just switch off the internet for 2 days while the engineers make the change, that's not acceptable.

Links:

<a href="http://www.lowyat.net/2015/06/tmunifistreamyx-services-facing-severe-slowdown-across-the-country/" target="_blank">http://www.lowyat.net/2015/06/tmunifistreamyx-services-facing-severe-slowdown-across-the-country/</a>

<a href="https://news.ycombinator.com/item?id=9704952" target="_blank">https://news.ycombinator.com/item?id=9704952</a>

<a href="http://www.washingtonpost.com/sf/business/2015/05/31/net-of-insecurity-part-2/" target="_blank">http://www.washingtonpost.com/sf/business/2015/05/31/net-of-insecurity-part-2/</a>

<a href="http://www.bgpmon.net/massive-route-leak-cause-internet-slowdown/" target="_blank">http://www.bgpmon.net/massive-route-leak-cause-internet-slowdown/</a>