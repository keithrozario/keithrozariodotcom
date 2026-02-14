+++
title = "HTTP vs. HTTPs : Why SSL and TLS are important"
date = "2012-08-06T12:24:33"
draft = false
tags = ['Maxis']
categories = ['Malaysia', 'Misc']
+++

I was looking for some detail on Maxis Fibre to Home service until I came across this while trying to to access the Maxis Customer Forum online:

<center><a href="/uploads/Maxis_SSL_Fail.png"><img class="alignnone  wp-image-2657" title="Maxis_SSL_Fail" src="/uploads/Maxis_SSL_Fail.png" alt="" width="550" height="193" /></a></center>In the early days of the internet, all the data flowing through was done in plaintext, this meant that everything flowing on the internet was fair-game for anyone to hijack and view. It was akin to sending postcards all around, all the post-men and intermediaries could view the entire contents of your messages because it was out there in the open, no need to open sealed envelopes. So everything from your letters to your uncle Bob or your resume for a new job or even your most intimate personal letters could only be sent via postcard--anyone could read it.

There was a strong requirement however to design a mechanism to encrypt data flowing through the internet, because unless you could encrypt data, personal and credit information couldn't (or rather shouldn't) have been trasmitted across the internet. So it was important that someone somewhere figure out how data on the internet could be encrypted to enable things like online shopping, social networking, even simple email. So sometime in the mid-90s Netscape (the default browser at the time was Netscape Navigator), took up the gauntlet and invented SSL.

<span style="color: #888888;">At this point, I'm also reminiscing the days when browsers were actually pay-ware rather than freeware. Remember when Netscape Navigator Gold used to cost money?<!--more--></span>
<h2>How does SSL/TLS work?</h2>
SSL and it's successor TLS utilize a public-private key pair. In a public-private key pair, there exist 2 keys.

A Public key, to be shared with the public, and a Private key, to be kept private. In this particular case, The Public key is used for encrypting, while the private key is used for decrypting. Anything encrypted with the Public Key can only be decrypted by the Private Key--so that anything sent to the owner of the Private key could be encrypted easily, and only the owner of the Private key could decrypt the message.

So in a Https setting (which utilizes SSL or TLS), when you access a site, the site will provide you with it's Public Key. Now this is public knowledge, so the public key can be transmitted in plaintext--no problem.

The next step is that the user's browser will then verify the Public Key with a list of known certification authorities (or CA), think of these guys as the notaries of the internet. If the certification authority says everything is fine and dandy, then the browser takes it to the next level, if there are issues with this certifications--the browser spits out some rather nasty warnings.

If the CA certifies the key, then your browser now generates a 'random' encryption key. It will encrypt this key with the public key given by the site. So only the website can decrypt it, because only the website should have the private key. Since they only people who know the new 'random' encryption key are you (because you generated it), and the website (because only the website could decrypt it) all data between you and website can now be securely encrypted with this key.

It's also important to note that the 'random' encryption key is a private-private key, meaning it's a symmetric (the same key encrypts and decrypts the data) and it's private only to the parties involved in the transaction.
<h2>What kind of protection does SSL/TLS afford?</h2>
SSL/TLS are more a method of selecting a final encryption key rather than encryption itself. So the true security of the connection is dependant on what kind of encryption is finally used, however in most cases Bad Certificate warnings prompt up pretty big and bold on a browser. There's a good reason for that, Firstly a bad certificate could mean the site was comprimised, or someone is performing a 'man-in-the-middle' attack on you. So for instance if I placed malware on your PC, ensuring that everytime you type www.maybank2u.com.my, you end up at a fake site of mine that looks like maybank2u, you wouldn't know the difference with just your eyes.

Your browser however could detect that the certificate I presented from my fake site wasn't as expected or couldn't be verified by a certification authority. I couldn't present the original certificate from my site because then I wouldn't be able to decrypt the information you sent to me, since information encryption with the public key could only be decrypted by the private key--and the private key is kept secret by Maybank.

So most of the time these sorts of attack neglect https altogether, therefore <strong>it's very important to ensure that connections to sites that you share you private data with are encrypted just by noticing the extra s at the end of https</strong>. The second reason some sites prompt up really nasty warning messages is because there's something wrong with the certificate. In most cases this is because a certificate hasn't been renewed, certificates have renewal dates, and will expire otherwise. There's a good reason for putting an expiration on a certificate as well. Just like any other form of encryption, with enough time, malicious hackers would figure out the private key of a certificate based on it's public key, putting a time-limit of one year for example was important. Although the time taken to crack one of these babies would be significant.

The cost of renewing SSL certificates has become so low, it's surprising to see that many webmaster still procrastinate of renewing them. In some rare cases, we also see an improperly setup certificate. This is when a certificate isn't correctly setup for the website in question. For the most part this is harmless, but it could still point to other issues with the site, particularly security vulnerabilities.
<h2>Maxis Forum SSL Error</h2>
So it was really surprising to see a company like Maxis, incorrectly setup the certificate for their Maxis forum. <strong>Forum.Maxis.com.my</strong>, is supposed to be a forum for Maxis customers to congregate and discuss issues and ideas on their service, it's the  main source of information for my post on <a title="How to enable VPN connectivity on Maxis Mobile" href="http://www.keithrozario.com/2012/07/maxis-vpn-mobile-setting-3g.html">configuring maxis for your VPN</a>.

However, Maxis seem to be using an incorrectly generated certificate for ideaspost.maxis.com.my for the forum, using a certificate configured for ideaspost.maxis.com.my, your browser detects that the URL for the cert and the site are different and prompts up a nasty warning. This is really a schoolboy error, and I wonder how this slipped through testing.

This has since changed, and Maxis have tried now to revert to the original certificate that <strong>expired on the 31-Mar 2012</strong>. Certificates expire for a reason--certification authorities need a recurring source of income. Just kidding. SSL certificates expire, because just like everything else, if you try long enough to attack a certificate you can eventually figure out the private key based on it's public key, changing a certificate on a site has almost no impact to the end user, but it keeps your website certificate fresh, so once a key is updated an attacker has to try all over again. It's the same reason some sites have a strict password renewal policy, mandating you update your password once every 3 months for example.

To be fair, you don't really need SSL for a public forum, particularly one like Maxis, but you never really know. Like I said this could be harmless, but it does pose some serious questions about how seriously the largest telco in Malaysia is taking it's security practices.

<center><a href="/uploads/Maxis_SSL_cert_expired.png"><img class="alignnone  wp-image-2658" title="Maxis_SSL_cert_expired" src="/uploads/Maxis_SSL_cert_expired.png" alt="" width="550" height="193" /></a></center>