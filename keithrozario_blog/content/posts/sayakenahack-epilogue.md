+++
title = "Sayakenahack: Epilogue"
date = "2017-11-24T19:00:29"
draft = false
categories = ["Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

I keep this blog to help me think, and over the past week, the only thing I've been thinking about, was sayakenahack.

I've declined a dozen interviews, partly because I was afraid to talk about it, and partly because my thoughts weren't in the right place. I needed time to re-group, re-think, and ponder.

This blog post is the outcome of that 'reflective' period.

The PR folks tell me to strike while the iron is hot, but you know -- <em>biar lambat asal selamat.</em>
<h2>Why I started sayakenahack?</h2>
I'm one part geek and one part engineer. I see a problem and my mind races to build a solution. Building sayakenahack, while difficult, and sometimes frustrating, was super-duper fun. I don't regret it for a moment, regardless of the sleepless nights it has caused me.

But that's not the only reason.

I also built it to give Malaysians a chance to check whether they've been breached. I believe this is your right, and no one should withhold it from you. I also know that most Malaysians have no chance of ever checking the breach data themselves because they lack the necessary skills.

I know this, because 400,000 users have visited my post on "<a href="https://www.keithrozario.com/2012/07/change-unifi-password-wifi-dlink.html">How to change your Unifi Password</a>".

400,000!!!

If they need my help to change a Wifi password, they've got no chance of finding the hacker forums, downloading the data, fixing the corrupted zip, and then searching for their details in file that is 10 million rows long -- and no, Excel won't fit 10mln rows.

So for at least 400,000 Malaysians, most of whom would have had their data leaked, there would have been zero chance of them ever finding out. ZERO!

The 'normal' world is highly tech-illiterate (<a href="https://www.bfm.my/tech-talk-consequences-tech-illiterate-keith-rozario.html">I've even talked about it on BFM</a>).  Sayakenahack was my attempt to make this accessible to common folks. To deny them this right of checking their data is just wrong.

But why tell them at all if there's nothing they can do about it? You can't put the genie back in the lamp.<!--more-->
<h2>What's the point though?</h2>
A recurring criticism of the site is that people can't do anything about the breach, hence the site pointless, and dangerous.

Which is crazy to me, because your right to know, shouldn't be contingent on your ability to do something about it. Legal rights don't work that way.

In any case, regardless of people's ability to respond, the site has achieved a few things. One of which is give us clarity on the data.

Within the telco breach, once I loaded data from Maxis, Digi, Celcom, UMobile, TuneTalk, and RedTone -- the total rows in the Database was <em><strong>only</strong></em> 37mln (not 46 mln as most claim). That's because people (including lowyat) were blindly counting rows in Excel. But when you put that data into a data model and start inserting those millions of row into a database, things get interesting.

Some files were missing myKad numbers (<em>hence not loaded in the system</em>) and others had duplicates. I estimate that with the smaller telcos that number might have increased to 38mln, but not any higher.

I think the Malaysian public deserve <strong>more</strong> than a cursory Excel analysis -- don't you? And it gets better.

Some telco's gave a lots of information, others gave a bare minimum. The amount of your personal data exposed in the breach is highly dependent on which telco you were subscribed to in 2014. And even then, some anomalies existed, such as missing names and addresses (this is typical of any IT system).

Hence, not everyone was equally affected, and the site was built to communicate 'effectively' how and where you were breached, with as much detail I could provide without infringing on people's privacy.

My code checks each row of each file, and reports which fields are present, to give people very specific information about what data of theirs is in the breach.

A blanket statement like "All Malaysians impacted" is highly simplistic, and ineffective. Putting your masked number on a screen after you've entered your IC, really brings home the fact that your data has been leaked.

If you're uncomfortable with seeing your own details on a screen, how much more uncomfortable would it be to know that any Tom, Dick and Harry online can view those same details about you at the click of a button.

Blocking my site, and trying to put the genie back in the bottle -- that's pointless. Giving people the ability to discern exactly what elements of their personal data is exposed is not.

So hopefully you get why I did, and now let's move on to the question of legality.
<h2>Is it legal?</h2>
It was always going to be grey area, but I strive to make it more white than black.

The bar council seems to think <a href="https://www.thestar.com.my/news/nation/2017/11/18/bar-council-website-did-not-breach-law-sayakenahackcom-only-provides-information-does-not-allow-data/">sayakenahack is alright,</a> and while I'm no lawyer, I obviously agree.

If you make it illegal to hold stolen data, then only criminals will have it. Legitimate researchers and journalist would thread cautiously around it, ensuring that none of it gets reported, and even less people are aware.

The only thing worse than having your data exposed, is not knowing about it being exposed.

If you make services like sayakenahack illegal,  people will start going to services like <a href="https://www.troyhunt.com/thoughts-on-the-leakedsource-take-down/">Leakedsource</a>, if only to check on themselves. You will legitimize the business practice of selling stolen data, and put more folks at risk. Is that what you want?

Making something illegal has never deterred criminals from doing it. It's kinda what they do.

Blindly following the PDPA, is to hold ourselves hostage to ancient legislation (7 years is 2-3 generations in tech) that was probably enacted by technically illiterate members of parliament. I'm not saying we don't follow the law, I'm just saying we don't blindly follow it. There are multiple exemptions to the law, and some of them can be applied her.

But even if this site was on the white side of grey, and even if my intentions were noble, and even if we assume it's perfectly legal -- how can you trust me?
<h2>How can we trust you?</h2>
My name, reputation  and even possibly freedom is based on keeping this thing legitimate. Like everything else, if you don't trust me, don't enter your IC number.

I cannot prove that I don't log data, anymore than I convince you that there is no spaghetti monster orbiting the 3rd moon of Jupiter. You can't prove a negative.

But at least trust in logic and maths.

200,000 users visited sayakenahack. Without the block, I estimate that number would have been 500,000.

But 500k out of 37mln is still less than 1.5%. ONE POINT FIVE PERCENT!!!

Accusing me of phishing through the site, is like accusing Bill Gates of pickpocketing at the MRT. Why would a billionaire with so much money, waste his time and risk himself, to steal a fraction of his fortune?

Why would I bother with 500 thousand, when I have 37 MILLION.

There's no logical reason for me to log.

And yet they used it as an excuse to block me.
<h2>What do I think of the block?</h2>
Well, I don't agree with censorship in general, regardless of whether it affects me or not. So the block isn't a good thing. I wasn't happy with the <a href="https://www.keithrozario.com/2017/09/potongsteam.html">#potongsteam</a> block, and I don't even play that many games.

That being said, AWS cost dollars. so blocking the site actually saves me money :).
<h2>Did the MCMC or PDP contact you?</h2>
No.
<h2>Did you contact the MCMC or PDP?</h2>
Yes.

Both of them.

No answer so far.
<h2>What about siapakenahack and Lowyat?</h2>
Between the two of them, CF Fong and Vijandren Ramadass have accused me of <a href="https://www.themalaysianinsight.com/s/23152/">manipulating data</a>, <a href="https://www.youtube.com/watch?v=q9zz6DEnmrk">being unethical</a>, and <a href="https://forum.lowyat.net/topic/4458963/+80">glory-hogging.</a>

Just to let you know, that I'm none of those things.

When I tweeted about the number of hits the site was getting, I thought it was cool that my architecture could support that kind of traffic. I never meant that data breaches were cool, which is what Vijandren suggest, and cites as the moment he 'gave up' on me.

And I'm more than happy for someone to critique my design, comment on the architecture, or point out flaws. But calling me unethical?! That's harsh.

Even so, I'm letting bygones be bygones. Time for everyone (including me) to move on.
<h2>What's next?</h2>
I go back to Malaysia soon. If you don't see me after that, you'll know where I am.

Take care Malaysia.
<h2>Conclusion</h2>
The vast (vast!) majority of folks have been supportive of sayakenahack, and for that I am <em>(and will forever be)</em> immensely grateful. <strong>Immensely !!</strong>

You can't please everyone, and contrary to popular belief, I even appreciate the critics. At least they're keeping you on your toes. I especially liked the legal disclaimer of siapakenahack -- couldn't stop laughing when I saw it.

So thanks everyone for your support. If the rumors I hear are right, this story is far from over. Expect earth shattering headlines next week -- and hopefully I won't be in them :).

Keith out (mic drop!!)

<em>[FYI, that two year old interview from BFM has aged remarkably well, I highly recommend it (<a href="https://www.bfm.my/tech-talk-consequences-tech-illiterate-keith-rozario.html">link here</a>)]</em>