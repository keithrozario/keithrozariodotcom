+++
title = "RHBNOW Email: Intricate details of a Phishing scam"
slug = "rhb-phishing-scam-details-phishing-scam"
date = "2014-07-03T22:47:16"
draft = false
tags = ['RHB', 'Scam']
categories = ['Security &amp; Privacy']
+++

Last month alone I've received 6 phishing emails asking me to change my RHB banking password. I always wondered what would happen if I'd actually clicked on one of the links in the email--and today I did just that. Immediately I was transported to a dodgy world of sophisticated deception, and soon realized this was far more complicated that I initially expected.

Before I proceed a friendly word of caution--Kids don't try this at home--the scam is an elaborate ploy geared towards robbing you of your cash, and if you're not sure what you're doing--chances are you'll be a victim yourself. The simplest way to avoid a scam like this is to never click on an email from the bank--regardless of how genuine it looks. Banks never send you email--so don't expect one from them. Not even a Christmas card.

But if you'd like to see what happens when you click on one--read on:
<h2>Step 1: The email from RHBGroup.com</h2>
![Email from RHB Group](/uploads/rhbgroup_email-1024x364.png)

 

First there's the email, it was <em>(supposedly)</em> from <strong>sshccserv356@rhbgroup.com</strong>. Quite deceptive, and if you visit rhbgroup.com you'll find that it's the legitimate RHB Bank website. So it appears this email from rhbgroup.com would be legitimate as well.

Except it's not.

Email is a remnant of the internet past--it was created at a time when security wasn't a priority, hence Emails lack any form of authentication <em>(validating whom the email is from)</em> which allows them to be easily forged. This inherent insecurity is what Emails should never be trusted, especially when those emails come from external sources like a bank.

