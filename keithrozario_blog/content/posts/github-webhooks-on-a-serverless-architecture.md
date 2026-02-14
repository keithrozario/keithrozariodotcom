+++
title = "GitHub webhooks with Serverless"
date = "2018-10-15T22:37:54"
draft = false
categories = ['Misc']
+++

<!-- wp:cover {"url":"https://www.keithrozario.com/wp-content/uploads/Step_3_Github_Webhook-1.png","id":6548} -->
<div class="wp-block-cover has-background-dim" style="background-image:url(https://www.keithrozario.com/wp-content/uploads/Step_3_Github_Webhook-1.png)"><p class="wp-block-cover-text"><strong>GitHub </strong>Webhooks <br>with Serverless</p></div>
<!-- /wp:cover -->

<!-- wp:paragraph -->
<p>Just because you have webhook, doesn't mean you need a webserver.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With serverless AWS Lambdas you've got a free<em> (as in beer)</em> and always on ability to receive webhooks callbacks without the need for pesky servers. In this post, I'll setup a serverless solution to accept incoming <code>POST</code> from a GitHub webhook.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>But first, let's understand what a webhook is.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Think of a webhook as a <em>reverse</em> API. A regular ol' <em>forward</em> API is something that exposes end-points for users to query (or post). This kind of API is completely passive, every action is triggered from the user-end. But sometimes you need the server-end to trigger events and push them back to you -- especially if only the server-end is aware of when those events occur in real-time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, I have a code repository on GitHub and want to trigger an action every time the repository is updated. In the past, I'd schedule periodic queries of the API to check for changes. And when I discover a change, I'll trigger a job to do some processing. This technique is called <span style="text-decoration: underline;">polling</span>, and while still widely used -- is sub-optimal.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For starters, we'd have to decide how often we'd like to poll. Poll too frequently, and we'd be wasting resources checking for changes that rarely occur, Poll too <em>infrequently</em>, and we could be out of sync for a long duration. Like I said, polling is sub-optimal.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6547,"align":"center"} -->
<div class="wp-block-image"><figure class="aligncenter"><img src="/uploads/untitled2.png" alt="" class="wp-image-6547"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There must be a better way.<br></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's called webhooks. A webhook is when an API goes active, and will actually <strong>push</strong> data your way. In the GitHub example, instead of me polling the GitHub API every hour, I could setup a webhook, so that GitHub will POST data <strong>to</strong> me at the moment the repository is updated. Thus no resources are wasted and no superflous API calls are made, the only time an API call is excuted is when there actually <strong>is</strong> a change.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But no such thing as free lunches, webhooks have a down-side. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When you query an API, all you have is code on an internet connected machine calling the API, But to receive webhooks you now need something to listen for it -- for 24 hours a day, 7 days a week. In the past, this would be a full-blown webserver, continuously listening for a webhook call-back, this is OK if you already have a web-server. But if you don't have one, spinning up a webserver, even if it's nicely package in a docker container, is an expensive solution for this small problem.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There must be a better way.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And again, there is! </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6544,"align":"center"} -->
<div class="wp-block-image"><figure class="aligncenter"><img src="/uploads/Step_1_Github_Webhook.png" alt="" class="wp-image-6544"/><figcaption>Webhooks</figcaption></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The solution is an API endpoint using AWS API gateway + Lambda. All a GitHub webhook needs is a place to make a <code>POST</code> message, and that's exactly the definition of an API. I already had an API running (all serverless-ly), so I just added an additional endpoint called <code>/github</code> that would receive the <code>POST</code> message and invoke a lambda function for processing. GitHub even lets you decide what events trigger webhook call-backs -- in my case only <code>push</code> events to the repo would callback the API. New comments on threads, new issues, or even wiki entries wouldn't call-back, and thus wouldn't waste resources.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A simple, and free way to receive GitHub webhooks, as AWS grants you 1 million GB-seconds of lambda executions per month. <br></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Problem solved or rather Solved-ish!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because now we have a security concern.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The API needs to be exposed to the internet -- How do we ensure a malicious actor isn't calling this function willy-nilly?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There must be <strong><span style="text-decoration: underline;">a</span></strong> way. And there is! It's a shared secret between GitHub and your Lambda</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6545,"align":"center"} -->
<div class="wp-block-image"><figure class="aligncenter"><img src="/uploads/Step_2_Github_Webhook.png" alt="" class="wp-image-6545"/><figcaption>Webhook with Shared Secret</figcaption></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>When you setup a Webhook on your GitHub repo, you can specify a secret. GitHub doesn't encrypt the messages in transit (but it will perform TLS on endpoints that support it) -- but if you specify a secret for the webhook, they'll go a step further and provide a signature value in a header for you to validate.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>From the <a href="https://developer.github.com/webhooks/securing/">documentation</a>, GitHub uses HMAC with SHA-1.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>HMAC is a keyed-hash fuction, which is a hash that takes in both the digest <strong>and</strong> a key, to generate the signature. It provides for both authentication <em>(this message really came from GitHub)</em> and integrity <em>(the message has not be corrupted or tampered with)</em> -- since a single bit change in either the key or the data would result in a different signature.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Note: I'm not 100% certain my terminology is right, but I use signature instead of just 'hash', as this is a keyed function. Some refer to it as hash-value, but it is stored in a header called <code>X-Hub-Signature</code></em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once you load a secret onto the GitHub webhook, it's easy for you to verify the authenticity of a message, by comparing the signature provided in the <code>POST</code>&nbsp; against the signature that you calculate on the receiving end. If they match, you can be sure the message has come from someone in possession of the shared secret -- hopefully that's <strong>only</strong> GitHub.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Note: GitHub go out of their way to recommend you use <code>secure_compare</code> or some equivalent function to prevent timing attacks. In my Python code I use the <a href="https://docs.python.org/3/library/hmac.html"><code>compare_digest</code></a> function from the hmac libary, which isn't much harder that coding a <code>==</code>, but is built specifically to prevent timing attacks</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Using a secret on the GitHub webhook solves for both the Authentication and Integrity problem.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Problem Solved? Not quite, now we have a new question -- Where to store the secret for our lambda.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If I hard-coded it into the code (code I publicly publish on GitHub) 
that wouldn't be secure at all. I could have opted to store it in an S3 
file, a file only the lambda could read, but that seemed very tricky, 
and hardly sustainable (versioning, and permissioning would be pretty 
nightmarish)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There must be a better way.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And the better way is using AWS Secrets Manager. You could use 
something like HashiCorp Vault, but there's no way I could figure out 
how to run that serverless-ly (is that even a word?) so AWS Secrets 
Manager it is!</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6546,"align":"center"} -->
<div class="wp-block-image"><figure class="aligncenter"><img src="/uploads/Step_3_Github_Webhook.png" alt="" class="wp-image-6546"/><figcaption>Using Secrets Manager</figcaption></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Secrets Manager (at least to me) is nothing more than a API for 
Key-Value store. But because it's an AWS resource, with an ARN, you can 
manage access to it via IAM roles. But that's not the magic -- after all
 files in s3 buckets have individual ARNs as well, and they also do have
 versioning, so why pay $0.40 per month for secrets manager?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First of all, the Secrets Manager API is far easier to call then an S3 file. Second, the Secrets manager API is <strong>extremely</strong>
 easier to update and rotate. It's not hard to imagine a script that 
