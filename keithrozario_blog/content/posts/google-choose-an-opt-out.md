+++
title = "Googles Wi-Fi strategy: The Power of Defaults"
slug = "google-choose-an-opt-out"
date = "2011-11-30T19:51:09"
draft = false
categories = ['Misc']
+++

![](/uploads/index.jpg "index")One of my favorite blogs, nakedsecurity recently published an article that Google <a title="Naked Security" href="http://nakedsecurity.sophos.com/2011/11/17/google-forces-opt-out-wi-fi-snooping/" target="_blank">"<em>offering to stop mapping wireless access point location data, granting network owner s worldwide the choice to opt out from its Wi-Fi geolocation mapping</em>"</a>. The problem is, that Google is asking users who want to opt-out of their service to change the SSIDs of their Wi-Fi and add a <strong>_nomap</strong> postfix. This means that all Wi-Fi networks without the _nomap postfix would automatically be added to Googles database of Wi-Fi access points.

What does this all mean? Well apart from the obvious icky feeling you have in your stomach right now, the main summary is that Wi-Fi access points that aren't changed will automatically be added to Googles database (the Google Location Server). In short, the default setting is that you give permission to Google to store your Wi-Fis SSID until otherwise stated....eeeyeew.<!--more-->

If you're thinking it's no big deal, check out this image taken from <a title="Dan Ariely" href="http://danariely.com/2008/05/05/3-main-lessons-of-psychology/organ-donations/" target="_blank">Dan Arielys blog</a>:

![](/uploads/od_plot.jpg "od_plot")

The chart shows the percentage of citizens by each country who are registered organ donors. The obvious thing you notice is that the blue countries (Belgium, Austria, France..etc) have a near 100% organ donation record while the gold countries (Denmark, Netherlands and Germany) struggle to just break the 25% mark. Before you read further, let me also point out that in The Netherlands the government actually sent a letter to every single citizen nearly begging them to be organ donors and they're at 27.5% while in the blue countries no such action was taken (or even neccessary). It's also interesting to note that Belgium shares a border with The Netherlands and they're more or less in the same in every respect including culture and governance.

So how did the Belgians beat the Dutch?

The Belgians chose an opt-in strategy for their organ donation. In Belgium the moment you can drive, you have to fill up a form to be an organ donor. On the form, lies a box for you to tick to 'opt-out' of being an organ donor. In other words the default is that you're an organ donor and you have to tick the box to opt-out.

What's the effect of making it an opt-in instead of opt-out. If you compare Belgium to Germany, it's about 76%. If you compare Belgium to Denmark it's 90%.

Coming back to Googles example, had Google made it an opt-in rather than opt-out strategy, they probably wouldn't have capture anywhere from 70-90% of the SSID hotspots (possibly quite more), that's probably the rational behind it.

Naked security put it best in a rather eloquent graphic:

![](/uploads/google-nomap.jpg "google-nomap")

So the next time you want to influence behavior, don't forget to use defaults. They're really powerful.