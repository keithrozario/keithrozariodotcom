+++
title = "How the StarHub DDOS (possibly) happened"
date = "2016-10-27T23:46:38"
draft = false
tags = ['DDOS', 'Dyn', 'IOT', 'Singapore']
categories = ['Misc']
+++

<a href="/uploads/StarHub-DNS-attack-1.jpg"><img class="alignleft wp-image-5873 size-medium" src="/uploads/StarHub-DNS-attack-1-300x225.jpg" alt="starhub-dns-attack" width="300" height="225" /></a>Customers of Singaporean ISP StarHub, suffered two major disruptions to their service over the past week, in what the telco said was a result of a "intentional and likely malicious distributed denial-of-service (DDoS) attacks".

Oh the humanity!!

In what appears to be a copycat of the <a href="http://hub.dyn.com/dyn-blog/dyn-analysis-summary-of-friday-october-21-attack">Dyn attack</a> we saw (at roughly the same time), the attack signals the first local salvo in the war of IOT devices. But is it really that serious?

If you're wondering what the hell happened, let's walk this through step-by-step, from the attackers perspective.<!--more-->
<h2>Step 1 : Download Mirai Source Code</h2>
10 days ago, a hacker by the Anna-Sepai <a href="https://krebsonsecurity.com/2016/10/source-code-for-iot-botnet-mirai-released/">released the source code</a> for Mirai,  an extra-special malware used for executing DDOS attacks.

Think of Mirai as a virus built to hack into Internet-of-Things (IOT) devices like CCTVs, and IP cameras. Mirai would infect a device and turn it into a slave awaiting instructions from its 'master'. With each infection, the master gains control of an additional device, beginning with the first device and ending up with a army of them--typically called a botnet.

