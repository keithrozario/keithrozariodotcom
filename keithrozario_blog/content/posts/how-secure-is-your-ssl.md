+++
title = "How secure are the webpages of Malaysian Banks and Telco"
slug = "how-secure-is-your-ssl"
date = "2013-06-20T08:00:51"
draft = false
tags = ['CIMB', 'Digi', 'LHDN', 'Lowyat', 'Malaysiakini', 'Maxis']
categories = ['Malaysia', 'Security &amp; Privacy']
+++

![SSL](/uploads/SSL.jpg)I've almost been fascinated by the fact, that our money in the bank these days are secured not by steel doors or armed guards, but rather by cryptography and the encryption keys that enable them. To put it in the simplest form  your money in the bank is protected by a number--that's what an encryption key essentially is. A long binary number of 1's and 0's that protects your life savings...

<span style="font-size: 13px; line-height: 19px;">Most (if not all) of your 'secure' internet communications is protected by something call SSL, or its successor, TLS. SSL is the stuff of legend, initially invented by Netscape to encrypt internet communications, SSL is now used by nearly everyone online. You see it when you login to your bank account on Maybank or CIMB, when you log into a online store like the ones run by Digi and Maxis even when you do your Tax filings on e-Filing LHDN website.</span>

However, just like every standard in IT, SSL and TLS act as frameworks, and different websites could implement these frameworks slightly differently, usually based on the customer segmentation or the amount of security required. Each implementation could vary from one to another and yet still remain compliant to the 'standard', we wouldn't need consultants if it were otherwise.

The problem is, that just because some website use TLS or SSL, doesn't mean it's secure--all it means is that the website is now using a standard, but could have implemented the standard poorly, making it vulnerable to attack, and possibly leaking out your data (some of which might be very very sensitive).

The best way to think about is to go back the number analogy, and assume that the amount of security you get from encryption is determined by the length of the number. So a 10 digit number is less secure than a 100 digit number--and a 1 digit number is less secure than both of them. In security jargon, we call this the key length, and it's quite a common criteria used to determine the security of a given SSL/TLS implementation. This of course is just one of the criteria to determine how secure the the implementation is.

<span style="font-size: 13px; line-height: 19px;">Basically it's not enough to check if a website is using SSL or not, it's more important to figure out how well the encryption is implemented by the website. Of course, this is beyond the scope of most people, no one has the time or inclination to perform a security audit on their banks website, although it is in their best interest to do so. Usually that green lock icon at the bottom of the screen helps me sleep well at night--but it shouldn't, it's a good start, but not a guarantee of security.</span>

Fortunately, there's a really quick and dirty way, to determine how secure the SSL/TLS implementation of a website is. Head on over to <a title="http://www.ssllabs.com" href="http://www.ssllabs.com" target="_blank">SSLLabs.com</a> and enter the url of the website you want to evaluate and the perform a really good audit of the site in real-time, measuring things like key-length and SSL versions, up to the certificate authenticity.

So armed with SSLLabs.com, I decided to just quickly perform a quick check of the most popular secure websites in Malaysia to see if these websites were offering the security their users deserved. Checking out the most popular forum in Malaysia, two telco companies, two banks, one government agency and a news portal, the good news is that 3 out of 7 got straight A's on their test--the bad news is that the other 4 got F's--and it's possible to get E by the way...so an 'F' is what most people call an epic failure.<!--more-->
<h2>Malaysian sites that implement SSL beautifully</h2>
![CIMBCLICKS_SSL](/uploads/CIMBCLICKS_SSL.jpg) ![Lowyat_SSL](/uploads/Lowyat_SSL.jpg)
![Malaysiakini_SSL](/uploads/Malaysiakini_SSL.jpg) 

Cimbclicks, the Lowyat forum and Malaysiakini--come on down and get your prize. These guys scored as high on their SSL security as Google!! So all in all, this was a really good showing. Of course, just because the SSL security is high doesn't mean the system isn't vulnerable in some other way--but it does suggest the organization in question is serious about security.

