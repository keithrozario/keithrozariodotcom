+++
title = "Part 8: False prepaid registrations"
date = "2017-12-20T11:00:08"
draft = false
categories = ['Misc']
+++

Consider this a bonus piece from my long thoughts about data breaches. You might the <a href="https://www.keithrozario.com/2017/12/that-long-post-about-data-breaches-you-never-wanted-to-read.html">older post</a> before reading this. So let's dive in.

The telco breach was a giant hairball of issues, and one of the strands in the hairball is false prepaid registrations.

Immediately after releasing sayakenahack, people reported that they were seeing additional numbers linked to their mykad numbers. From <a href="https://www.thestar.com.my/news/nation/2017/11/16/bad-news-for-the-victims-more-data-breach-likely-to-happen/">TheStar</a>:
<blockquote>Malaysian Communications and Multi­media Commission (MCMC) network security and enforcement sector chief officer Zulkar­nain Mohd Yassin said it would <span style="text-decoration: underline;">most likely be a case of other people using another person’s identity to register</span>.

“We are serious about this. That’s why you see many compounds issued by the MCMC to service providers in respect of non-compliance with the guidelines of prepaid registrations,” he said.</blockquote>
He's right, telcos have been issued summons for false registrations every year from <a href="https://www.mcmc.gov.my/media/press-releases/mcmc-audits-mobile-prepaid-registration?lang=en-US">2014 to 2017</a>, with<a href="https://www.digitalnewsasia.com/digital-economy/mcmc-fines-five-telcos-nearly-rm1mil-over-false-prepaid-registration">Tune Talk chief executive officer Jason Lo telling Digital News Asia (DNA):</a>
<blockquote>...although there are many systems in place to ensure registrations are as accurate as possible, with a network of thousands of dealers, it can be hard to monitor every one</blockquote>
The Malaysian Telco Breach was two issues. One was the chronic problem of false prepaid registration, and two, the breach itself. The former is not a trivial issue, because the Evidence Act in Malaysia states:
<blockquote>A person who is registered with a network service provider as a subscriber...on which any publication originates from <strong>is presumed to be the person who published ...</strong>unless the contrary is proved.</blockquote>
Hence, if a phone number, that is registered to you, is publishing seditious statements on WhatsApp you would be deemed to have published them. And the onus is on YOU, to prove otherwise, a guilty till proven innocent kinda law.

So what do we do?

In I.T we have a saying, if you can't prevent, at least detect.

So if we can't prevent false registrations, we should at least allow for victims to check regularly.

But how to check?
<h2>Solutions that scale</h2>
<a href="https://themalaysianreserve.com/2017/11/21/siapakenahack-com-designed-educate/">The Malaysian Reserve</a>, quoted one expert saying that we should all call our mobile providers to find out, the expert added that it took him 'only' 20 minutes to do so.

Only 20 minutes? Only??!!

Malaysia has 10 different Telcos, if calling one takes 20 minutes, calling all of them would take 3 hours. That's too high a price just to check if you're part of the breach. No wonder nobody has bothered.

The telco breach had millions of records, If we assume that 20 million victims made these 3 hour calls, that's 60 million man hours spent.

Even if the telco's collectively dedicate 3000 people, working 8 hour shifts, 24x7. It would take <strong>7 years</strong> to inform all the victims. If those 3000 people were paid a monthly salary of RM1000, the cost for labour alone would be RM250 million.

Any solution that requires victims to place phone calls, will fail, because the scale of the breach cannot be solved manually. A solution that would work for 1000 victims may not work for 20 million.

The solution should be, <em>oh, I don't know</em>....something like a central website, where you type in data, and get a automated response with no human intervention, and maybe it would be able to verify your phone number through a One-Time-Password if the owner had cash.
<h2>Final Disclaimer</h2>
Some have suggested my data isn't 100% accurate, and accused me to sharing inaccurate data.

They're right. Three things though.That hasn't happened.

One, I've never claimed sayakenahack was 100% accurate, I'm just claiming, that I found data online, some of which has your myKad number on it. Whether that data represents accurately what is (or was) in the telco database, is not something I can guarantee.

Two, because of false prepaid registration, nobody can be absolutely sure of all the numbers registered in their name, unless they go to each and every telco <strong>physically</strong>.

Three, MCMC has promised to<a href="https://www.lowyat.net/2017/133401/prepaid-topup-ic-no/"> resolve the issue of false prepaid registration by 1st December 2017</a> (yes, that date is past), including requiring MyKad registration for top-ups. I'm not sure if that has happened yet.