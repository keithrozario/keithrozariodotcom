+++
title = "How I hacked 4 Unifi accounts in under 5 minutes"
slug = "hack-unifi-in-5-minutes"
date = "2014-01-02T22:00:14"
draft = false
categories = ["Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

So I was wondering if I should publish this, but I guess I have to. If you're one of the 500,000 Unifi subscribers in Malaysia, you need to know that your stock router--is completely hackable. TM has left you literally hanging by your coat-tails with a router that can be hacked as easily as pasting a link. So I was struggling to figure out if I really should have made this post, but in the end I think it's better for you (and everyone else) to know just how easy it is to Hack Unifi accounts--not so you can hack them, but so that you can take some precautions over the situation.

But first, some caveats--everything I'm showing here is already public knowledge, the only difference is that I've culled and aggregated knowledge from different streams to show you just how easy an attacker can circumvent your password protection on your Unifi Dlink DIR-615 router, which is the stock router that comes with Unifi. It's better for you to know about it than to remain oblivious to possibility that anyone from anywhere in the world, sitting in their room with their pyjamas on, can log onto to your router and start doing some rather nasty stuff.

Second caveat, is that as a result of this, some 'kiddy-hackers' may see this post and now be empowered with the means to attack, that's a risk I'm willing to take to allow for everyone to know about it, so that they can do something about it. Keeping everyone in the dark about vulnerabilities of their routers is not a good thing. Security works better when everyone has access to the same information, this is how security works, and if you don't agree--well tough luck.

With that said, here's how you use Shodan, and a well known exploit to hack Unifi. The final exploit which doesn't require any knowledge of the passwords starts at 4:08

<span style="color: #c0c0c0;"><strong>Update 22-Jun:</strong> My Apologies: YouTube have removed my video because someone reported it as being inappropriate. I am appealing..I'm not sure what about the video was inappropriate, and I have made no attempt to mis-lead anyone. Stay tuned. I've updated the video with a Vimeo upload instead.</span>



![Video Rejected by Youtube](/uploads/Video_Rejected_Content_Inappropriate_2.png)



<iframe src="//player.vimeo.com/video/98848750" width="500" height="281" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

<a href="http://vimeo.com/98848750">Hacking Unifi Dlink routers using Shodan</a> from <a href="http://vimeo.com/user29391644">Keith Rozario</a> on <a href="https://vimeo.com">Vimeo</a>.

Details of the hack:

1. To access the password page the appendage is <span style="color: #888888;">/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd</span>

2. To search for Dlink Routers on <a title="Shodan " href="http://www.shodanhq.com/" target="_blank">Shodan</a> the query is <span style="color: #888888;">Mathopd/1.5p6 country:MY</span>

I've alerted TM to this much earlier, in August 2013 actually, and they promised they'd fix it by the end of the year. To be honest though, I don't blame them, your router security is your responsibility and not TMs, so I think that TM<span style="text-decoration: underline;"> isn't doing anything wrong by not doing anything</span>. A user should be responsible for the security of the router, just like how you are responsible for the security of your phone--even if you did get it free from Maxis or Digi. So anyhow, in the absence of any clear action from TM, I've taken it upon myself to inform you of the router vulnerability, and here's hoping you do something to fix it.

As always--stay secure.

To address the issue check out my post on how to prevent this on your Unifi router, click on my post <a title="How to prevent your Unifi account from being hacked" href="http://www.keithrozario.com/2014/01/prevent-unifi-hack-fix.html">here</a>.

<!--more-->



![TM were informed in August](/uploads/TM-changing-passwords.png)





![Telekom_malaysia_acknowledge_exploit](/uploads/Telekom_malaysia_acknowledge_exploit.png)

