+++
title = "Securing Lambda Functions"
date = "2019-02-17T21:21:16"
draft = false
categories = ['Security &amp; Privacy', 'Serverless']
+++

<!-- wp:image {"id":6674} -->
<figure class="wp-block-image"><img src="/uploads/Dt7GO7aUUAAfgIc.jpg-large.jpg" alt="" class="wp-image-6674"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>First a definition.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A lambda function is a service provided by aws that runs code for you without the introducing the complexity of provisioning servers of managing Operating Systems. It belongs in a category of architectures called serverless architectures.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's a whole slew of folks trying to define with is serverless, but my favorite definition is this.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>Serverless means No Server Ops</p><cite>Joe Emison</cite></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>They're the final frontier of compute, where the idea is that developers just write code, while allowing AWS (or Google/MSFT) to take care of everything else. This includes H/W management, OS Patching, even application level maintenance like Webserver upgrades are not your problem anymore with serverless.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Nothing runs on fairy-dust though, serverless still has servers -- but in this world those servers, their operating systems, and the underlying runtime (e.g. Python, Node, JVM) are fully managed services that you pay per use. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As a developer you write some code into a function. Upload that function to AWS -- and now you can invoke this function over and over again without worrying about servers, operating systems or run-time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But how does AWS achieve this?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Before we can understand how to secure a serverless function, we need to at least have a fair understanding of how Serverless functions (like AWS Lambda) work. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So how does a lambda function work?</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>AWS Lambda: Under the hood</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This talk from re:Invent 2018 is an amazing intro into how lambda's work, and you need to watch it (if you haven't already).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Under the hood, every time a Lambda function is invoked, a container is spun-up in an AWS data center, with the memory &amp; compute capacity specified. The container is short-lived and exits after its task is complete or has exceeded its per-specified timeout.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That container runs in a VM running Amazon Linux (a derivative of RHEL6). The container itself has a few bits and pieces that you'd expect from a standard linux install, but not all of them. For example, it has OpenSSL but not Git, Wget or Curl. For a sub-set of what's available in the container view this <a href="https://gist.github.com/keithrozario/f525d4f51c97b4d2598eab447f2a70e5">gist here</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Go a bit deeper, and that the container has <code>/bin/bash</code> shell, and it's environment variables contain AWS credentials that are associated with the IAM role the lambda was assigned. This is important, so I'll repeat it, an AWS  function is a container with an IAM role, and the <span style="text-decoration: underline;">credentials to that role exists in the environment variables of the functions container.</span></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This container interacts with all other components via the AWS API. There is nothing special -- in fact, because lambdas have no persistent storage, it's only method of communicating with anything once invoked is via the network interface.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The only difference is the AWS credentials used for the calls are short-lived and automatically provisioned into the container at build-time. AWS rotates the credentials, but I'm unsure of the frequency of rotation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now while the container will terminate once the function has completed execution -- it will not entirely disappear. AWS keeps 'warmed-up' containers on standby just in case the function is invoked again. This speeds up the next invocation, avoiding a 'cold-start' problem.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AWS will invoke the exact same container, on the exact same VM, if it has a  chance to do so. This drastically improves the start-time of the function.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's important to understand this concept, as containers have disk space available in the <code>/tmp</code> directory. A recycled container will persist the data in <code>/tmp</code>even though it might be a different invocation, lambda will freeze connections and variables outside your main handler, which some folks use to improve performance, by <a href="https://www.jeremydaly.com/reuse-database-connections-aws-lambda/">re-using DB connections</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A re-used container will bring the contents of the <code>/tmp</code> directory and any variables outside of your handler function to a new invocation, so if you're writing data to disk in a lambda function, it's wise to wipe it clean before exiting. Even if not for security, you're still limiting the disk-space available to the next invocation. A cool trick I learnt is to use things like Pythons ByteIO write data from memory directly to files in S3 Buckets, never touching the disk on lambda.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6673} -->
<figure class="wp-block-image"><img src="/uploads/a-serverless-journey-aws-lambd-6011aa65-e55a-4cc5-96dc-6e76be2d4740-86362699-181130054549.jpg" alt="" class="wp-image-6673"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Also, AWS guarantee that the function is isolated from other functions at an OS level.No two functions (from even the same account) will run on the same VM, let alone two functions from different accounts. This provides a big level of isolation between functions even within the same account.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, by default Lambda Functions have access to the internet. If you want to limit their connectivity you'll have to deploy them onto a VPC.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now let's focus on Security.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Security on Lambda Function</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let's start at the end -- this <a href="https://www.darkreading.com/cloud/securing-severless-defend-or-attack/a/d-id/1333078?">madman</a> intentionally published <a href="http://www.lambdashell.com/">Shell Access </a>to his lambda function online, and even gives you a GUI for write shell commands directly into his AWS account (<a href="http://www.lambdashell.com/">lambdashell.com)</a>. It's been there since Oct-2018 (making it nearly 4 months now) and no one has managed to cause any serious damage.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sure, some folks managed to <a href="https://www.darkreading.com/cloud/securing-serverless-attacking-an-aws-account-via-a-lambda-function/a/d-id/1333047?page_number=1">delete his webpage </a>using over-privileged functions, and others managed to mine some crypto (albeit at 3 seconds per invocation) -- but this only happened <strong>after</strong> he intentionally introduced some loose permissions to his setup.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With default settings, even with an RCE vulnerability on a function has limited damage potential. The most serious exploit came from denial of wallet attacks, where attackers were creating thousands of Cloudwatch logs, or filling them up with useless garbage.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Lambda functions aren't perfect, but they have much smaller attack surface than EC2 instances. With limited memory, space and run time -- it's much harder to leverage a potential lambda vulnerability than something similar on an EC2. A shell on EC2 would be mining crypto-currency all day long and could probably run things like wget and curl to run more payloads.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So here's a few quick tips to hardened up the Lambda function:</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>De-serialization &amp; Vulnerable depedencies</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":6677} -->
<figure class="wp-block-image"><img src="/uploads/Screenshot-2019-02-17-at-9.18.28-PM.png" alt="" class="wp-image-6677"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The most popular way of getting an Remote Code Execution on a lambda function is via Deserialization attacks or vulnerable dependencies. Neither of these are exclusive to serverless architectures of course, but avoid using things like Pickle (Python), serialize (Java/PHP), Marshal (Ruby) or <strong>eval()</strong> and you've covered ~80% of the RCE potential of your code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And maybe you don't use pickle, but you may use Numpy that uses Pickle. Just last month, <a href="https://tools.cisco.com/security/center/viewAlert.x?alertId=59492">a vulnerability in numpy was found over the way it used Pickle</a>. So be clear over what dependencies your code runs on, and what further dependencies those introduce. For python, something as simple as having a free service like GitHub or Pyup scan your requirements.txt files can alert you to these issues.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I prefer to keep dependencies such as external packages (like requests) and binaries (like Git &amp; ffmpeg) into layers. Layers make dependencies much easier to manage, and provide a easy way to report on which functions use which dependencies. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Just  these two things help significantly reduce the exposure a lambda has.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Lock down IAM &amp; Resource</h2>
<!-- /wp:heading -->

