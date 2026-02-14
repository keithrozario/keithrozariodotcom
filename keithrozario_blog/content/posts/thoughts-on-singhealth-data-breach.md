+++
title = "Thoughts on SingHealth Data Breach"
slug = "thoughts-on-singhealth-data-breach"
date = "2018-08-04T20:56:59"
draft = false
tags = ['dataBreach', 'Singapore']
categories = ['Security &amp; Privacy', 'Singapore']
+++

![](/uploads/data-breach.jpeg)On the 20th of July, Singaporean authorities announced a data breach affecting SingHealth, the country largest healthcare group. The breach impacted 1.5 million people who had used SingHealth services over the last 3 years.

Oh boy, another data breach with 1.5 million records ... **yawn**.

But Singapore has less than 6 million people, so it's a <strong>BIG</strong> deal to this island I currently call home. Here's what happened.
<h2>The lowdown</h2>
According to the <a href="https://www.moh.gov.sg/content/moh_web/home/pressRoom/pressRoomItemRelease/2018/singhealth-s-it-system-target-of-cyberattack.html">official Ministry announcement</a> administrators discovered 'unusual' activity on one of their databases on 4-Jul, investigations confirmed the data breach a week later, and public announcement was made 10 days after confirmation.
<blockquote><strong>4-Jul </strong>: IHiS’ database administrators detected unusual activity on one of SingHealth’s IT databases
<strong>10-Jul</strong> : Investigations confirmed the data breach, and all relevant authorities were informed
<strong>12-Jul</strong> : A Police Report is made
<strong>20-Jul</strong> : A public announcement is made</blockquote>
The official report states that <em><span style="color: #333333;">"data was exfiltrated from 27 June 2018 to 4 July 2018...no further illegal exfiltration has been detected".</span> </em>

The point of entry was ascertained to be <span style="color: #333333;"><em>"that the cyber attackers accessed the SingHealth IT system through an initial breach on a particular front-end workstation. They subsequently managed to obtain privileged account credentials to gain privileged access to the database"</em></span>

And finally that <span style="color: #333333;"><em>"SingHealth will be progressively contacting all patients...to notify them if their data had been illegally exfiltrated. All the patients, whether or not their data were compromised, will receive an SMS notification over the next five days"</em></span><!--more-->
<h2>A word about Medical Data</h2>
Breaches on health/medical data are typically attributed to the Chinese government. They're believed to be <a href="https://www.threatconnect.com/blog/the-anthem-hack-all-roads-lead-to-china/?utm_campaign=Anthem-Hack-Blog-Post&amp;utm_source=premera-blog-link">responsible</a> for the two largest medical data breaches that are publicly known, namely Anthem and Prenerra. Both these breaches were not just attributed to the chinese government -- but specifically to<a href="https://www.threatconnect.com/premera-latest-healthcare-insurance-agency-to-be-breached/?utm_campaign=Anthem-Hack-Blog-Post&amp;utm_source=from-anthem-post"> the same team within the government</a>.

In Anthem and Prenerra, the attackers utilized a phishing campaign to gain access, and then went on to extract data out of a database. At least in the Anthem case we've seen an internal memo stating :
<blockquote>"<em><strong>On January 27, 2015, an Anthem associate, a database administrator, discovered suspicious activity – a database query running using the associate's logon information. He had not initiated the query and immediately stopped the query and alerted Anthem's Information Security department. It was also discovered the logon information for additional database administrators had been compromised."</strong></em></blockquote>
Which sounds extremely similar to the SingHealth report that states <em>"On 4 July 2018, IHiS’ database administrators detected unusual activity on one of SingHealth’s IT databases"</em>. The Singapore government is tight-lipped about who did this, or how -- but they did say the breach was "<a href="https://www.wsj.com/articles/singapore-health-database-hit-by-cyberattack-1532085919">a deliberate, targeted and well-planned cyberattack and not the work of casual hackers or criminal gangs</a>" -- and most <a href="https://www.straitstimes.com/singapore/method-of-attack-showed-high-level-of-sophistication">experts</a> <a href="https://www.trustwave.com/Resources/SpiderLabs-Blog/SingHealth-Data-Breach-%E2%80%93-An-Analytical-Perspective/">agree</a>.

Data from these kind of breaches rarely end up traded on the internet -- haveibeenpwned has only one HealthCare breach in it's records, although <a href="https://www.healthcare-informatics.com/news-item/cybersecurity/2017-breach-report-477-breaches-56m-patient-records-affected">they've been at least 477 breaches of this kind in 2017 alone!</a>

