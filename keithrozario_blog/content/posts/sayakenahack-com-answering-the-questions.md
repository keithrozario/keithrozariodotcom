+++
title = "Sayakenahack.com answering the questions"
slug = "sayakenahack-com-answering-the-questions"
date = "2017-11-16T23:50:35"
draft = false
categories = ['Misc']
+++

<a href="/uploads/image2017-11-12_19-2-50.png">![](/uploads/image2017-11-12_19-2-50.png)</a>OK, this is my last post on sayakenahack.com, and I've got a script scheduled to run at Sunday midnight to tear down the database. So if you wanna check, you better do it now, cause in 3 days time, it'll be gone.

*poof*

But here are my thoughts on this whole debacle -- and it's going to get emotional, so don't say I didn't warn you.

So let's start with the basics.
<h2>The right to know</h2>
I believe that if you're data was leaked online, you have a right to know.

You might choose to "not know", but that is a right you can choose to exercise. No one should be allowed to withhold that information from you.

I believe that you have a right to know about it, in a timely manner. Authorities can't sit on the data for weeks without letting you know on any pretense.

I believe that the correct authority to do tell you about leaks is the MCMC. But till today they have made no attempt to create such a service, not even communicated a plan to implement one. There is no evidence to suggest they have (or had) any intention to do anything about it.

If I can code sayakenahack within 4 weeks <em>(in my sparetime, while holding a 9-to-5 job, being a father and husband)</em> there is no logical reason why the MCMC or the telcos couldn't do something better in a shorter time-frame.
<h2>Even if you can't do anything about it</h2>
I believe the right to know about a breach should exists even if you can't do anything about it.

If you have terminal un-treatable cancer -- does that mean a Doctor shouldn't tell you about it? If you're on  plane that's about to crash, should the pilot remain silent?

You have a right to know about the leak. Regardless of whether you can do anything about it.
<h2>Only hackers and geeks should see the data</h2>
This data is freely available for anyone to download. The only people with the skills to find it though, are people we generally refer to as 'geeks' or 'hackers'.

To ban <em>sayakenahack</em> is to say geeks and hackers can access the data -- but <strong>not</strong> the average joe. It's emphasizing that normal people don't deserve that knowledge while geeks and hackers do.

This is elitism, and it's wrong.

When Lowyat published the initial report, the knew of it's importance. But chose to remove the article when the MCMC came. They continue to side with the MCMC, in saying that <em>"sheer amount of information made available on the site could subject it to abuse."</em>

They fail to mention that the <em>'sheer amount of information'</em> is already made available, just not to common folks, but to geeks and hackers. Effectively Lowyat is saying that it's OK for geeks and hackers to have this data, but god-forbid the average joe get a hold of it.

God-forbid the actual data subject who is actually impacted be notified, the great Gods of Lowyat think that's too much.

Oh, and btw, when Lowyat published the article, the site took roughly 200+ concurrent users at one time. When the star published the article in the morning, the site did 2000+ concurrent users (10 times more!)

Most Malaysians are technically illiterate and don't visit Lowyat. They shouldn't have less information because of it.
<h2>Manipulating vs. Masking</h2>
Lowyat's editor then goes on to tell the <a href="https://www.themalaysianinsight.com/s/23152/">Malaysian insight that</a> <em>"It’s blocked because it’s not right to manipulate the stolen data”.</em>

Oh, give me a fucking break!

The word 'manipulate' is a dishonest choice. I <strong>mask</strong> the data, not manipulate it. No IT professional would ever make confuse manipulation with masking. Manipulation carries a negative connotation, that implies I'm changing the data in some way. Masking though is the intentional removal of data, to protect its confidentiality.

I'm masking. I'm <strong>not</strong> manipulating.

I went out my way to ensure that enough data was left so that users could still identify their numbers, yet not enough for somebody else to guess.

If you buy anything a credit card, your masked credit card number will be on the printed receipt. Generally the first 6  and last 4 digits are in the clear, while the middle 10 are masked ("replaced with asterisks"). This ensures that there's enough information left on the receipt to trace a transaction, but not enough for fraudsters to get a card number. That's a PCI-DSS rule, the gold-standard security framework for credit card processing, and I've spent 10 years deploying PCI systems. Masking is an acceptable practice to do this sort of thing.

