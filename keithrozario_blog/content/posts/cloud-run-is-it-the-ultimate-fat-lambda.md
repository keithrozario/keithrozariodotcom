+++
title = "Cloud Run -- is it the ultimate Fat lambda?"
slug = "cloud-run-is-it-the-ultimate-fat-lambda"
date = "2019-11-18T22:39:07"
draft = false
categories = ['Serverless']
+++

<!-- wp:image {"id":6835,"sizeSlug":"large"} -->


![](/uploads/GoogleCloudRun.jpg)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Everyone knows that I'm a Lambda fanboy, and to be fair Lambda deserves all the praise it gets, it is **the** gold-standard for serverless functions. But yesterday, I gave Google Cloudrun a spin, and boy(!) is Lambda is going to get a run for its money.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which is surprising given Google has traditionally lagged in this area -- <em>isn't it quaint that we use words like 'traditional' in the serverless world! </em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But I digress.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Lambda equivalent in the Google world, is <strong>Google cloud functions</strong> ... which is (generously speaking) what lambda was 2 years ago-- pretty boring. The only advantage I saw it having over Lambda, was the ability to build python packages natively in the <code>requirements.txt</code> file. But that incurred a build during deploy, which in turn had a <a href="https://cloud.google.com/functions/quotas">limit.</a> </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And while, it did allow for a larger package size (double what AWS Lambda offers) it was severely more complex to understand. Just looking at it's <a href="https://cloud.google.com/functions/quotas">limit</a> and <a href="https://cloud.google.com/functions/pricing-summary/">pricing models </a>can make you dizzy. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In short, Google Cloud functions lacked the simplicity of Lambda, with little benefit for incurring all that additional complexity.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But Cloud Run is something else. It's still more complex than lambda, but here the trade-off seems worth it. So let's take a peek at Google's new serverless Golden Boy!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Containers vs. Functions</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In Lambda the atomic unit of compute is the <em><strong>function</strong></em>, which for an interpreted language like Python is just plaintext code uploaded to AWS. But in Cloud Run the atomic unit is the <strong>container</strong> -- and that can be a container for just the one function, or the container for the entire app itself -- with all the routing logic embedded within it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now why would you need apps for the serverless world?! You ask indignantly. Aren't these all supposed to be function based?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well actually lots of people have legacy code written at the application level, and re-writing an entire application takes a long time, and very rarely succeeds on the first try.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Functions vs. Apps</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Last month, I met Rich Jones, the creator of Zappa over at PyConSG. <a href="https://github.com/Miserlou/Zappa">Zappa</a> is a framework that allows developers to port existing web applications (written in Flask of Django) directly into Lambda. Effectively, turning the atomic unit of Lambda from <strong>function</strong> into <strong>application</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's a minor miracle what Rich did with Zappa (so miraculous in fact, that AWS straight up copied it to make a lesser known framework called Chalice!)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Zappa still doesn't create container -- but rather what we refer to as a 'fat' function, one big giant function, that mimics all the functionality of your entire application.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This isn't ideal, because now all your function invocations, run the same 'fat-lambda' that has 'fat-privileges', so you lose the <strong>modularity</strong> (<em>changing just one function and deploying it</em>) and <strong>granularity</strong> (<em>setting IAM roles and memory sizes at a function level</em>). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But you know what? Zappa has <a href="https://github.com/Miserlou/Zappa">9.9k stars on Github,</a> not because it "isn't ideal"  -- it's popular because it solves a real problem.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you have an existing app, you get much more value moving it lock-stock-barrel into lambda first, rather than trying to dissect it one function at a time. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because the moment you do the big-bang migration you stop worrying about servers (<strong>hooray!</strong>), and that's going to translate to instant recognizable savings on day one.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But trying to dissect an application into its constituent functions, means you'll worry about servers till the day that you pry that very last function from the cold dead hands of your monolith!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Fargate!! Fargate!! </h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Fargate doesn't quite cut it. Firstly, it's more complex than both Lambda and EC2 (significantly!) -- and the trade-off for all that added complexity is a platform that's more expensive and still doesn't scale to zero!! At least not for an API use-case.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But here's where Cloud Run comes in, it is a true scale down to zero container platform. It's effectively Lambda, but for containers. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>What's so special about containers</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Containers != Docker.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Think of them of as a super-power that allows you to create a single executable file out of any application (any application!). While they're used predominantly in microservices, its perfectly acceptable to package up a large monolith if you can, because this makes it easier to deploy and move across underlying hardware.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Containers are also an understood medium of communication, most people understand how to read a Dockerfile -- or at least can be thought to with little effort.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Lambda's are .... let's say ... exotic, in their packaging. For example, there's a lot going on when you're trying to package and external python package for lambda -- and understanding why and how these layers work make it difficult for first-time visitors to the rabbithole that is Lambda Environments.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Plus containers have a much larger package size, I managed to squeeze in a 700MB model file into a Cloud Run container, something that's impossible in Lambda until this day! (or at least impossible to my feeble mind)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, it's super easy to package an existing Flask, Django, Express, Spring... or whatever web service into a container, and then run it on Cloud run. This gives you all the advantage of scale down to zero infra, without a large amount of dissection needed.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There are some downsides though...</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Security in the cloud</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>With Lambda, AWS took care of everything from runtime down, you only worried about the application code and its dependencies. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Got a OS level patch to perform? No! AWS took care of it for me!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Got to fix your code for Meltdown or Spectre? No!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But in Cloud Run you now own the entire container, which includes the runtime and OS. OS level patches would probably require (at a minimum!) a re-build of the container. Which starts to place an additional burden on you -- the question is whether this burden is worth the price?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It depends. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For one, container security seems to be a hot topic, and you're probably already worrying about it (with or without Cloud Run). Just shout "I need container security" and no less than 100 sales folks will line up outside your office hoping to sell you their next shiny thing. And maybe 3 of those folks will have something working :)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Secondly, Cloud Run is still ephemeral, the container isn't long-lived, it's going to get killed eventually...which is still a better posture for you than a running VM.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The only downside, is that most of the folks running these fat-lambdas, are going to give it fat-privileges, which means the security of the entire container is only as good as it's weakest function...which is a bummer, but no worse off than you are today -- and I'd argue much better than a VM.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But containers aren't the only reason Cloud Run is worth this trade-off, because Google has a trick up its sleeve here, and it is a killer feature!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Concurrency ... the Lambda killer?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Cloud Run let's you serve multiple request from a single container. Which means a single container running flask (and some gunicorn process) is going to be able to serve mutliple http requests, just like in the real-world.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Effectively, you can serve 1, 10, 100 requests per container. Hence, fat containers can actually be more efficient than thin lambdas -- since one fat container incurs just one cold-start, while serving 100's of request in parallel.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This wasn't the case with Lambda, where there is a strict one event per invocation limit. So in order to process 1000 concurrent invocations, you'd need 1,000 Lambdas -- this is not the case for Cloud Run, which can theoretically do this with just 10 fatter containers. Surprisingly, for the large scale solutions -- this might actually turn out to be cheaper, as the slide below suggest:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6827,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2019-11-18-at-9.35.16-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>To be honest, all but 0.01% of use-cases would scale to the point where Lambda is unsuitable, but I think concurrency feature if freaking amazing! And probably opens the door for more tuning and enhancements.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I mean if you're going to create a fat-lambda, you might as well get concurrency. And this is the perfect fat-lambda :) </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Theoretically, you might also get away with returning a response to the request, while still doing work on the request through a sub-process call -- whether this is a good idea remains to be seen.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But you'd think Google would embrace the fat lambda paradigm and go all in -- but no, it's fallen short in the one area it should have pushed the advantage, CloudRun containers don't size up to Lambda!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Downsides</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Cloud Run containers get a fixed 1 vCPU, as opposed to Lambdas, which can go all the way to 1.67 vCPU. Then they only gets a max 2GB of RAM, a full 1GB less than Lambda, and probably insufficient for some usecases -- specifically the loading of large models for AI/ML execution. To be fair, even though lambda has a larger memory size, this is quite impossible to do on that platform as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is the error I got when trying to run the large Spacy Model on Cloud Run. At least I managed to package the model into the container. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6826,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2019-11-18-at-12.30.16-AM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Lastly, since it's containers, you have to build them. I built using Google Cloud Build and the experience was pretty great. But deploying just raw text into Lambda is far faster :) </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So prepare yourself for slower build times, and additional build steps.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you're building a brand new application, AWS Lambda and serverless functions are the way to go. They provide great modularity, and granularity across your new application, and will increase your velocity like crazy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But if you've got an existing application -- you could use tools like Zappa to encapsulate that into Lambda, but I think you're better off in Cloud Run.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>My thoughts at least...what are yours?</p>
<!-- /wp:paragraph -->