+++
title = "Streamyx forced ads (202.71.99.194)"
slug = "streamyx-forced-ads-202-71-99-194"
date = "2014-12-18T18:31:31"
draft = false
categories = ['Security &amp; Privacy']
+++

![Streamyx forced ads](/uploads/streamyx-forced-ads.png)

A couple of days back, I was at my in-laws doing some browsing on their PC. Now my in-laws have a Windows XP laptop, that isn't secured, which is fine because as far as I can tell, I'm the only one that uses it. Most of them now go to their phones or tablets for internet access--nobody uses PCs anymore!!

But I noticed something strange. I wasn't able to access Amazon, which was where I was browsing for some Christmas shopping (but not logging in of course). Somehow every time I typed www.amazon.com on the browser, it would re-direct me to a Lazada advert. Now this looks like a piece of malware---sounds like a piece of malware--but after some investigations, I discovered this WASN'T a piece of malware.

Instead I realized that this was a problem with the streamyx DNS. For some reason all the traffic that should have been routed to Amazon, was being routed to a TM IP address at 202.71.99.194. A quick Google search led me to this <a title="https://forum.lowyat.net/topic/2960704/all" href="https://forum.lowyat.net/topic/2960704/all" target="_blank">lowyat</a> post, and this <a title="https://forum.lowyat.net/topic/2840467/all" href="https://forum.lowyat.net/topic/2840467/all" target="_blank">one</a>,  post from 2013--so this wasn't new. TM was routing all unresolvable domain names to adverts that looked so much like malware, it's indistinguishable from a malware infection.

TM was doing exactly what malware authors do!!

I would never have encountered this problem, because I use Open DNS--but this is unacceptable from TM. To deploy something, that behaves and acts like a piece of malware, just so they can force feed you some adverts isn't just unethical and bad ISP practice--it's terrible security.

Because when you deploy something that looks and acts like malware--but isn't. Then people get de-sensitized to malware infections and soon ignore malware infections, thinking it's legitimate shit done by their ISP.

TM should fix this--and really should stop this nonsense.

It's now a good a time as any to change your DNS settings so you're not susceptible to this Malware look-alike.