Remember that term IOT and botnet we'll be using it often.
<h2>Step 2 : Deploy Mirai and start building your botnet</h2>
Once the hacker downloaded the code, she could simply unleash it on the general internet, hoping to infect as many devices as possible. In this particular case though, the hacker set her sights on just StarHub IP addresses. (we'll see why in a minute).

If you're wondering how easy it is to hack into IOT devices like routers or DVR, just look at <a href="https://www.keithrozario.com/2014/01/hack-unifi-in-5-minutes.html">what I did 3 years ago</a>.

In many cases these IOT devices are un-secureable. Meaning the security on them is so poor, you couldn't secure them even if you wanted to---and quite frankly very few customers who buy a $100 camera is going to worry about things like internet security.
<h2>Step 3 : Pick a target to attack</h2>
Once the hacker had amassed enough devices in her botnet, she could then order it to attack.

But attack what?

Well, the internet might be distributed, and there are pockets of centrality, and one of those pockets is called DNS.

DNS is a topic we've covered often here, and that's because the entire web hinges on it. Think of DNS as the GPS of the internet, every time you instruct your computer to go somewhere like Google.com, or keithrozario.com, your computer refers to the GPS to tell it how to get there.

And just like my wife, your computer is completely lost without GPS. So the moment you disrupt GPS, it's as good as disrupting the internet.

DNS is that GPS for the inernet, and while your computer may be working perfectly, and the website you plan to visit is also up--your computer doesn't know how to get there. So from your perspective the site is as good as down.
<h2>Step 4 : Attack!!</h2>
So with a target set, and the botnet ready, the hacker then unleashed the attack.

A DDOS attack is the blunt-instrument, it's purely about hitting a server as hard as possible. So all the botnet did was generate traffic to the DNS servers hosted by StarHub for their customers. If there were enough devices in the botnet, and they generated enough traffic the StarHub DNS service would soon experience degradation, leading to complete failure.

Basically the DNS service was tied up with traffic from the botnet, it couldn't respond in a timely fashion to legitimate request from StarHub subscribers.

So now that we know what happened to StarHub, how did they respond?
<h2>StarHub strikes back</h2>
According to StarHub's <a href="http://www.straitstimes.com/tech/starhub-broadband-disruption-due-to-spike-in-traffic-that-jammed-its-domain-name-servers">official statement </a>they "mitigated the attacks by filtering unwanted traffic and increasing our DNS capacity, and restored service within two hours".

The simplest way to resist a DDOS attack is to have more capacity then your attacker. Also, by filtering traffic, that reduces the load on the servers as well--allowing them space to respond to legitimate request.

Overall, pretty straightforward solutions---and they worked!

But if StarHub managed to resolve their attacks in two hours, how come the internet is panicking over the same attacks on Dyn?
<h2>Why StarHub is different?</h2>
First of all, StarHub's attack was probably on a much smaller scale than the 620Gbps attack that hit Brian Krebs website 2 weeks earlier,  or the 1.2Tbps attack that hit Dyn.

Secondly, StarHub's DNS service is an internal service available only to its subscribers. Although I didn't check this, ISPs in Malaysia host DNS servers that are accessible only by customers of the ISP, and I'm guessing StarHub is the same.

Since StarHub is only providing DNS to their customers, they block any request to their DNS service from outside their network. Put it simply, only StarHub subscribers can access StarHub's DNS.

Therefore, only StarHub subscribers can DDOS StarHub's DNS.

Hence why the attacker only chose to infect StarHub devices.

So obviously the <a href="http://www.todayonline.com/singapore/ddos-attacks-starhub">source of the DDOS traffic had to be from StarHub subscribers</a>, and more importantly, meant the attacker actually chose the target of her attack <span style="text-decoration: underline;">first</span> before infecting the IOT devices, because why else would she limit herself to just StarHub subscribers.

In plain English, an attacker decided to attack StarHub's DNS service, and only then set out to infect machines to accomplish this task. This puts the attacker in a whole different light, because this suggest that she wasn't some script-kiddie looking to test out Mirai on a random service, but rather she executed a well planned attack, presumably for some end-goal that isn't quite clear.

But I'm digressing--back to why this is different from Dyn.

Dyn is a global service available to anyone with an internet connection, and just about everything on the internet is global in nature. It's much harder for  a global service to 'filter' their traffic, because all traffic 'legitimate or otherwise' appears the same, and they can't do geo-blocking.

So Ok, StarHub isn't the same as Dyn--what can you do?
<h2>What can you do?</h2>
First things first, if you experienced the outage, that means you're using StarHub's DNS service--at at the very least re-adjust your DNS settings to point to either <a href="https://developers.google.com/speed/public-dns/">GoogleDNS </a>or <a href="https://www.opendns.com/home-internet-security/">OpenDNS</a> (or better both of them with one primary and one secondary). <em>[Pro Tip: if you <a href="https://www.keithrozario.com/2013/09/best-vpn-malaysia-privateinternetaccess.html">use a VPN like PIA</a>, the DNS resolution happens on their end, giving you even more privacy from your ISP]</em>

Secondly, make sure you're not part of the botnet.

The Mirai malware, targets a specific type of IOT device from a specific <a href="https://krebsonsecurity.com/2016/10/who-makes-the-iot-things-under-attack/">supplier(s)</a>.

Even if the owner of the infected camera were to hard-reset their device (i.e. hold down the reset button and setup the camera again), chances are the camera would be <a href="https://krebsonsecurity.com/2016/10/who-makes-the-iot-things-under-attack/">re-infected in minutes</a>. Basically the only thing you can do is throw away the camera and get a new one.

Problem is, I don't know which one to recommend, because they all apparently have shitty security.
<h2>Conclusion</h2>
There really is some next level shit going on in the world of DDOS, but the StarHub isn't any cause for concern.

Other publicly available services may not be so lucky though. Imagine if the myTax portal gets hit on submission date, or a private news portal gets hit during election season, or worse yet, a hacker DDOS's foodpanda on a Friday evening---how will I eat?

If anything this was a pretty mild attack, because StarHub could easily respond--but we might not be so lucky in the future.

For more of my thoughts on the subject, read yesterday's post here.

&nbsp;