+++
title = "Powerline adapter for better networking at home"
slug = "powerline-adapter-wifi-boost-extend-network"
date = "2014-06-17T09:00:30"
draft = false
categories = ['Misc']
+++



![AV500 Gigabit Powerline Adapter TL PA511](/uploads/AV500-Gigabit-Powerline-Adapter-TL-PA511.png)

A popular question I get, is how to boost a WiFi signal. Folks struggle to get good WiFi connections on the 2nd (or 3rd) floors of their homes because the routers they have don't pump enough  'juice' to go around. This is particularly true for those that work from home, having poor WiFi while trying to have a teleconference-- just sucks. While other applications like YouTube and Facebook could use buffering or caching, a real-time conversation with someone over skype relies on good connectivity all the way from one party to the other, and it doesn't matter if you have Unifi 20Mbps, if your WiFi is laggy.

I thought I could fix this <a title="Asus N12 HP: The best Unifi replacement router?" href="http://www.keithrozario.com/2013/08/asus-unifi-rt-n12-hp.html">by buying a more powerful router</a>--but that didn't work. The signal strength increased, but the quality was still below par.

The best solution is to skip WiFi  and get a Powerline Adapter instead. A powerline adapter uses your home electricity wiring to transmit the data, and because it uses wires, it'll beat any wireless connection you have. The adapters fit nicely into your 3-Pin wall sockets, and all you need is Ethernet cables to plug into them to hook up your laptop or PC to your router located somewhere else in your home.

The premise is quite interesting and the results are even better.

<!--more-->
<h2>Setup a Powerline Adapter</h2>
To setup a powerline connection you'll need a minimum of two adapters. You can buy these as a 'starter' kit from any computer store. They cost about Rm150-Rm200 and allow you to hook up your home router to just about any other power socket you have in your home.

So if your home-office is upstairs while your Unifi router is downstairs, you can hook up these two points without any additional wiring or WiFi boosters. Just plug one adapter near the router and connect an Ethernet cable there, and plug the second adapter to your home-office upstairs for your laptop to connect into.

I won't even described how to set it up here, because it really was a press of buttons. The setup took less than a minute, and once your two adapters are configured you can move them around your home without any further configuration.

One last thing, get a Powerline adapter with AC-Passthru, which allows you to use the wall socket for your electrical appliances even with the Adapter. Some adapters don't come with AC-Passthru, which means you can't use the AC socket once you're connected. That just sucks.



![Powerline Adapter passthru](/uploads/Passthru.jpg)


<h2>The Quality of a Powerline Adapter</h2>
The quality of a powerline connection is dependent on two things:

1. The length of wiring

2. Your home wiring configuration (3-phase, circuit breakers, etc). A Powerline adapter can work in a 3-phase wired house, but if the two sockets are on different phases you can expect some loss of quality for a connection between the two.

Because 1 and 2 are hard to determine in your home. I've conducted a few test to help you compare a powerline adapter to WiFi.
<h2>Testing the speed of a Powerline connection</h2>
To test the speed of the powerline connection I setup two machines on my LAN.

First a laptop connected to the router via a Powerline connection. Second a PC connected to the router directly via a direct Ethernet cable. The router is the <a title="Asus N12 HP: The best Unifi replacement router?" href="http://www.keithrozario.com/2013/08/asus-unifi-rt-n12-hp.html" target="_blank">ASUS RT N12 HP</a>, which is a decent router, but not blazingly fast.

The Powerline adapters I used was the <a title="TP Link AV500 Powerline" href="http://www.lazada.com.my/tp-link-av500-powerline-adapter-with-ac-pass-through-starter-kit-543401.html" target="_blank">TP-Link AV500 powerline adapter which I bought as part of a starter kit from Lazada at Rm15</a>5.

Finally I installed LanSpeedTest(lite) on the laptop on used it to transfer 1 GB of data from the laptop to the PC. LanSpeedTest would both write and read the data.
<h2>Powerline vs. WiFi 10ft</h2>
At a distance of 10 feet from the router, both WiFi and Powerlines perform equally well. The write speeds are identical, but the read speeds for WiFi is much better than Powerline and this is expected. In fact the Wifi was able to read fata at 85Mbps, while the powerline could only do so at 68Mbps.

While the power socket itself is just 10ft from the router--the wiring for the powerline connection will need to travel from the input to the fusebox and then to the output, which could be 50ft for all I knew.And if the input and output sockets are on different phases you'll lose a couple of dB on top of that. So over close distances, WiFi is actually better, but how did it do when my laptop was upstairs?



![Powerline vs. WiFi 10ft](/uploads/Powerline-vs.-WiFi-10ft.png)

<a href="/uploads/Powerline-vs.-WiFi-10ft.png">
</a>
<h2>Powerline vs. WiFi (2nd floor)</h2>
Here's where the powerline adapter really shines, because the powerline experiences less degradation over distance, the gap between WiFi and Powerline grows bigger with every meter you put between yourself and the router. So while the WiFi quality dropped significantly when I moved the laptop upstairs, the Powerline connection didn't. Resulting in almost identical speeds whether you were 10ft away from your router, or 100ft.



![Powerline vs. WiFi 100ft](/uploads/Powerline-vs.-WiFi-100ft.png)


<h2>Powerline vs. Ethernet</h2>
Just to give you a flavor of how quick Ethernet is, I did a test where I hooked up my laptop to the router directly via an Ethernet cable. The results show the absolute maximum speed of the router, which helps put the Powerline numbers into perspective. As expected, since my router only supported IEEE 802.3u, the fastest connection possible was 100Mbps, and my real world results were about 93% of the theoretical maximum.



![LAN Speed Test-routerdirect(2)](/uploads/LAN-Speed-Test-routerdirect2-284x300.png)



What this means is that a powerline connection through at least 100ft of wiring can maintain nearly 75% of the theoretical maximum speed of your router. Which is really good. I wonder if I had a Gigabit capable router what my speeds could be?

The real-world results demonstrate that while powerline isn't as good as Ethernet--it's almost as good, and for connections through your multi-storey house, a powerline adapter is a far better option than a WiFi booster.
<h2>Conclusion</h2>
If you're looking for  a more stable connection at home, a Powerline adapter i the s a great choice. It works remarkably well and provides better speed and reliability over a regular WiFi connection.

However, there are drawbacks. Some readers have commented that you can only run one Powerline circuit at your home--meaning connecting to just one machine. Running more connections over your home wiring severely degrades the speed and reliability of the connection.

Secondly, the Powerline adapter doesn't work with WiFi only devices, and a lot of new netbooks are being shipped without Ethernet ports. For those you can try Powerline Wifi extender instead (link <a title="Powerline WiFi Extender" href="http://www.lazada.com.my/tp-link-300mbps-av500-wifi-powerline-extender-starter-kit-543407.html" target="_blank">here</a>)

So the Powerline adapter may only work on specific cases. But it's a cheap and far easier solution than a Wifi Booster--and provides better reliability.