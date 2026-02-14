+++
title = "Security Headers for Gov-TLS-Audit"
slug = "security-headers-gov-tls-audit"
date = "2018-07-08T22:00:56"
draft = false
tags = ['GovTLS', 'Malaysian Government']
categories = ['Malaysia', 'Security &amp; Privacy']
+++

Gov-TLS-Audit got a brand <a href="https://govscan.info">new domain today</a>. No longer is it sharing a crummy domain with <a href="https://www.keithrozario.com/2017/11/sayakenahack-com.html">sayakenahack</a> (which is still blocked in Malaysia!), it now has a place to call it's own.

The domain cost me a whooping $18.00/yr on AWS, and involved a couple hours of registration and migration.

So I felt that while migrating domains, I might as well implement proper security headers as well. Security Headers are HTTP Headers that instruct the browser to deny or allow certain things, the idea being the more information the site tells the browser about itself, the less susceptible it is to attack.

I was shocked to find out that Gov-TLS-Audit had no security headers at all! I assumed AWS (specifically CloudFront) would take care of 'some' http headers for me -- I was mistaken. Cloudfront takes care of the TLS implementation, but does <strong>not</strong> implement any security header for you, not even <code>strict-transport-security</code> which is TLS related.

So unsurprisingly, a newly created cloudfront distribution, using the reference AWS implementation, fails miserably when it comes to security headers.



![](/uploads/step_1_F.jpg)



I guess the reason is that HTTP headers are very site-dependant. Had Cloudfront done it automatically, it might have broken a majority of sites And implementing headers is one thing, but fixing the underlying problem is another -- totally bigger problem.

But what security headers to implement?<!--more-->
<h2>HTTP Security Headers</h2>
Mozilla have a great page on web security, with a <a href="https://infosec.mozilla.org/guidelines/web_security#web-security-cheat-sheet">cheatsheet</a> of things to do in a proposed order. The cheatsheet and my score for govscan.info (before I changed it) are here:
<ul>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#https">TLS Configuration</a> - <strong><span style="color: #0000ff;">Done</span></strong></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#resource-loading">Resource Loading</a> - <span style="color: #0000ff;"><strong>Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#http-redirections">Redirections from HTTP</a> - <span style="color: #0000ff;"><strong>Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#http-strict-transport-security">Strict Transport Security</a> <span style="color: #ff0000;"><span style="color: #000000;">-</span> <strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#x-frame-options">X-Frame-Options</a> - <span style="color: #ff0000;"><strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#csrf-prevention">Cross-site Request Forgery Tokenization</a> - <span style="color: #ff0000;"><strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#cookies">Cookies</a> <span style="color: #000000;">- Optional</span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#x-content-type-options">X-Content-Type-Options</a> - <span style="color: #ff0000;"><strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#contributejson">contribute.json</a> - Optional</li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#content-security-policy">Content Security Policy</a> - <span style="color: #ff0000;"><strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#cross-origin-resource-sharing">Cross-origin Resource Sharing</a> - <span style="color: #ff0000;"><strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#referrer-policy">Referrer Policy</a> - <span style="color: #ff0000;"><strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#x-xss-protection">X-XSS-Protection</a> - <span style="color: #ff0000;"><strong>Not Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#robotstxt">robots.txt</a> - Optional</li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#subresource-integrity">Subresource Integrity</a> - <span style="color: #0000ff;"><strong>Done</strong></span></li>
 	<li><a href="https://infosec.mozilla.org/guidelines/web_security#http-public-key-pinning">Public Key Pinning</a> - Optional</li>
</ul>
The list is arranged in priority order, with the highest priority actions at the top, so there was a lot of red for me, fortunately all of them was http headers, so it was a simple fix (sort of). In fact, I could fix all but one of the problems above by just setting the following headers:
<blockquote><code><strong>X-Content-Type-Options:</strong></code> nosniff
<code><strong>X-Frame-Options:</strong></code> DENY
<code><strong>X-XSS-Protection:</strong></code> 1; mode=block
<code><strong>Strict-Transport-Security:</strong></code> max-age=63072000
<code><strong>Referrer-Policy:</strong></code> no-referrer</blockquote>
The most difficult http header to tackle was the Content Security Policy. So before we go into adding http headers on Cloudfront, let's first understand what <code>content-security-policy is</code>.
<h2>Content Security Policy</h2>
There's a great many resources on Content Security Policies (CSP) from <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP">Mozilla</a>, <a href="https://content-security-policy.com/">content-security-policy.com</a> &amp; <a href="https://www.troyhunt.com/locking-down-your-website-scripts-with-csp-hashes-nonces-and-report-uri/">troyhunt</a>. It all boils down to this, a CSP is a directive to the browser on what resources are whitelisted for your website. It tells the browser, what scripts, images, fonts, etc can be loaded and which sources are permitted for these elements to be loaded from.

