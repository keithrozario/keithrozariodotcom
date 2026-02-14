+++
title = "Everything wrong with TalkingPoint's \"Cybersecurity\" episode"
slug = "everything-wrong-with-talkingpoints-cybersecurity-episode"
date = "2017-04-19T23:50:46"
draft = false
categories = ['Security &amp; Privacy', 'Singapore']
+++

Channel News Asia <a href="http://www.channelnewsasia.com/news/singapore/your-phone-number-is-all-a-hacker-needs-to-track-you-steal-your/3673268.html">posted last week</a> that hackers could steal your info by<strong> just</strong> knowing your phone number.

Woah!! Must be some uber NSA stuff right--but no, it was a couple of guys with Metasploit and they required a LOT more than 'just' the phone number.

The post was an add-on to a current affairs show called <a href="http://video.toggle.sg/en/series/talking-point-2016/ep40/484984">Talking Point</a>, that aired an episode last week about cybersecurity, which (like most mainstream media reporting) had more than a few errors I'd like to address.
<h2>Problem 1: Cost of cybercrime -- but no context</h2>
The show starts off, by highlighting that Cybercrime cost Singaporeans S$1.25bln, which might be true, but lacks context, or rather had the context removed.

Because the very report that estimated the cost, also mentioned<a href="/uploads/pictures/rp-economic-impact-cybercrime2.pdf"> that society was willing to tolerate malicious activity that cost less than 2% of GDP</a>, like Narcotics (0.9%) and even pilferage (1.5%). S$1.25bln is less than 0.3%<em> </em>of Singapore's GDP, and is long way off the 2% threshold. Giving out big numbers without context gives readers the wrong impression.

So allow me to provide context on just how big that S$1.25bln is.

In 2010, Singapore's retail <a href="http://www.enterpriseinnovation.net/article/singapore-retail-shrink-rate-rises-first-time-three-years-1301935024">sector lost S$222 mln to shrinkage</a>, a term used to describe the losses attributed to employee theft, shoplifting, administrative error, and others. Had we split the cost of cybercrime across different industry based on their percentage of overall GDP, the total losses for cybercrime on the retail sector in 2015 would be $225 mln--almost identical to what the sector lost to shrinkage....7 years ago!

Cybercrime is a problem, but not one that is wildly out of proportion to the other issues society is facing.<!--more-->
<h2>Problem 2: Hacking with just a phone number</h2>


![](/uploads/Downloading-an-Apk.png)



Channel News Asia headline their article with <a href="http://www.channelnewsasia.com/news/singapore/your-phone-number-is-all-a-hacker-needs-to-track-you-steal-your/3673268.html">"Your phone number is all a hacker needs to track you, steal your info"</a>, which isn't true.
<ol>
 	<li>The hackers sent an sms with a link, the victim willingly clicked on it, downloaded the app, opened the app, and then kept the app on the phone. This is clearly shown in the full episode, but somehow was redacted from their 2-minute clip.</li>
 	<li>The host admits the sms was suspicious and clicked it anyway, in fact he even guessed it was from the hackers. Anytime you see a link with a odd IP address--you probably shouldn't click it.</li>
 	<li>I saw a meterpreter shell--which suggest that the hackers injected a payload into a standard apk file, and sent it to the victim to download.</li>
 	<li>Which requires that the victim intentionally set his phone to allow unauthorized sources.</li>
 	<li>This attack wouldn't work on iPhone, <a href="/uploads/2012/05/Blackbox-YKA-Whitepaper-Smartphones.pdf">blackbox place iPhone penetration in the island-nation at 73%</a> (not a typo!) which means the attack wouldn't work on most phones in Singapore.</li>
 	<li>This attack, probably won't work on a current Android phone with side-loading disabled either.</li>
</ol>
So, the attackers need your phone number, they need you to click a link, download a file, open the file, keep the program running and you have to intentionally disable security features on your phone--oh, by the way, this doesn't work on iPhones.

The hackers need a whole lot more than your phone number.

I want to make clear just why these headlines piss me off so much.

