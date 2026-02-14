+++
title = "Agents productivity vs. Quality"
date = "2026-01-12T14:14:37"
draft = false
categories = ['Misc']
+++

<!-- wp:paragraph -->
<p>This year, I managed to complete the entire problem set of <a href="https://github.com/keithrozario/advent-of-code">advent of code</a>. Last year, I could only complete 43 out of 50 problems. So there was ... progress!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you're unfamiliar, Advent of Code is a series of daily coding challenges released during the season of advent (the period just before Christmas). I encourage you to try these challenges for yourself. None of them are easy (at least to me), but all of them solvable with enough elbow grease and time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That said, the challenges are still contrived. Firstly, the questions are better written than a typical Jira ticket, yhey include a detailed description of what must be done, and sample inputs and outputs you can test. Secondly, the challenges extend beyond what most coders do on a daily basis, one challenge required writing code to ‘defrag’ a disk, another required building a tiny assembler that ran its own program, and multiple questions involved you navigating a 2D maze with obstacles along the way. All fun things you will probably <strong>not</strong> do as a programmer in the real world.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I tried the 2024 advent of code in March 2025 when I was between jobs, but this year I did it during the actual season of Advent -- and just 8 months gap between my first and second attempt, I actually improved quite substantially. The quality of my code improved and my approach as well. Still there was about 3 times during the challenges when code assistance actually helped me break out of a rut. Honestly, I would not be able to complete those challenges with AI guidance --- or a lot of rumination and thinking.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The typical way we measure 'agentic' value is through productivity. Doing something faster -- thereby having time to do MORE!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But, could we also measure agentic value through quality. Doing something better -- or solving a problem that would otherwise be unsolvable. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Cory Doctorow does his usual phenomenal job at describing it:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p id="92dc">If my Kaiser hospital bought some AI radiology tools and told its radiologists: “Hey folks, here’s the deal. Today, you’re processing about 100 x-rays per day. From now on, we’re going to get an instantaneous second opinion from the AI, and if the AI thinks you’ve missed a tumor, we want you to go back and have another look, even if that means you’re only processing 98 x-rays per day. That’s fine, we just care about finding all those tumors.”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p id="6017">If that’s what they said, I’d be delighted. But no one is investing hundreds of billions in AI companies because they think AI will make radiology more expensive, not even if it that also makes radiology more accurate. The market’s bet on AI is that an AI salesman will visit the CEO of Kaiser and make this pitch: “Look, you fire 9/10s of your radiologists, saving $20m/year, you give us $10m/year, and you net $10m/year,&nbsp;<mark>and the remaining radiologists’ job will be to oversee the diagnoses the AI makes at superhuman speed, and somehow remain vigilant as they do so, despite the fact that the AI is usually right, except when it’s catastrophically wrong.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p id="651c">“And if the AI misses a tumor, this will be the human&nbsp;<em>radiologist’s</em>&nbsp;fault, because they are the ‘human in the loop.’ It’s their signature on the diagnosis.”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p id="83cb">This is a reverse centaur, and it’s a specific kind of reverse-centaur: it’s what Dan Davies calles an “accountability sink.”&nbsp;<mark>The radiologist’s job isn’t really to oversee the AI’s work, it’s to take the blame for the AI’s mistakes.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://doctorow.medium.com/https-pluralistic-net-2025-12-05-pop-that-bubble-u-washington-8b6b75abc28e">https://doctorow.medium.com/https-pluralistic-net-2025-12-05-pop-that-bubble-u-washington-8b6b75abc28e</a></p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>In his article he details what he introduces the concept of Centaurs and Reverse Centaurs. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A Centaur is a human using AI to drive something that the human alone (in their limited human body and mind) would not be able to do. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A reverse centaur is an AI using the human to accomplish task (or take blame) where the AI cannot. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Unfortunately, in the industry today, we seem to be peddling reverse centaurs, a human in the loop is just code for "organic material checking for mistakes that the inorganic material made". Then takes the blame for it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The MRI analogy stuck with me -- why don't we think of AI as a enabler? Why don't we sell it this way? That a human with AI is going to improve the quality of their output -- and that increased quality may still comes with a decreased quantity. The trick isn't that AI makes things faster, or more 'productive' but that AI will help individual humans accomplish something they otherwise could not -- like spotting a rare tumour.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In Software Development this is a hard problem. We measure software by functionality, or by proxy metrics like lines-of-code, or code-coverage. We use these metrics as a stand in for measuring the real quality of the software because we have no definitive way to benchmark if one piece of code is 'higher' quality than another.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When it comes to code, the proof is in the pudding -- high quality software last.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And it last because it can be modified over and over again, while low quality software calcifies into stasis. Consider SQLite, which was first released in 2004, and had its latest release last month, more than 21 years on. The Linux Kernel goes even further back, and continues to churn out newer releases.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Compare that to your average ERP solution, where anything more than 15 years old is considered Legacy and is unable to take on new features -- necessitating a 'transformation'.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Writing good code takes time and takes skill. Gaining skill takes even more time. There is no compression algorithm for experience.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Developers who use code assistance like a Centaur, where humans use AI to help them achieve things they otherwise could not -- are the ones who benefit the most, and the ones who will go the furthest. They are the Radiologist who use the AI to check their work -- not the other way around.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Developers who use code assistance like reverse centaurs, where you give the AI one large problem statement, and you press the button to 'accept' are the ones who will regress. They are the accountability sinks on the AI, they are there merely to execute what the AI could not.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What kind of Centaur will you become?</p>
<!-- /wp:paragraph -->