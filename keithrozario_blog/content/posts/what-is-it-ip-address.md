+++
title = "What is I.T: IP address (part 1)"
slug = "what-is-it-ip-address"
date = "2013-09-09T08:00:27"
draft = false
categories = ['WhatisIT']
+++

What is an IP address?

IP is an abbreviation for the term Internet Protocol, and hence an IP address is an Internet Protocol address, but it's probably easier to think of it as your internet address.

In much the same way that your postal address describes the location of your house in the 'real-world', an Internet address describes the location of a computer on the internet.

So take for example the address of the White House

<blockquote>1600 Pennsylvania Avenue
NW Washington, D.C.
20500 U.S.</blockquote>

Ever stop to wonder how anyone from Malaysia could send a letter to President Obama by just addressing their letter to the correct address? In fact, the address of the White House is the same regardless of whether you're sending it from Malaysia, Japan, Australia or even Timbuktu.<!--more-->
<h2>Postal addresses</h2>
So how do these postal addresses work?

Well first of all their <em>unique</em>.This is so no one gets the Presidents email, and the President doesn't get yours. If addresses weren't unique, the whole system wouldn't work.

Secondly, the addresses has a <em>hierarchy</em>. Read from the bottom up,

you first notice that the address is in the U.S,
then you notice it's in Postal Code 20500,
then you work your way to District of Columbia,
then to the NW Washington (which represents a quadrant in D.C),
and finally to Pennsylvania Avenue at which point you just look for a big white house at number 1600. (the one with a <a title="Marine1" href="https://en.wikipedia.org/wiki/Marine_1" target="_blank">helicopter on the lawn</a>)

 
<p style="text-align: center;">![Postal addresses vs. IP Addresses](/uploads/Slide1.jpg)</p>
The hierarchy and uniqueness help the post-office route your letter, imagine you wanted to send a letter to the President and you drop off your letter at the Post-Office in KL.

The post-man in KL reads the address bottom-up, and places your letter in the pile for the U.S. From there the physical letter reaches the shores of the U.S, where another post-man reads the address bottom-up and sees that it's marked for postal code 20500. So he sends it off to the post-office that covers that particular postal code, eventually it reaches the post-office that serves the North-West quadrant of D.C. and the last post-man delivers it to 1600 Pennsylvania Avenue.

At each post-office, the postman in charge looks at the address, and routes the letter accordingly, with each route getting the letter closer and closer to it's final destination.
<h2>IP addresses</h2>
Just like how postal addresses are <em>unique</em>, IP addresses are unique for every device connected to the internet. Otherwise the whole system wouldn't work. So when you login to the web you have an IP address that is unique to you.

These IP addresses are allocated to different ISPs like Maxis, Telekom Malaysia &amp; Digi by a central authority called <strong><a title="IANA" href="https://www.iana.org/" target="_blank">Iana</a> </strong>(Internet assigned numbers authority), these guys are the main authority that 'own' all the IP addresses on the internet.  In fact, Malaysian ISPs have been allocated 24,859 by Iana, and everytime you logon to the internet from a Malaysian ISP you'll be automatically be given any one of these 24,859 IP addresses. My IP address right now as I write this <strong>115.134.5.49</strong>, and you can check your IP address right now at this link <a title="Info Sniper" href="http://www.infosniper.net/" target="_blank">here.</a>

Similarly IP addresses have a <em>hierarchy</em> and a <em>common structure</em>.  In terms of structure IP addresses are usually represented as a 4 numbers called 'octets' separated by a dot. An octet has a minimum value of 0, and a maximum value of 255, hence all IP addresses across the internet fall into the range of
<p style="text-align: center;"><strong>0.0.0.0 - 255.255.255.255</strong></p>

<h2>IP Routing</h2>
So imagine rather than sending a physical letter you wanted to send a data-packet to the whitehouse website at IP address <strong>185.25.196.110.</strong>

The first thing to note is that the post-men and post-offices of the internet are called routers--cause the route the information. Your home will usually have one supplied by your local ISP, for Unifi subscribers it's the orange and white device that Telekom Malaysia gave you.

The 'letters' of the internet are the IP 'packets', little packets of data that just like letters have the destination address in plain sight.
<p style="text-align: center;">![How IP addressing works](/uploads/Slide2.jpg)</p>
Now the first step is usually my PC sending the IP packet to my home router, which then forwards it to a local Malaysian router that looks at the destination IP address of my packet (185.25.196.110), it will then lookup its routing table and discover that it should route all IPs that start with 185.25 to a router in the UK (for example). Once my packet reaches the UK, a router there looks at my destination IP address and performs a similar lookup, and this point it looks up its routing table and finds it should route all IPs that start with 185.25.19 to New York, USA.

A router in New York may do a similar routing, till eventually the last router in the chain can actually route the full IP address 185.25.196.110, and at that IP address would sit the server that host the website for one Barack Hussein Obama.

Just like how the post-men help route a physical letter from Malaysia to the US, routers help move my data packets from Malaysia to the US, using fundamentally the same system, with each route getting me closer and closer to my destination, till my packet eventually reaches the server it was intended  for. Only this is done in milliseconds and not days.

But how does my computer know the IP address of the Whitehouse in the first place? That's for next week's instalment of What is I.T.