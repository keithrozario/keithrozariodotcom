+++
title = "MySejahtera privacy concerns"
date = "2020-12-06T17:35:16"
draft = false
categories = ['Misc']
+++

<!-- wp:paragraph -->
<p>Last week, a friend sent me a <a href="https://www.youtube.com/watch?v=ZR_6JGA0gXw">video of viral video by 'Fat Bidin'</a>, highlighting privacy concerns of the MySejahtera app. The same author (a.k.a Zan Azlee) also wrote a <a href="https://www.malaysiakini.com/columns/551758">comment piece in Malaysiakini </a>explaining his concerns over the Government's contact tracing application.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Specifically, he was concerned that MySejahtera had a "slew of different capabilities that is very much of a concern, such as:"</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Pair with Bluetooth devices</li><li>Directly call phone numbers</li><li>Find accounts on your phone</li><li>Read your contacts</li><li>Read the contents of any external storage on your phone like SD cards</li><li>Modify or delete the contents of your SD cards</li><li>Prevent phone from sleeping</li><li>Modify your contacts</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Wow, that's a worrying list. But just where did Fat Bidin get this list from?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It comes from fine folks at exodus-privacy, which claims itself to be "<strong>The privacy audit platform for Android applications</strong>". Exodus Privacy is run by hacktivist, and although Fat Bidin claims it has an affiliation with Yale University I'm unable to find anything to verify that. Other than articles stating they've worked together once in 2017.<sup>[<a href="https://privacylab.yale.edu/trackers.html">1</a>][<a href="https://law.yale.edu/yls-today/news/isp-privacy-lab-publishes-research-hidden-trackers">2</a>]</sup></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Permissions vs. Actions</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I'm not saying that the Exodus-Privacy isn't to be trusted, on the contrary I believe it to be very accurate, I disagree on the conclusion. This is a list of <strong>permissions</strong> the app requests for, not the list of actions the app actually performs. Exodus <a href="https://reports.exodus-privacy.eu.org/en/info/permissions/">detail this difference on their site</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sure it sounds like semantics, because why would the app ask for permissions for something it doesn't use -- well if you've been around in technology for as long as I have, you'll recognize this to be a very(!) common pattern. My opinion (humble as it is) is that should never attribute to malice that which is adequately explained by poor design. An app asking for permission to do something, doesn't necessarily mean the app will actually do it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I have my wife's permission to wash the dishes everyday -- but that doesn't mean I actually do it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So let's dig deeper.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Using exodus-privacy I looked up what permissions <a href="https://reports.exodus-privacy.eu.org/en/reports/sg.gov.tech.bluetrace/latest/#trackers">TraceTogether</a> and <a href="https://reports.exodus-privacy.eu.org/en/reports/uk.nhs.covid19.production/latest/">NHS Covid-19</a> use, these are similar apps from the Singaporean and UK governments respectively. Lo' and behold, they both request the same Bluetooth pairing request, with <a href="https://reports.exodus-privacy.eu.org/en/reports/au.gov.health.covidsafe/latest/">Australia's CovidSafe</a> going  further and requesting bluetooth admin rights as well. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Perhaps MySejahtera isn't made for the same purpose as these apps, but it goes to show that bluetooth pairing on a tracking app is quite normal. Another worrying action highlighted by Fat Bidin was "Reading external storage". This permission was present in TraceTogether but not on the NHS or Australian apps -- again, I'm no expert but I suspect it's not abnormal either. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The cynics among you might point out that ALL governments want to spy, and this is indicative of government behavior. Then, let's look at non-government apps.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If we continue to browse exodus-privacy for applications that request for external storage access, we find apps including <a href="https://reports.exodus-privacy.eu.org/en/reports/155849/">MiFit</a>, <a href="https://reports.exodus-privacy.eu.org/en/reports/155865/">Weather App</a>, and even <a href="https://reports.exodus-privacy.eu.org/en/reports/155870/">Oral-B</a> (<strong><em>like what?!</em></strong>). The Oral-B application had Bluetooth Admin access (which MySejahtera didn't), and MiFit had more than twice the permissions requested by MySejahtera. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let that sink in, an app from a toothbrush is asking for more permissions than a contact-tracer from the government.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which all goes to show -- this is common in the Android ecosystem, and the loose permissions of the MySejahtera app are more easily explained by the status quo of Android, than a government super app designed to spy on citizens.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But what about the contact information? Surely the app can't have any business accessing and modifying contact information. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You're right -- it shouldn't. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And it <strong>doesn't</strong>!!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you go into exodus-privacy, and type in MySejahtera, you'll see that it doesn't have those rights -- at least not the current version (<a href="https://reports.exodus-privacy.eu.org/en/reports/154280/">v1.0.25</a>), it's only the older version (<a href="https://reports.exodus-privacy.eu.org/en/reports/126526/">v1.0.10</a>) that had it. But why would Fat Bidin choose to reference the older more permissive version, instead of the latest version.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To be fair, the latest version was only scanned by Exodus-privacy on the 20-Nov (the same date as the Comment on Malaysiakini), so it probably just wasn't there when he made the video or posted the comment. So at least some improvement is being made.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Did the developers change the app on the same day, because as Fat Bidin's comment -- it's highly unlikely they're that efficient (and I mean <strong>vanishingly</strong> unlikely). They've have to compile, build, test and release a new version, while simultaneously hoping Exodus pick up their latest release and scan it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which brings me to my next point.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Spying doesn't suddenly make us competent</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I find it fascinating that many Malaysians believe that the Government is incompetent in everything -- except spying. When the topic of spying comes up, suddenly a sleepy, incompetent government bureaucracy kicks into hyper-efficiency.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Back in 2016, In the wake of the <a href="https://www.digitalnewsasia.com/tags/hacking-team">hacking</a> <a href="https://www.bfm.my/podcast/enterprise/tech-talk/tech-talk-are-we-being-spied-keith-rozario">team</a> breach, I've read hundreds of emails between Hacking Team and various government agencies procuring their spyware. And believe me -- it is rife with incompetence, just read <a href="https://wikileaks.org/hackingteam/emails/emailid/517498">this exchange</a> where they discuss basic home networking equipment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To reference more recent events, the MITI website crashed <a href="https://www.asiaone.com/malaysia/malaysian-government-website-crashes-over-100000-applications-reopen-businesses-flood">after only 100,000 applications </a>-- what more 13 million Malaysian users uploading their contact details?!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Of course, I'm not arguing we take comfort in incompetence, but we have to be realistic about what the government is trying to achieve. I'm no fan of the government, but I believe that many Government officials are just trying to do the best for Malaysia, with the limited resources they have. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And accusing them on abusing the MySejahtera application for spying, especially when there's no evidence -- isn't very effective in helping us combat this novel problem.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Efficacy of contact tracing</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I'm also not saying contact tracing is super effective, we've learnt that it o<a href="/uploads/documents/2020/11/national-contact-tracing-review-national-contact-tracing-review.pdf">report to the Australian cabinet</a> put it rather politely that <em>"There is <strong>scarce</strong> evidence on the effectiveness of digital or automated contact tracing."</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Ouch!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But a <a href="https://www.medrxiv.org/content/10.1101/2020.09.07.20189274v3.full">peer-reviewed study on Swiss Covid</a> (which uses the Google and Apple protocol) seems to suggest a contact-tracing app does indeed work. <em>(I must admit the maths in the paper is beyond me, so happy to be proven wrong)</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We're not sure what works, and what won't work. Novel problems require novel solutions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our best bet is to try things, and course-correct along the way. I'm sure mistakes will be made, but it's better than doing nothing. Countries that do nothing will fail -- look at America!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The richest country in the world, paralyzed by their own distrust of their government(s), make them unable combat the virus effectively. Ironic, that the country most likely to produce the vaccine is also the one least likely to have its citizens take it. And it's in COVID that we see the weakness of a decentralize systems -- all the countries (Malaysia included) that have had success in dealing with COVID have a strong central government calling the shots.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But if there's one thing we learnt in 2020, it's that Malaysian politicians are grimy slimeballs, something between a <a href="https://www.imdb.com/title/tt0118880/characters/nm0000518">"a cockroach and that white stuff that accumulates at the corner of your mouth when you're really thirsty"</a>. And obviously we can't let them call the shots without some checks and verification.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But we need to have a level of rationality about those checks, and perhaps even go so far as give them the benefit of the doubt in some cases, particular non-political government servants like D-G Hisham. Criticism for criticism sake, isn't the best solution for now.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In conclusion, the app looks OK, it'll be nice if they made it open-source though, although that doesn't guarantee anything, unless some <a href="https://www.schneier.com/blog/archives/2020/12/open-source-does-not-equal-secure.html">private third-party is willing to deep dive and audit the code</a>. Android apps have always been somewhat troubling, and MySejahtera probably is not that different. Governments the world over are trying new things, and we should cut them a bit of slack, because if we sit around and do nothing, we'll definitely suffer far worse.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>What you can do</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>As a last section of this post, I wanted to let Malaysians know you can actually turn of permissions for apps if you're worried about what they can do. You can still have the app on your phone, but at least you wouldn't grant the app access to specific access (like Wifi, Bluetooth, External storage) etc.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I'm not an Android user, but I guess you can use the following:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://support.google.com/googleplay/answer/6270602?hl=en">https://support.google.com/googleplay/answer/6270602?hl=en</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://support.google.com/android/answer/9431959?hl=en">https://support.google.com/android/answer/9431959?hl=en</a></p>
<!-- /wp:paragraph -->