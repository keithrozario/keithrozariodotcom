+++
title = "govScan.info now has DNS records"
slug = "govscan-info-now-has-dns-records"
date = "2018-10-15T01:36:30"
draft = false
categories = ['Misc']
+++

<!-- wp:cover-image {"url":"https://www.keithrozario.com/wp-content/uploads/Screenshot-2018-10-15-at-1.34.14-AM.png","id":6532} -->
<div class="wp-block-cover-image has-background-dim" style="background-image:url(https://www.keithrozario.com/wp-content/uploads/Screenshot-2018-10-15-at-1.34.14-AM.png)"><p class="wp-block-cover-image-text">DNS Queries on GovScan.Info</p></div>
<!-- /wp:cover-image -->

<!-- wp:paragraph -->
<p>This post is a very quick brain-dump  of stuff I did over the weekend, in the hopes that I don't forget it :). Will post more in-depth material if time permits over the weekend.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>govScan.info, a site I created as a side hobby project to track TLS implementation across <code>.gov.my</code> websites -- now tracks DNS records as well. For now, I'm only tracking MX, NS, SOA and TXT records (mostly to check for dmarc) but I may put more record types to query.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>DNS Records are queried daily at 9.05pm Malaysia Time (might be a minute or two later, depending on the domain name) and will be stored indefinitely. Historical records can be queried via the API, and documentation has been updated.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading {"level":3} -->
<h3>Architecture of the DNS Queries</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I want to spend some time walking through the architecture of DNS querying on GovScan.info, DNS queries are almost a separate distinct aspect of the site that I can draw the architecture of the DNS queries independently from other functions of the site:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6531} -->
![](/uploads/latest_architecture1.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The architecture might look a bit daunting, but we can break it down into easier to understand components. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Beginning from the top of the diagram, the lambda function <code>get_hostnames</code> reads a <a href="https://github.com/keithrozario/list_gov.my_websites">GitHub repo</a>, that contains the list of all domains to scan. The result of the read is stored in two separate .txt files in an S3 bucket. These files correspond to two API end points <code>/listFQDNs</code> and <code>/listDNs</code> respectively. <br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>However, that <code>get_hostnames</code> is only invoked when there is a change to the Repo itself, and for that I use a GitHub Webhook. The Webhook will post a change to the <code>/github</code> endpoint, which will trigger <code>get_hostnames</code>. This means that the two files in the S3 bucket will remain static until there is an actual push to the Repo. <br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You'll notice from the diagram that the GitHub webhook post to the API Gateway, and not via Cloudfront. This means that the webhook would post to a url that looks like this:<br/><code>https://xxx.execute-api.us-west-2.amazonaws.com/ProdNew/api/v2/github</code><br/>rather than this:<br/><code>https://govscan.info/api/v2/github</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The rationale for this is simply that CloudFront (at least via the GUI) did not give me the option to allow the POST method without also allowing for PUT, PATCH and DELETE, which are obvious security worries. Also, by using a the native API endpoint instead of the generic govscan.info, I'm able to hide my webhook url from the public.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6530} -->
![](/uploads/Screenshot-2018-10-15-at-1.06.15-AM.png)<figcaption>CloudFront Options</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Obviously we shouldn't rely on security through obscurity alone, so I used the recommended secret implementation for GitHub webhooks. With secret enabled, GitHub will sign the entire body of the POST method with a pre-shared secret. The signed value is provided in a HTTP header, and passed along with the message, this way the end point can verify that the POST message actually does originate from GitHub.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The next challenge is of course -- where to store the secret? The Lambda function that is invoked by the API should able to verify the signature, but to do that it would require the plaintext secret. I could store it in a S3 bucket, but I preferred to use AWS secret manager instead. It's a dead-simple API to call, and will allow me more flexibility for future secrets and control via IAM roles.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I manually generated a secret with openSSL, copied it into GitHub via the GUI, and stored it in secret manager via the AWS GUI as well (although there's no reason both of these actions can't be automated). When GitHub POST to the endpoint, the lambda will first retrieve the secret from secrets manager, and do a compare_digest between what it calculates and what was provided, if the digest match, it performs additional validation of whether the event from GitHub is a push. Only then does it invoke the<code>get_hostnames</code> function.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Note: GitHub were very adamant folks use compare_digest rather than the '==' syntax. Apparently, compare_digest is written in a way to prevent timing attacks on your function.</em> </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, we have to grant the functions the correct permissions. Fortunately this is quite easy to do with the Serverless Framework. It's an easy couple of lines to the yml file -- note I granted the function explicit permission to read just this one secret, and nothing else, applying the principle of least privilege.<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Moving on to the actual DNS queries. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The function <code>invoke_dns_queries</code> is scheduled (again via serverless) to run daily at 9pm Malaysian time. The function in turn will invoke <em>asynchronously</em> individual lambda functions to query each domain name. This means that each domain is being parallely queried, which allows me to query 613 domains in under 2 minutes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The functions then write back their results to a DynamoDB table that exposes it's data via the <code>/DNSHistory</code> endpoint.<br/></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The code is available via my GitHub <a href="https://github.com/keithrozario/Gov-TLS-Audit">repo</a>. I'll blog in more detail, specifically around the GitHub webhook which took me a while to build, and the lessons I learnt along the way.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The neat thing is that GitHub publishes the webhook calls from within their GUI, making it easy to troubleshoot and investigate issues. It also gives a nice green feeling for when everything works:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6532} -->
<figure class="wp-block-image">![](/uploads/Screenshot-2018-10-15-at-1.34.14-AM.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><br/></p>
<!-- /wp:paragraph -->