<!-- wp:image {"align":"left","id":6678} -->
<div class="wp-block-image"><figure class="alignleft"><img src="/uploads/IAM-1.png" alt="" class="wp-image-6678"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Each lambda function has an IAM role, the credentials for which are in the container it runs on. If an attacker retrieves the credentials out of the function, they can use those credentials for everything the role permits.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If the function had access to write to your DynamoDB, or read sensitive files on S3, bad things will happen.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Avoiding de-serialization and vulnerable dependencies allow us to reduce the likelihood of losing those credentials in the first place, but we should also limit each function to just the permissions it needs. This is a bit of a chore, but with plugins for frameworks like <a href="https://medium.com/@glicht/serverless-framework-defining-per-function-iam-roles-c678fa09f46d">serverless-iam-roles-per-function</a> it's a one-time high value operation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This way, a vulnerability in one function can't assume the role of another, and it's likely you'll have many IAM roles, each with limited value, spread across the application, making any one vulnerable function less damaging. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The alternative is of one giant IAM role shared by all functions, making a vulnerability in any function result in serious damage, regardless of what the function does.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Also make sure your other AWS resources are locked down. Lambdas don't exist in a vacuum, they typically have access to DynamoDB, S3 buckets etc, ensure those resources (especially S3) are set to private as much as possible, and accessible only by your account. Why bother with hacking lambda if the S3 bucket is exposed to the internet?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, sticking with the principle of least privilege, lambda functions have access to the internet by default. If that's not needed, deploying them onto a locked-down VPC improves security even more, but this security step is quite tedious for most, a lambda in a VPC does introduce some complexity.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But that complexity ensures the attacker can't retrieve code from the internet, but has to inject it via the parameters passed to the function -- hopefully this will make them easier to sanitize or detect.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Monitoring Logs &amp; Detection</h2>
<!-- /wp:heading -->

