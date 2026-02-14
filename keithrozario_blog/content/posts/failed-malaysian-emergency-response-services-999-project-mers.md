+++
title = "Why it failed: Malaysian Emergency Response Services 999  Project (MERS 999)"
slug = "failed-malaysian-emergency-response-services-999-project-mers"
date = "2013-12-31T15:09:26"
draft = false
categories = ['Malaysia']
+++

As we approach the end of the year, and I have some free time to blog again, I thought I'd re-visit the Auditor Generals report for 2012, and focus specifically on that one project everyone is talking about, the MERS 999 project.

This wonderful project, that cost Malaysian citizens upwards of RM800 Million, was a monumental failure on behalf of the government and for all contractors and sub-contractors involved, however to be fair the blame probably lies squarely on the shoulders of those over-seeing the procurement of the service as opposed to the IT folks--but they have to take some heat as well.

As someone with years of experience delivering IT projects, I think this is an area that I comfortably call myself an expert in, so I think I'm fluent enough in IT to take a sneak peek at this particular project to find out what exactly went wrong and what could have been fixed. Unfortunately, the results aren't that good, but if you'd like to hear a self-proclaimed expert dissect this, then please continue reading.<!--more-->

Firstly, let's be honest--every large scale IT project is wrought with similar challenges. Earlier this year, the Jewel of President Obamas health care plan--the Healthcare.gov website, was hit with similar issues, albeit it was fixed far quicker than MERS. The general rule of thumb in IT is that the bigger the project, the more likely it is to fail, and government projects are even worse.

What surprises me is the audacity of the government in considering that RM800 Million was a realistic figure to pay for a system such as this. To put this in perspective, it's more than RM30 for every single Malaysian, or about RM120 for a family of four. At those prices we could buy every household in Malaysia, a cheap dedicated mobile phone program it to phone the local police/bomba/hospital, and tell them to only use it in emergency situations. Not an ideal solution--but then again neither was this.
<h2>Those damn consultants</h2>
What makes matters even more frustrating is the RM25.88 Million we paid for consultancy services. That's nearly Rm1 for every Malaysian citizen, and to be honest I've been on big big projects before that have deployed far complex solutions than MERS and we've never had consultancy services cost so exorbitantly high, and I work in Oil &amp; Gas.

In fact, I can't phantom how the RM800 million was broken down, and how a project that paid Rm25 Million in consultancy services still failed--doesn't that clearly indicate the consultants weren't up to par.
<h2>Infrastructure can cost a lot</h2>
I decided to figure out what exactly the MERS projet was delivering, in some cases, a project delivers huge amount of infrastructure and hardware that require lots of cash.

Malaysia is a pretty big country, and if you include Sabah and Sarawak, the geographic spread of our great nation does take a toll on nationwide deployments, particularly communications infrastructure.

Most Petrol Stations you visit have a huge satellite somewhere on the roof, these are VSAT dishes that connect to satellites for internet and local connectivity. You see, although your home may have easy access to wired broadband, in general it's quite difficult to pull a fibre line to even Petrol stations located by highways, let alone more rural areas--which makes VSAT connectivity (although very expensive and slow), the only realistic option. That's just a flavor of how difficult it is to do a nationwide deployment in Malaysia, without details its hard to gauge whether RM800 Million is reasonable or not.

Maybe the MERS project required to hook up every single Police Station, Hospital, Klinik Kesihatan, Balai Bomba...etc etc, and by hooking up it would mean a laying a fibre-optic cable all the way from the nearest node to the end-point, I've seen these cost before, and I can tell you they aren't cheap even in Peninsular Malaysia, what more the far flung areas of Sabah and Sarawak. So, even though 800 Million sounds like a lot of money, if most of it was burned into laying fibre-optic cables, you could begin to see where the money went--legitimately.

In any case though, the figures still look ridiculously high to me, but my point is that we can't fully judge until we see the details--unfortunately those aren't easy to find.
<h2>One website can tell a lot</h2>
Without the detail, I decided to look at the MERS website, hosted at www.999.gov.my, to see what they were delivering--again I was upset over the lack of detail. However, I'm the freaking Tech-evangelist, and I know how to tell if someone is an IT pro, or a noob.

For instance, the MERS website is hosted on Wordpress--nothing wrong with Wordpress. My blog is hosted on Wordpress, and I'm a big fan of it. Hosting your website on Wordpress is good for two reasons, firstly its an open source and common platform, meaning you're never locked into a particular vendor and your website will never be at the mercy of a incompetent web-designer. Secondly, and most importantly, Wordpress is pretty secure, everytime a bug is discovered, it's fixed, and provided you constantly update your site, you're going to be FAR FAR more secure with a Wordpress site than you are on a custom-built design. The same is true of Joomla or Drupal, and the difference is more personal preference if you ask me--but you should never go custom, unless you require something very very unique.

However, the Wordpress version is 3.4, that's a pretty old version, that's a noob mistake (to be honest, my blog runs on 3.7.2 which is one version behind the latest and greatest version 3.8). I'm a personal blogger, running a personal blog, if you're running the MERS website, the least you could do is bloody update your site when a patch is released, to me this is unacceptable. Coupled with the fact, that there isn't any SSL on the site, makes me even more upset. Further browsing reveals<a title="Dead 404 Links" href="http://www.999.gov.my/?page_id=75" target="_blank"><strong> dead 404 links</strong></a>, which is really a mistake that would be unacceptable for a College students final year project--let alone an government funded one that cost nearly 1 Billion ringgit.

