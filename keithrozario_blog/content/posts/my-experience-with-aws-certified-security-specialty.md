+++
title = "My experience with AWS Certified Security - Specialty"
slug = "my-experience-with-aws-certified-security-specialty"
date = "2020-03-28T08:49:08"
draft = false
categories = ['Cloud Computing', "Keith's Favorite Post", 'Security &amp; Privacy', 'Serverless']
+++

<!-- wp:image {"align":"center","id":7007,"sizeSlug":"large"} -->
![](/uploads/aws-certified-logo_color-horz_360x60.jpg)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Last week I took the <a href="https://aws.amazon.com/certification/certified-security-specialty/">AWS Certified Security - Specialty</a> exam -- and I passed with a score of 930 (Woohoo!!)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this post I cover why I took it, what I did to pass, my overall exam experience, and some tips I learnt along the way.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So let's go.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Why?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Why would anybody pay good money, subject themselves to hours of studying, only to end up sitting in a cold exam room for hours answering many multiple choice questions! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And the reward for that work is an unsigned PDF file claiming you're 'certified', and 'privilege' access to buy AWS branded notebooks and water bottles!! <em>Unless those water bottles come with a <a href="https://twitter.com/QuinnyPig/status/1243316557993795586">reserved instance for Microsoft SQL server in Bahrain</a>, I'm not interested.</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But, jokes asides, I did this for fun and profit, and fortunately I really did enjoy the preparing for this exam. It exposed me to AWS services that I barely knew -- and forced me to level-up my skills even on those that I knew.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The exam has a <strong>massive</strong> focus on VPC, KMS, IAM, S3, EC2, Cloudtrail and Cloudwatch. While lightly touching Guardduty, Macie, Config, Inspector, Lambda, Cloudfront, WAF, System Manager and AWS Shield. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You need to catch you breath just reading through that list!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But for those diligently keeping count -- you'd notice that the majority of those services are serverless -- meaning the exam combined my two technological love-affairs ... security and serverless!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I wasn't lying when I said it was fun. So what about the profit. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I'm not sure how good this would be for my career <em>(I literally got the cert last week)</em>, but for $300, it's is relatively cheap, with a tonne of practical value. So trying to get an ROI on this, isn't going to be hard. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For comparison, the CCSP certification cost nearly twice as much, is highly theoretical and requires professional experience.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The results also help me validate my past years of working on serverless projects, proving I wasn't just some rando posting <a href="https://github.com/keithrozario">useless hobby projects</a> on GitHub. Instead, I'm now a <strong>certified AWS professional</strong>, posting useless hobby projects on GitHub <em>(it's all about how you market it!)</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So now that we've covered the why, let's move onto <span style="text-decoration: underline;">how</span>.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>How to Pass?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The general consensus from all my online research was to subscribe to the <a href="https://acloud.guru/learn/aws-certified-security-specialty">acloud.guru</a> and <a href="https://linuxacademy.com/course/aws-certified-security-specialty/">LinuxAcademy</a> courses, and I can absolutely confirm, that these two courses taken <span style="text-decoration: underline;"><strong>together</strong></span> are a great <strong><span style="text-decoration: underline;">start</span></strong> for your exam preparation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you have the AWS recommended 5 years IT security experience and 2 years hands-on experience securing AWS workloads, then perhaps they're enough. But I don't that experience ... and the two courses certainly wouldn't have been enough for me.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I work as an architect in an organization with <span style="text-decoration: underline;">not much</span> on the cloud, and I've never worked in an official security role. So I wasn't the target audience for this exam, and just watching the courses definitely wasn't going to get me a good score. I'm smart enough to know, that I'm not<strong> that </strong>smart!!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But... </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I do have in-depth experience with serverless (mostly from my <a href="https://github.com/keithrozario">side</a> <a href="https://github.com/keithrozario">projects</a>), a 'good enough' appreciation of Terraform, and I'm kick-ass at Python!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So I came up with a game-plan that leveraged my strengths to overcome the lack of experience, and if you're interested keep on reading for how I did it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Terraform like there's no tomorrow</h2>
<!-- /wp:heading -->

<!-- wp:image {"align":"center","id":7010,"sizeSlug":"large"} -->
![](/uploads/Terraform.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For one, I repeated most of the course material from acloud.guru and LinuxAcademy -- but on Terraform!! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I found blindly copying the instructors console actions to be of little value -- instead, trying to rebuild in Terraform, what the instructors were building on the console, was the quickest way to get an in-depth knowledge of the materials. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Terraform is by no means 'quick' -- but once you build something in it, you develop an appreciation for the details of that service that the console abstracts away from you!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Plus, Terraform gave me the confidence of tearing down and re-building infrastructure, like playing an adventure game that lets you save your progress -- allowing you to risk your life anytime and anywhere in the game, with the assurance that you can also revert to the last save-point.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Believe me, having that confidence to tinker, speeds-up learning. You're more willing to modify an AWS Config recorder, if you know, no matter how badly you screw it up, some <code>ctrl-Z</code> and <code>terraform apply</code> is going to get you back to the last working configuration.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For scripting I used the deadly combo of Python and boto3. For example, when learning STS Assume Role or creating key grants, it's far easier scripting 20-30 lines of code, than it is do work on the console. Plus, once you've written down the code, a push to GitHub saves it for the <a href="https://archiveprogram.github.com/">next 1,000 years</a> -- which is roughly the time it took for me to finish studying anyway :)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Your own code, are the best notes you can take for the exam. Additionally, I've found the <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html">boto3 </a>and <a href="https://www.terraform.io/docs/providers/aws/r/s3_bucket.html">Terraform</a> docs to be the best way to learn a new service, and this was no exception. Actually using something, forces you to learn it -- who knew?!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But for some use-cases, it's going to be more theory than practice, for example DDoS mitigation, Guardduty findings, Incident response etc.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For those you need to research.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Research</h3>
<!-- /wp:heading -->

<!-- wp:image {"align":"center","id":7029,"sizeSlug":"large"} -->
![](/uploads/6876694340_01a10c613b_c.jpg)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>On top of course material, there are other mandatory materials that'll help you in the exam. Some of these appear in every blog post on the subject, but some are strangely missing. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, the <a href="https://aws.amazon.com/about-aws/whats-new/2019/05/announcing-new-and-updated-exam-readiness-courses-for-aws-certifications/">AWS Certified Exam Readiness</a> was a phenomenally useful resource -- and it was free! At the end of the course, you get a practice exam with 24 questions that come with thoughtful answers. I guess it's missing from most online post because it's new. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So here are some additional resources you might not find as recommended reading material elsewhere:</p>
<!-- /wp:paragraph -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:heading {"level":4} -->
<h4>Whitepapers</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li><a href="https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf?did=wp_card&amp;trk=wp_card">DDoS best practices</a></li><li><a href="https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf?did=wp_card&amp;trk=wp_card">Well Architected Framework (Security Pillar)</a></li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4>Must-Watch YouTube Videos:</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li><a href="https://www.youtube.com/watch?v=YQsK4MtsELU">Becoming an IAM policy Master</a>: Absolute must-watch!!</li><li><a href="https://www.youtube.com/watch?v=CJexxdv054c">Soup to Nuts: Identity Federation for AWS</a></li><li><a href="https://www.youtube.com/watch?v=o2YaIsps5LY&amp;t=1753s">Deep Dive on Amazon Guardduty</a></li><li><a href="https://www.youtube.com/watch?v=X1eZjXQ55ec&amp;feature=youtu.be&amp;t=1375">Best Practice for Implementing AWS Key management</a></li><li><a href="https://www.youtube.com/watch?v=6DX7p-OirGU">Provable Access Control</a>: Not relevant for the exam, but amazing talk!</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4>Others:</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li><a href="https://www.aws.training/Details/eLearning?id=34786">AWS Certified Exam readiness</a></li><li><a href="https://aws.amazon.com/about-aws/whats-new/2014/07/07/aws-certification-practice-exams-now-available/">AWS Practice Exam</a></li></ul>
<!-- /wp:list --></div></div>
<!-- /wp:group -->

<!-- wp:paragraph -->
<p>But pure researching isn't really going to help that knowledge sink in -- especially on a 3-hour exam. For areas where you're unsure off, it's always a good idea to write it down....</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Write it down!!</h3>
<!-- /wp:heading -->

<!-- wp:image {"id":7030,"sizeSlug":"large"} -->
![](/uploads/19893436479_462a12ab31_c.jpg)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Writing is thinking clearly. Can't stress this enough.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I have a repo where I wrotedown my notes and kept my Terraform and python scripts, but apart from that, I also wrote down in blog form things I learnt along the way. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example I wrote a ~3000 word <a rel="noreferrer noopener" href="https://www.keithrozario.com/2020/01/amazon-kms-intro.html" target="_blank">article on KMS,</a> that included diagrams and links, and even IAM policies. The post didn't garner much viewership -- but that's not the point! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The point is writing something in essay form, forced me to think about about it clearly, which quickly revealed gaps in my understanding -- gaps I could easily remediate <span style="text-decoration: underline;">before</span> the exam, but not <span style="text-decoration: underline;">during</span> the exam!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After writing the post, I posted it to a few forums for which I got great feedback written in very thoughtful form (thanks Mark!). This feedback helped me reveal the unknown-unknowns, things I had no idea I didn't know!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, did you know that CMK key policies are special exception for AWS resources -- in that their resource policies must explicitly allow permissions even for Principals in the same account. I surely didnt!!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And... did you also know that <code>arn:aws:iam:::&lt;account>:root</code> doesn't refer to the root user (like what!!). Instead it refers to <a href="https://www.youtube.com/watch?v=X1eZjXQ55ec&amp;feature=youtu.be&amp;t=1375">delegated IAM control</a>. Not super useful for the exam -- but super fun to learn. The moment I learnt how all of this worked, my brain just lights up, and that's where all the fun comes in.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But I digress, the point is, I wouldn't have learnt any of this, if I hadn't written it down, and published it for general feedback. You should too -- and ignore the snarky one-liner critics (they're always there), there's some great folks in the security community who are willing to give wonderful feedback if you ask nicely. Worse case, if you're really desperate -- you can always ask me, I promise to help!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Going into the exam, KMS was one of my strongest areas, and I owe it all to writing and publishing that blog post.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So to recap how I passed, </p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Took the acloud.guru and LinuxAcademy course</li><li>Terraform-ed like there's no tomorrow</li><li>Researched like crazy; and</li><li>Wrote stuff down.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Now onto the exam itself!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Overall experience</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":7032,"sizeSlug":"large"} -->
![](/uploads/6394785643_fafa2f3926_c.jpg)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>As the world is now combating Covid-19, <a href="https://aws.amazon.com/certification/faqs/">AWS recently announced you can take a virtual proctored exam</a>, so your experience will differ from mine, as I took mine in a physical location here in Singapore.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The exam is 65 questions over 170 minutes -- take a bathroom break before you start!! I flagged questions I wasn't sure off, and made my first pass through all of them in 90 minutes. For which, a large chunk of questions were flagged (22 in total). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>At this point, my confidence was low, 22 questions is a large percentage of the exam. I was feeling bad -- like <em>"WTF am I doing here??!!"</em> bad...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But I collected my thoughts, took deep breaths -- and moved on, one question at a time. Re-reading the questions, re-reading the answers, and applying some cognitive power. Slowly I started answering off the flagged questions. Gaining confidence with each answer :)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I went through the entire set of 65 again (eliminating 2-3 careless mistakes!), and eventually I finished with 30 minutes to spare. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Remember, you <span style="text-decoration: underline;">don't need to know the right answer if you can eliminate all the wrong ones</span>! And unlike other exams, the security specialty sometimes has questions with 2-3 workable answers -- your job is to pick the one that matches the questions requirements (e.g. Fastest, Cheapest, Simplest...etc). So pay attention to that!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And if I can go from "WTF am I doing here" to scoring 930 -- so can you. Just remember this if you're feeling a bit flustered during the exam -- you got this!!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Exam Dumps aren't worth-it</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>There's a websites claiming to have "100% exam questions", but they are more problematic than helpful. For one, most of the questions are plagiarized from Acloud.guru or Linux Academy sample questions, so there's no point if you subscribed to the courses already.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Secondly, these dumps have many obvious wrong answers. Avoid them like you would a mosh-pit during covid-19 lock-down!! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you want practice questions here's more kosher sources:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><a href="https://d1.awsstatic.com/training-and-certification/docs-security-spec/AWS%20Certified%20Security%20-%20Specialty_Sample%20Questions.pdf">10 sample questions</a> on the AWS website. </li><li><a href="https://www.aws.training/Details/eLearning?id=34786">24 sample questions</a> at the end of the Exam Readiness course (with an additional 12+ sprinkled throughout the course)</li><li><a href="https://aws.amazon.com/certification/certified-security-specialty/">20 sample questions</a> in the practice exam</li><li><a href="https://acloud.guru/">Acloud.Guru</a> and <a href="https://linuxacademy.com/course/aws-certified-security-specialty/">Linux Academy</a> practice exams.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>From there you've got 54 questions from AWS, and ~150 questions from both acloud.guru and LinuxAcademy combined -- you don't need any more.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But let me share with you two tips before I end.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Tip 1: Lambda for the win!</h2>
<!-- /wp:heading -->

<!-- wp:image {"align":"center","id":6770,"sizeSlug":"large"} -->
![](/uploads/AWS-Lambda_dark-bg.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Tip 1: </strong>Use Lambda instead of EC2.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When testing running code in a VPC subnet, it's much easier to just deploy a lambda function into that subnet, than spinning up an EC2 instance. You don't have to worry about key-pairs, and ip logging, NAT and security groups etc, and god-forbid the subnet is completely private, leaving you to mess around with Bastion Hosts, or Session manager.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Instead, you can easily deploy lambda functions with the runtime of your choice (including AWS-CLI running on <a href="https://github.com/gkrizek/bash-lambda-layer">Bash custom runtime</a>) directly on any subnet. You can invoke those functions from your local machine on the internet -- even if the function resides in a private subnet -- and get the response immediately! Check out <code><a href="https://serverless.com/framework/docs/providers/aws/cli-reference/invoke/">sls invoke</a></code>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Also, with the <a href="https://github.com/functionalone/serverless-iam-roles-per-function">serverless-iam-roles-per-function</a> plugin for serverless framework, you can assign different IAM roles to each lambda. Allowing you to test different permission policies, all from a single <code>serverless.yml</code> file! This is the best way to test new permission policies to see their effect on running code!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, nearly all security offerings on AWS are serverless in nature, hence you spend a lot of time, interacting with APIs and IAM roles, something any serverless practitioner is going to feel at home with. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Serverless first baby!!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Cost</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":7031,"sizeSlug":"large"} -->
![](/uploads/41145631035_0ceb85138e_c.jpg)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Tip 2:</strong> Here's how to save 90 bucks!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here is my end-2-end cost for the exam:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Exam cost : $300</li><li>Practice Exam: $40</li><li>3 Months <a href="https://acloud.guru/">Acloud.guru</a>: $87 (subscribed in Dec 2020 at $29/mo)</li><li>2 months <a href="https://linuxacademy.com/course/aws-certified-security-specialty/">Linux Academy</a>: $98 ($49/mo)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>For a grand total of $525. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I really hope the merger between the <a href="http://acloud.guru">acloud.guru</a> and <a href="https://linuxacademy.com/course/aws-certified-security-specialty/">LinuxAcademy</a> completes soon, and I get to keep my grandfathered price of $29/mo -- it's phenomenal content!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But there is slight 'hack' you can do, once you know you get a <a href="https://aws.amazon.com/certification/benefits/">50% discount voucher on all AWS exams once you pass any exam</a>. Instead of taking the $300 Security Specialty exam directly, take the $100 cloud practitioner, and apply that 50% discount for the $300 Specialty exam. Which means you get 2 certs (and a free practice exam) for $250 -- instead of $340 had you paid rack price (like stupid ol' me!).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That's it folks. Leave you comments below on your experience below, or ask questions and I'll try my best to answer.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Credit:</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Research quote from <a href="https://www.flickr.com/photos/astronomyblog/">astronomy_blog</a></li><li>Writing image from <a href="https://www.flickr.com/photos/jvk/19893436479/in/photolist-wiV4A8-8Yba81-Wqcmrg-93d4UK-pMrTJk-7A5VXg-Gv4ziV-bBLYhZ-T4exnh-Wec4Wj-TowPS4-29CrPC5-SMCHF3-dcxvQe-YFUTGh-bTKhyK-Kz6BDk-rVCM1G-TrLyte-T4exuS-qHZj5N-J1itDq-UZ2Str-VJaVeg-sxt4yL-bMbCnF-9oz7Li-Pjws9T-JNzKwt-LMUKhi-dQgT43-Q2tPAV-7Ao2Bj-9TgxmY-8aLw1E-8kQ3KS-auBnQV-TzXWVF-dxR11F-22Ss9gY-FskUmv-YqFxAb-Cuxa4R-8Vxwd2-areww1-PREzFZ-b545DR-M5XYEG-gYL8r4-VMfRKk">Asa Stellar Graphic</a></li><li>Money on calculator from <a href="https://www.flickr.com/photos/157270154@N05/41145631035/in/photolist-25FU7BD-9Uv4aE-4fSZu8-8LCMVv-5GFbYD-g7Ep72-btEme-2cbccna-5SYbC7-NUm3N-dhSUQy-QeKJeD-8rfCL3-NUm3A-7HaRNh-2gYabH-2gvpBkX-azeP6g-8dgmhP-R54UqW-QymsH3-6ApWbu-R54Up3-7fQLQJ-2cBfiag-2iDa9MW-7Mhr4y-uVvk8y-7Mdrae-APB1SY-oLGRYp-v9Tc5-3EidWz-2beoS7N-k5iErU-aGyWGB-d35SkE-TAoi9p-9oTEhv-rp8yi-bNravX-K9Nzr-c4iA9q-7s9VFc-7d3ESt-5JNg57-p49q8X-74r3Kt-oLFSPq-5npvZZ">Mike Lawrence</a></li><li>Exam from <a href="https://www.flickr.com/photos/18614695@N00/6394785643/in/photolist-aK5WYT-6xixp7-7kuz2S-9hXxvB-9hXxHr-Yu8hd-nWqZ8e-4mCQ7y-ifwxsT-6P4MYn-63KtMU-deFtqh-Y2DY84-9AVy43-sgoBa6-WqCx7C-dh8moG-N7SxZh-nkxxLK-217PL-iYjVzv-VfoEJ4-29TBvor-MKZRrb-et2CW-et2CD-rzae3w-X3Ekdp-2ge8DSW-bvfFx2-fqiZtg-EDLrAJ-irMhR5-e5bj5R-4Hbpey-EYAm2h-25DdZMf-e8hRQ7-EarQhD-nLePir-4enA2g-ee8Xoo-5eX77C-7kgeta-fjrZqX-e8bMhp-6C8rdW-9vqAw4-76Nxh7-4QotYx">Xavi</a></li></ul>
<!-- /wp:list -->