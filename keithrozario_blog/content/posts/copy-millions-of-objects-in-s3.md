+++
title = "Copy Millions of S3 Objects in minutes"
slug = "copy-millions-of-objects-in-s3"
date = "2019-04-16T23:44:02"
draft = false
categories = ['Serverless']
+++

<!-- wp:paragraph -->
<p>Recently I found myself working with an S3 bucket of 13,000 csv files that I needed to query. Initially, I was excited, because now had an excuse to play with AWS Athena or S3 Select -- two serverless tools I been meaning to dive into.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But that excitement -- was short-lived!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For some (as yet unexplained) reason, AWS Athena is <a href="https://aws.amazon.com/about-aws/whats-new/2019/03/athena_canada_central/">not available in us-west-1</a>. Which seemingly, is the only region in the us that Athena is not available on!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And.... guess where my bucket was? That's right, the one region without AWS Athena. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now I thought, there'd a simple way to copy objects from one bucket to another -- after all, copy-and-paste is basic computer functionality, we have keyboard shortcuts to do this exact thing. But as it turns out, once you have thousands of objects in a bucket, it becomes a slow, painful and downright impossible task to get done sanely.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For one, S3 objects aren't indexed -- so AWS doesn't have a directory of all the objects in your bucket. You can do this from <a href="https://medium.com/@daniel_38232/s3-indexing-and-querying-with-athena-dbed731560f2">the console</a> -- but it's a snap-shots of your current inventory rather than a real-time updated index, and it's very slow -- measured in days slow! An alternative is to use the <code>list_bucket</code> method. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But there's a problem with <code>list_bucket</code> as well, it's sequential (one at a time), and is limited 'just' 1000 items per request. A full listing of a million objects would require 1000 sequential api calls just to list out the keys in the your bucket. Fortunately, I had just 13,000 csv files, so this part for fast, but that's not the biggest problem!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once you've listed out your bucket, you're then faced with the monumentally slow task of actually copying the files. The S3 API has no bulk-copy method, and while you can use the <code>copy_object</code> for a file or arbitrary size, but it only works on one file at a time. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence copying 1 million files, would require 1 million API calls -- which could be parallel, but would have been nicer to batch them up like the <code>delete_keys</code> method.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So to recap, copying 1 million objects, requires 1,001,000 API requests, which can be painfully slow, unless you've got some proper tooling.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AWS recommend using the <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/UsingEMR_s3distcp.html">S3DistCP</a>, but I didn't want to spin up an EMR server 'just' to handle this relatively simple cut-n-paste problem -- instead I did the terribly impractical thing and built a serverless solution to copy files from one bucket to another -- which looks something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6705} -->


![](/uploads/s3-71-Architecture.png)


