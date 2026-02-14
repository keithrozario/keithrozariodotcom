+++
title = "Access Keys in AWS Lambda"
slug = "access-keys-in-aws-lambda"
date = "2020-06-14T17:55:51"
draft = false
categories = ["Keith's Favorite Post", 'Security &amp; Privacy', 'Serverless']
+++

<!-- wp:image {"align":"center","id":7164,"linkDestination":"media"} -->
<div class="wp-block-image"><figure class="aligncenter"><a href="/uploads/lambda-sts.png">![](/uploads/lambda-sts.png)</a></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Let's look at AWS Access Keys inside a Lambda function, from how they are populated into the function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html" target="_blank" rel="noreferrer noopener">execution context</a>, how long they last, how to exfiltrate them out and use them, and how we might detect an compromised access keys.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But before that, let's go through some basics. Lambda functions run on <a href="https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/" target="_blank" rel="noreferrer noopener">Firecracker</a>, a microVM technology developed by Amazon. MicroVMs are like docker containers, but provide VM level isolation between instances. But because we're not going to cover container breakouts here, for the purpose of this post we'll use the term container to refer to these microVMs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Anyway...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Lambda constantly spins up containers to respond to events, such as http calls via API Gateway, a file landing in an S3 bucket, or even an invoke  command executed from your aws-cli.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>These containers interact with AWS services in the same exact way as any code in EC2, Fargate or even your local machine -- i.e. they use a version of the AWS SDK (e.g. boto3) and authenticate with IAM access keys. There isn't  any magic here, it's just with serverless we can remain blissfully ignorant of the underlying mechanism. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But occasionally it's a good idea to dig deep and try to understand what goes on under the hood, and that's what this post seeks to do.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So where in the container are the access keys stored? Well, we know that AWS SDKs reference credentials in 3 places:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Environment Variables</li><li>The <code>~/.aws/credentials</code> file</li><li>The Instance Metadata Service (IMDS)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If we check, we'll find that our IAM access keys for lambda functions are stored in the environment variables of the execution context, namely:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>AWS_ACCESS_KEY_ID</li><li>AWS_SECRET_ACCESS_KEY</li><li>AWS_SESSION_TOKEN</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>You can easily verify this, by printing out those environment variables in your runtime (e.g. <code>$AWS_ACCESS_KEY_ID</code>) and see for yourself.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>OK, now we know where the access stored keys are stored, but how did they end up here and what kind of access keys are they? For that, we need to look at the life-cycle of a Lambda function...</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Access Keys in a Function</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Every lambda function starts as a piece of code stored within the Lambda service. When the function is first invoked, it undergoes a <strong>cold-start</strong>, which creates an execution context for that function before executing it. If the subsequent invocation occurs shortly after, Lambda re-uses that execution context, resulting a much quicker <strong>warm-start</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A cold-start involves finding some compute resource within the Lambda service, and creating the container to run our code within those resources. The warm-start simply reuses that container, and is therefore faster. But a cold start isn't a once-in-a-lifetime event, it occurs fairly often as Lambda purges old containers off the platform to make way for new ones.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7150,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/cold-start.png">![](/uploads/cold-start.png)</a><figcaption>Inspired by: https://www.twitch.tv/videos/647501563?t=00h07m51s</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>This picture was inspired by a wonderful talk from James Beswick linked <a href="https://www.twitch.tv/videos/647501563?t=00h07m51s" target="_blank" rel="noreferrer noopener">here</a>. But we still don't see any injection of access keys ... for that we need to dig into Cloudtrail logs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In Cloudtrail, we discover that a cold-start doesn't just create the container, it also creates an <code>sts:AssumeRole</code> and <code>logs:CreateLogStream</code> event. I don't know precisely where these events occur during the cold-start, but imagine it's something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7151,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/cold-start-full.png">![](/uploads/cold-start-full.png)</a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>We know from the logs that <code>sts:AssumeRole</code> is invoked by the Lambda Service, <strong>lambda.amazonaws.com</strong> (not the lambda container!). Here's a stripped down event from CloudTrail of the AssumeRole, notice the credentials expiration date against the eventTime, and also note that this call was made from lambda.amazonaws.com.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7158,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/assume-role-3.png">![](/uploads/assume-role-3.png)</a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The next event for this function is <code>logs:CreateLogStream</code>, which is executed from the lambda container using the newly minted access keys (from AssumeRole). Notice here we have an actual sourceIPAddress field and userAgent, but more importantly, we can see that the <code>userIdentity.accessKeyId</code> matches the key id from the previous event. Here's the event:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7159,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/CreateLogStream-1.png">![](/uploads/CreateLogStream-1.png)</a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><em>Strangely for my Python function this was executed by a Rust SDK user agent, suggesting it occurs even before the execution environment is setup</em>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It looks like the Lambda Service, gets Temporary Access Keys from STS, and injects them into the container during a cold-start. From there the container uses those credentials for everything it needs to do, not just creating the new logstream. Here's an example of the CloudTrail event of the same function Listing all Buckets in an account:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7160,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/ListBuckets-1.png">![](/uploads/ListBuckets-1.png)</a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>We can correlate them using the <code>$.userIdentity.accessKeyId</code> field, as they'll be the same across these operations. So we can know that a cold-start generates these temporary access keys, but how are these temporary credentials rotated?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Short answer is ... They Don't!</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Access Key Lifecycle</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>At least from my research, Lambda always requests for 12 hour tokens (which is the maximum duration possible). I've confirmed this from other content online as well, including <a href="https://youtu.be/H4WoQd2yVJQ">this</a> great talk from ServerlessDays Virtual. And because 12 hours is a STS limit (not Lambda) we see the same behavior for provisioned concurrent functions as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>My theory is that a Lambda Execution Context wouldn't last as long as the token, and hence tokens don't need refreshing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To test this theory, I created a lambda function that ran every 3 minutes, and kept it running for over 10 hours. The function performed one API Call that listed all the accounts S3 buckets, the actual call is irrelevant, it's purpose is to help us log the usage of the access key in CloudTrail.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Indeed, I found that the average lifespan of the container came in at just over 2 hours, far shorter than the 12 hour lifespan of the STS token. </p>
<!-- /wp:paragraph -->

