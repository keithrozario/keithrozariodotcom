+++
title = "What Challenge 13 taught me about LLMs."
slug = "what-challenge-13-thought-me-about-llms"
date = "2025-03-02T17:32:37"
draft = false
categories = ['Misc']
+++

<!-- wp:image {"id":7868,"sizeSlug":"large","linkDestination":"none","align":"center"} -->


![](/uploads/image-7-619x500.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>While doing programming challenges in Advent of Code, I came across an interesting behavior of LLMs in coding assistants and decided to write about it to clear my thoughts.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First some background.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Advent of Code is a series of daily coding challenges released during the season of advent (the period just before Christmas). Each challenge has 2 parts, and you must solve part 1 before the part 2 is revealed. Part 2 is harder than Part 1, and usually requires re-writes to solve. Sometimes quite extensive rewrites, and others they are small incremental steps.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you haven't done these challenges before, I encourage you to try. None of them are easy (at least to me), but all of them solvable with enough elbow grease and time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That said, the challenges are still contrived. Firstly, the questions are much better written that what you'd see in a Jira ticket or requirements document,. They include a detailed description of what must be done, and sample inputs and outputs you can test. Secondly, the challenges extend beyond what most coders do on a daily basis, one challenge required writing a small program to 'defrag' a disk, another required building a tiny assembler that ran it's own program, and multiple questions involved you navigating a 2D maze with obstacles along the way. All fun things you will probably <strong><span style="text-decoration: underline;">not</span></strong> do as a programmer in the real world.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I took on the challenges, both to improve my coding skills, and to learn how I could use coding assistants like in these <em>close</em> to real-world scenarios. The hope was I would gain some insight into how I could use these tools more effectively should I need to do something more than solving contrived programming challenges before Christmas.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>OK. Background complete.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's move onto the challenge that changed the way I would look at LLMs forever.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>There are 25 challenges in total, each consisting of 2 parts. Here is a summarized version of the first part of <a href="https://adventofcode.com/2024/day/13" target="_blank" rel="noopener" title="">Challenge number 13</a>:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>A resort has an arcade with claw machines.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Each machine has two buttons, A and B.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Button A costs 3 tokens, Button B costs 1 token.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Each button moves the claw a specific amount along the X and Y axes.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>To win a prize, the claw must be positioned exactly above the prize on both axes.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Each button can be pressed a maximum of 100 times.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Find the minimum number of tokens for each machine required to win the prize</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>And example scenario would be the following:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Pause for a moment and try to construct your strategy for solving this puzzle. Keep the mind the solution will require to solve quite a few of these machines.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Done? Ok, let's proceed.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This questions is especially beautiful because contains "hints" that are actually nefarious red herrings. But I don't want to spoil the fun, so let's go ahead and solve this.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because we know each button can only be pressed at most 100 times, hence there's only 10,000 possible combinations per machine. This might sound like a lot, but my 6 year old macbook did this easily. We can construct a simple brute-force solution like this.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/a5f10493fe9fa40773b64c1085fcf9e7.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>We iterate 100 pushes of button A, with 100 pushes of button of B, and find any solution that would get the claw to the location we wanted. Next we calculate the number of tokens required for those solutions, and print out the smallest of those token counts as our final answer.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Easy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But now let's go part 2. Which has a twist that makes it more difficult ... as always:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>You realize there is a unit conversion error in the position of the prizes</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>They're off by a factor of more 10 million</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Now instead of just 100 presses for each button, each prize will require more than 100 Billion presses</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Nested for loops aren't going to cut it here. Well they could, but you'd be looping through 10 sextillion (!!) iterations for each machine. I'm not a very good programmer, but even I know you should never consider nested loops for numbers that end with 'illion'.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Take a pause again, and think about how you might solve part 2. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The solution is simple once you realize this is a linear algebra problem, and quite a simple one at that.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We can see this on lines 9 and 10 of our initial solution. There are two equations with variables <code>a_pushes</code> and <code>b_pushes</code>, and since we have 2 variables and 2 linear equations, this is solvable. Personally I like the <a href="https://www.mathcentre.ac.uk/resources/uploaded/sigma-matrices8-2009-1.pdf" title="">matrices approach</a>, and Python conveniently has the numpy package, that solves this problem in one line.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/47cbc9fdc99271e68cd35f87e40af81b.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Much more performant. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Much more elegant. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Certainly better than the solution we wrote for in part 1.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But .... why did we come up with such a slow solution for part 1 in the first place? I think it was the last 2 lines of the instructions:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item {"style":{"elements":{"link":{"color":{"text":"var:preset|color|typology-acc"}}}},"textColor":"typology-acc"} -->
<li class="has-typology-acc-color has-text-color has-link-color">Each button will be pressed a maximum of 100 times.</li>
<!-- /wp:list-item -->

<!-- wp:list-item {"style":{"elements":{"link":{"color":{"text":"var:preset|color|typology-acc"}}}},"textColor":"typology-acc"} -->
<li class="has-typology-acc-color has-text-color has-link-color">Find the minimum number of presses for each machine to win the prize</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The first is what I call a pink herring. It helps you in part 1, but sends you wildly off course for part 2. Yes, for part 1 it helped us solve by guiding down the nested for loops, but this was completely untenable for part 2. Had the question <strong>not</strong> included a maximum number of presses, we might have gone straight to linear algebra requiring no rewrite for part 2.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The second is a particularly nasty red herring. This question only has 1 (and only 1!!) solution. There is no concept of minimum or maximum, because there is only ONE solution. Any code you wrote to choose a minimum from a list of possible solutions was completely and utterly unnecessary.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And here is where we talk about the LLMs in coding assistants.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First off, none of the LLMs in any of the assistants could solve this puzzle in one go (even just part 1). Some came close, requiring minimum tweaking to get it to work for part 1.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Secondly ALL the LLMs used the nested for loop solution like me in their first iteration.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ALL!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Without exception!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sonnet, GPT-4o and Gemini Flash.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That's interesting, that the LLMs fall for the same tricks that humans do. But then again, the red herrings 'prompt' the LLMs down a certain path, so we shouldn't be <strong>all</strong> that surprised.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7867,"sizeSlug":"full","linkDestination":"none","align":"center"} -->
<figure class="wp-block-image aligncenter size-full">![](/uploads/4617759902_d62819c715_w.jpg)<figcaption class="wp-element-caption">https://www.flickr.com/photos/jdhancock/4617759902</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If you grew up watching Star Trek like me, you know that Data, the Android on the Starship Enterprise is rational, emotionless, and super intelligent. Data wouldn't be tricked by this. These red herrings are more likely to trick a robot like C3P0, a bewildering buffoon whose code you certainly wouldn't trust.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I'm not saying the LLMs are like C3PO -- but they're certainly not like Data.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I prompted them again, to improve their code to make it faster:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>the solution is too slow, it times out because the real values, the number of presses can be in the millions. Is there a faster way to solve this?</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>And voila, all of them, manage to identify that this is a Linear Algebra, and surprisingly all 3 had different takes on how to solve them. Each solution worked in the end (after some tweaking), and the problem was solved. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But .... the LLMs still maintained the concept of minimum tokens. Either through the naming of the function/method. Or at least with one of them, it still checked for a minimum value. To me, this just means the LLMs never really 'understand' anything, even though they give off the impression of deep understanding.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Any human who understood linear algebra, would remove all mentions of 'minimum' in their code once they understood the problem. There is no minimum here, we should not mention it to improve our code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Code Assistants really did help me solve these questions faster -- but I think we need to be cautious of what help to accept. If you don't understand linear algebra, having the LLMs write out code that uses it would mean that you would be running code that neither you (nor the LLM) understood well. That's a recipe for disaster.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>LLMs are susceptible to trickery just like humans -- so how can we use them more effectively?</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">System 1 and System 2</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A framework I thought was useful to understand comes from psychologist Daniel Kahneman. If Psychology was football, Kahneman would be standing amongst Pele, Maradona, Messi and Ronaldo.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In his book, <a href="https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow" target="_blank" rel="noopener" title="">Thinking, Fast and Slow,</a> he mentions two systems in our brain that act almost exclusively and independently. Which he bestowed the unfortunate names of System 1 and System 2 (reading too much Cat in the Hat?)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>System 1 is responsible for quick judgments and decisions based on patterns and experiences.  .  It's responsible for automatic activities like detecting hostility in a voice, reading words on billboards, and driving a car on an empty road. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>System 2 is slower, more deliberate, and more logical. It's responsible for complex problem-solving and analytical tasks.  It's responsible for seeking new or missing information, making decisions, and logical and skeptical thinking. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The best way to illustrate this is from the Baseball and Bat question. I'm sure you've seen this before:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>A baseball and bat together cost $1.10. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The baseball cost $1 more than ball. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>How much does the ball cost?</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>The immediate answer that jumps into your brain is 10 cents ($0.10). But that is the wrong answer. Upon learning this is the wrong answer, most folks can slowly figure out that the correct answer is indeed 5 cents ($0.05). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The first answer of 10 cents, comes from System 1. It's always on, ready to go, and barrels in with an answer instantly. Once you're told this is wrong, your mind immediately kickstarts system 2, and system 2 may do a little algebra, or a quick calculation or two, and eventually end up with the correct answer of 5 cents. System 2 is not always on, it's a finite resource with expensive computational requirements, it needs does some sanity checks on System 1 -- and is only ever in full-drive mode when required.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>System 1 is easily fooled by red herrings, like find the minimum number of tokens in this problem with only one solution. System 2 is more deliberate and works of first principles -- it's the system that you start up whenever you tell yourself <em>"let's take a step back"</em>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Are LLMs purely System 1 automatons? </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well the question <a href="https://medium.com/towards-data-science/large-language-models-and-two-modes-of-human-thinking-1322160755e8" title="">has been posed before</a>, and initially (like in GPT3 days) the LLMs would fall for these tricks, but have since been improved. But have they improved to the point that actually are reasoning at a System 2 level? </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Or is it still just System 1 with guardrails that prevent them from making silly mistakes on very popular psychology questions? Are LLMs in coding assistants, purely system 1 automatons with hard-coded checks to make them look like System 2?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>All the models were able to correctly solve the linear algebra problem once prompted about the solution being slow. They correctly identified the problem, but only after being told to effectively ignore the '100 presses' condition. They still thought there would be a minimum token count (the other red herring we never prompted them to ignore). So red herrings work, until you explicitly tell the model to avoid it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In other words, the model has no way to figure out if it were a red herring, unless the user explicitly tells it to. It doesn't have a deep understanding of linear algebra -- or even just a high school level understanding of it. It's brain-dumping.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's a<a href="https://youtu.be/e049IoFBnLA?si=mn9E4tGS4QpFheG2" title=""> brilliant talk by Terrence Tao</a>, where he says this about the LLM models and how they help humans solve complex math's problems that really resonated with me:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>...they're not solving the problem from first principles, they're just guessing at each step of the output what is the most natural thing to say next. The amazing thing is sometimes that works, but often it doesn't</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Of course this talk was from GPT4 days, and perhaps things have changed, but I'm yet to see something that actually solves from first principles rather than trying to predict the next token. Just saying "explain your steps" isn't fundamentally changing the way the model approaches the problem. The underlying model operation is still passing input through a large complex network of vector calculations and getting an output, just because there is 'reasoning' doesn't necessarily mean there is understanding or building from first principles.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After all, System 1 works in about the same way as an LLM -- you don't start every conversation with a plan of action on where you will conclude, you just blurt out the words, and by the time you say something, the next thing pops into your mind and you say that ... ad infinitum, that's System 1.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>System 2 is deliberate writing, you start with something, refine it over iterations, ensure the message is clear, and only then publish it out. So can we use an LLM something knowing that's a sort of System 1 assistant?</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Challenge 23</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Challenge 23 helped me further clarify my thoughts. Part 1 of that challenge can be summarized as below:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>You're given a network map of computer connections</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Each connection is represented as two computer names joined by a hyphen (e.g., <code>kh-tc</code>)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Connections are undirected (order doesn't matter)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Task:<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>Find all sets of 3 computers that are fully connected to each other</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Count how many of these sets contain a computer with a name starting with 't'</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>I first attempted to solve this on my own, but with a twist. Recognizing that this was a Graph problem, I looked for popular Graph tools for Python (my programming language of choice). Initially I looked at <a href="https://cogdb.io/" title="">CogDB</a>, since it was the first search result that made sense. But I soon gave up, while it had promise, the project seemed to be somewhat abandoned.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Adter searching a bit more, I stumbled across this<a href="https://www.reddit.com/r/Python/comments/185xexg/what_are_the_best_libraries_to_work_with_graphs/" title=""> Reddit Post</a>, which suggested I use <code><a href="https://networkx.org/" target="_blank" rel="noopener" title="">networkx</a></code>. I did a little more digging and found rich documentation and a community around the package -- so I used it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After finding networkx, I used the coding assistants to help me write code for it, and in barely 20 minutes, I had managed to solve the challenge. The main logic was solved in under 3 lines of code. Most of the time spent researching the problem and possible solutions -- very little was spent actually coding.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What happened next was even more impressive. When Part 2 rolled out, the question then asks to find the maximum size of a clique. This was one extra line to my code. Because I had used an external package that was purpose built over many years to solve Graph problems. What would sometimes take massive re-writes, or performance improvements was solved in just one extra line here.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>More importantly, I didn't need the LLMs to generate large code blocks for me either, I was using code within a high quality package. There was little technical debt generated by this approach.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you asked the LLMs to solve the problem, they would all barrel down through System 1 and write nested for loops and massive if-else statements to solve it. Developers running on System 1 would do exactly the same thing -- start writing code for a problem the instant you see it. The problem here is that even if it solves the problem, now you've got 100s of lines of code to maintain and test and validate -- when an external battle-hardened opensource solution would have been far better.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><s>Good </s>Great developers, read a problem, understand the requirements, research possible solutions before they even write that first line of code (unless it's a space they're extremely familar with). Chances are you're not them, and just dumping this thing onto a LLM is definitely not the way to go. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Engage your system 2, pose the problem, and suggest possible solutions like an external package that you're confident will cover your use-case , and you'll get a much better solution, that is not only more elegant but more maintainable.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The human (at least for now) has to initiate the System 2 behavior. Think about how to solve the problem -- perhaps even take your time, knowing the actual coding part (where System 1 takes over) can be substantially automated and accelerated.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is all new to me, but I'm now getting the hang of LLMs. I'm not a professional coder, but manage to solve most of the Advent of Code Challenge with help from the coding assistants. Without the assistants I would not have been able to do it -- at least not in the same amount of time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>However, I think the best coders will always be the ones who work from first principles. Who are able to decline what the LLM offers, and guide it down the 'right' path of code. Everybody else is going to 'produce' hundreds or even thousands of lines of code from an LLM, most of which wouldn't make sense, and even if they work would be unreadable.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I shudder at a world where code is rewritten over and over again, and maintained in a million different places.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Coding assistants are here to stay. At $20-$30 a month, it's hard to find fault in them. Developers can cost anywhere from $300 - $3000 a day, the ROI for a coding assistant will be something in the order of 1 hour a month, or if you're really expensive, perhaps even 15 minutes a month. This will certainly pay for itself and more immediately.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>However ..... this isn't a case of free-ing up System 1 so developers can focus on System 2, because that's not what will happen. There's a reason System 2 isn't always engaged, it's expensive cognition, and a finite resource that has a max hours per day of usage. Just because you have time for System 2 doesn't mean it can be engaged. But, if developers know that the final writing code part of the solution can be accelerated, they can spend more time engaging the design phase of a problem, confident they'll hit deadlines with LLM by their side.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So....</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Be careful how you use them. Blindly accepting what an LLM outputs out is a recipe for disaster, so too is dumping them a question and hoping for a good solution. The solution has to be coaxed out of the LLM with you as the human being the System 2 thinker. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sure, someone posted on LinkedIn about how the latest LLM manage to compile a binary that accomplished everything they wanted in a single shot -- but there's millions of people using these assistants. One of them is certain to have that one in a million response -- do not expect that this is the norm. People only post exceptional things after all.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To consistently use LLM effectively requires some fine-tuning of the user to understand what the limitations of these things are, and how we can avoid the pitfalls that come with them.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Addendum</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I found this <a href="https://news.ycombinator.com/item?id=43340662&amp;utm_term=comment#43341506" title="">beautiful comment on YCombinator</a> that I absolutely had to include here as well:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>There's this concept in aviation of "ahead of or behind the plane". When you're ahead of the plane, you understand completely what it's doing and why, and you're literally thinking in front of it, like "in 30 minutes we have to switch to this channel, confirm new heading with ATC" and so forth. When you're behind the plane, it has done something expected and you are literally thinking behind it, like "why did it make that noise back there, and what does that mean for us?"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I think about coding assistants like this as well. When I'm "ahead of the code," I know what I intend to write, why I'm writing it that way, etc. I have an intimate knowledge of both the problem space and the solution space I'm working in. But when I use a coding assistant, I feel like I'm "behind the code" - the same feeling I get when I'm reviewing a PR. I may understand the problem space pretty well, but I have to basically pick up the pieced of the solution presented to me, turn them over a bunch, try to identify why the solution is shaped this way, if it actually solves the problem, if it has any issues large or small, etc.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's an entirely different way of thinking, and one where I'm a lot less confident of the actual output. It's definitely less engaging, and so I feel like I'm way less "in tune" with the solution, and so less certain that the problem is solved, completely, and without issues. And because it's less engaging, it takes more effort to work like this, and I get tired quicker, and get tempted to just give up and accept the suggestions without proper review.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I feel like these tools were built without any sort of analysis if they _were_ actually an improvement on the software development process as a whole. It was just assumed they must be, since they seemed to make the coding part much quicker.</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>I guess the best way to be 'ahead of the code' is the be the active human in the loop. Instructing the LLM while maintaining full control of what's happening. Asking the assistant to provide you hundreds of lines of code without knowing what choices/decisions were made will always put you behind the code.</p>
<!-- /wp:paragraph -->