These guys do simple things really, the use good certificates, they reject older implementations of SSL and they have sufficiently long key lengths, it represents a good approach to security. These last two criteria are essential, supporting SSL versions of 2.0 and older, or using key lengths of under 128-bit is a sure fire way to fail this test.
<h2>How about the F's.</h2>
![Digi_SSL](/uploads/Digi_SSL.jpg)![LHDN_SSL](/uploads/LHDN_SSL.jpg) 

![Maxis_SSL](/uploads/Maxis_SSL.jpg)![Maybank_SSL](/uploads/Maybank_SSL.jpg)This is where things get ugly, you would really expect LHDN and Maybank to get their act together. Maybank and LHDN fail by allowing users to use SSL 2.0 (which is considered 'bad' or deprecated), as well as utilize key lengths of under 128-bit, which in todays world really isn't good enough. Sites should start at 128 and go from there if you ask me.

It's worst for Maybank because they're a freaking BANK. In fact, industry standards like PCI-DSS explicitly disallow the use of SSL 2.0, stating in <a title="Security Protocols" href="https://www.pcisecuritystandards.org/pdfs/pcissc_assessors_nl_2008-11.pdf" target="_blank">2008 update </a>that:

[box icon = "chat"]PCIDSS Requirement 4.1 requires the use of strong cryptography and security protocols to safeguard cardholder data during transmission over public networks, namely the Internet. Strong cryptography and security protocols must be deployed and <strong>SSL v3.0/TLS v1.0 should be considered the minimum standard</strong>. </blockquote>

I was surprised as there really is no reason to support SSL v2.0 anymore. Popular web browsers no longer support it. IE7, Chrome, Safari, Firefox and Opera all turn of SSL v2.0 support either completely, or by optional default, so the chances of their being this one user who still uses an old browser accessing the site is minimal at best. Even then it's probably more advisable to train these users, rather than compromise the security of the entire site for all other users.

Now before you panic--most browser protect you to a certain extent, however Banks shouldn't completely rely on users for their security, and hence this easy-fix should be fixed. Also, I'm not sure if the two-factor picture authentication from Maybank mitigates their support of SSL v2.0, but I don't think so. Finally, Maybank does offer two-factor authentication via sms for one-time transfer that weren't previously registered on the portal--but even then....this should be fixed.
<h2>Conclusion</h2>
So let's put this into perspective. It turns out a public forum runs their website with more security than the Malaysian tax authority and Malaysia's largest bank. However, I did realize that it probably wasn't fair on Maxis and Digi to test their store/shop sites, these sites probably don't require high end security--and even vulnerable SSL implementations would suffice (unless of course the username/password for these stores are the same as their main sites). So I re-tested their customer logins to see what kind of security they provided, and lo and behold' Maxis scored the highest marks I've seen on any site in Malaysia (equalling Malaysiakini), while Digi still fails miserably (presumably for their continued acceptance of SSL 2.0).

![Maxis_MOI_SSL](/uploads/Maxis_MOI_SSL.jpg)   ![Digi_login](/uploads/Digi_login.jpg)Security is a real hot topic right now, not a day goes by when we don't see some Fortune 500 company or government agency losing data to attackers, utilizing weak SSL implementations not only paints a big red target on a site--it also suggest a lackadaisical approach to security from the organization in question. It probably isn't in my best interest to be critical of Digi at this junction, since I'm in the running for their WWWOW awards again--but what the hell, I've just gotta be me.

What surprised me though is how Maxis has vastly different scores for the moi.maxis.com.my (customer login) and store.maxis.com.my (online store). The differences couldn't be wider, the moi site actually addresses BEAST attacks, uses secure cipher suites and doesn't support SSL 2.0. They probably have two different teams looking at these sites--and we all know whose the more secure one.