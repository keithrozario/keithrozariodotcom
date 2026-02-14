+++
title = "Malaysian Government Hacked Environmental website?"
date = "2014-11-08T15:06:36"
draft = false
categories = ['Copyright and Censorship', 'Malaysia', 'Security &amp; Privacy']
+++

<img class="wp-image-4051 aligncenter" src="/uploads/Slide2.jpg" alt="How IP addressing works" width="550" height="309" />

<span style="color: #000000;">Environment News Service, an environmental focused news website this week accused Malaysian government hackers of attacking it after it ran a story implicating Sarawak governor Tun Abdul Taib Mahmud of corruption and graft. As a result, the site was down for 2-hours, before the site manage to re-gain control.</span>

"The attack on our site came from a Malaysian government entity as identified by their IP address," Sunny Lewis, editor-in-chief of Environment News Service (ENS)

But what exactly is an IP address, and how did ENS identify it?

Let me explain.<!--more-->
<h2>What is an IP address?</h2>
The internet runs on a protocol--a set of rules that determines how data gets routed from one corner to another. These rules allow for every computer connected to the internet to communicate with every other computer and the protocol itself is aptly named the Internet Protocol, or more commonly known as IP.

Part of the protocol stipulates that every computer connected to the internet must have a unique number that identifies itself to the network. Just like how telephones have unique phone numbers, devices connected to the internet have unique internet numbers--or more accurately called IP addresses.

You can easily determine your IP address by logging onto <a title="What is my IP" href="http://www.whatismyip.com/" target="_blank">www.whatismyip.com</a>, or even just typing "what's my IP" into Google. But where does your IP address come from? Unlike Phone numbers, IP addresses aren't static, your IP address changes every time you reboot your router. Your IP address was 'given' to you by your Internet Service Provider (Unifi, Maxis, Digi..etc) and once you log-off or shutdown your router, your ISP then takes that IP address and assigns it to someone else. IP Addresses are like gold these days and ISPs need to dynamically allocate them to you, because they're subscribers exceed the number of IP addresses they have.

So your IP addresses are given to you by your ISP. But who gave your ISP their IP addresses?

The answer is your local Network Information Center (commonly called a NIC)

In our part of the world it's APNIC (or the Asia-Pacific NIC). You see as de-centralized as we think the internet is--there is still some level of centralization that requires an authority to administer. This is especially true in the allocation of IP addresses to Internet Service Providers--every region of the world has a local NIC that manages the IP address allocations to the local Internet service providers, to prevent them from issuing identical IP addresses across two different networks. It also means that there is a central repository that can tie each IP address and who that IP address was allocated to.

So while your IP address changes with every logon, at the very least it will continue to be a Unifi IP address each time (or Maxis or Digi..etc). Your ISP has a <span style="text-decoration: underline;"><strong>fixed</strong></span> pool of IP addresses that it then <span style="text-decoration: underline;"><strong>dynamically</strong></span> allocates to subscribers like you.

So how did Environment News Service know that Malaysian government hackers attacked them? They simply traced the IP address of the attacker (which they knew), and my guess is found it registered to the Malaysian government. I further speculate that the IP address would have belonged to <a title="GITN" href="http://www.gitn.com.my/" target="_blank">GITN</a> (the official network provider to the government)--which I wrote a couple of years back was used to <a title="Government Network used to download porn : Privacy is dead" href="http://www.keithrozario.com/2013/04/malaysian-government-network-download-porn-privacy-dead.html" target="_blank">download some porn on bit-torrent</a> -- so this wouldn't be the first time some hanky-panky went on over at GITN.
<h2>Some unanswered questions</h2>
Now some questions.

If these hackers were smart enough to hack a website, how come they weren't smart enough to hide their IPs? It's quite trivial to hide an IP (j<a title="Internet Privacy with TOR: Should the internet be anonymous" href="http://www.keithrozario.com/2012/06/internet-privacy-tor-anonymous-tracking.html" target="_blank">ust use TOR</a>)....which makes me sceptical of this entire claim, but then again we'll know more when we Environment News Service publish more information.

In any case, I highly doubt anyone in our government has the skills to do this--and someone as rich as Taib would have probably hired more competent professional to execute the so-called 'hack'. There are guys who openly advertise services to take down websites, and they start from as low as <a title="DDOS as a service" href="http://krebsonsecurity.com/2013/05/ddos-services-advertise-openly-take-paypal/" target="_blank">RM1 for every 10 minutes</a>. Basically these hackers offer their 'attacking' services for a fixed price--and some of them even offer 24/7 helpdesk support, and I'm not joking. So why in the world would someone like Taib even bother going to the government for something as trivial as this--when competent professionals are easily available.

The Malaysian government has been accused of taking down Malaysiakini and other news portals in the past. and in those instances the attack didn't come from the government, the very first attack in 2004 was reported to have originated from APIIT (yes the IT school), then Radio Free Sarawak was attacked prior to the 2013 General election, and that <a title="DDOS from 36 thousand IP addresses" href="http://blog.sucuri.net/2013/05/malaysian-election-and-ddos.html" target="_blank">DDOS came from more than 36,000 IP address</a> (yes, that's 36 THOUSAND)--this new attack seems like a paltry downgrade when compared to those, and run by amateurs.

I can only speculate of course, the Government is known to be <a title="I’m Sorry, the Malaysian Government IS spying on you" href="http://www.keithrozario.com/2013/05/the-malaysian-government-is-spying-on-you-finspy-fisher.html" target="_blank">spying on citizens</a> and <a title="10 Things you need to know about kangkung censorship" href="http://www.keithrozario.com/2014/01/10-things-you-need-to-know-about-kangkung-censorship.html" target="_blank">censoring the internet</a>--but sometimes the stories being thrown around make me question their authenticity.
<h2>Conclusion</h2>
Thanks for reading. If you want to learn more about IP addresses and what the hell IPV6 is, check out my two videos below:

<iframe src="//www.youtube.com/embed/0OMh3BlgyTo?list=UU_EIvVr3TnGpe5RgQ9E48-g" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>