<!-- wp:image {"align":"left","id":6679} -->
<div class="wp-block-image"><figure class="alignleft"><img src="/uploads/cloudwatch.png" alt="" class="wp-image-6679"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Lambda's by default come with Cloudwatch logs, that log high level stats of the function, and anything additional you've logged from your code. Unfortunately, the logs don't provide OS level details like CPU utilization or shell commands (since this is serverless), but they do provide maximum memory usage and duration of the function.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So in the scenario where an attacker has managed to manipulate your function, monitoring logs is probably the best way to detect any compromise.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And now, with <a href="https://aws.amazon.com/about-aws/whats-new/2018/11/announcing-amazon-cloudwatch-logs-insights-fast-interactive-log-analytics/">cloudwatch insights</a> which lets you run pseudo-SQL queries on all your logs it's even easier to pick out outliers for further analysis. The best thing about insights is that you don't need to download the logs, the query is run 'in-place' while the logs are still on AWS.  The bad news it that the queries cost money, and are directly proportional to the size of your logs you're querying.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you suddenly see a spike of lambda functions running longer than they should, or using more memory than usual -- or even just odd exceptions that are showing up in your logs (stderr is captured onto logs), it might be time to take some hard manual analysis</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Unknown unknowns</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Of course, all of this is premised on the traditional view of, attack a web-app, get a shell, priv-esc or laterally move across the network.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's kinda hard to laterally move when the function kills itself every few seconds <em>(lambda has a 15 minute limit, but API Gateway imposes a 29-second limit)</em>, and even harder to priv-esc when the containers run on the latest OS and kernel version (AWS manages this, not you!)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But maybe in this new serverless world, new attack paradigms will emerge. If data exist in S3, RDS or even Cloudwatch logs, why bother getting a shell if you can access that data via some other means. Lambda's also persist data both in <code>/tmp</code> and  variables outside the handler -- there's definitely an attack vector there, made worse by the fact that few know it even exists.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It helps that AWS offer VM level isolation across functions, but that's based on firecracker which is still relatively new.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It'll be exciting to see what emerges over the next 2-3 years as more applications move to serverless, and it starts becoming main-stream enough to merit the attention of real-world attackers, and not just researchers.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>It's just a good time to be serverless.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Honorable mention</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Puresec has a product called <a href="https://github.com/puresec/FunctionShield">FunctionShield</a>, which is 'sort-off' AWS plugin that allows you limit the functionality of the lambda function. The 'plugins' are language specific but are usually just imported packages, that allow you to code statements in function that prevent the function from writing to <code>/tmp</code>, accessing the internet, and even disable child process execution. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because it's a statement into your function, you have very fine-grained control over what you code can do where -- i.e you can limit writing to <code>/tmp</code>only at specific points of your code, so that an attacker gaining RCE in the earlier points of your code has less to leverage on. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's a great idea, but I'm no so certain that the solution to securing lambda is adding one more imported package/dependency into your code. That being said, this does give you flexibility above and beyond what most other solution offer, plus the solution logs data to cloudwatch which helps in monitoring and detection.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Other resources:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><a href="https://github.com/OWASP/Serverless-Top-10-Project">OWASP Serverless Top 10</a></li><li><a href="https://github.com/OWASP/Serverless-Goat">Serverless Goat </a>(similar to WebGoat)</li><li><a href="https://github.com/OWASP/DVSA">Damn Vulnerable Serverless App</a> (similar to DVWA)</li><li><a href="https://www.insomniasec.com/downloads/publications/Deserialization%20-%20%20What%20Could%20Go%20Wrong.pdf">Introduction to Deserialization</a></li><li><a href="https://github.com/alestic/lambdash">LambDash</a> (shell in a Lambda Function)</li><li><a href="https://github.com/puresec/FunctionShield">FunctionShield</a> (locking down lambdas)</li><li><a href="https://www.jeremydaly.com/securing-serverless-a-newbies-guide/">Newbies guide to securing lambda</a></li><li><a href="http://www.lambdashell.com/">LambdaShell.com</a> (lambda shell exposed to the internet)</li><li><a href="https://www.darkreading.com/cloud/securing-serverless-attacking-an-aws-account-via-a-lambda-function/a/d-id/1333047?page_number=1">Attacking lambdashell</a> (write up on attacking lambda shell)</li><li><a href="https://www.youtube.com/watch?v=QdzV04T_kec">AWS Lambda Under the Hood</a>  (video from re:invent 2018)</li><li><a href="http://Peeking Behind the Curtains of Serverless Platforms">Peek behind the curtains on serverless platforms</a></li></ul>
<!-- /wp:list -->