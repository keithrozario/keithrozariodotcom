+++
title = "Playing with files within the memory of Lambda function"
slug = "playing-with-files-within-the-memory-of-lambda-function"
date = "2020-04-18T11:40:14"
draft = false
categories = ['Misc', 'Serverless']
+++

<!-- wp:paragraph -->
<p>A lambda function is a like a little island, surrounded by network. Unlike Fargate containers, of EC2 instances, they do not have EFS, EBS or some other fast storage support. Everything that goes into a lambda, goes in via the network interface (and network only).</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7044,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2020-04-18-at-11.37.04-AM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>And hence, since Lambda's are ephemeral, everything going in and out of the lambda has to transverse that network 'moat'. And because they have no long-term storage, everything of value must be exfiltrated out the function's execution context, and onto something else (like S3)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is easy for HTTP requests or messages via SQS/SNS, but when dealing with files, the common tactic is to store them in <code>/tmp</code> for reading or processing. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7046,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2020-04-18-at-11.39.49-AM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>But a lesser known technique, bypasses the need for storing anything in the lambda <code>/tmp</code> directory. Instead it uses Python's inbuilt <a href="https://docs.python.org/3/library/tempfile.html#module-tempfile" class="aioseop-link">tempfile</a> module, to create temporary files in memory, that be read/process the files in place like so:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/7103036520b153cdeb41e269a4a88c50.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>This bypasses the need for <code>/tmp</code>, and the limitations of the directory's size (currently capped at 512MB). Since the file is loaded into memory, you get a larger capacity (though by not as much as you think).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Plus it actually incurs some additional complexity as well, because I'm not entirely comformtable coding <code>io.Bytes</code> and <code>io.String</code>, but generally speaking this does make your architecture neater at the expense of a couple lines of 'not-so-straigtforward' code.</p>
<!-- /wp:paragraph -->