This prevents anyone from inserting images, scripts and even fonts directly on the page, because the CSP would not allow it. You can even set two CSPs on your site, one that will be enforced by the browser (will not load scripts, unless whitelisted by CSP) and one that will merely be reported by the browser -- a report will be sent to the endpoint for further screening.

At the end though, this was the CSP I settled on:
<blockquote><code><strong>Content-Security-Policy:</strong></code> default-src 'none'; script-src 'self' https://maxcdn.bootstrapcdn.com https://code.jquery.com; style-src 'self' https://maxcdn.bootstrapcdn.com; upgrade-insecure-requests; form-action 'self'; connect-src 'self' api.govscan.info; img-src 'self'; frame-ancestors 'none'; base-uri 'self'; https://cspgovscan.report-uri.com/r/d/csp/enforce</blockquote>
It might look confusing, it's basically a bunch of semi-colon delimited fields, which we can read last-to-first.
<blockquote>report-uri https://cspgovscan.report-uri.com/r/d/csp/reportOnly</blockquote>
This tells the browser to report all violations to the endpoint above. Report-Uri is a collaboration between <a href="https://twitter.com/troyhunt">troyhunt</a> and <a href="https://twitter.com/Scott_Helme">scotthelme</a>, and it's a great tool to get started for securing your site.
<blockquote>base-uri 'self';</blockquote>
This limits any <code>&lt;base&gt;</code> elements to origin. The <code>&lt;base&gt;</code> elements specifies the base url for all relative urls to use. There isn't a good reason for this to be anything other than origin.
<blockquote>frame-ancestors 'none';</blockquote>
This specifies valid parents that may embed on a page, since govscan.info has no embeds like tweets, or youtube videos, I didn't need this. So I set to 'none'. Note that this element doesn't fallback to <code>default-src</code>.
<blockquote>img-src 'self';</blockquote>
This tells the browser that all images should only be loaded from origin. i.e. all images on this site should only come from <code>govScan.info</code> and nowhere else.
<blockquote>connect-src 'self' api.govscan.info</blockquote>
The API on the site actually connects to <code>https://govscan.info/api/v2/</code> but just to future proof this, I decided to allow <code>api.govscan.info</code> as well. Changing a CSP on CloudFront using the method we're about to use is painfully slow (as we'll see).
<blockquote>form-action 'self';</blockquote>
All forms should only post to origin.
<blockquote>upgrade-insecure-requests;</blockquote>
Any requests from site should be upgraded to <code>https</code> instead of <code>http</code>. This will actually give you a performance boost if you have a lot of <code>http</code> requests, and obviously make those request more secure.
<blockquote>style-src 'self'  https://maxcdn.bootstrapcdn.com;</blockquote>
All css files should come either from origin or <code>https://maxcdn.bootstrapcdn.com</code>, since i use bootstrap's <code>bootstrap.min.css</code>.
<blockquote>script-src 'self' https://maxcdn.bootstrapcdn.com https://code.jquery.com;</blockquote>
Scripts should only be trusted from origin, maxcdn and code.jquery. Important to note, that the html on the page sources these scripts via https, anonymously, and using an integrity sha-256 check to ensure they haven't been manipulated.
<blockquote>default-src 'none';</blockquote>
Block everything by default unless explicitly mentioned here. Not all fields above will fallback to default, so you still have to hand-pick each field to be sure, but a default of 'none' is a good starting point.

Now how to add these headers to the page?
<h2>Lambda@Edge to insert http headers</h2>


![](/uploads/lambda@Edge.png)

The only way (I know off) to insert http headers into a S3-based website on AWS, is via the use of CloudFront + Lambda@Edge. You need CloudFront for custom domains with TLS anyway, and now you need an additional Lambda@Edge implementation to inject those http headers into the user response.

Amazon allow you to run Lambda@Edge at 4 possible points in time during a user request. The seemingly obvious place to inject them would be just before a response is sent to the user (viewer-response), but this is expensive as we'd need to run the Lambda functions at every user response.

The better place to run them is at origin-response, i.e. after CloudFront has retrieved the object from the origin, but BEFORE it has saved it to cache. This way your injected http-headers get pushed to cache, and your lambda function is no longer needed. It's faster, and less expensive -- although I'm still moaning over the need to run a lambda function to do this.