It's a different type of attacker, and one that exposes victims to different types of risk.
<h2>Detection</h2>
Some were annoyed that SingHealth took a week to notice the data exfiltration. But frankly speaking, if this were some nation state -- a week is surprisingly efficient.

And let's be clear, this wasn't a case of somebody finding the data floating on the Internet, this was an investigation into a 'unusual' event that occurred on their network. Kudos to the team for even noticing the the unusual activity in the first place. A lot of organizations, get breached, and don't learn about it till <a href="http://troyhunt.com">Troy Hunt</a> or <a href="https://krebsonsecurity.com/">Brian Krebs</a> gives them a call.

So to give credit, within just 16 days at SingHealth &amp; MOH managed to:
<ul>
 	<li>Detect the intruder</li>
 	<li>Locked out the intruder <em>(supposedly!)</em></li>
 	<li>Determined the data that was accessed</li>
 	<li>Determined when that data was accessed</li>
 	<li>Determined how the intrusion took place; <strong>and</strong></li>
 	<li>Put a plan in place to inform the victims</li>
</ul>
That's a long list of actions to have been accomplished in 16 days, and quite frankly it's impressive to me. It's true that GDPR-ish regulation mandates breach notification within 72 hours, which makes the 10 days for SingHealth look exceptionally long. <em>(I'm only counting from the time they confirmed the breach to the date of public disclosure)</em>

But, in their defence, it sounded to me like they were <a href="https://www.straitstimes.com/singapore/method-of-attack-showed-high-level-of-sophistication">dealing with an active crime</a>, that while the confirmed the breach, and tried to investigate, they were dealing with re-intrusions of the attackers into their network at the same time. Of course, I'm not privy to detail, but if you accept that this was a nation-state, then you have to cut them some slack, after all how many healthcare providers you know can stand-up to an attacker this sophisticated?

I don't know any.
<h2>Risk</h2>
At this point of course, we have to inevitably talk about risk.

There's always a risk of getting breached if your data is on a computer -- especially if that computer is shared across hospitals and government agencies. The <span style="text-decoration: underline;">downside</span> is your data is lost in this breach and your privacy is invaded.

But there's also an <span style="text-decoration: underline;">upside</span>, in cases of emergencies, having your medical data available to doctors immediately is a good thing. It certainly can't hurt to have this information made available to emergency services?

And seeing as how you're more likely to end up in a medical emergency (hopefully not) then be a target for nation-state attackers -- it's a fairly straight forward decision to keep your data in these systems.

The alternative of having everyone go back to medical records stored in filing cabinets is just no feasible. This is an inherent risk of the modern world.

It doesn't mean we don't try to secure our systems, of course we will. But let's be clear, if a nation-state attacker is targeting your data, it's very unlikely you'll be able to secure your data from them. On the Internet, attack is much easier then defence, and if the attacker is well-resourced and infinitely patient, then defence becomes almost an impossibility.

Again, the Singapore Government gets top marks for trying to assuage fears that this would derail their smart-nation plan -- how effective their efforts are is up for debate, but they are doing it, and that's the right thing. People tend to over-react to this things, and it is important that we put data breaches in their right perspective.
<h2>Breach Notifications</h2>
So if we accept that this was the work of a nation state attacker (perhaps!).

And we accept that breaches of this kind are inevitable, where the authorities really shined was in their approach to breach notifications. They informed (quite promptly) all victims, and even non-victims of their status -- which lies in pretty stark contrast to what Malaysia does.

The only downside to me was that the government should have stood up a more centralized notification site, where victims could come to learn more. I doubt this will be the last breach in Singapore, and having a central site for victims (of any breach) to come into and learn about their 'collective' breach status across multiple breaches seems like a good idea.

5 years from now, people might forget which breaches they were in (or not in), a central notification site would solve for that.
<h2>Conclusion</h2>
The Singapore Authorities get pretty high marks for their response (at least in my book), they could have improved the timeliness of their notification and provided a central site, but in general their response was exemplary.
<h2>Bonus Reading</h2>
As a bonus for this post, <a href="https://risky.biz/RB481/">here's a link</a> to amazing interview by Risky Business with a person from the IT team of Anthem while they were breached. It's a scary interview -- so don't listen to it too late at night :).