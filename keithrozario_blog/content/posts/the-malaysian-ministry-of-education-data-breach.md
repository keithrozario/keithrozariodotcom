+++
title = "The Malaysian Ministry of Education Data Breach"
slug = "the-malaysian-ministry-of-education-data-breach"
date = "2018-06-18T22:44:08"
draft = false
tags = ['dataBreach']
categories = ['Malaysia', 'Security &amp; Privacy']
+++

![](/uploads/MoE_SAPS_0906_1.png)Ok, I've been pretty involved in the latest data breach, so here's my side of the story.

At around 11pm last Friday, I got a query from Zurairi at The Malay Mail, asking for a second opinion on a strange email the newsdesk received from an <em>'anonymous source'</em>. The email was  regular vulnerability disclosure, but one that was full of details, attached with an enormous amount of data.

This wasn't a two-liner tweet, this was a detailed email with outlined sub-sections. It covered why they were sending the email, what the vulnerable system was, how to exploit the vulnerability and finally <em>(and most importantly!)</em> a link to a Google Drive folder containing Gigabytes of data.

The email pointed to a Ministry of Education site called <a href="http://sapsnkra.moe.gov.my/">SAPSNKRA</a>, used for parents to check on their children's exam results. Quick Google searches reveal the site had security issues in the past including one blog site advising parents to <a href="https://sapsibubapa.net/saps-ibu-bapa-semakan-keputusan-peperiksaan/">proceed past the invalid certificate warning in firefox</a>. But let's get back to the breach.

My first reaction was to test the vulnerability, and sure enough, the site was vulnerable to SQL Injection, in exactly the manner specified by the email. So far email looked legitimate.

Next, I verified the data in the Google Drive folder, by downloading the gigabytes of text files, and checking the IC Numbers of children I knew.

I further cross-checked a few parents IC numbers against the electoral roll. Most children have some indicator of their fathers name embedded in their own, either through a surname or the full name of the father after the <em>bin, binti, a/l or a/p</em>. By keying in the fathers IC number, and cross-referencing the fathers name against what was in the breach, it was easy to see that the data was the real deal.

So I called back Zurairi and confirmed to him that the data was real, and that the site should be taken offline. I also contacted a buddy of mine over at MKN, to see if he could help, and Zurairi had independently raised a ticket with MyCert (<i>a ticket??!!</i>) and tried to contact the Education Minister via his aide.

Obviously neither Zurairi nor myself, or any of the other journalist I kept in touch with, could report on the story. The site was still vulnerable, and we didn't want someone else breaching it.

The next morning, I emailed the anonymous source and asked them to take down the Google Drive, explaining that the breach was confirmed, and people were working to take down the site. Hence there was no reason to continue exposing all of that personal information on the internet.

They agreed, and wiped the drive clean, and shortly after I got confirmation that the SAPSNKRA website had been taken down. So with the site down, and the Google Drive wiped cleaned, it seemed the worst was behind us.

Danger averted...at least for now.

But, since <a href="https://www.keithrozario.com/2017/12/that-long-post-about-data-breaches-you-never-wanted-to-read.html">Data breaches last forever</a>, and this was a breach, we should talk about what data was in the system. Zurairi did a good job <a href="https://www.malaymail.com/s/1640346/putrajayas-exam-portal-shut-down-after-data-breach-affecting-millions">here</a>, but here's my more detail take on the issue.<!--more-->
<h2>But is this a breach? And what's in it?!!</h2>
![](/uploads/data-breach.jpeg)Sadly it IS a breach.

Once the data left the servers, and were placed onto a Google Drive, it was breached! By exploiting the vulnerability, instead of just reporting it, the anonymous source unintentionally caused the biggest data breach Malaysia has seen (so far!).

The data included the names, addresses, classes, schools, MyKad Numbers and even the <span style="text-decoration: underline;">race and religion</span> of millions of students. Worse, it included the MyKad numbers of parents as well and teachers. The number of unique IC numbers (parents, students &amp; teachers) totaled nearly 10.5 million, and while this is smaller than the large telco breach, I feel this is bigger, simply because it has additional relationship information, which the telco breach did not.

<em>Years from now, people will still know the Mothers Maiden name of these students -- which would make their credit card security question easy to guess!!
</em>

If I know the MyKad numbers of parents, I can quite accurately deduce that those two adults are married to each other (or at least <em>were</em> married at some point), and I can figure out the full list of classmates for every student in the breach. That's a scary amount of data, and worse this is for children.

On top of that, data from nearly 450,000 teachers were in the breach, aged from 19 to 85 years old (at least based on MyKad numbers). I initially thought this had to include retired teachers, but then I realized the number of teachers above 55 were minimal, I suspect this might be teachers rehired on contract -- after all we have 93 year old PM, what's an 85 year old teacher?
<h2>So What now?</h2>
It's important to note, that up until the email was sent out, the system was vulnerable but not breached <em>(at least not that we know off)</em>. The vulnerability in question, SQL Injection is so basic and common, it's something we'd teach a first year computer science class -- so it's probable that someone else had executed the same attack, and obtained the same data.

Although I've not seen this data pop up on any database dump so far, I'm not entirely good at finding them.