In the end, this is the JavaScript function that injects the headers into my site:
<script src="https://gist.github.com/keithrozario/ce9454de89e2e4c11e8a55a2180e664b.js"></script>

 
<h2>Testing your CSP</h2>


![](/uploads/using_burp.jpg)

However, origin-response is a pain to test, because any change to the CSP, requires that you redeploy the lambda@Edge functions (which aren't to deploy as their non-edge siblings), then wait for it to propagate across all edges <strong>and</strong> invalidate the cache. That's a lot of steps to test.

Instead, I found, running unit test with <a href="https://portswigger.net/burp">BurpSuite</a> to be easier. I initially considered spinning up an Apache webserver just to do this, but that would also require cert generation etc. BurpSuite also requires cert generation, but the process is pretty straightforward as the tool generates them for you already.

I found that by simply running a proxy, you can add a CSP http header to the response, to check if your CSP works. You don't even need to worry about looking at the browser console, as BurpSuite will intercept the outgoing post to your report-uri instantly, and you can view it on the same tool.

This allows you to quickly fine-tune your CSP, to get it out of 'unit-test' mode. This won't work if you've got 100's of pages to test with, but works pretty well for something like govScan.info, which only has a handful of pages.
<h2>Deploying Lambda@Edge</h2>


![](/uploads/implement_lambda@Edge.jpg)

Once you're OK with the CSP, and pretty confident if won't break. Create a Lambda@Edge function (remember it has to be in us-east-1/N.Virginia), and associate it with the CloudFront behavior.

Now, here's the tricky part, Lamdba@Edge requires a specific version of your function. Unlike regular lambda's that can reference <code>$Latest</code>, Lambda@Edge requires that you publish a version of the function, and use the published version.

Once you have a version of the function, you can then associate it with a CloudFront behavior -- remember, the function is associated with the CloudFront Behavior, not CloudFront distribution. A behavior is a path specific parameter, that specifies which origin CloudFront should reference, e.g. I have a behavior for <code>/api/v2</code> that sends traffic to an API Gateway, and a <code>/files</code> behavior that redirects traffic to an S3 bucket, and finally a <code>*</code> with takes all other traffic to a html file hosted on a separate S3 bucket.



![](/uploads/cache_behavior.jpg)



For the purpose of this exercise, I only embed the security headers for the site (and not the API) -- the API Gateway can use it's own lambda functions to provide the headers.

<a href="https://aws.amazon.com/blogs/networking-and-content-delivery/adding-http-security-headers-using-lambdaedge-and-amazon-cloudfront/">This is the best link on implementing security headers via Lambda@Edge</a>.
<h2>Modifying Lambda@Edge</h2>
But once you've got your http headers deployed, that's the only time you can test them against <a href="https://observatory.mozilla.org">Mozilla's observatory</a>, or scott helme's <a href="https://securityheaders.com">security-headers.com</a> and obviously you'll probably want to make changes.

There is a serverless plugin available to deploy lambda@edge, but the plugin deploys the function on new CloudFront distributions everytime, not modify existing ones. So for me that was a serious problem. Cloudfront distributions are one of the slowests things to deploy on AWS. So I decided to do this the old fashioned way -- by hand.

By first deleting the trigger old lambda function -- and then creating a new version of function, and repeating the previous steps. It's not just tedious and manual (3 button clicks) -- it's very very slow. The CloudFront distribution takes ~20 minutes to propagate and then you still need to invalidate the cache, another ~5 minutes before you can test.

Hence, try to test as much as possible using BurpSuite, and use this as a last minute tidy up.



![](/uploads/Deleting_Old_lambda.jpg)


<h2>Results:</h2>
Once all was done, and a couple iterative re-test, here's what I got.

![](/uploads/scan_A.jpg)



And of course, a few more tweaks (like <code>base-uri</code> and <code>frame-ancestors</code>) got me this on Mozilla's observatory -- which had no recommended changes for me <strong>(whoop!)</strong>



![](/uploads/scan_latest.jpg)



Not bad for a weekend's work.
<h2>Conclusion</h2>
As much work as putting a CSP together is, doing this early on in your project is far easier than doing it later. If you're thinking of starting a project today, make sure you implement a CSP as part of your 'hello world' phase. Trying to undo CSP errors later on is a nightmare.

If you've already got a project, putting a CSP together for a blog with 500+ post, and God knows how many embeds is going to be painful, but you can always start with very restrictive CSPs in report-only mode, and go from there (which is the recommended).

Now that govScan.info has a new domain, and spanking new domains, I'll be looking to do some robots.txt, security.txt and contributions.json files before finally biting the bullet and try to make it 100% serverless.