That's why your bank will NEVER send you an email. It's too easy to forge. So rest assured that every email you receive from the bank is a fake (there are exceptions of course, like transfer notice etc, but those emails don't require any action from your end)

Analysing the email further, I find the first victim of the scam. A website called pjpan.co.uk, a pajama-store (<em>of all things</em>). The website url was all over the email-header, which just like every other aspect of the email could be spoofed. Why the scammers chose to us pjpan.co.uk was beyond me, but they did. In any case the email was sufficiently obfuscated that trying to determine its origin would be difficult and probably pointless as well. <!--more-->
<h2>Step 2: Clicking the link</h2>
Next I decided to click on the link, but it was an unusual address:
<blockquote>
<pre style="color: #000000;">http://www.papuaharapan.org/wp-admin/network/715ae326f928ca3a740661ec08a3aa5c/</pre>
</blockquote>
If you visit http://www.papuaharapan.org, you'll see a nice website of a school for indigenous kids in Indonesia. This isn't a front for the scam, it's a genuine website of a real school. I was left quite stumped as to why a nice school in Indonesia was part of this scam...

Then I realized that the scammers had hacked the website. Papuaharapan.org wasn't a scammer--it was a victim of  a hack and there's a pattern as well. Earlier in the post I mentioned that I received 6 of these emails so far--and all six emails have links to websites that run wordpress. The common hack was inserting some scripts into folders that weren't properly permission-ed, particularly the css\my folder of the wordpress installation.

Using a common security mistake, these scammers places a simple re-direction script on the website of papuaharapan to lead to the actual scam website. This allowed them to place layers of obfuscations between them and the scam emails--quite ingenious. Also it allowed them to send many different links that end up at the same website--I imagine this allowed them to bypass spam filters.

So even before I arrive at the actual scam, there's already 2 victims here. But wait till you see what comes up next.
<h2>Step 3: Arriving at the scam website
![RHB Phishing Website Scame](/uploads/RHB_Phishing_Entry_Page-1024x729.png)</h2>
I clicked on the link and arrived at a website that looked exactly the same as the <em><strong>REAL</strong></em> RHBNow login page. Its got the security lables, the ENTRUST logo, even the phishing alert that tells you<em> "Not to fall prey to online banking scams"</em>. However, if you're observant that the address bar points to an unknown url--nulldivision.com instead of rhb.com.my.

If you've followed the advice of never clicking on links in emails from banks (because the REAL bank would never send you an email), you'll never end up here--but if you've ever wondered how to determine if a banking website was legitimate look out for what I like to call the GREEN BAR OF SSL. Below you'll see the real RHB login page, and the only real difference is that the address bar in your browser turns green for a banks real website.

Even if the spammers managed to infect your laptop with nasty viruses and malware--they're unlikely to be able to spoof the GREEN BAR OF SSL without first infecting your PC or laptop. In fact, if they've found a way to spoof the green bar without infecting your PC--they probably be smart enough not to target you, and aim for a billionaire instead.

Remember folks:<strong> If it ain't Green, don't login.</strong>

Of course my website doesn't have the green bar, and neither do countless other blogs. However, every BANK website should have it, and it's an easy way to determine if the rhb.com.my website you're at is legitimate.

![Real RHB Website](/uploads/RHB_Real-1024x744.png)
<h2>Step 4: Login into the website</h2>
I decided to login into the website to see what else the scammers had in store for me. I just entered a random username and password, and found myself at a page requesting my security code and one-time password.

The hackers weren't content with my username and password, since they couldn't do much with it. They needed a security code as well. RHB utilizes two-factor authentication, where a security code is sent to your phone as a second form of authenticating you to the bank, since the scammers don't have access to your phone, this provides a layer of security because you'd need both your password and security code to perform a new transaction.

Here the scammers performed a man-in-the-middle attack, they placed a website that looks like RHB, so you can insert the security code into their website yourself. They might not have hacked your phone, but they've tricked you into giving them the security code <strong>from your phone</strong>--sometimes the weakest link isn't hardware or software, it's Human-ware.

What's happening is that while you're entering your username and password on the first page, the scammers are entering it on the <strong>real</strong> RHB logon page to get into your account. Then they request a security code from RHB, which will be sent to your phone--which they're hoping you'd enter into their  fake website.

With the security code they can now perform transactions on your behalf, like emptying your bank account while you're still wondering what's going on.

![RHB_Phishing_Security_Code](/uploads/RHB_Phishing_2.png)
<h2>Step 5: Lose your money--but how?</h2>
If you clicked on the link in the email, entered your passwords and security code, you can rest assured that you and your money would soon be departed.

But HOW?

I don't have a definitive answer, but I think the reason RHB is the only bank impacted is that it's the only bank with Paypal integration in Malaysia. So the scammers could potentially load as much money as possible into a Paypal account and then transfer that money internationally to some other country leaving no paper trail. This would suggest that the syndicate running these scams isn't local, but international.

In fact, the range of emails I got, suggest that these are similar attacks--but executed by different people. The email patterns and email headers look different from each other, which to me indicates various sources. Fortunately, it's not long after these emails surface that the calvary comes marching in.
<h2>Step 6: Protection kicks in</h2>
About 2-3 hours after I received the email, trying to visit the site on either Google or Firefox led me to a page that looks like this:

![Firefox phishing protection](/uploads/RHB_Phishing_Warning-1024x383.png)

So after a couple of hours, the phishing scam gets reported and firefox and chrome begin to warn you when you visit it. This means that the scammers only have 2-3 hours to scam as many people as they can, before Firefox and Chrome start protecting users.You should never rely on this as your main source of protection, but FireFox and Chrome do protect you against threats quite effectively.
<h2>Conclusion:</h2>
Overall this RHB scam was well orchestrated and had multiple victims. From this one email alone:

1. A pajama shop in the UK had it's email spoofed

2. A school in Indonesia had their website hacked

3. A Malaysian citizen was 'potentially' duped of their money

I'm not sure if nulldivision.com was also another victim of the scam, or whether it was really run by the scammers. But the overall sophistication left me impressed. The guys spoofed email to look like it came from RHBNOW, hacked a website to place a re-direction script, disconnecting them from the spam email they sent out, and ran a website that must be scripted to both receive input from the user and output data to the real RHBNOW website.

In fact, when I viewed the source of the website, I found some comments about Publicbank and PBEBANK.com.my, suggesting these guys ran a public bank scam sometime in the past, or are planning to do this in the future.

As mentioned before if you're going to learn one thing from this post, let it be this:
<blockquote>
<h2><span style="color: #ff0000;">Your Bank will NEVER (EVER!) send you an email--period!</span></h2>
</blockquote>
Stay safe people, and if you've ever received this or been a victim, leave your comments below. Love to hear from you.