+++
title = "3 times GovTLS helped fixed government websites"
slug = "gov-tls-fixed-websites"
date = "2018-06-16T09:21:52"
draft = false
tags = ['GovTLS', 'Malaysian Government']
categories = ['Malaysia', 'Security &amp; Privacy']
+++

Couple months back I started GovTLSAudit. A simple service that would scan  <code>.gov.my</code> domains, and report on their implementation of TLS. But the service seems to have benefits above and beyond that, specifically around having a list of a government sites that we can use to cross-check against other intel sources like Shodan (which we already do daily) and VirusTotal.

So here's 3 times <a href="https://gov-tls-audit.sayakenahack.com/">GovTLSAudit</a> helped secure government websites.
<h2>That time Yayasan Islam Terengganu was used a phishing website</h2>
I used virustotal's search engine to see if they had extra .gov.my domains to scan, and found a few rather suspicious looking urls including:
<blockquote><a href="https://www.virustotal.com/en/domain/paypal-security-wmid0f4-110ll-pp16.yit.gov.my/information/" target="_blank" rel="noopener">paypal-security-wmid0f4-110ll-pp16.yit.gov.my </a>
<a href="https://www.virustotal.com/en/domain/appleid.corn-security2016wmid7780f4-110ll-16.yit.gov.my/information/" target="_blank" rel="noopener">appleid.corn-security2016wmid7780f4-110ll-16.yit.gov.my</a>
<a href="https://www.virustotal.com/en/domain/paypal-security-wmid7110f4-110ll-pp16.yit.gov.my/information/" target="_blank" rel="noopener">paypal-security-wmid7110f4-110ll-pp16.yit.gov.my </a></blockquote>
This was an obvious phishing campaign being run out of a <code>.gov.my</code> domain. Digging further, I found that the IP address the malicious urls resolve to was local, and belonged to Exabytes. And while the root page was a bare apache directory, buried deep within the sites sub-directories was a redirect that pointed to a Russian IP.

I took to twitter to report my findings -- I kinda like twitter for this, and the very next day Exabytes come back with a followup that they were fixing it. That's good, because having a phishing campaign run on <code>.gov.my</code> infrastructure isn't exactly what you'd like.

There's a lot more details in the tweet about how I investigated this,-- click <a href="https://twitter.com/keithrozario/status/1000639200784367616">here</a> to follow the thread. A warning though -- I regularly delete my old tweets. So get it while it's there :).

<a href="/uploads/Exabytes-TQ.jpg">![](/uploads/Exabytes-TQ.jpg)</a>
<!--more-->
<h2>That time we found invalid certificates</h2>
Of course GovTLSAudit was purpose built to audit TLS implementations, and finding bad certificates is what it does.

Again, taking to twitter I reported a bad certificates on <a href="https://twitter.com/keithrozario/status/1002054785799831552">MSC Malaysia</a> and <a href="https://twitter.com/keithrozario/status/1002053807667273728">Bank Negara</a>. I was impressed by MDEC's quick response on the mscmalaysia domain, they were quick and happy to respond.

The issue was them using the mdec cert for mscmalaysia, hence browsers reported an hostname mismatch. They quickly implemented a redirect from mscmalaysia to mdec and all was fixed (well mostly fixed!)

I was less impressed with Bank Negara, who till today (weeks later) have not responded.

<a href="/uploads/mdec-tq-1.jpg">![](/uploads/mdec-tq-1.jpg)</a>

If you download a full daily scan (available <a href="https://gov-tls-audit.sayakenahack.com/files.html">here</a>), you can do a quick filter in Excel to find all sites with misconfigured certificates, either they're expired, invalid or just self-signed.
<h2>That time we found default credentials</h2>
Since the scans stitch together Shodan information, I decided to go for a stroll on anything on non-standard http ports. These are http sites hosted on port 8080, 8000 or 8081, which you're certain to find something juicy.

And sure enough after a quick stroll I found two sites with default credentials, even one that had admin/admin on their Tomcat Manager! If I remember correctly, that site belonged to the Ministry of Defence :)

Fortunately, a quick email to the technical contacts on the WHOIS entries (thank God for <a href="https://krebsonsecurity.com/2018/04/security-trade-offs-in-the-new-eu-privacy-law/">WHOIS</a>), and they were taken down the very next day.
<h2> <a href="/uploads/MOD-TQ.png">![](/uploads/MOD-TQ.png)</a>Conclusion</h2>
I'm really happy that the project is helping secure at least some low-hanging fruits on gov domains. Also, it's good to see people respond quickly and positively to the feedback -- except BNM, but they have massive problems now, so who can blame them :)

The one thing I'd recommend most folks do, is implementing a <a href="https://securitytxt.org/">security.txt</a> file on their site, it helps provide a good point of contact that goes directly to the security folks instead of the a online ticketing system that goes nowhere.

Sites should also have updated technical contacts on their WHOIS records. That helps a lot.

And finally a good <strong>contact us </strong>page somewhere on their site. That way, anyone that does find an issue can contact the right person immediately, and not be placed in a ticketing system that leads nowhere.

That's all folks.