And Yes, the site should be secured, but we can't judge a site created in 2011 using our 2018 lens of the world. 2011 predates all the large breaches we fondly remember today, like Target, Anthem, OPM, or Yahoo. 2011 predates the Sony Pictures Hack, and all the security stuff we've only recently taken seriously.

So it's easy to see, how a php system with a glaring SQL Injection vulnerability, went live into production with sensitive personal data. It's not that hard to understand. You might disagree with it, you might not like it, but if you've ever worked in IT delivering these kind of projects, you'd understand immediately how this happened.

However, there are two hard questions we have to ask.
<ol>
 	<li>How did the vulnerable site continue to be up?</li>
 	<li>Why didn't anyone respond to the initial vulnerability report by the anonymous source?</li>
</ol>
Let's tackle the 2nd question first.

<b>Responding to vulnerability disclosures</b>![](/uploads/original-complaint.png)After contacting the source, we further chatted about a few things, and they(*) shared with me their frustrations and lack of response from the Ministry.

A report was lodge using the <a href="http://moe.spab.gov.my/eApps/sdmscasepool/SdmsCasePool/check.do"><em>Sistem Pengurusan Aduan Awam</em> </a>website, which isn't the right place to report these things. But if the government isn't clear on where to report security vulnerabilities, then people are going to be confused.

The report (pic above) was dated 28-May, which meant a 2 week gap between the report and the email blast to the press. Now, two weeks is a very short time to expect a <strong>fix</strong>, it's a very long time to expect a meaningful response -- which never came.

What I suspect is that the Sistem Pengurusan, is a glorified ticketing center, that didn't comprehend what was being reported to them (after all who knows what SQL Injection is??!), the Sistem then put the complaint through it's workflow and usual 'under investigation' status, which further frustrated the source.

The report wasn't taken seriously, because there isn't a proper place to disclose vulnerabilities on government websites. When I find vulnerabilities, I usually email the <a href="https://www.keithrozario.com/2018/06/gov-tls-fixed-websites.html">Technical Contact on the WHOIS record</a>, or somehow find my way to someone who knows what I'm talking about, or as a last-ish resort blast out a tweet on twitter.

The government should either have a centralized place to disclose vulnerabilities on any government infrastructure -- or mandate that all government sites have a <a href="https://securitytxt.org/">security.txt</a> file, or something else.

Had the source been able to contact a legitimate technical contact who understood what they were talking about, we wouldn't be here.

Now onto the second point.
<h2>How did the vulnerable site continue to be up?</h2>
![](/uploads/penetration-testing.jpeg)If you ask most folks, they'll tell you the same thing -- site should have been pentested.

A pen-test (short for penetration test) is hiring 'ethical hackers' to attempt to break your system. At the end of the test, they present to you their findings, you fix them, and hopefully your system goes live in an more secure state. <em>(remember it's more secure, not absolutely secure)</em>

It's a great idea, and it's always valuable to have a real human-being (if you consider pentesters human) try to crack your system. Any pentester would have found the SQL Injection vulnerability on SAPS immediately.

But pentesting only works on a point in time. If you ran a pentest in 2011, and again in 2014, the later pentest would have uncovered more vulnerabilities, simply because the security community has found new ways to exploit systems. Pentesting is great, but it only bears fruit if you regularly do it.

Obviously the MOE didn't pentest SAPS, either at the implementation phase, or anytime after. But that's only the tip of it.

A side project of mine scans 3,500 government websites for TLS and just under 500 of them implement TLS correctly. If you can't implement a standard like TLS correctly, it's likely a lot of other things are messed up on your site as well -- like SQL Injection, or XSS or a hundred other entry level vulnerabilities.

We shouldn't judge developers from 2011 with our 2018 lens, but we can certainly judge any site still up and running in 2018 with our current standards -- and by those standards a large majority of government infrastructure is sub-standard.

<em>[A few friends of my commented that various PHP frameworks were already mature in 2011. Facebook was mostly built up on PHP, and had the developers used a framework (which they should) then this wouldn't have happened. 2011 was long ago, but it wasn't that long. </em><em>I must say, I stand corrected]</em>
<h2>Conclusion</h2>
It's tough man. Imagine you're in charge of IT over at the Ministry, and you're told:
<ul>
 	<li>Here's 70+ websites, some of which are 10 years old</li>
 	<li>Here's 40+ servers, some of which run obsolete software, some of which we have no idea what they do.</li>
 	<li>Your job is to keep these servers up, running and secure, while still delivering new projects.</li>
</ul>
It's not a job anybody in their right mind would want. So I sympathize with the IT folks.

But at the same time we can't be exposing personal data on insecure infrastructure. At the very least, we should pentest everything, and start a bug bounty program (similar to Singapore) and then take some budget out to fix these issue before we have a repeat of last week's debacle.

Also, running a pentest on everything, and having a parallel bug bounty program might incur a relatively low cost (millions), the price of fixing all the bugs that are discovered will be significantly higher, and we have to prioritize what we'll fix based on what risk those sites pose.

Nothing in that equation is easy, quick or cheap.
<h2>Footnotes</h2>
<em>* I use 'they' to refer to the anonymous source not because its a group. It is a young individual, for whom I do not want to divulge any further information including their gender.</em>

<em>* Image for penetration testing is a great book I recommend for folks looking to dabble into some 'hacking'. Click on the link to head to the Amazon sale page.</em>