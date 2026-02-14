+++
title = "Introducing potassium-40"
slug = "introducing-potassium-40"
date = "2018-12-20T21:38:27"
draft = false
categories = ['Misc']
+++

<!-- wp:image {"id":6573,"align":"left","width":187,"height":206} -->
![](/uploads/K-1.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Over the past few weeks, I've been toying with lambda functions and thinking about using them for more than just APIs. I think people miss the most interesting aspect of serverless functions -- namely that they're <strong>massively</strong> parallel capability, which can do a lot more than just run APIs or respond to events.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's 2-ways AWS let's you run lambdas, either via triggering them from some event (e.g. a new file in the S3 bucket) or invoking them directly from code. Invoking is a game-changer, because you can write code, that basically offloads processing to a lambda function directly from the code. Lambda is a giant machine, with huge potential.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What could you do with a 1000-core, 3TB machine, connected to a unlimited amount of bandwidth and large number of ip addresses?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's my answer. It's called potassium-40, I'll explain the name later</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>So what is potassium-40 </h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Potassium-40 is an application-level scanner that's built for speed. It uses parallel lambda functions to do http scans on a specific domain.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Currently it does just one thing, which is to grab the <code>robots.txt</code> from all domains in the <em><a href="https://umbrella.cisco.com/blog/2016/12/14/cisco-umbrella-1-million/">cisco umbrella 1 million</a></em>, and store the data in the text file for download. <em>(I only grab legitimate robots.txt file, and won't store 404 html pages etc)</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This isn't a port-scanner like nmap or masscan, it's not just scanning the status of a port, it's actually creating a TCP connection to the domain, and performing all the required handshakes in order to get the <code>robots.txt</code>file.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Scanning for the existence of ports requires just one SYN packet to be sent from your machine, even a typical banner grab would take 3-5 round trips, but a http connection is far more expensive in terms of resources, and requires state to be stored, it's even more expensive when TLS and redirects are involved!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which is where lambda's come in. They're effectively parallel computers that can execute code for you -- plus AWS give you a large amount of free resources per month! So not only run 1000 parallel processes, but do so for free!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A scan of 1,000,000 websites will typically take less than 5 minutes.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6574} -->
![](/uploads/prompt_results.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>But how do we scan 1 million urls in under 5 minutes? Well here's how.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Inner workings</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>You can download the code and try it yourself <a href="https://github.com/keithrozario/potassium40">here</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After installation you can run the <code>get_robots -n 800</code>script, which asynchronously invokes 800 lambdas, with each lambda requesting the <code>robots.txt</code> file from 1,250 sites.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After much testing, I learnt that the best way to rapidly invoke hundreds of functions at once is to first <strong>reserve</strong> the concurrency for the specific function, guaranteeing there's enough free executions in your account to accept the downpour of invocations. The tool uses multiple processes to invoke the functions which allow for all 800 lambdas to be invoked in ~20s (depending on latency)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The lambda's are invoked asynchronously, which means that the calling application (the script on your local machine) receives a 202 status almost immediately after invoking it, without waiting for the lambda to complete.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> Unfortunately, that means the output the function cannot be returned to the calling application. This is done intentionally to improve performance -- but it introduces many challenges which we'll go through later. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Boto3, which is the python SDK for AWS, uses a blocking function to invoke lambdas -- each invocation can only happen after the previous one has completed, some have tried to write their own custom asynchronous invocation call,  but I thought it best to stick with the official AWS SDK.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Next, within each function, we run 125 processes, based on some loose testing I did, 125 is the perfect number for a 1.2GB function. And yes, lambda functions can be <a rel="noreferrer noopener" aria-label=" (opens in a new tab)" href="https://aws.amazon.com/blogs/compute/parallel-processing-in-python-with-aws-lambda/" target="_blank">multi-process!</a> But not with the usual Queues or Pools that most are familiar with, instead we have to use <strong>pipe()</strong>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Note of caution, the code provided in the AWS blog <a href="https://aws.amazon.com/blogs/compute/parallel-processing-in-python-with-aws-lambda/">here</a> has an error -- if you pass a large enough object to the calling function, it **will** result in a deadlock condition, I spent hours troubleshooting this, till I found the solution <a href="https://stackoverflow.com/questions/23278788/python-pipe-send-hangs-on-mac-os">here.</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once all processes are initialized, the functions make their http requests using the python requests module. This is an extremely versatile module, that's purpose built for http-requests it's even recommended in the <a href="https://docs.python.org/3/library/urllib.request.html#module-urllib.request">python documentation</a> -- it's as close to an official module as one can get. We all need to be careful over what libraries/modules/packages we import into our code -- but I trust the requests package.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The biggest challenge was monitoring the functions. Because we request them asynchronously, we needed a way to check if each invocation <strong>has started</strong>, is <strong>in progress</strong> or has <strong>ended</strong>. To do this, we poll the CloudWatch logs for lambda invocations, to check the number of started and ended lambda invocations within a given time period, it's not very elegant, but gets the job done. If you know a better way, let me know -- please!!!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, each function places a json file into the s3 bucket, think of the bucket as temporary storage of the function's return result. The json file is a flat array of json objects that look like this: </p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>[{"domain_1": "abc.com", "robots.txt": "User-Agent:..."},</p><p>.......</p><p>{"domain_2": "def.com", "robots.txt": "User-Agent:..."}]</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p> Once all functions have finished, the script then invokes the <code>potassium40_compress_bucket</code> lambda function, that reads in all ~800 files from the bucket, consolidates them into a single file (by simply appending them to each other), compresses them back into a zip, and uploads the data back into the bucket.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Spending a fraction of cent to run this function that reduces the number of files and the size of the data, is worth the effort in lieu of downloading 800 uncompressed files. I spent some time engineering the function to perform all task in memory. Lambda functions have 512MB of disk space in the <code>/tmp</code> directory, but since this was a 3GB function, using memory would have been faster, but only marginally. I use 3GB to get the most CPU power, as AWS allocate CPU in proportion to the memory of the function.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In the end, a scan of 1 million websites would take less than 5 minutes, with the compression another 2 minutes after that. Hence, scanning 1 million websites, and grabbing their robots.txt file would take 7 minutes in total. Not bad!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Eventually you end up with an architecture that looks like this</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6612} -->
![](/uploads/ARCHITECTURE1.png)<figcaption>Architecture</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>But what about cost I hear you ask. Surely spinning up 1TB of memory within 800 different processes is going to break the bank. Well actually...</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Cost<br></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>So let's break this down, the most expensive cost is going to be running the lambda functions themselves, here's some metrics from a run I did earlier today:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6571,"align":"center","width":367,"height":290} -->
<div class="wp-block-image"><figure class="aligncenter is-resized">![](/uploads/duration.png)</div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>These were 800 lambda invocations, with an average duration of 35.2 seconds (the metrics are in milliseconds).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Each lambda by default is allocated 1280MB of memory. AWS charge $0.00001667 per Gigabyte-second of execution time, hence for 800 lambdas running an average of 35.2 seconds, the total cost would be:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1280/1024 <strong>GB</strong> * 35.2 <strong>Seconds </strong>* 800 <strong>parallel Lambdas </strong>* 0.00001667) = $0.60 </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AWS give you 400,000 Gigabyte-seconds per month for free, which means you can run this scan 10 times a month for free!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I limit each lambda function to 180 seconds of execution time, this will incur 1-2 errors, as some functions take an unexplainable amount of time. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Also some folks, basically kill robots by serving up large random content for every bot requests. This is bad etiquette as robots.txt is a file built for robots, but alas, we have to cope with this by sacrificing some them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This means we'd lose around results from 1-2 functions. But that's just 0.25% of the 800 functions that were invoked, many fast scanners like zmap are prepared to lose this level of accuracy at the price of speed, and so am I. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I might reduce the error rate, by allowing the function to run for the maximum 15 minutes -- by why double, triple, or quadruple my scan time just to increase the accuracy by 0.25%?!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Next, since S3 buckets charge per Gigabyte-Month, which is calculated as the average Gigabyte-hours per month, the total cost of using the bucket is actually a fraction of 1 cent per scan. I did the calculations, so trust me :)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Had we used DynamoDB, which would have been much easier to extract -- but we'd also have incurred about 40-50 times more cost. Sure it goes from 1 cent to 40 cents, but that kind of magnitude severely limits the scalability of the scan. In the future I may use DynamoDB, just to make this more manageable -- but again, why store the data in DynamoDB if we'd just dump it out into a zip file? Plus I'm not if DynamoDB could cope with a sudden surge of volume?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The last two cost are also quite irrelevant, which include the egress data out of the function (you pay for all http requests) and the cost of the Cloudwatch logs storage. Together they're less than 1 cent of charges as well (since incoming data is free!), and the outgoing requests is quite small.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So a scan of 1 million websites, would cost less than 60 cents, much less than a cup of coffee here in Singapore :)</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>It's a great way to end the year by making something you're proud off. I skipped a lot of details about the build, like how I used lambda layers for the first time, and how the <code>undeploy.py</code> script will actually delete even the Cloudwatch logs to leave your AWS account without a single trace of potassium-40 (it's radioactive after all). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Also, I run the scan on a randomized list of the cisco umbrella top 1 million, to avoid lumping domains by popularity or latency. Zmap run similar strategies to ensure each parallel process receives a representative sample.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Next year, I'm going to try to refactor the requests package out of the function and into it's own layer, giving me far more flexibility, plus maybe include DynamoDB.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>So why call it Potassium-40?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Lambda is symbol for the decay constant of radioactive isotopes, and potassium-40 is one such radioactive isotope . But what really seals the deal is potassium has the chemical symbol of <strong>K</strong>, which is both the first letter of my name, and the mathematical symbol for 1000 (albeit small k for kilo), which is the maximum number of concurrent functions per region that AWS allows.</p>
<!-- /wp:paragraph -->