<!-- /wp:image -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Copy them with Lambdas</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Using a combination of SQS Queues and Lambda Functions, I'm able to distribute the load of those 1,000,000 api calls across a large number of lambda functions to achieve high throughput and speeds. The SQS queues help keep the whole system stable, by implementing retries and exception handling.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The program starts on your local laptop, where you send across 100 messages onto an listObjects SQS queue that invoke the list_objects function, which -- well, list the objects in the bucket.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>While listing out S3 objects is a sequential task, you can distribute that across 'prefixes' -- hence you can have individual lambda functions listing out all objects in a bucket that begin with the lower-case letter 'a', and another function for 'b', 'c' and so on. The 100 messages, correspond to the <a href="https://docs.python.org/3/library/string.html#string-constants">100 printable characters in ASCII</a>, there's a down-side to this approach which I explain later on in the post, but let's continue....</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If the keys in your bucket are random enough, the listing can be quite quick, as each prefix gets it's own process. In practice it took 3 minutes to list all 1,000,000 objects in a bucket spread across just 16 lambda functions (objects were limited to hexadecimal characters). If your bucket has a more diverse set of prefixes, this would be executed far quicker.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>While the lambdas are listing out the objects in our bucket, they also begin placing messages onto a separate copyObject queue -- before going back to list the objects. This means, objects begin to get copied before the bucket is completely listed (more parallelism = more speed!)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As there's no guarantee the listings would complete in the 900 second timeout window, we add additional logic for the function to invoke itself if it ever gets too close to timing out. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The function constantly checks how long it has to live (via the lambda context object) -- and would place a message back onto the listObjects SQS Queue with its current <code>ContinuationToken</code> and exit gracefully. The SQS queue would kick off another lambda, to pick up from the <code>ContinuationToken</code> but with a fresh 900 second window. You can see this illustrated as the re-invoke line on the diagram above, and here's a snippet of the code that actually does this:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/ea4c63ed056bab69399a34c1996eed67.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Later on I'll explain why we use queues instead of invoking the lambda recursively, but for now let's move onto the actually copying of objects.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The copy_objects function is invoked from the copyObjects queue. Each message has a total of 100 keys (default setting), which the function loops through and runs the <code>copy_object</code> method on. Fortunately, the method doesn't download the file to disk -- so even 128MB lambda can copy a 3GB file with ease, you just have to give it enough time to complete.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In practice we could copy 100 files in ~6 seconds, depending on size) and provided both buckets were in the same region. The real power comes from spinning up plenty of them in parallel, but even s3 has limits, so be careful.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I got 150 lambdas to give me a throughput of 22,500 files per second -- the maximum throughput of your s3 bucket is dependent on the number of prefixes (folders in S3 parlance) you have, spinning up too many lambdas will spit out too many exceptions because S3 will begin throttling you!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>All-in-all copying a million files from one bucket to another, took 8 minutes if they're in the same region. For cross-region testing, it 25 minutes to transfer the same million files between <code>us-west-1</code> and <code>us-east-2</code>. Not bad for solution that would fit easily into your free AWS tier. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To be clear, the files are tiny -- 4 Bytes each, but in general, even 100 large-ish files should be transferable in under 900 seconds.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The results look like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6706} -->


![](/uploads/Screenshot-2019-04-16-at-11.28.55-PM.png)


<!-- /wp:image -->

<!-- wp:heading -->
<h2>So why use a Queue</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>At this point it's worthwhile to ask why use an SQS Queue, when we can invoke the lambda directly. The answer, SQS can do the following :</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Gradual Ramp up</li><li>Re-try functionality</li><li>Exception Handling</li><li>Recursive Lambda invocation</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Using an SQS we're able to <a href="https://docs.aws.amazon.com/lambda/latest/dg/scaling.html">scale our lambda invocations</a> up in an orderly fashion, which allows our back-ends (e.g. DynamoDB or S3) to also scale up in tandem. Instantly invoking 800 lambdas to read an S3 bucket is a recipe for a Throttling and the dreaded <code>ClientError</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you ever get Throttled and the lambda exits, SQS can invoke a re-try based on a specific policy. Hence all lambdas get a chance to complete, with failed lambdas being retried, and completed lambdas having their messages removed from the Queue -- this is all amazing stuff, and yet another reason why SQS triggers for lambda's are the way to go.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Thirdly, SQS allows for wonderful exception handling -- if the message has been retried too many times, you can have it redirected to a <code>Dead-Letter-Queue</code>. This is where messages that have been retried too many times go to die -- in other words in a single place to view messages that failed to process.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, SQS allows for a more managed recursive invocation of a lambda. Rather than have the lambda call itself (and find yourself unable to control an infinite recursion) -- you can have the lambda simply put a message on a SQS queue that calls itself. The benefits are getting all the 3 points above, but also you can halt all lambas by simply purging the queue.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Caveats</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We spread the listing load, by listing all objects beginning with a certain character -- as a default we only consider the printable ascii characters.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This approach has a major drawback -- as S3 allows for objects to have names that begin with any utf-8 character (all ~1 Million of them!). This means that if you have objects that begin with ® or ø, the program won't pick them up. It's on my to-do list to solve this problem -- just not now.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The code is available on<a href="https://github.com/keithrozario/S3-71"> github here</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I think serverless is a perfect approach for <a href="https://en.wikipedia.org/wiki/Embarrassingly_parallel">embrassingly parallel</a> problems like this, and the combination of SQS Queues + Lambdas just make serverless solutions far more robust in terms of monitoring, exception handling and scaling.</p>
<!-- /wp:paragraph -->