would update both my GitHub WebHook secret, and my Secrets manager 
secret at the same time. Creating the same for an S3 file would not be 
hard -- but it wouldn't be easy to maintain. Truth be told though -- I 
was just excited to try out a new AWS offering... sue me!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's 2 drawbacks to secrets manager -- one is that it's not free. 
$0.40 per secret regardless of whether that secret is used or not 
(pretty high pricing). Second, it's region aware -- i.e a secret is 
stored not in a global instance (like S3), but a region specific store. 
Which is a bit painful, specifically when you're calling them from 
lambda's, but not a deal-breaker -- but you either have to replicate the
 store across regions, or hard-code the region into the api call.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So in conclusion.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Just because you have a webhook, doesn't mean you need a web-server.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>All you really need is a end-point capable of receiving HTTP messages, and that's what API Gateway + Lambda is. PLus it's free!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Building that is dead-simple, create an API end point capable of 
receiving POST messages, to trigger a lambda that does the processing on
 your end. But remember to secure that endpoint, obviously run it over 
TLS, but also make sure you do some form of authentication prior to 
execution. Generic Python lambda function that will process a GitHub 
Webhook, lookup a secret in AWS Secrets Manager, and then compare_digest
 the two is here.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Last minute Addition.</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Even though my API was exposed via a CloudFront distribution, I decided to point the GitHub webhook to the 'native' API Gateway uri. In AWS, every API Gateway gets a unique uri, which is then encapsulated as a CloudFront behavior. However, if you poss the data via CloudFront, you'll need to enable POST messages at the distribution -- which is OK, but I couldn't find a way to enable POST only, without enabling PATCH, PUT and DELETE as well. <br></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Post-Script</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="https://gist.github.com/keithrozario/adebb42ae53fa71a075648e4b1cfc05d">My code</a> that would validate a GitHub signature and invoke a lambda (you'll need to modify for your own usage)</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/adebb42ae53fa71a075648e4b1cfc05d.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph {"align":"left"} -->
<p style="text-align:left">Setting Up GitHub looks like this:<em> (make sure you use the right Payload URL and set the Content to JSON)</em></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6553} -->
<figure class="wp-block-image"><img src="/uploads/Screenshot-2018-10-15-at-8.51.47-PM.png" alt="" class="wp-image-6553"/></figure>
<!-- /wp:image -->