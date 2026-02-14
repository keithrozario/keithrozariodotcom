+++
title = "Supply Chain Woes"
slug = "supply-chain-woes"
date = "2018-10-07T22:27:21"
draft = false
categories = ['Misc']
+++

<!-- wp:cover-image {"url":"https://www.keithrozario.com/wp-content/uploads/Super-Micro.png","id":6522} -->
<div class="wp-block-cover-image has-background-dim" style="background-image:url(https://www.keithrozario.com/wp-content/uploads/Super-Micro.png)"></div>
<!-- /wp:cover-image -->

<!-- wp:paragraph {"dropCap":true} -->
<p class="has-drop-cap">The security community has been abuzz with an absolutely <a href="https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies">shocker of story from Bloomberg</a>. The piece reports that the Chinese Government had subverted the hardware supply chain of companies like Apple and Amazon, and installed a 'tiny chip' on motherboards manufactured by a company called Supermicro. What the chip did -- or how it did 'it' was left mostly to the readers imagination.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Supermicro's stock price is down a whooping 50%, which goes to show just how credible Bloomberg is as a news organization. But besides the Bloomberg story and the sources (all of which are un-named), no one else has come forward with any evidence to corroborate the piece. Instead, both <a href="https://www.apple.com/newsroom/2018/10/what-businessweek-got-wrong-about-apple/">Apple</a> and <a href="https://aws.amazon.com/blogs/security/setting-the-record-straight-on-bloomberg-businessweeks-erroneous-article/">Amazon</a> have vehemently denied nearly every aspect of the story -- leaving us all bewildered.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But Bloomberg are sticking to their guns, and they do have credibility -- so let's wait and see. For now, let's put this in the bucket called <span style="text-decoration: underline;">definitely <strong>could</strong> happen, but probably <strong>didn't</strong> happen.</span></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I can only imagine how hard it must be to secure a modern hardware supply chain, but the reason for this post is to share my experience in some supply chain conundrums that occurred to a recent project of mine.<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I operate (for fun) a website called <a href="http://GovScan.info">GovScan.info</a>,  a python based application that scans various <code>gov.my</code> websites for TLS implementation (or lack thereof). Every aspect of the architecture is written in Python 3.6, including a scanning script, and multiple lambda functions that are exposed via an API, with the entirety of the code available on <a href="https://github.com/keithrozario/Gov-TLS-Audit">github</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And thank God for GitHub, because in early August I got a notification from GitHub alerting me to a vulnerability in my code. But it wasn't a vulnerability in anything I wrote -- instead it was in a 3rd-party package my code depended on. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6521} -->


![](/uploads/Dependency.png)


<!-- /wp:image -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Dependency Hell!</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"dropCap":true} -->
<p class="has-drop-cap">Modern day programs aren't just one 'block' of code written by one person (or even just one thing). They're a many blocks of code coming together to achieve a specific task. In my case, I was running a Python script that required a Python Interpreter (obviously!) -- but above and beyond that I was depending <a href="https://github.com/keithrozario/Gov-TLS-Audit/blob/master/requirements.txt">28 different Python packages</a> written by people who were not me or Python.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>These included packages to help me integrate to AWS, to call Shodan for their results, to extract TLD data from a domain, and the list goes on Instead of writing all these from scratch, I decided to import existing python packages that were already written (mostly by people smarter than me), and this tremendously improved the time-to-market of the end solution.<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, you should never try to write your own Python Package to call the Amazon API directly -- instead use <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html">Boto3</a>, it'll be safer, quicker, more secure and you're guaranteed it'll be maintained for a long time.<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But I was also depending on code that wasn't written by big companies like Amazon. Some were written by independent folks, people like me, just coding something over the weekend. How could I be sure that these folks aren't malicious -- or at the very least keep their code up to date and free from vulnerabilities. (<strong>spoiler alert:</strong> I can't be sure)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And here's the real kicker -- some of the packages I depended on, had dependencies of their own!!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A single <code>import</code> statement in my code, could include multiple dependencies that originated from dozens of people, all of whom may not even know each other --  and a single malicious actor in that chain could compromise my code and any other that used the same packages. And to me it would look like one dependency -- but in reality there could be dozens of dependencies hidden underneath it.<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In my case, the vulnerable package was <code>cryptography</code>, which I didn't import directly, but rather was imported by <code>sslyze</code>, a separate package I used to extract certificate information from websites. I didn't even know I was depending on cryptography, but fortunately GitHub picked it up from the <code>requirements.txt</code> file. Which thankfully I kept up to date (after all this is how I deploy the app)<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It didn't take me long to upgrade the package, re-test and re-deploy, but next time I might not be so lucky. <a href="http://GovScan.info">GovScan.info</a> is just a side-project of mine, so this wasn't a big deal. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But imagine a worst-case scenario<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"dropCap":true} -->
<p class="has-drop-cap">You've got a Production running script your company relies on for a core business operation. Today, a high severity vulnerability was reported in a python package that 70% of your code base relies on -- and to make matters worse, the developer of the package and since stopped supporting it <em>(nobody is going to fix this for you!)</em>. Ripping out the package from the python script won't be easy, and worse still, you're a small operations with no automated testing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You've got 3 options:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>replace the package with another similar package, re-code and re-test</li><li>fork the package and try to fix the vulnerability, supporting the package indefinitely from now on</li><li>Find some clever way to limit the risk of the vulnerability to an acceptable level.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>In the short-term your choices are clear, either live with the vulnerability for 6 weeks, or shutdown a core business process. Guess which one management is going to gravitate towards?  </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And devoting developer time to do this, will severely impact the timelines of another critical project.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With all of that, it's clear that using un-supported packages is not a good idea -- but that's what people do all the damn time! Most folks aren't even aware of their first-level dependencies, let alone their 2nd, 3rd of 4th level ones. And the example is Python, but you can replace with Java, C, PHP or whatever other language you choose, and it would still hold valid.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If this was all a vendor product, it'll be moot -- you can just choke the vendor (assuming you know what packages they rely on -- or hopefully the vendor knows). In-House built applications though may not go through this level of scrutiny, or perhaps only go through this on an ad-hoc 'as-you-deploy' basis. Legacy applications written in 6 year old versions of Java may be riddled with vulnerable dependencies but still run happily in production until someone comes along for a code-base scan.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Plus, this is not a binary outcome, just because you use a vulnerable package doesn't mean you're vulnerable, in many cases you'll need to use the package in a specific way to be vulnerable -- and that requires some human intervention to really figure out.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And we've not even begun to explore the other stuff running on the server, like what OS are your running, what version JRE or .NET, what version of that logging application, that monitoring tool, that little batch script that bob wrote before he left? </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Has anyone even looked at the hundreds of excel macros littered in the organization? Whose validated that the Excel VBA Rebecca wrote two days before she quit, doesn't exfil data to pastebin? <br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The point is, supply chain issues are a massive problem -- it's tremendously hard with hardware, but even software supply chain problems (with theoretically should be easier) is immensely hard.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The Bloomberg isn't a cause for alarm -- yet!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's probably a hundred easier ways for China to hack into you, without the need for specialize hardware -- and even if they needed the hardware, it'll probably be easier hijacking a local laptop than a server that maybe behind a massive amount of firewalls and NAT-ed routers.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What's probably more pressing is the software supply chain, especially in custom built apps, most media outlets I know use Wordpress and install a boat-load of plugins on them -- whose checked any of those for vulnerabilities lately?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In any case, taking a fine tooth comb to your software supply chain probably couldn't hurt -- but it won't be an easy task.<br/></p>
<!-- /wp:paragraph -->