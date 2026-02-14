+++
title = "SayaKenaHack.com"
slug = "sayakenahack-com"
date = "2017-11-12T18:50:11"
draft = false
tags = ['sayakenahack']
categories = ["Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

<a href="/uploads/image2017-11-12_19-2-50.png">![](/uploads/image2017-11-12_19-2-50.png)</a>

On the 19th of October, Lowyat.net reported that a user was <a href="https://www.lowyat.net/2017/145654/personal-data-millions-malaysians-sale-source-breach-still-unknown/">selling the personal data of MILLIONS of Malaysians</a> on their forum. Shortly after, the article was taken down on the request of the MCMC, only to put up again, a couple of days later.

Lowyat later reported that a total of <a href="https://www.lowyat.net/2017/146339/46-2-million-mobile-phone-numbers-leaked-from-2014-data-breach/">46.2 Million phone numbers were exposed,</a>  and the data included IC numbers, Addresses, IMSI, IMEI and SIM numbers as well. In short, a lot of data from a lot of people.

So Malaysia joined the ranks of <a href="https://www.troyhunt.com/when-nation-is-hacked-understanding/">The Phillipines</a>, <a href="http://www.businessinsider.com/turkish-citizenship-database-allegedly-hacked-and-leaked-2016-4?r=UK&amp;IR=T">Turkey</a> and <a href="https://www.businesslive.co.za/bd/national/2017-10-17-revealed-30-million-id-numbers-is-this-sas-biggest-data-dump/">South Africa</a> to have data on their entire population leaked on the internet. <strong>[Spoiler alert: This is not a good thing]</strong>
<h2>Where can I check?</h2>
You can head over to a site I created: <a href="https://sayakenahack.com">sayakenahack.com</a> to check if you're part of the breach. So far I've loaded data from Maxis, Digi, Celcom and UMobile onto the site. I'll be adding the smaller telcos later this week (stay tuned).

Medical council, etc...I'm still debating whether I should put that in. Maybe some doctors don't want to be identified as doctors, so that data stays out for now.
<h2>Waah... That means you downloaded illegal data?</h2>
Technically yes, the data might be illegal. But any geek can find it online, it's a google search away.

I'm just making the data available to the 'normals', people who don't look around in hacker forums.

Plus all data is masked, so only the first 4 and last 2 digits of the phone number is available. Which is almost as good as the <a href="https://www.pcicomplianceguide.org/whats-the-best-practice-for-masking-or-truncating-pan/">masking of credit card numbers on your printed receipts</a>.

I also don't publish any names or addresses. If you're unhappy with this, you should be unhappy with the Election Commission website that publishes your name in FULL on their website upon entering just an IC number. Similar to PTPTN etc.
<h2>Did you pay for the Data?</h2>
No. Contrary to what's being reported the data is available for FREE online. Even the 'hacker' who was selling it on Lowyat was basically a re-seller.

I did not pay for the data, I would never validate the business case of reselling stolen data.
<h2>If I search for my IC, will you log my data?</h2>
No.

In technical terms, I've switched of logging for my API Gateway, CloudFront &amp; Lambda.

If I wanted your data -- I wouldn't need you to search for you. I already have it.
<h2>OMG I'm breached !!! What can I do?</h2>
Unfortunately, there's little you can do.

Your IC number is a permanent fixture of your life --and can't be changed. This is bad design, but it's the design we have at the moment.

If you lose your Phone Number, Credit Card details or E-mail address, you'd still have some form of mitigating the damage. But if someone gets your IC number, you can't go to the NRD and get them to issue you a new one.

To be fair IC numbers (in their modern form) are at least 25 years old, so I'm not blaming anyone -- but the reality is that we should either stop using IC numbers so extensively , or find some way to make them mutable. Not and easy task, but until that happens the damage of this leak will continue... in perpetuity.

Now onto the good news!

The leak is from 2014, so the chances of you having the same phone is minuscule. I know of only one person whose phone is older than 3 years old, everybody else has changed their phone. So IMEI numbers (which are tied to your phones) from 2014 are pretty useless.

IMSI and SIM are almost the same as well. Over the past 3 years, I'm almost certain a large percentage of the victims (50-80%) would have their sim cards swapped -- primarily from buying a new phone that required a micro or nano sim or from porting telcos, or just losing their phones.

What's not so good is the fact that most people still keep their Name, Address and Phone Number. So those are the top 3 (4 if you count IC Numbers) data elements in the breach, and unfortunately their almost all there.
<h2>Where did the data come from?</h2>
Well......

The breach includes not just Telco data but Jobstreet and various other sources as well. Let's just focus on Telco because that's the big one.

There's only 2 possibilities on where the telco data came from:
<ul>
 	<li>Someone hacked into individuals telcos and took it; or</li>
 	<li>Someone hacked a central source with all the data</li>
</ul>
Now, consider that <strong>all</strong> Telco's are in this breach -- including Altel, PLDT, Redtone, etc. Which self-respecting hacker, with the skills to hack Maxis, Digi and Celcom, is going to waste time on Altel? Really?!

Consider also, that if you downloaded the data, (which I obviously have), it's clear as day where the leak came from. It's so clear, Stevie Wonder can see where the data was leaked from.

I'm hoping over the next few days somebody somewhere will make an announcement.

In the mean-time stay safe Malaysia.
<h2>End notes and Special Thanks</h2>
Thanks to Bin Hong for alerting me that I had a few logs on the GitHub repository. I've torn down the old repo and created a new one.

Thanks to Ang YC for letting me know I gave too much info to folks.

Thanks to **rax***n for sharing the data on the *ahem* site.

Thanks to Ridhwan Daud for correcting my API spelling. (it's case sensitive).

All data available on sayakenahack.com is available somewhere on the web. I'm just making sure that it's not just geeks/hackers who have this data, but the average citizen can also be informed if they're part of the leak.

I'm especially proud of the architecture underlying sayakenahack. It's completely serverless, and I'll make a post about it soon. But learning DynamoDB and about a gazillion AWS services to deploy this was both fun and tiring.

For now, you can build your own version of sayakenahack with the data, by using the api at:
<blockquote><a href="https://sayakenahack.com/api/v1/breach?icNum=12345">https://sayakenahack.com/api/v1/pwn?icNum=12345</a></blockquote>
I've changed the API many times. I promised this version is stable for the next 3 months.

The api is CORS enabled, so you can call it with javascript on your browser. There's only one endpoint for now, I'll documenting the API and will publish some documentation soon.

I spent a good 40+ hours building all of this, the code is mostly available on my <a href="https://github.com/keithrozario">GIT repository</a>. Couple of elements aren't there (lambda function to query DynamoDB) -- but I'll upload that when time permits.