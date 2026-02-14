+++
title = "Logging within AWS Lambda Functions (python edition)"
slug = "logging-within-lambda-functions"
date = "2020-04-30T19:14:18"
draft = false
categories = ['Serverless']
+++

<!-- wp:paragraph -->
<p>This post covers how to perform logging within AWS Lambda. Lambda has built-in integration to Cloudwatch logs, making it a default choice for logs, but the way a distributed system like lambda performs logging, is quite different from how you'd do in a monolithic app.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For the brave folks still reading this -- let's dive in.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Lambda Logging: 101</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>When building lambda functions, it's always a good idea to sprinkle logging statements throughout your code -- particularly in areas where something important happens. This is just generally good advice regardless of whether you're using Lambda.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And Logs aren't just for troubleshooting, they're used for metrics, tracing, and information capture. In this post though, we'll focus on using logs to give us visibility on specific Lambda invocations to triage issues.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Unfortunately, log statements by themselves are useless, in order for them to be valuable, they need to appear somewhere accessible. You can have the most generous log statements known to mankind -- but it still won't help you, if those logs are locked up in an inaccessible container.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Lambda has no SSH capability, so you can't just log out to files -- because those files will be inaccessible. But it does have in-built cloudwatch logs integration, which makes shipping logs to Cloudwatch far easier compared to EC2 or Fargate. It literally is 2 lines of code in Python to setup.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Better still Cloudwatch Logs requires no configuration to setup, can be viewed directly from AWS console, and is a purely serverless offering. For more detailed analysis, you can ship them off to your 3rd-party tools, like your own ELK stack, but today we'll explore just how far we go with native tools in AWS like Cloudwatch Logs and Cloudwatch Insights.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Note: <code>Cloudwatch Logs</code> is a service that is distinct from <code>Cloudwatch</code>. Do not confuse the two to be same thing -- it isn't even referenced with the same service name in boto3 (<code>logs</code> vs. <code>cloudwatch</code>)</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Log Hierarchy</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you've ever used Cloudwatch you'd notice these things named LogGroups and LogStreams, and initially they can seem confusing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A LogGroup is a single 'partition' within Cloudwatch that captures data, and LogStream is a sub-partition within that group that actually stores the individual log messages. Within frameworks like Serverless Framework, the default behavior is to create a LogGroup per Lambda function.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Each LogGroup will then have multiple LogStreams -- with each LogStream corresponding to one <a class="aioseop-link" href="https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html">Execution Context</a>, the more parallel executions you spin up, the more Execution Contexts get created, and the more LogStreams you have in that LogGroup.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>LogStreams, like the name implies, are streams of log messages, arranged in chronological order, with a clear delineation between each request. The overall relationships looks like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7127,"sizeSlug":"large"} -->


![](/uploads/log_relationships.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>And on the console it looks like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7125,"sizeSlug":"large"} -->


