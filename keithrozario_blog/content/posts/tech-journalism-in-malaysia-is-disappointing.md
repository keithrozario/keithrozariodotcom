+++
title = "Tech Journalism in Malaysia is disappointing"
slug = "tech-journalism-in-malaysia-is-disappointing"
date = "2015-04-21T02:08:12"
draft = false
categories = ['Misc']
+++



![GOOGLEHACKED-M](/uploads/GOOGLEHACKED-M.png)

Last week visitors browsing to Google's Malaysia website were greeted with a big bold image stating the website was hacked. The media had a field day proudly proclaiming that Google's website was hacked, because that was exactly what the page they visited said....Google Hacked!!

Only, Google <span style="text-decoration: underline;"><strong>wasn't</strong></span> hacked.

<a title="MyNic hacked" href="http://www.thestar.com.my/Tech/Tech-News/2015/04/14/DNS-redirect-attack/" target="_blank">MyNic was hacked</a>.

They're the agency in charge of managing all internet addresses ending with the .my suffix. Hackers had infiltrated MyNic, and reconfigured the systems to point <span style="text-decoration: underline;"><em>www.google.com.my</em> </span>to their own servers instead of Google's. Then they simply pasted a silly looking screen that boldly proclaimed their 'hack' to the world, claiming to hack Google rather than MyNic---which is what you'd expect from hackers. But the media, took that to mean Google was comprimised, and boldly proclaimed that Google Malaysia was hacked, going so far as to ask if 'user data was compromised'.

The analogy is that if someone hacked Waze, and took all unsuspecting tourist who were trying to get to KLCC, and re-directed their route to an abandoned warehouse in Klang, the headline for that story should read <strong>"Waze hacked"</strong> instead of <strong>"KLCC destroyed"</strong>. Everyone knows how absurd a headline like the latter would be, but very few people would think the same thing the moment 'internet things' get involved--if the website says Google hacked, surely it must be true, in the same way that if Waze says this dilapidated factory lot is KLCC, surely it is, because Waze is never wrong right?!<!--more-->
<h2>The problem of un-suspecting tourist</h2>
The problem is that most internet users  are the equivalent of un-suspecting tourist in a foreign land, not knowing the geography or even the language of this country we call the internet. I'd wager 95% of internet users haven't even heard of a Domain Name Server (DNS) let alone understand how it works, yet this fundamental piece of technology is what makes the world wide web possible. And by the way the internet and the world wide web are NOT the same thing?

That 95% isn't some number plucked from the thin air , I have evidence to back this , my post on how to change your <a title="How to change your Unifi password" href="https://www.keithrozario.com/2012/07/change-unifi-password-wifi-dlink.html" target="_blank">UniFi WiFi password</a> gets about 150 hits everyday.But if I tweak the technical complexity a bit higher, like <a title="How to Port Forward your Unifi Dlink Dir-615 router" href="https://www.keithrozario.com/2012/09/port-forwarding-unifi-dlink-dir-615.html" target="_blank">Port Forwarding your UniFi router</a>, or <a title="Setting up a Dlink DDNS for your Unifi Router" href="https://www.keithrozario.com/2012/09/setting-up-dlink-ddns-unifi-router.html" target="_blank">implementing DDNS</a>, that number drops from 150, to just 10 a day. That's a factor of 15 difference, people who know things like DNS and want to do DDNS are outnumbered significantly by the clueless internet user.

I'd say 95% of Malaysian users wouldn't know how to change their WiFi passwords without Googling, and if you need to Google just to do something that simple, you definitely don't know how DNS works. <em>(BTW, the title of the post UniFi WiFi is technically wrong, as the WiFi and UniFi connection are separate things, however, some SEO from Google told me that's what users were searching for)</em>
<h2>Too much technology, too little knowledge</h2>
We're at a really bad place. Technology is so ubiquitous and pervasive, that even my mother now is on Facebook, Whatsapp and Viber, yet she has absolutely no idea how these things work, and just like your mother is clueless on how to secure herself from online threats, in this space that she frequently visits. Lots of technology, lots of people using it, but very few who do it securely.

Hence, I think geeks like me have a social obligation to help others, in the same way Doctors have an obligation to heal, or journalist have an obligation to report the truth, even when it hurts them, and even when they get little to no compensation for it, it's a duty and responsibility.

And if we don't step up, the consequences will be catastrophic.

Unfortunately, the geeks aren't really helping. We're either sequestered in their ivory towers, or hanging out on forums that no one but geeks visit--which leaves the rest of the 'civilian' population having to read their tech news from places like TheStar or <a title="Google Hacked" href="http://www.therakyatpost.com/news/2015/04/14/google-malaysia-hacked-search-engine-assures-passwords-are-safe/" target="_blank">RakyatPost</a>, who may be able to report on politics and sports, but they're definitely under-staffed and incapable of reporting on technology.
<h2>Mainstream media reporting of CyberSecurity</h2>
Take for instance yesterdays article in TheStar, titled <a title="Kaspersky: Cyber threat MH370" href="http://www.thestar.com.my/News/Nation/2015/04/19/Kaspersky-Cyber-attack-launched-after-MH370-went-missing/" target="_blank">"Cyber attack launched after MH370 went missing"</a>, which on the face of it looks like a good attention grabbing title. But MH370 went missing a year ago, why are Kaspersky talking about this now? Sure they have their cybersecurity summit in KL this week, but that's pretty stale news in the fast-moving world of computer security.

