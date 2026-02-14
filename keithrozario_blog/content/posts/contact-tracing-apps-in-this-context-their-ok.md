+++
title = "Contact Tracing Apps: they're OK."
date = "2020-05-10T16:46:28"
draft = false
categories = ["Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

<!-- wp:image {"align":"center","id":7074,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="/uploads/Screen-Shot-2020-05-10-at-10.56.10-AM.png" alt="" class="wp-image-7074"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>I thought I'd write down my thoughts on contact tracing apps, especially since a recent BFM suggested 53% of Malaysians wouldn't download a contact tracing app due to privacy concerns. It's important for us to address this, as I firmly believe, that contact tracing is an important weapon in our arsenal against COVID-19, and having 54% of Malaysians dismiss outright is concerning.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But first, let's understand what Privacy is.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Privacy is Contextual</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Privacy isn't secrecy. Secrecy is not telling anyone, but privacy is about having control over who you tell and in what context.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, if you met someone for the first time, at a friends birthday party, it would be completely rude and unacceptable to ask questions like:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>What's your weight?</li><li>What's your last drawn salary?</li><li>What's your age?</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>In that context you're unlikely to find someone who will answer these questions truthfully.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Age and weight, are perfectly acceptable questions for a Doctor to ask you at a medical appointment, and your last drawn salary is something any company looking to hire you will ask. We've come to accept these questions as OK -- under these contexts.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You might still not want to answer them, which might mean you don't get the job, or the best healthcare -- but you certainly can't be concerned by them. Far more people will answer these same questions truthfully if you change the context from random stranger at a party to doctors appointment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So privacy is <strong>contextual</strong>, to justify concerns we have to evaluate both the context and the question before coming to a conclusion.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So let's look at both, starting with the context:</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>What's the Context</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The context is, we have a highly contagious virus spreading through society that threatens to over-load our health care system and kill millions of people.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>These extraordinary times allow for extraordinary measures. I'd like the Government to stay out of my social interactions, but I'd also like our Hospitals to continue working. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Contextually, it's reasonable (and even expected) of the government to ask questions of us. Especially if the sole reason is to assists in contact tracing. So what are the questions they're asking?</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>What's the question</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The question is slightly different depending on which Contact Tracing protocol you'll be using, but let's look at BlueTrace and Google+Apple's contact tracing.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>BlueTrace</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Singapore's BlueTrace protocol doesn't really ask it's users anything. Instead only those found to be infected have their contact data uploaded to central servers -- and only after a manual process of interviewing the patient do authorities contact "<a href="https://bluetrace.io/static/bluetrace_whitepaper-938063656596c104632def383eb33b3c.pdf" class="aioseop-link">individuals as-sessed to have a high likelihood of exposure to the disease</a>"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So infected individuals upload their anonymized contact data to the a central server -- that central server, will de-anonymize those contacts down actual phone numbers -- that can be contacted by health authorities. Healthy individuals never upload their data to central servers (at least according to protocol specifications), and will only ever be called if they have been in close contact to a infected person (as you'd expect).</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>Google and Apple (GApple)</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>With Google and Apple (GApple)'s <a href="https://blog.google/documents/56/Contact_Tracing_-_Cryptography_Specification.pdf" class="aioseop-link">soon to be released contact tracing protocol </a>actually does ask a question of all it's users.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>Can you check if you've come into contact with this device, as it belongs to an infected person.</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>In their design, all users constantly download a list of "Diagnosis Keys", which contain the unique identifiers of devices belonging to infected users. Each user can then match up against a list of devices they've come in close contact with to determine if they're at risk. This matching occurs on the device, and never leaves it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Differences</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The key difference GApple and BlueTrace is that GApple shifts the onus for determining contact to the user's device and discretion. In contrast, BlueTrace requires a central server that will perform this action, and can de-anonymize the data (to a phone number), from where health authorities can reach out.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There are other differences as well -- such as how the unique keys are generated (and by whom), but these are minor differences and be ignored.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In both scenarios, the contact data of healthy users are never uploaded to a central repository directly -- data on your device remains on your device until (and unless) you are found to be infected.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Obviously as a techie whose political views border on libertarianism, I'd prefer GApple, but to be honest BlueTrace works for a country like Singapore, where trust in Government competence is extremely high, and generally they're both pretty OK&gt;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Having a central authority that knows who has be closed to an infected person has some pros, namely: </p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>It circumvents the problem of rogue patients, people who have are now feeling sick and know they've been in contact with an infected person, refusing to get tested, and continue to roam in public. <a href="https://www.scmp.com/week-asia/health-environment/article/3077497/coronavirus-cluster-emerges-another-south-korean" class="aioseop-link">Like that one lady in Korea</a>. </li><li>It can live across multiple devices, as you can re-register yourself. GApple's approach would be null and void if you'd lost your device.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>But at the same time, centralization has cons as well:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Raises privacy concerns for individuals that don't trust government</li><li>Centralized repositories can sometimes end up leaking very private data on thousands of citizens -- <a href="https://www.bbc.com/news/world-asia-47288219" class="aioseop-link">it's happened before</a></li></ul>
<!-- /wp:list -->

<!-- wp:image {"id":7073,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/uploads/Comparison.001.jpeg" alt="" class="wp-image-7073"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If you're looking for a conclusion on which one is 'better', the answer is nothing is perfect, but they're both OK. But both have significant drawbacks -- although that's not protocol specific.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>The real drawbacks</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>TraceTogether, the app that implements the protocol in Singapore, ask iOS users to <a href="https://tracetogether.zendesk.com/hc/en-sg/articles/360044846854-Does-TraceTogether-need-to-be-in-the-foreground-to-work-Can-I-use-other-apps-" class="aioseop-link">keep the app in the foreground</a>, something that's quite a big ask for most folks. We can at least confirm with Australia's COVIDSafe app that "<a href="https://risky.biz/covidsafeissues/">two iOS devices running COVIDSafe in the background <strong><em>do not</em></strong> exchange identifiers</a>."</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To be clear, this is a limitation of iOS, rather than a design choice of BlueTrace. The downside of GApple is that it doesn't exist yet, and while it's arrival is imminent -- it is as yet unavailable.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hopefully when GApple release their protocol, both issues will be resolved in one go.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>So the context is, we're under siege by an invisible enemy, and having contact tracing apps allow us one extra weapon in our combat against it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The question is only ever asked of infected individuals, and personal data of healthy individuals never leave their device. Whether it's BlueTrace or GApple they both seem to have taken privacy concerns seriously.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If this were 5 years ago, I guarantee you none of the privacy enhancing designs would even be a considered. These designs, while not perfect, are entirely reasonable and appropriate -- provided they're executed well!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And that is the crux, only if the Government executes this well, choosing either BlueTrace or GApple (don't roll your own!), and then ensuring that government agencies and not private <em>(politically connected)</em> organizations are running these systems, will the necessary trust be earned. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Importantly, Government will also have to open-source their apps, and subject them to 3rd-party scrutiny -- I know this is not common for Goverments, but if citizens are asked to do extraordinary things, so too must governments.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Government (especially in Malaysia) needs to earn the trust of the people, at the moment it has none! In order for this to be useful, that trust must be earned through transparency and honesty!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now ... let me speak from my heart ...</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Final words</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I was one of the first to <a href="https://www.digitalnewsasia.com/insights/what-malaysia-bought-from-spyware-maker-hacking-team" class="aioseop-link">detail</a> out the <a href="https://www.theedgemarkets.com/article/azalina-lied-about-not-buying-spyware-says-blogger" class="aioseop-link">Government's purchase of spyware</a>, and I created sayakenahack which was <a href="https://www.thestar.com.my/news/nation/2017/11/17/mcmc-blocks-sayakenahackcom" class="aioseop-link">later blocked by MCMC</a>. I'm no government shill.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Having privacy concerns is a good thing -- but we cannot dismiss outright the benefit of contact tracing apps just because we're "concerned". We owe it to ourselves (and to those around us), to at least investigate further the veracity of these concerns, and change course if the facts point us in another direction.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After digging in on these protocols, I see no reason to be overly concerned. It is irresponsible (and immature) to dismiss a contact tracing app even before execution. We at least owe ourselves that! </p>
<!-- /wp:paragraph -->