Normal people in society, have no idea how technology works. Headlines like these are irresponsible because the trigger the wrong reactions. A 'normal' reading this would most likely stop sharing their number with people--but phone numbers were designed to be shared with people. You may be able to request anonymization of your mobile number--but that doesn't work when you're sms-ing or using whatsapp (where 90% of conversations are taking place).

Instead, we should prompt people to not root their phones, not click on suspicious links and for the LOVE OF GOD, don't download software onto your phones from outside the approved stores--DON'T!!
<h2>Problem 3: WiFi sniffing</h2>


![](/uploads/salesforce-logon.png)

Then we move onto unsecured WiFi.

But the shows confuses unsecured WiFi with keyloggers. I'm not sure how connecting to a public WiFi installs a keylogger onto your device, but the segment starts with un-secured WiFi but quickly demo's a keylogger on the phone.

Let's get one thing clear--applications that have End-to-End encryption like Whatsapp and Signal are not susceptible to eavesdropping by anyone in the middle, whether that's the government monitoring the undersea cables into a country, or a hacker on a Public hotspot. The segment suggest that somehow connecting to a public hotspots makes all your communication visible--it does NOT!

And the example they show is the url <em>login.salesforce.com (screenshot)</em>. I checked, and this url doesn't just have TLS enabled, it also has HSTS, which makes man-in-the-middle attacks near impossible. But I hear you say, what if the hacker compromised the phone, but that's a different attack than an unsecured WiFi.

There was definitely somethings lost in translation between the geeks and the producers for this segment--if the keylogger was downloaded as part of the WiFi registration process that should have been made clear. I'll let this pass because there's too little content to make any judgement on it, other than it was way too brief.

In any case, using a VPN is probably better advice than downloading anti-virus software for your phone.
<h2>Problem 4: Ransomware advice</h2>
To be honest, they get this partially right. The solution they recommend for ransomware is backups.

What they left out, was that the backups need to be a separate location. Otherwise the ransomware will just infect your backups as well, like it <a href="https://www.keithrozario.com/2017/02/so-you-got-hit-by-ransomware.html">did my uncle a few months back</a>.

To properly protect yourself from ransomware--just get dropbox. Trust me...just do it.
<h2>Conclusion</h2>
So to conclude:
<ul>
 	<li>Cybercrime is a problem, but financially it's not that big of a deal--at least not yet.</li>
 	<li>Hackers can't hack your phone with 'just' your phone number--they just can't.
<ul>
 	<li>And the hackers that can, are probably not targeting you anyway</li>
 	<li>And worrying about them is just not worth your time</li>
</ul>
</li>
 	<li>Avoid public WiFi like the plague of death
<ul>
 	<li>But if you absolutely have to use one, use a VPN (<a href="https://www.keithrozario.com/2013/09/best-vpn-malaysia-privateinternetaccess.html">I recommend PIA</a>)</li>
</ul>
</li>
 	<li>Ransomware can cause you a lot of hurt, so to prevent it backup all your files using a cloud backup solution with versioning
<ul>
 	<li>I suggest Dropbox</li>
</ul>
</li>
</ul>
Don't believe the mainstream media when it comes to 'Cyber' -- refer to these sources instead:
<ul>
 	<li><a href="https://arstechnica.com/">ArsTechnica</a></li>
 	<li><a href="https://motherboard.vice.com/en_us">Motherboard</a></li>
 	<li><a href="https://www.wired.com/">Wired</a></li>
 	<li><a href="https://threatpost.com/">Threatpost</a></li>
</ul>
For more focused blog-style content
<ul>
 	<li><a href="https://www.schneier.com/">Schneier on Security</a></li>
 	<li><a href="https://krebsonsecurity.com/">Krebs on Security</a></li>
 	<li><a href="https://www.troyhunt.com/">TroyHunt</a></li>
 	<li><a href="https://www.grahamcluley.com/">Graham Cluely</a></li>
</ul>
For podcast (if that's your thing):
<ul>
 	<li><a href="https://risky.biz/">RiskyBiz</a></li>
 	<li><a href="https://twit.tv/shows/security-now">SecurityNow</a></li>
 	<li><a href="http://podcast.wh1t3rabbit.net/">Down the security rabbit hole</a></li>
</ul>
And of course...keithrozario.com