Now the reality is that sometimes the website work is outsourced to digital media companies, that make great looking websites, but don't pay attention to security. However, based on the whois of the site, it appears this <a title="WHOIS 999.gov.my" href="http://who.is/whois/999.gov.my" target="_blank">website is still operated by Telekom Malaysia</a> (the chief contractor of the MERS project).

So based on this one data point--the quality of the MERS 999 website, we can safely say, we've wasted our money.If you can't even deliver a website properly, what more the complicated network infrastructure, mobile apps, service integration and business processes that would have been part and parcel of a successful MERS delivery.

At this point, I'd just like to say that if you're with the government procurement department and you have another RM800 Million project--please consider me first, at the very least, I'll give you an updated Wordpress site. :)
<h2>So why did the project fail</h2>
On top of bad contracting and procurement practices (something quite typical in projects of this size), and the consultants were probably over-paid (way over-paid). But that doesn't explain why the project failed.

You see the project didn't just cost a bomb--it literally bombed. There are many statistics to point to how ineffective the whole system has been, but consider just this one tiny factoid.

<strong>7.65 Million calls were un-answered by the system. </strong>

Quite possibly 10% of those were false alarms, but that still means almost 7 Million calls made by 7 Million people caught in distressing situations were left un-answered. 7 Million!!

How is this possible? Of course 7 Million is a lot, and most of these were non-emergency calls. This has nothing to do with IT. If people call 999 because their neighbor is noisy, or their cat got stuck on the roof, that's really not something the system can fix, but I would be surprised if this wasn't the case before the MERS project, this should have been expected. This suggest a deep-rooted inability to accurately predict the volume of calls expected--how could a system design to answer calls not address such a fundamental question. Couldn't one of the consultants that were paid millions have suggested this? This is more than enough to know that the system was executed poorly on all fronts, and execution my friends is key.
<h2>End</h2>
This is the Auditor-Generals finding on the MERS 999 project:

<blockquote>

<strong>Malaysian Emergency Response Services 999 Project</strong>

a. The Malaysian Emergency Response Services 999 Project (MERS 999) was implemented in May 2007 under the Ministry of Energy, Water and Communications (MEWC) with the objective to provide a comprehensive and integrated
emergency line services using the number 999 with One Malaysia One Number concept. In 2009, the communication function was consolidated under the Ministry of Information Communication and 50 Culture (MICC) and the project continued under the new ministry. Telekom Malaysia Berhad (TM) was appointed through direct negotiations to develop
this project with a total cost of RM801.55 million.

This included the cost of development (Capital Expenditure-CAPEX) amounting to RM596.25 million and the cost of operating (Operating Expenditure-OPEX) amounting to RM205.30 million. Audit findings revealed that the overall
project management was particularly poor in contract compliance, contract administration and project monitoring. Among the weaknesses identified were as follows:
i. late execution on the development and installation of MERS 999 system in 16 sites and 34 sites were operated later than the timelines stipulated;
ii. increase in the number of non-emergency calls and there were continuous occurrence of drop calls;
iii. the first interim payment amounting to RM26.4 million was made before the issuance of Letter of Acceptance (LOA) while the signing of 2 contracts was delayed between 8 to 10 months from the date of the LOA;
iv. the validity period of the performance bond guarantee did not cover the warranty period of 12 months after the contract ended;
v. appointment of local and foreign consultants did not comply with the financial regulations and the consultancy service fees exceeded the prescribed rate by RM1.92 million. The consultancy service fees amounting to RM25.88 million was paid in lump sum without supporting details on the services provided. The cost of reimbursement on consultant
services amounting to RM480,000 was paid in a lump sum without being supported by receipts. In another instance, the project management fee was overpaid amounting to RM295,036;
vi. payments for cost of conducting workshops amounting to RM3.43 million, courses conducted amounting to RM1.90 million and overseas trips amounting to RM3.34 million were made without complete supporting documents. The cost of workshops conducted amounting to RM2.03 million did not comply with the prescribed rate. Workshops and courses for the contractor personnel totalling RM3.27 million were paid by the Government;
vii. rental of TM Training Centre, Taman Desa was double charged;
viii. the cost of overseas trip totalling RM253,813 was not reasonable. Payment amounting to RM3.19 million was made on cancelled promotional and publicity programmes. While promotional and publicity programme payments 52 totalling RM2.86 million were made without being supported by proper and complete documentation;
ix. incentive payments to Master of Trainers (MOT) amounting to RM295,094 that should be borne by TM has been paid by the Government. While the office space rental charges amounting to RM373,312 and the recurring charges for Automatic Number Identification/Automatic Location Identification connectivity totalling RM0.9 million were
overpaid to the contractor. A payment amounting to RM1.03 million was made for hardware and software which were not supplied; and
x. the monitoring committee was not effective in safeguarding the interest of the Government according to the terms of the rules and conditions of the contract causing an improper payment amounting to RM13.54 million.

</blockquote>

source: <a href="https://www.audit.gov.my/images/pdf/LKAN2012/Persekutuan/Siri2/synopsis%20lkan2012%20siri%202%20-%20a5.pdf">https://www.audit.gov.my/images/pdf/LKAN2012/Persekutuan/Siri2/synopsis%20lkan2012%20siri%202%20-%20a5.pdf</a> (page 49)