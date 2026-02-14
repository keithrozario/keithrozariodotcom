+++
title = "Hosting a static website on S3 and Cloudflare"
date = "2018-10-03T23:34:57"
draft = false
categories = ['Misc']
+++

<!-- wp:cover {"url":"https://www.keithrozario.com/wp-content/uploads/cf-facebook-card.png","id":6507} -->
<div class="wp-block-cover has-background-dim" style="background-image:url(https://www.keithrozario.com/wp-content/uploads/cf-facebook-card.png)"><p class="wp-block-cover-text">Hosting an S3 site via Cloudflare</p></div>
<!-- /wp:cover -->

<p>From my previous post, you can see that I hosted a slide show on a subdomain on <a href="https://hitbgsec.keithrozario.com">hitbgsec.keithrozario.com</a>. The site is just a keynote presentation exported to html format, which I then hosted on an S3 bucket.</p>
<p>The challenge I struggled with, was how to point the domain which I hosted on Cloudflare to the domain hosting the static content.</p>
<p>The recommended way is to just create a simple CNAME entry and point it to the S3 bucket, but that didn't work because the 'crypto' settings on Cloudflare apply to the entire domain -- and not individual subdomains.</p>
<p>And since my website at www.keithrozario.com had a crypto setting of 'Full', the regular CNAME entry kept failing. I could have downgraded to 'Flexible' but that would mean my blog would be downgraded as well -- which wasn't ideal.</p>
<p>Why downgrade my main blog to accommodate a relatively unimportant sub-domain.</p>
<p>Instead found that the solution is to overlay a CloudFront Distribution in front of S3 Bucket -- and then point a CNAME entry to the Distribution.</p>
<p>The solution looks something like this:</p>

<!-- wp:image {"id":6508} -->
<figure class="wp-block-image"><img src="/uploads/cloudflare.png" alt="" class="wp-image-6508"/></figure>
<!-- /wp:image -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>And here's the steps:<br></p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Create a CloudFront Distribution using the S3 bucket as your origin</li><li>Enter the domain (in my case <code>hitbgsec.keithrozario.com</code>) as an Alternate Domain Name for the Distribution.</li><li>Set the default root object to <code>index.html</code></li><li>Set Viewer Protocol policy to <strong>redirect http to https</strong></li><li>Set Object Caching to customizable and set the minimum TTL to a ridiculously long number (this is a static site, cache very aggressively)<br></li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Once done. We merely take the domain name of the distribution (e.g. <code>dorwqk7jz5uyr.cloudfront.net</code>) -- and create a CNAME entry for <code>hitbgsec.keithrozario.com</code> pointing to it.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6509} -->
<figure class="wp-block-image"><img src="/uploads/Screenshot-2018-10-02-at-10.22.15-AM.png" alt="" class="wp-image-6509"/><figcaption><strong>CNAME Entry in CloudFlare</strong></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Voila. This way, we get to keep a <code>full</code> SSL cloudflare connection while hosting our contents in a static S3 bucket.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Note:</strong> that as of now, CloudFront doesn't charge for storage on the edge, hence the aggressive cache settings don't cost extra (unless you wanna start invalidating the cache). This speeds up the website, as CloudFlare will always get it's data from the CloudFront distribution without it having to go back to the S3 origin -- should this change, you might want to revisit storing the entire 100MB presentation on the edge.</p>
<!-- /wp:paragraph -->