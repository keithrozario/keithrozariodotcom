+++
title = "I scanned 1000 government sites, what I found will NOT shock you"
slug = "gov-tls-audit"
date = "2018-02-25T09:03:22"
draft = false
categories = ['Misc']
+++

![](/uploads/SSL.jpg)Previously, I moaned about dermaorgan.gov.my, a site that was probably hacked but was still running without basic TLS. This is unacceptable, that in 2018, we have government run websites, that ask for personal information, running without TLS.

So I decided to check just how many .gov.my sites actually implemented TLS, and how many would start being labled 'not secure' by Google in July. That's right, <a href="https://www.theregister.co.uk/2018/02/08/google_chrome_http_shame/">Google will start naming and shaming sites without TLS</a>, so I wanted to give .gov.my sites the heads up!
<h2>Why check for TLS?</h2>
TLS doesn't guarantee a site is secure (nothing does!), but a site without TLS signals lack of care from the administrator. The absence of TLS is an indicator of just how lightly the security of the servers has been taken.

Simply put, TLS is necessary for not sufficient for security -- and since it's the easiest thing to detect for, without running intrusive network scans, it seems like the best place to start.
<h2>How I checked for TLS?</h2>
But first I needed a list of <em>.gov.my</em> sites.

To do that, I  wrote a web-crawler that started with a few <em>.gov.my</em> links, and stored the results. It then repeated the process for the links, the links of the links...and so forth. After 3 iterations, I ended with 20,000 links from 3,000+ individual hostnames <em>(a word I wrongly use in place of FQDN, but since the code uses hostnames, I'm sticking to it for now -- please forgive me networking nerds)</em>

I then manually filtered the hostnames to those from a <em>.gov.my</em> or <em>.mil.my </em>domain and scanned them for a few things:
<ul>
 	<li>Does it have a https website ( if it doesn't redirect)</li>
 	<li>Does it redirect users from http to https</li>
 	<li>Does the https site have a valid certificate
<ul>
 	<li>Does it match the hostname</li>
 	<li>Does it have a fresh certificate (not expired)</li>
 	<li>Can the certificate be validated -- this required all intermediary certs to be present</li>
</ul>
</li>
 	<li>What is the <span style="text-decoration: underline;">IP</span> of the site</li>
 	<li>What is the <span style="text-decoration: underline;">asn</span> of the IP</li>
 	<li>What is the <span style="text-decoration: underline;">server</span> &amp; <span style="text-decoration: underline;">X-Powered-By</span> headers returned by the host</li>
</ul>
Obviously, as I was coding this, my mind got distracted and I actually collected quite a bit more data, but those fields are in the csv for you the Excel the shit out off! The repository contains both a json and jsonl file that has more data.
<h2>Now onto the results</h2>
<!--more-->

Overall, 1180 hostnames were scanned. Of which only 501 (43%) had TLS, this includes sites that re-directed users from http to https (the right way), and sites that did not.

![](/uploads/TLS-Breakdown.png)While some sites like <em>pengundi.spr.gov.my, </em>had fully functioning TLS sites (and probably just forgot to re-direct), others had massive issues with their configurations. This included expired certs like <em>www.1dana.gov.my</em>, or the use of self-signed certs, like <em>fms.skm.gov.my</em>.

Ironically, Muzium Negara , with its certificate that expired in 2013 <span style="text-decoration: underline;">isn't</span> the oldest cert in the scan. That honor goes to <em>vlibimr.moh.gov.my, </em>with a certificate that expired in ... wait for it... 2006. Yup, a certificate that expired 12 years ago is still floating around on government servers. Let's also mention <em>egsentrik.mohe.gov.my, </em>who made a tri-fecta of mistakes. Using self-signed certs that were expired, and utilized MD5.

![](/uploads/oldest_cert.png)

A total of 23 sites (or just 2%) of .gov.my sites used cloudflare. Even then, 7 of those decided to not use the free(!) https offering, and most chose to ignore re-directing users (again it's a FREE Service from cloudflare). Finally a special shout-out to <em>invite.skillsmalaysia.gov.my </em>for screwing up so massively by re-directing users from HTTPS to regular HTTP. That's right, skillsmalaysia will actually force you the un-encrypted version of their site, even if you request an encrypted one.

A total of 15 sites (1%) of .gov.my sites used Let's Encrypt. What's shocking is that some of these sites decided to stop, for example eservices.moh.gov.my, has a let's encrypt certificate that expired in 2017. Only 10 sites out of 1180 are actively using the free certs from them.

Looking at the issuers from the 501 sites, COMMODO issued 107 certificates,  Entrust follows closely with 100, DigiCert with 61, cPanel has 51, and GeoTrust with 40.  Most of these are Domain Validated not Extended Validated. That's a MOOLAH for something Let's Encrypt gives for free. Apart from a bunch of self-signed certs, there were 5 that were issued by Dapat Vista WebAdmin CA, which my version of firefox didn't recognize. Worse still, these certs last till 2038.

![](/uploads/Dapat-Vista-Cert.png)

While most sites were hosted in Malaysia, a small number were overseas (based on their IP addresses). These included <em>www.tabunghaji.gov.my</em>, and<em> www.selangor.gov.my, </em>who appear to be hosted by LINODE in NL. Of the 3 sites hosted on DigitalOcean, none of them chose Singapore -- why?! To be clear, nothing wrong with overseas hosting, I just though it would be interesting. Lastly, www.parlimen.gov.my seems to be behind the a SECURI firewall hosted in the US.

In terms of servers, 569 sites were hosted on some version of Apache, 193 were on IIS, with 79 on NGINX. The remaining either don't provide any server response in the http-header, or provide something odd, like <strong>TehTarikAis/1.7.2.9</strong>.

Based on the X-Powered-By header response, 311 sites use some version of PHP, while 169 use ASP.net, the rest are just out there.

Data from the scan is <a href="https://github.com/keithrozario/Gov-TLS-Audit/tree/master/files">my Git Repo</a>, code in the Repo isn't ready for Prime Time, if you clone the repo, the code will require some massaging to work. (forgive me python masters!)

For the unintiated, here's the <a href="/uploads/files.zip">CSV, JSON and JSONL of the scan results</a>, which includes the hostnames for the .gov.my sites I scanned.
<h2>TL; DR</h2>
After scouring through various government websites, I now consider myself an expert on <em>.gov.my.</em>

A couple of key highlights I want to point out, the website for Jabatan Perdana Menteri actually had a page that contained both a username and password in plaintext. There are hundreds of government sites that request users to input in their MyKad numbers, passwords and emails without TLS, which is just sad.

Some really odd websites include <em>http://cloud.pcb.gov.my:5000/ </em>which looks to be a NAS box connected to the internet, stating "The best storage place where we can share our memories"

But the most laughable page of all, was the website for the Chief Ministers Office of Melaka -- which was hacked (possibly by Russians) to sell Viagra. I contacted them a week ago to let them know, but so far no one has responded, and site is still serving up ads for Viagra and Cialis.

Well at least your tax dollars are <span style="text-decoration: underline;">hard</span> at work.

![](/uploads/image2018-2-24_20-28-17.png)

 

 