If you took the time to visit the Kaspersky blog (which is an amazing blog to follow), they detail the <a title="APT wars Kaspersky" href="https://securelist.com/analysis/69567/the-chronicles-of-the-hellsing-apt-the-empire-strikes-back/" target="_blank">APT wars</a>.What Kaspersky were reporting on their blog was that :
<ol>
	<li style="text-align: left;">Cyber-attacks were carried out by a group called Nakion, targeting senior diplomatic entities in ASEAN</li>
	<li style="text-align: left;">This group carried out attacks shortly after MH370 went missing</li>
	<li style="text-align: left;">THEN, a totally separate group called Hellsing, decided to attack Nakion back</li>
	<li style="text-align: left;">Hellsing replied back to the Nakion attack e-mails and tried to use social engineering and other techniques to determine the origin of Nakion</li>
	<li style="text-align: left;">Hellsing targets included Malaysian government entities as well as other ASEAN member states</li>
	<li style="text-align: left;">Kaspersky labled these the APT wars, because it was the first time they've seen an attacker being attacked back.</li>
</ol>
Now, if you go back to the original star report, you'll find that it only reported (1) and (2), while the actual point of the story, that the attackers were being attacked, was missed out entirely. Either Kaspersky didn't share this information in their summit (quite unlikely), or the reporter from TheStar went to the summit, heard the first few opening slides, and then dozed off the moment the Kaspersky folks talked about APTs and RATs... <em>Advanced Persistent what now??!!</em>

Or a third possibility that the reporter did report on the entire story, and the editor cropped out only what they thought was interesting to the Malaysian readers.

Doesn't matter why it happened, the fact is most Malaysians didn't get to read the full story. The only Malaysians who would have even had a chance to gaze upon it would be the tech-geeks themselves who subscribe to the Kaspersky blog or other cyber security news outlets, but how many of your mothers are reading security news every week?

The conclusion I draw is that if you rely on TheStar or RakyatPost for your tech news, you're going to be either <strong>mis</strong>-informed (like Google hacked) or <strong>un</strong>-informed (like APT wars).
<h2>How can we fix this?</h2>
So what's a tech geek like yours truly to do? I don't have the media muscle of people like the star, this blog barely crosses 30,000 hits a month, I'm a nobody.

But if I were wave my magic wand and get the mainstream media to buck up and report on tech news accurately and comprehensively, would people even understand what was going on? How do I explain the Google Hack without first explaining DNS, and how would you even begin to talk about APTs, let alone Hellsing vs. Nokian? These are not trivial to understand, but their vital.

This is real challenge facing geeks, how do you make these cyber security topics relevant to the public, to get them interested and informed? Fortunately, there is a role-model to follow.
<h2>Be the Neil DeGrasse Tyson of Tech</h2>
Enter Neil DeGrasse Tyson, he's the guy who hosted the Cosmos series, and if you just Google his name, and listen to his lectures, you can sit for hours through his narration, while he astounds you on topics like black holes and death comets, stars and planets. The moment he speaks, audiences just falls in the palm of his hand, but he's talking about physics, and science, and the last time I checked the public wasn't all that interested in those subjects, how come their interested why Dr. Tyson speaks?

How does he get people interested in topics, that they generally don't care about? What can the cyber security folks do, to follow in those footsteps?

I don't have a full idea, but here's some key takeaways.

First step, stop using the freaking acronyms. In astrophysics, things are given easy to understand names.
<blockquote>Universe starts with a big release of energy--Big Bang.

Dead star that sucks everything with its enourmous gravity--Black Hole.

Unknown mass in the universe that we can't see--Dark Matter.</blockquote>
The names make perfect sense, now contrast that with Advanced Persistent Threat of Domain Name Server. If we're really serious about communicating with the public, we need to keep this jargon in the IETF and IEEE documents, but away from the public. We need easier names to explain to the public.
<blockquote>Advance Persistent Threat---Bad Ass Hackers.

Domain Name Server--Web Address listing.</blockquote>
Next we need to stop feeling the need to go to the nth-degree to explain everything. No one has time for a 1500 word document explaining how this Bad Ass Hacker broke into a server, we need to compress it into 300 words, it's not impossible, we just need to prioritize and distil the message...every single time.

Finally, we need to get off our high horses. Dr. Tyson doesn't laugh at people who don't know that light is made out of photons, in fact he seems to get a kick from teaching. Cyber-security 'professionals' usually get a kick from feeling superior and mighty. I admit, I do this sometimes, when I arrogantly tell people to use better passwords, rather than take the time to explain why they need to protect their phone.

I guess at least acknowledging that there is this enormous understanding gap in the general public, and how the geeks aren't really doing anything about it, is the first step towards actually fixing the situation.