<!-- wp:table {"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes"><table><tbody><tr><td><strong>Access Key ID</strong></td><td><strong>First Event</strong></td><td><strong>Last Event</strong></td><td><strong>Duration</strong></td><td><strong>Source IP</strong></td></tr><tr><td>ASIA-1</td><td>02:31:24</td><td>04:37:24</td><td>126 min</td><td>54.255.220.21</td></tr><tr><td>ASIA-2</td><td>04:38:46</td><td>06:40:24</td><td>122 min</td><td>18.140.233.226</td></tr><tr><td>ASIA-3</td><td>06:42:11</td><td>08:49:24</td><td>127 min</td><td>18.141.233.97</td></tr><tr><td>ASIA-4</td><td>08:52:24</td><td>10:55:24</td><td>123 min</td><td>13.251.102.127</td></tr><tr><td>ASIA-5</td><td>10:55:33</td><td>12:49:23</td><td>114 min</td><td>13.228.70.250</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>AWS are pretty coy about how long containers get recycled in Lambda, I think it's down to an algorithm that takes into account the current volume on the entire Lambda service in that region at that instant, and a some other metrics from your functions invocation history. Hence it's pretty unpredictable, which makes publishing any estimate very hard.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The important piece of information though is that once a Temporary Access Key is generated -- it is <span style="text-decoration: underline;">only used by the exact same IP for all future API calls</span>. There is a tight affinity between these Temporary Access Keys and IP addresses. I assume this is because once a container is created, it is assigned a static IP address that is never changed (but might be shared with other containers).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>From the CloudTrail logs, I see that everytime a new <code>sts:AssumeRole</code> event is called for the function, there is a corresponding <code>logs:CreateLogStream</code> event, and the next operation of the function uses the new Access Key ID <strong>and</strong> has a new source IP. All of this suggest the old container was recycled, and we went through a cold-start.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7165,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/ip-accesskey.png">![](/uploads/ip-accesskey.png)</a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Under normal conditions, an Access Key ID is never shared across multiple source IP addresses. So let's put this all together shall we.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Putting it all together</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>It's a bit hard to make conclusions based on reverse engineering log files, but I'll go out on a limb and say the following:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>An <code>sts:AssumeRole</code> call from the Lambda service is made during a function's cold-start</li><li>The assume Role generates a temporary access key with<ul><li>A new Access Key ID</li><li>A new Session Token</li></ul></li><li>The credentials are injected into the function's new execution context</li><li>The function then has the credentials it needs for API Calls</li><li>The function execution context will die before the credentials expire</li><li>The behavior is identical for provisioned concurrency function</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The temporary access keys are for the Execution Role of the function, which means they are limited to whatever the permissions the role has. Remember lambda functions have a function-policy and an execution-role, these define who can invoke the function and what the role can do respectively. For this, we're only interested in execution role.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So now we know where the access keys are, and where they came from. How do we exfiltrate them? That's actually an easy answer.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Any compromise on the function's code, that would allow <span style="text-decoration: underline;">access to the environment variables</span> would suffice, because that's where the keys are stored (unencrypted!). From there we could use a standard boto3 session to impersonate the lambda function from our local machine, or just about anywhere we could run an AWS SDK.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But is there a way to differentiate a legitimate API call from a lambda function vs. a malicious API call using these stolen access keys?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Maybe....</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Detecting Stolen Keys</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Here's a call I used from my Macbook using the STS tokens from a function:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7161,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/ListBuckets_CLI.png">![](/uploads/ListBuckets_CLI.png)</a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Looking through CloudTrail logs, only two fields differ between legitimate calls from Lambda vs. these malicious calls using stolen creds:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>sourceIPAddress</li><li>userAgent</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>UserAgent only differs I'm calling an API from my Macbook . But I'm certain this can tweaked (just like browser user-agents can be tweaked) which limits our ability to rely on this field as a detection method.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>sourceIPAddress is the most promising field, if we know that temporary access key was assumed by <code>lambda.amazonaws.com</code>, then we can assume that that access key should only be used by AMAZON IP addresses. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But attackers could simply load credentials into a lambda container, and evade detection -- fortunately, there seems some restrictions here.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because a temporary access key has a tight affinity to an IP address, we can be certain that if we <span style="text-decoration: underline;">detect an access key that was assumed by <code>lambda.amazonaws.com</code> running on multiple different IP addresses</span>, that's a good sign we need to start worrying.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But after we detect it, there's the problem of fixing it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Revoking stolen keys</h2>
<!-- /wp:heading -->

<!-- wp:image {"align":"center","id":7167,"sizeSlug":"large","linkDestination":"media"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><a href="/uploads/revoke_keys.png">![](/uploads/revoke_keys.png)</a></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Firstly, let me say, I'm not a big fan of 'network' level protection for serverless -- the benefits don't justify the complexity. Serverless resources like DynamoDB, StepFunctions, and EventBridge don't support resource-based policies, and can't be restricted to specific VPC-endpoints like S3 or EC2. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can allow your VPC to connect to DynamoDB, but you can't limit DynamoDB to only your VPC. The only mechanism we have is IAM.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Plus stolen credentials from a function might look cool, but practically this has no value, after all if attackers have already compromised your lambda to the point of dumping environment variables -- chances are they don't need to exfill those credentials to poke around.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With those practical considerations in mind, we need two steps to fix this issue, the first is a pro-active measure to ensure function get its own IAM role, with scoped down permissions for only what the function needs to do. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This means that even if the access keys of a lambda function were compromised, the attackers couldn't do anymore damage, then they could have already done.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The second fix, is about addressing the problem of the specific lost key. For this we need to fix the compromised function <strong>first</strong> -- revoking any specific access key isn't going help, as the attackers could compromise the same function again to obtain newer access keys, just like a genie that grants more wishes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Assuming we plugged the hole in the function, we still have the issue of a 12-hour token, that (as we saw previously) can live long past the expiration of the function.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We can't revoke the temporary token itself, even if we knew the exact access key with ID, AWS doesn't have this capability (AFAIK). Instead, we could revoke the IAM Role that the token belongs to. This is tough, because revoking that role will damage all instances of your function as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Fortunately, if we use Serverless framework, and the <em><a href="https://www.npmjs.com/package/serverless-iam-roles-per-function" target="_blank" rel="noreferrer noopener">IAM-Roles-Per-Function</a></em> plugin, we can rename the IAM role of the function, and re-deploy the stack. This will invalidate the previously issued tokens (as the role would be deleted), and redeploy a new version of the function pointing to the new IAM role. Hence, we invalidate the old tokens, but keep our current function executing correctly.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7163,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/serverless-role.png">![](/uploads/serverless-role.png)</a></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To me, Lambda functions are the way future compute will be built around. We've just started this journey, and the hype train is on it's way. But just because AWS own the servers, doesn't mean we should remain blisfully unaware of what goes on under the hood.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What I've found is understanding how Lambda works (even though we're not orchestrating it) is a worthwhile investment of time, and helps me write better functions. Hopefully this post helped you to.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Note: The final solution depends on <code>sts:AssumeRole</code> returning a unique accessKeyID everytime. This might not be the case, as I see no guarantee of this anywhere in the docs, but from my practical testing this has always been the case.</em></p>
<!-- /wp:paragraph -->