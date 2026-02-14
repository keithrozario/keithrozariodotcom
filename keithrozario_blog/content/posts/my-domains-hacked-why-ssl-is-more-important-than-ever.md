+++
title = ".my domains hacked: Why SSL is more important than ever"
slug = "my-domains-hacked-why-ssl-is-more-important-than-ever"
date = "2013-07-02T15:34:29"
draft = false
categories = ['Security &amp; Privacy']
+++

![MYNIC_HACKED](/uploads/MYNIC_HACKED.png)MyNic is the organization responsible for managing the .my Top Level Domain, which means every website address that ends with a .my is under their administration. These centralized control centers act as giant targets for hackers, but for the most part, they're protected better than Fort Knox--or they should be.

Yesterday, a hacker going by the name Tiger-M@te successfully manage to hijack the .my addresses of popular websites belonging to Google, Microsoft, Dell and even Kaspersky (an Anti-Virus company). Instead of being presented with the usual webpage, visitors who entered urls like www.google.my, or www.skype.my were redirected to a static page with the word <span style="color: #ff0000;">HACKED</span> emblazoned in big red letters.

Initially, word around the tech community was that this was a DNS poison, but later on <a title="malaysian domain hijacked" href="http://plus.evozi.com/204/malaysia-domain-mynic-registry-hacked-numerous-my-sites-redirected/" target="_blank">evozi.com reported</a> that this was a DNS hijack. The difference is that a DNS poison is where just one DNS resolver is 'poisoned', and a user could easily circumvent the issue by choosing a separate resolver like one provided by Google or OpenDNS. A DNS hijack on the other hand is where the actual Top Level Domain (TLD) administrator has been compromised, resulting in every DNS resolver replicating the wrong IP address.

A DNS poison is a localized issue affecting just a portion of the servers that make up the DNS eco-system, a DNS hijack is a global issue affecting everyone.

Put another way--MYNIC screwed up, big time! The vulnerability in this case had nothing to do with Google, Dell, Microsoft or Kaspersky, it was all MyNic.

I'm not sure on whether DNSSEC would have solved this issue. DNSSEC implicitly relies on the trustability of the TLD domain name server, and if that server is comprimised DNSSEC wouldn't help. However, DNSSEC does require the signing of these domains by a key, and if that key were protected, the hijack wouldn't have worked. At worst, user wouldn't have been able to access the webpages, they wouldn't be redirected.

Most websites, including Lowyat.net had <a title="Google DNS poisoned" href="http://www.lowyat.net/2013/07/01/9986/google-dns-poisoned-numerous-my-sites-redirected/" target="_blank">advised users to be cautious of using services like Online Banking</a> at this time. However, a straightforward and secure way around the issue is just to ensure you're browser is operating in SSL mode (that's the https vs. http question), and check the certificate to ensure you're on the right page. In fact SSL was built for this sort of thing, as it provides both Authentication and Encryption--this is a case where the former would help but not the latter.

If anything this is a stark reminder on why it's important to check the SSL certificates of websites you're visiting constantly, and not rely on Google Chrome to do it for you. It's also a wake up call to any entity dealing with private and personal data to implement SSL and implement it well.

I was absolutely SHOCKED to find out that bloody MYEG doesn't have SSL enabled on their website. In fact the login form for MyEG resides on a non-encrypted and non-authenticated site, it's only the form that is finally posted to a https page. Not good at all, as there 'may' be encryption, but definitely no authentication for the main page, and MYEG would be ripe and ready for this sort of attack. It's a wonder why Tiger-M@te didn't choose it?

Finally, the conspiracy theorist have looked at the <a title="Source code of hacked page" href="http://pastebin.com/kS3GCEE0" target="_blank">source code of the hacked page</a>, and noticed that some of script used on the page was written in bahasa...stragerer and strangerer.

 