![](/uploads/log_groups.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If you're troubleshooting this one issue that occurred for that one customer back in May, drilling to the specific <strong>request</strong> is the place you want to quickly get into -- as they are the actual events leading up to the issue in question. And in this post, we'll delve into how to do that.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><strong>Side Note:</strong></p><p>Choice of Framework is important. Serverless framework does this by default without the user even seeing it, but tools like Terraform require you to work through the verbosity of creating individual logGroups, and then assigning the right permissions, <code>logs:CreateLogStream</code>, and <code>logs:PutLogEvents</code> to the underlying functions. With Terraform modules this isn't a monumental task, but it's still undifferentiated heavy-lifting.</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>With that intro, let's look at how we can configure our Logging within our Lambda Functions...</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Logging in Python</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To setup logging within a Lambda function use the following code snippet:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7110,"sizeSlug":"large"} -->


![](/uploads/logger_example.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If you ran the code above in a Lamba Function, you'd get the following logs in cloudwatch (I removed some superfluous data)</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7118,"sizeSlug":"large"} -->


![](/uploads/log_output-1.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Obviously the Debug error wasn't displayed, because the log setting is set to <code>INFO</code>, but the logs do still look verbose as they contain the standard log format, which is a tab delimited text made up of the following four fields.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Level</li><li>Time(isoformat) in milliseconds</li><li>AWS_REQUEST_ID</li><li>Log Message</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>But reading flat-lines of text aren't ideal for analysis and consumption. Can you imagine parsing through 10,000 lines of this. Instead let's try to change the format of the logs to something better like JSON, which will give us some sane structure.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 id="TL-DR">AWS Lambda Powertools</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To log out in JSON from within AWS Lambda simply use <a class="aioseop-link" href="https://github.com/awslabs/aws-lambda-powertools">AWS Lambda Powertools.</a> The tools allows us to add the ability to log out in structured JSON with just two lines of code (well 3 if you count the decorator):</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7108,"sizeSlug":"large"} -->


![](/uploads/logging_aws_powertools.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Once you're logging out in JSON, half the battle is won. We've now got some structure that we can search within. We'll soon see how to query these logs, but before that let's explore the functionality power tools offers us.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Firstly, we can set log level via an Environment Variable, rather than within the function:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7121,"sizeSlug":"large"} -->


![](/uploads/carbon-2.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>This allows to change the log level without redeploying functions. It only works though, if you've already pre-added these debug log lines throughout areas of your code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can dynamically set a percentage of your logs to <strong>DEBUG</strong> level via env var <code>POWERTOOLS_LOGGER_SAMPLE_RATE</code>. This will dynamically set a percentage of your requests to DEBUG, meaning any issues in production will already have a ready population of DEBUG logs to be consumed without any redeployment. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Fortunately, AWS Powertools is also available as a Lambda Layer from <a class="aioseop-link" href="https://github.com/keithrozario/Klayers">Klayers</a>, so including it into your functions is as simple as pasting an ARN into the AWS Console. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But, as we said writing out logs is half the battle. Reading them is where we really see how powerful structured logging is.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Reading Logs</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The benefit of structured logging boils down searching rather than reading. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By default, Cloudwatch can perform simple text based searching on logs from either LogStream or entire LogGroup, but when you structure your logs, you're able to search individual fields within those logs with high granularity. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We can do this from within the AWS console or your tool of choice, but because the real magic is in the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html" rel="nofollow">powerful filter and patterns</a> available via default in Cloudwatch.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, querying for <code>{$.level = "WARNING"}</code> gives us all the <strong>WARNING</strong> messages in a log group, or <code>{$.level = "WARNING" || $.level = "ERROR"}</code> gives us both <strong><strong>WARNING</strong></strong> and <strong>ERROR</strong> messages. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7101,"sizeSlug":"large"} -->


![](/uploads/Screen-Shot-2020-05-30-at-12.24.23-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>But looking at a standalone error message isn't helpful, we'd like to see the events leading up to the error. Fortunately, if you refer to screenshot above, each log message is also populated with a "function_request_id", which corresponds to the request in question. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now we're in business.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because if we search for just the request id, we can filter down to the specific lambda invocation that caused the error, and inspect the entire log messages from start to finish for just that single request. In this example we simply search for <code>{$.function_request_id = "b959bd9a-edd4-4e02-94e5-15379a31479c"}</code> :</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7102,"sizeSlug":"large"} -->


![](/uploads/Screen-Shot-2020-05-30-at-12.26.26-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The major downside though, is if we have a uncaught exception, they tend to bypass the structured log output and print out non-JSON lines in the tab-delimited manner we saw earlier. However, we can still search for them by simply searching for <code>"[ERROR]"</code>. From there, because we have a timestamp, and logStream, we can manually drill into the event. Less elegant, but still workable. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7103,"sizeSlug":"large"} -->


![](/uploads/Screen-Shot-2020-05-30-at-12.31.12-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Before we move onto querying across multiple LogGroups, it's always good practice to let the Lambda execution 'die', i.e. do not catch the exception and return, but allow the function to exit with an error code. This allows us to use tools like Lambda Destinations &amp; Cloudwatch metrics to alert us on catastrophic issues, which would otherwise be hidden from view.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Another thing that's easy to lose sight off, is that we don't have a log server anywhere for this. Access to Cloudwatch logs can be controlled via IAM Roles (just like everything else on AWS), and we only pay for what is stored &amp; searched in Cloudwatch. We can also set the log retention period to purge older logs out of the system so they stop costing money. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In other words, a highly scalable, minimal over-head solution, with no added servers or credentials to manage -- which is pretty powerful straight outta of the box.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So far so good, but what if we wanted to query across multiple CloudWatch log groups? If we needed to triage an issue in an application, but didn't know which function was causing it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Cloudwatch Insights</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Cloudwatch insights allows us to do similar search functionality, but across multiple Log Groups. Think of this as an application level log query tool.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By default, each cloudwatch log record will have a <code>@message</code> and <code>@timestamp</code> field. Modifying the format of the log output, changes the format of the <code>@message</code> field (it still exist). But if the format of the message is JSON, then cloudwatch <strong>automatically</strong> provides the ability to query on fields <strong>within</strong> @message by specifying just the field name.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, we can query all error logs from across multiple log groups using the following syntax</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7122,"sizeSlug":"large"} -->


![](/uploads/carbon-3.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>To the keen observer, this looks very similar to SQL Select queries, and indeed it is -- but there's still a small-ish learning curve. It's not super quick or efficient, but it gets the job done, without servers or separate 3rd-party tools.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Coming soon</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>More mature logging would enable us to specify correlation ids, across multiple Lambda functions performing task for a specific user request or transaction. This allows us to log at a transactional level, instead of individual lambda request, which is probably Holy Grail territory for a lot of folks.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Unfortunately, I'm not smart enough to do this, but it's something Powertools might look to do in the <a href="https://twitter.com/heitor_lessa/status/1267423951480856577">future</a>! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Begrudgingly, this tooling exist for Javascript, which is still king when it comes to Lambda functions, but Python ain't that far behind.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>So to conclude on how to log within python functions in AWS Lambda:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Use AWS Lambda Powertools to log out in structured format</li><li>Be Judicious with your 'INFO' logging (and sensitive), but also ensure you have DEBUG logging ready-to-go if you need them</li><li>Ensure the Logging Level (INFO, DEBUG) is not hard-coded into the function, but set as an environment variable which can be changed when you need to.</li><li>Set the <code>POWERTOOLS_LOGGER_SAMPLE_RATE</code> to ensure we have debug logs at some percentage.</li><li>Use Cloudwatch to query your logs, and cloudwatch insights for more wider search.</li><li>Set the right retention period for your logs to reduce cost</li><li>If you need more, consider 3rd-party tools which will include alerting/monitoring, but it's always preferable to choose a SaaS solution than standing your own.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Proper logging might seem like a waste of time -- but trust me, when it saves you hours of agonizing troubleshooting, you'll never go back to not logging ever. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But what most developers do, is over-compensate by logging out everything -- without any control, which makes analyzing logs a chore. The balance is ensuring we log out sufficient information (by setting the right log levels), and then having tools to comb through that info (using Cloudwatch insights) to us to quickly triage issues and gaining the most from our logs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once you get hang of it, a combination of cloudwatch logs, cloudwatch insights, and AWS Lambda Powertools, allows us to do effective and efficient logging within our functions, with minimal overhead in a completely serverless way.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Additional Reading</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To learn more, the following references are useful:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><a href="https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html">The python context object in Lambda</a></li><li><a href="https://stackoverflow.com/questions/50233013/aws-lambda-logs-to-one-json-line">Logging JSON in python</a></li><li><a href="https://www.denialof.services/lambda/">Deep Dive into a Lambda</a></li><li><a class="aioseop-link" href="https://github.com/awslabs/aws-lambda-powertools">AWS Lambda Powertools</a></li><li><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html">Filter Pattern Syntax for Cloudwatch</a></li><li><a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html">Cloudwatch insights query</a></li><li><a href="https://github.com/awslabs/aws-lambda-powertools-python">AWS Lambda Powertools | Github</a></li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Final Credit</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The wonderful <a href="https://twitter.com/heitor_lessa">@heitor_lessa</a> has been working on Powertools, which itself was inspired by other tools from the community. While core serverless tools are rarely Open Source (since they're tied to vendors), there's still a lot of Open Source initiatives in and around serverless -- and a wonderful community that's growing alongside it as well.</p>
<!-- /wp:paragraph -->