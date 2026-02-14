+++
title = "Investigating MYSPPL.com using OSINT"
date = "2022-03-08T13:26:26"
draft = false
categories = ['Misc']
+++

<!-- wp:image {"id":7633,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/uploads/image_from_malaysiakini.jpg" alt="" class="wp-image-7633"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>On September 2021, <a href="https://www.malaysiakini.com/news/592070">malaysiakini</a> reported on a website called mysppl, that was selling personal data online. The site used previous breached data on Malaysians, and was selling it to anyone with a credit card (or Grabpay account).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Note to aspiring criminals.. the last thing you want when doing something illegal like selling personal data ,is to tie that back to Bank Account by accepting payments. But I guess, anything goes these days. </em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Anyway...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I decided to see whether I could use generic Open Source Intelligence (OSINT) techniques to try to find out who is behind the site, and this post is about my journey through that process. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's go...</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>First, I did a regular WHOIS lookup on the domain. Most registrars offer free domain anonymization these days, but this is still the first port of call you want to try. Alas, no luck here, as the domain has the WHOIS data anonymized.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7615,"sizeSlug":"full","linkDestination":"none","className":"is-style-default"} -->
<figure class="wp-block-image size-full is-style-default"><img src="/uploads/Whois-Domsin-mysppl.png" alt="" class="wp-image-7615"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>OK, no big deal, I was expecting it to be that easy. Now, let's try to figure how where this website is hosted. Again, most websites now sit behind a CDN, which makes OSINT more difficult, but it's still a mandatory step to at least try this. Running a <code> dig NS &lt;domain_name&gt;</code> command will give us the Nameservers used to host this -- and here we see it's hosted on Cloudflare :(</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7616,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/uploads/Cloudflare-hosted-mysppl-744x500.png" alt="" class="wp-image-7616"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Next, I ran a ShodanHQ search and it turned out blank as well. Haih!.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But let's keep chugging -- on to Cert Transparency logs. Using <a href="http://crt.sh">crt.sh</a>, and searching for mysppl.com reveals some rather interesting tid-bits.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7618,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/uploads/Cert-Transparency-1-820x98.png" alt="" class="wp-image-7618"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Oooh -- this looks interesting. A2hosted is a hosting provider -- but what does Shariarb mean? Let's dig further. If I search for Shahriarb.a2hosted.com on crt.sh, I get even more weird domains:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>At least we have a bunch of domains to search. I'll spare you the details of the random domains that seem to be hosted here, but want to highlight two interesting ones:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The first is an insurance company -- that has a bird logo on it:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7620,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="/uploads/insurance-company.png" alt="" class="wp-image-7620"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And the second is a automotive part and supply website, take note of the phone number it'll come in handy later:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7621,"className":"is-style-default"} -->
<div class="wp-block-image is-style-default"><figure class="aligncenter"><img src="/uploads/partnsuppluy-526x500.jpg" alt="" class="wp-image-7621"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>OK, after diving through those various domains, I decide to do WHOIS History searches on these domains. I registered for a free account at WHOISXML, and ran a few queries. These are recorded WHOIS historical data, and after searching through some of domains I found this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7624,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="/uploads/whois-history.png" alt="" class="wp-image-7624"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Finally a Shahriar B -- it's a name!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If we do a quick search for the domain, we end up with a LinkedIN profile of the CTO of the insurance company with the bird logo:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7630,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/uploads/ShahriarB-CTO.png" alt="" class="wp-image-7630"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Now if we reverse search the WHOIS data for his name, we find other domains, including one with a phone number that's just 1 digit off, from the phone number of the auto-part supply website:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7631,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/uploads/reverse_whois-733x500.jpg" alt="" class="wp-image-7631"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>I think there's enough to conclusive prove that Mr. Shahriar B ran mysppl.com for a while. And after I started poking around he decided to shut down the website. Profiting off data breaches really isn't cool man....don't do it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Fortunately, mysspl.com is now shut for business, let's hope it stays that way.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7632,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/uploads/image-1.png" alt="" class="wp-image-7632"/></figure>
<!-- /wp:image -->