So give me a break, with your 'manipulating'. I love Lowyat to bits, but today they failed me big time.
<h2>How can we be sure the site is secure?</h2>
How can we be sure my site is secure?

Well there's no such thing as an un-hackable website, and that includes things like Maybank2u.com, or CIMB-Clicks. Do we tell the banks to shut-down their sites just because the might be hacked?

No. We weigh the benefits and risk, and make calculated decisions as to what to do. Just because something is hackable doesn't mean we take it offline.

We try our best to reduce the risk, until it reaches an acceptable level.

I would argue that the benefits of sayakenahack far outweighs the risk of it getting hacked. Hence continue to believe this was the right thing to do.
<h2>What if your site gets hacked?</h2>
So there are two parts here, how do I prevent a hack, and how do I mitigate the impact of breach (if it occurs).

First-off, the data is masked at source. i.e. the database only has the masked data. Making the data less valuable to fraudster. This is in the "minimize impact" bucket.

Below is the full representation of the data in the DB (for ic number 12345):

<a href="/uploads/JSON.png">![](/uploads/JSON.png)</a>

The data is masked at source, not in transit. So even I have no way to retrieve the full phone number from the DB. That's why I can't provide folks their full phone numbers -- it just doesn't work that way.

True, maybe this data is still valuable -- but how would you extract it?

The DynamoDB is capped at 20 reads/seconds (10 RCUs in AWS parlance). Reading the data at full capacity, would take you 3 weeks (provided you knew all the ICs). If you were guessing ICs, my rough estimate is 3 years to dump the DB.

So maybe you have the skills to query the API, throttle it to avoid attention, and patiently write it to a DB for 3 weeks. If you got those skills -- you probably found the files online already.
<h2>More AWS technical site</h2>
<em>*skip this if you're uninterested</em>

Now onto the prevent the hack bucket.

My AWS account is protected with a super long password, and 2FA protected with the code on just one iPhone. I work on the AWS console exclusively via my Ubuntu virtual machine, that I spun up for this purpose, and I intend to destroy that VM image on Sunday as well.

Let's get more details.

The entire architecture of sayakenahack is serverless. The html is served from a S3 bucket on Amazon via Cloudfront -- which has TLS enabled. The javascript on the html calls an API that is hosted on API Gateway (which also is via cloudfront and has TLS enabled). It took me a few iterations, but the API and website exist on the same domain (no same-origin policy violations, but I still keep it CORS enabled).

Which means that there are no servers to hack on this thing.

No RFI,  No LFI.

No un-patched Apache version, or some shitty PHP bug that a server-ed site would be vulnerable to.

