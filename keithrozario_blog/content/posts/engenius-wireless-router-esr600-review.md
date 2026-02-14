+++
title = "EnGenius Wireless Router ESR600 Review"
slug = "engenius-wireless-router-esr600-review"
date = "2015-07-01T08:00:46"
draft = false
categories = ['Misc']
+++



![dsc00503](/uploads/dsc00503.jpg)



A couple of weeks back, the guys over at infoversal loaned me a Engenius ESR600 router for a review, at first I was a bit hesitant, but my overall unhappiness with my TP-link router made me think twice. So I gave it a shot, and boy was it worth it.

The router looks pretty normal, nothing to shout about here. While its competitors like Asus and TP-Link opted to go for black exteriors, Engenius chose to stick to white-ish color, this thing doesn't look good near modern TV sets or  home theatre systems (which is where my router is), but the fact that it doesn't have antennas seems to be a saving grace.

That being said, the Engenius is a pretty slick device, I'm not sure how it does it, but the antenna-less design Engenius has more signal strength than my TP-Link router over both the 2.4Ghz and 5Ghz range. Yes, the router is dual-band and one that actually works well over both bands. So great points for Engenius in that category.<!--more-->
<h2>Setup</h2>
Setting up the router took some time, the guys from infoversal came over to help me set it up, and we managed to get it up and running in minutes, but my itchy fingers and a couple of wrong settings later forced me reset the router. Getting the router up-and-running from a factory reset took quite some time, and it wasn't easy, I had to call the guys up for help walking me through the steps, hopefully the final firmware version for Malaysia makes it easier to set this up. I've been told Infoversal created a special Unifi firmware for this so maybe that's why.

The other thing I need to mention is that the Engenius User Interface is one of the best I've seen. In my opinion still not as cool as the Asus interfaces, but pretty close. On the other hand TP-Link has an interface that looks like it was designed in the 80's by a color blind college student, while D-link looks cobbled together from left-over DOS games.
<h2>Features</h2>
There's a ton of features on most modern routers, even on the lower price points, the ones that are important to me are:

QoS settings 

![EnGenius Wireless Router ESR600](/uploads/EnGenius-Wireless-Router-ESR600.png)

QoS (Quality of Service) is a special setting on the router that allows you to select which traffic to prioritize. For example, in my home, I'd like to prioritize my gaming traffic, and my work traffic for when I take teleconference calls. This is very important, otherwise my wife can cause me to lose the game, or experience laggy meetings simply because she's watching korean dramas on her iPad.

I consider QoS to be an essential feature on a router, and most routers offer this out of the box. However, Engenius offers the feature to set specific machines to higher priority which saves you the trouble of figuring out the specific traffic you're interested in.

For example, if I want to implement QoS on my existing routers, I'd have to identify which game I was playing, what ports (or even IP addresses) were involved and set the QoS accordingly. This is painful if you play lots of game, a simpler solution would be to just give highest priority to your gaming machine, and no matter which game you were playing, that gaming traffic would get the highest priority.

This sets it apart from other routers like TP-Link and Asus, and don't even think about the standard D-Link 615, that doesn't even have this feature.
<h2>DDNS (dynamic DNS)</h2>
Most routers provide some sort of Dynamic DNS capability, but only a select few offer their own. I often find the routers that offer their own DDNS service to be more reliable, and doesn't require you to renew accounts on 3rd-party services.

In all, D-Link, Asus and Engenius provide their own DDNS service, TP-Link again lagging the pack here and bundle theirs with 3rd-party services, some of which no longer work, or can only be setup if you understood Mandarin.

The beauty about Asus and Engenius though is that theirs doesn't even require a lengthy registration process and can be completed from the router itself. For comparison sake, take a look at the steps involved in setting up DDNS for Dlink routers at this <a href="https://www.keithrozario.com/2012/09/setting-up-dlink-ddns-unifi-router.html">link</a>.
<h2>Signal Strength and others</h2>
I was really impressed with the Signal Strength of the Engenius routers. Really good coverage over my entire house over both bands. The only router that provides slightly better coverage was the Asus N12-HP and that had unusually long and powerful antennas, while this is antenna-less.

[caption id="attachment_5062" align="aligncenter" width="542"]

![signal-strength](/uploads/signal-strength.png)

 Signal Strength of the Engenius from about 10m away from the first floor of my home.[/caption]

[caption id="attachment_5060" align="aligncenter" width="431"]

![Encore-1GB-upstairs](/uploads/Encore-1GB-upstairs.png)

 Speed of a 1GB file transfer over Wifi on different floors in the house[/caption]

Other features that are standard include port-forwarding, port-triggering, guest networks, parental control...etc. Like most routers these days, it also comes with bloat features like IP Camera integration, file sharing etc, but I'd advise against using your router as an internet file-sharing device for multiple security reasons.

Overall, the router is solid, but has some drawbacks.
<h2>Drawbacks</h2>
Apart from the color, which I mentioned earlier, the Engenius has 2 real weaknesses that can't be easily over-looked.

Firstly, I can't switch off the WAN interface. Even after ensuring I set all the right settings to disable logging in via the internet, the router still has a web interface that is internet facing. What this means is that your router continually tells the internet that it's on and ready--that's a not a good thing with search engines like <a href="https://www.keithrozario.com/2014/01/hack-unifi-in-5-minutes.html">Shodan around</a>.

Secondly, nearly every change to the router requires a re-start. Whether it's a WiFi SSID change, or even a username/password change, that for most routers wouldn't be a problem. This means setting up the router can take an unusually long time, and that just dents the first impression you have of the router. Overall though, I wouldn't consider this big issue as long as Engenius fix the first one.
<h2>Conclusion</h2>
I can't recommend this router until (and unless) Engenius works diabling the entire WAN interface. If I set the router to not be accesible from the internet, the router shouldn't even be responding to pings, let alone display an interface publishing its make and model.

If however, you don't mind that, or you're using a Maxis connection with a private IP range, then I really think this is a solid router to use. With its great signal strength, nice interface looks, good feature set the only thing to consider would be its price point. If the Engenius comes it at around Rm180-Rm220 range, that would be perfect, anything less would be a steal, slightly more would still be OK but I'd have a hard time recommending this for anything over Rm250.

*I've been told the router would come in at the Rm300 price range, which is pretty premium, but you're still getting a better router than the RM220 Asus 12HP or the Rm250 Tp-Link N750 (both of which I own)