No SQLi (tehcnically it's a noSQL database), or CMS Vulnerability. No Windows server to patch, no FTP, SMTP vuln, and all the other crap that gets servers in trouble.

It doesn't mean that this is unhackable, it just means that I reduce my attack surface tremendously by getting rid of any servers.

The API calls a Lambda function that reads from the DynamoDB with an IAM that allows for only read access from the DB. Ensuring integrity of data.

A seprate IAM that allows for full DynamoDB access, the one I use to insert rows into the DB, is now keyless because I de-activated the key for it.

Finally the HTML site is a 'minimalist' design and I wrote it to be easily readable, any programmer can vet the code to detect bugs (or malicious stuff, like malvertising or bitcoin mining). The full code source is available on github for anyone can vet -- in fact some already have!

Oh and I don't log any API requests (they are cached though) -- but that's not the same as logging.

That's just the tip of the icerberg of what I have on AWS. This thing is a labour of love.
<h2>So what</h2>
Let's compare all of the above -- with this!!

<a href="/uploads/spr.png">![](/uploads/spr.png)</a>

That's the election commission website, that publishes your full name, and voting location based on a simple IC entry. The site is marked as insecure by Google Chrome because it doesn't even have TLS.

TLS!!!! In fucking 2017, your website doesn't have TLS??

A simple thing, that a <strong>free</strong> LetsEncrypt certificate would solve in less than 5 minutes.

What that means, is that when you search for your voting information on the website, the data is transferred in clear across the internet for anyone in the middle to see. It also means that your browser is not authenticating the site, and anyone can create a fake SPR website and make it look identical.

If you're logged onto the SPR website from a kopitiam WiFi, I can see the data you're sending (and receiving) just by logging on the same WiFi.
<h2>Trust on the internet</h2>
Fundamentally, when you log onto the SPR website, you're trusting all the infrastructure between you and SPR, kopitiam Wifi included.

Do you trust the SPR? How about their vendor? How about the company that supplied them the servers?

How about the guy managing their database? Or the company that host their datacenter?

Their SysAdmin? Their Web Admin? All of their guys who wrote their code? Trust all of them?

Oh, and if you're logging on to the site from home on Unifi -- you're probably trusting <a href="https://www.keithrozario.com/2014/01/hack-unifi-in-5-minutes.html">your stock-standard Dlink DIR-615 router, that's hackable from the open internet.</a>

The internet is built on a whole load of trust, and maybe you don't trust me, but have you ever considered the number of people who un-suspectingly trust by just visiting a simple website?

Just saying, maybe sayakenahack isn't a problem when the Election Commission's website is marked as insecure. Why doesn't Lowyat complain about the 'sheer amount of data' on the Election Commissions website?

This is sayakenahack.

<a href="/uploads/sayakenahack.png">![](/uploads/sayakenahack.png)</a>

That 1 cookie is for Google Analytics, it's the only bit of 'data capturing' I do, and it's industry standard. I collect data about who visits the site, and see what their load/lag times are, to ensure the site is operational and working well. But that doesn't capture query strings, so no IC numbers are tracked.

More importantly, the site is TLS protected. All data between you and servers is encrypted, meaning you don't have to trust the internet providers, or WiFi connection.

So, I go through great lengths protecting the site, and definitely more effort than the SPR.

As a bonus, here's the PTPTN website, that allows you to check your balance. To be fair, they at least have a TLS equivalent, but they don't re-direct you to it. So it's still possible to access their non-encrypted site. See that bit on the browser that says "Not Secure".

![](http://192.168.0.10:8090/download/attachments/9535583/image2017-11-16_22-19-57.png?version=1&amp;modificationDate=1510841997939&amp;api=v2 "Hacks &gt; ScreenShots &gt; image2017-11-16_22-19-57.png")

 

Sayakenahack forces re-direction. There is no un-encrypted version for either the website or API.

 

<a href="/uploads/sayakenahack-redirect.png">![](/uploads/sayakenahack-redirect.png)</a>
<h2>Yes, but these are government websites</h2>
Yes, the government (both state and federal) are exempt from PDPA.

But the damage inflicted on victims by a breach is identical whether the data comes from the government or private companies. I'm not sure why that exemption is there.

Secondly, there exist an exemption clause in the PDPA, specifically section 45(2)(f)(ii) that states there is an exemption IF:
<blockquote>(f) processed only for journalistic, literary or artistic purposes shall be exempted from the General Principle, Notice and Choice Principle, Disclosure Principle, Retention Principle, Data Integrity Principle and Access Principle and other related provisions of this Act, provided that—

(ii) the data user reasonably believes that, taking into account the <strong>special importance of public interest in freedom of expression, the publication would be in the public interest</strong>;</blockquote>
I don't know how you define, public interest, but the site got 100,000 visits today (even with the ban kicking in at 12pm) signals to me that there is public interest.

<a href="/uploads/PageViews.png">![](/uploads/PageViews.png)</a>

I know Public Interest doesn't literally mean things that interest the public, but you can't argue that this is something people should be aware of. And don't give me bullshit about hackers querying this instead of 'real-users'. Hackers would use the API, and bypass the Google Analytics, the 100,000 is purely from the Google Analytics data.

Now, the lawyer types tell me that that 'journalistic' may not apply to bloggers, but this might be a good test case. Let's see.

Also, I don't know of any journalist in Malaysia, that could trawl through hacker forums getting the data, and then stand up a site that can support querying a 37mln row database, while serving 2000 concurrent users.  Do you?

There is one more exemption I might play here -- but that's a long shot, and I'm playing my cards close to my chest on that one.
<h2>Conclusion</h2>
To be honest, I'm afraid.

Afraid that next time I land in Malaysia, I end up in handcuffs at the back of a police car.

But sometimes, you gotta do what's right, and not just what's 'legally permissible'.
<h2>Post-note</h2>
To all the reporters who've contacted me. I'm cancelling all interviews for now. This is my last post on the matter -- at least for the next week.

See you on the other side.