+++
title = "How corporations lie to the technologically challenged"
slug = "how-corporations-lie-to-the-technologically-challenged"
date = "2015-09-28T11:50:39"
draft = false
categories = ['CyberLaw', 'Malaysia', 'Security &amp; Privacy']
+++

![wpid-wp-1442992521638 (1)](/uploads/wpid-wp-1442992521638-1-300x170.jpeg)Two weeks ago, Lowyat.net published a <a href="http://www.lowyat.net/2015/74092/can-you-break-these-codes/">'challenge'</a> to their readers, one that would supposedly pay a cool RM100,000 to the winner.All you had to do was decrypt an AES-256 encoded blob of code (more accurately referred to as ciphertext).

As expected, no one won.

Because breaking that 'military-grade' encryption is beyond the capability of most normal human beings, and certainly not worth a paltry RM100,000 that was being offered. It's the equivalent of offering 50 cents for someone to build a rocket capable of going to the moon. In fact, Rm100,000 is exactly the cash prize celcom offered for it's cupcake challenge, because baking cup-cakes and breaking 'military-grade' encryption are the same thing.

Once the challenge has expired, Celcom conveniently launched their new <a href="http://www.lowyat.net/2015/75604/celcom-launches-zipit-chat-a-new-chat-app-that-boasts-military-grade-aes256-encryption/">zipit chat application</a>, which surprisingly used AES-256 encryption as well, and more importantly they released some statistics of a 'hackerthon' they conducted in which 18 Million people viewed the challenge, and 17,000 registered to participate but none succeeded.

OK, so while there was no official announcement from Celcom to tie the original lowyat challenge to their new zipit app, it was quite plain for all to see.

So let's go into why this upsets me.<!--more-->
<h2>Encrypt, Encrypt, Encrypt</h2>
First of all, everybody knows AES-256 is pretty much unbreakable with todays technology, the NSA admits it, and the Snowden leaks confirm it. In fact, the NSA takes great pains to get data where the communications has already been decrypted, because it's easier circumvent encryption than it is to break it.

But just because you use strong encryption doesn't mean your application is unhackable. If the creators of zipit chat were really serious about making such bold claims, they'd make a challenge to <strong>hack their app</strong>, not just some encrypted codes. It's also telling while the challenge was issued, Celcom hadn't revealed themselves as the sponsor, and more importantly no one from Celcom had published the key for decrypting the codes, even after the challenge had expired.
<h2>Conflating encryption with security</h2>
The thing that riles me up, is this conflating of different aspects of security, that just because the app uses AES-256 (which is uncrackable) then the app itself is unhackable. That's a pile of horse-shit and the creators of the app must know it.

Even the great guys over at soyacincau wrote a <a href="http://www.soyacincau.com/2015/09/23/celcom-launches-zipit-chat-an-encrypted-communications-app/">piece</a> suggesting zipit chat was better off than whatsapp or WeChat because the latter applications had some vulnerabilities exposed. But, Whatsapp and WeChat have been around for far longer than zipitchat, so obviously they'd have more vulnerabilities exposed than this never-heard-before app from Celcom. And there's absolutely no proof that zipit has a better level of security at the application level than other messaging apps.
<blockquote>
<h6>We’ve all heard of <a href="http://www.telegraph.co.uk/technology/internet-security/11850817/WhatsApp-security-breach-lets-hackers-target-web-app-users.html" target="_blank">WhatsApp</a> having massive security flaws, causing malicious affects on user data and devices. The same goes for <a href="http://www.soyacincau.com/2015/09/22/wechat-and-76-apps-on-ios-affected-by-xcodeghost-hack-remove-them-immediately-if-you-have-them/">WeChat</a> on iOS that was recently afflicted with the XcodeGhost code in its app – so the question remains, what alternatives do we have?</h6>
<h6>Coincidences are great, especially when they work in your favour, thus, Celcom wants to provide you a way “to maintain fullest control of privacy for” your chats and messages with Zipit Chat</h6>
-Soyacincau</blockquote>
I also know, that 'ordinary, technically-challenged' folks are going to be reading soyacincau and lowyat and thinking that this really is an 'unahackable' application just because it uses military-grade encryption, and these people are going to be forking out Rm10/month for a very false sense of security.

Plus if you really are serious about security, you'd have a website with TLS encryption, not plaintext http. Are you listening zipit chat? Even my hobby blog has TLS encryption, if you can't encrypt your website properly, what's the chances you encrypted the app.

Finally of course, we need to talk about Government spying. Zipit is an application provided by Celcom, a local telecommunications provider. If you're afraid of the Government spying on you, then this is the last application you want to use, because all the Government has to do is ask Celcom for your communications and Celcom are compelled under <a href="https://www.keithrozario.com/2015/05/the-technological-effects-of-sosma-and-pota.html">SOSMA</a> to provide it to them.
<h2>Secure messaging apps</h2>
![Secure Messaging Scorecard Electronic Frontier Foundation](/uploads/Secure-Messaging-Scorecard-Electronic-Frontier-Foundation-820x312.png)

If you really wanted to message your friends securely and safely, the two applications I recommend is <a href="https://telegram.org/">telegram </a>(with the secret chat functionality) and <a href="https://whispersystems.org/">textsecure</a>, both of these apps score full-marks on the <a href="https://www.eff.org/secure-messaging-scorecard">EFF's secure messaging scorecard</a>. They're free, and don't mislead you into thinking their apps are secure just because they use 'military-grade aes-256' encryption.

Of course, whatsapp is not secure (read <a href="http://www.thoughtcrime.org/blog/saudi-surveillance/">this</a> and<a href="http://m.heise.de/ct/artikel/Keeping-Tabs-on-WhatsApp-s-Encryption-2630361.html"> this</a>), and should only be used for casual conversation. But just because whatsapp isn't secure doesn't mean zipitchat is.
<h2>Conclusion</h2>
Nothing pushes my buttons more than people taking advantage of the technically challenged. Just because someone doesn't know technology, doesn't give you a license to lie and oversell your products. This is another prime example of why we need to combat the growing tide of technology illiteracy in Malaysia, and we should start soon.

Otherwise we'd all fall victim to corporations like Celcom taking us for a ride.
<h2>Post-Script: Did they get they're encryption wrong?</h2>
One thing that always bugged me about the Zipit Chat code challenge, was that they supposedly used AES-256, yet they managed to make it such that all 3 codes started with the same 8 characters.

In any modern block cipher, changing either the key or plain-text by even a single bit, completely changes the cipher-text. For example, if I encoded <strong>keithrozario.com</strong> with the key <strong>12345678</strong>, I get this:
<blockquote>Ar1OfyDJfYB1xvpsKVfzk0GaibZM2ob8IYMi9JY14w0</blockquote>
If I encoded <strong>keithrozario.com1</strong> with the key <strong>12345678</strong>, I get this:
<blockquote>n968ZOtXnjhCEYA1A6WEmOEOgRLXRdvNjJ7WTr+V2ig</blockquote>
And if I encoded <strong>keithrozario.com</strong> with the key <strong>123456789</strong>, I get this:
<blockquote>PZE/qUCRP7MJ2BIKY4dIcZ+1W0rs0GZqCvmbyqrKWDk</blockquote>
Even though, all 3 have very similar keys or plaintext, the output ciphertext is completely different. In contrast these are the 3 ciphertext published by the 'competition':
<blockquote>–##–<strong>eyJHMDkw</strong>MjQwQiI6IlVFM......./EjREtCz9Lq–##–

–##–<strong>eyJHMDkw</strong>NjQ3MiI6IkRZb.......h0CC28rk–##–

–##–<strong>eyJHMDkw</strong>NkIyRCI6Ik81........PPTaVOoDT–##–</blockquote>
The authors of the challenge, had to really go out of their way to ensure that the 3 ciphertext all started with the 6 same characters, or they just smashed together a bunch of characters to make a 'fake' competition that no one could possibly win, and that's why they didn't announce the source of the competition.

I wrote to Celcom for clarification, and here's what they answered, my questions in <b>bold.</b>
<blockquote><strong>1. Can you share the results of the code challenge? I presume this is the one organized on Lowyat.net, with 3-codes supposedly encrypted with AES-256. I would like the plaintext, and encryption keys for all 3 ciphertext</strong>
Coffee:A warm, delicious alternative to hating everybody every morning forever.Behind every succesful person is a substantial amount of coffee.U deserve a good cup.

Happiness can be found even in the darkest of times if one only remembers to turn on the lights. Provided one does not forget to pay the electric bills. W00t w00t!!

Calm u shall keep and carry on you must. Eat, drink and be merry. Why worry over something that we cannot control. Be prepared for the worst and pray for the best.

Unfortunately we don’t have the encryption key. That is stored in the sender devices which belong to some of the panel judges.
<strong>2.Does your application store the private keys of the communication on the cloud or is it purely on the device only?</strong>
Yes, in the device
<strong>3. You mention RSA for key exchange, but RSA requires a public-private key pair. Where do you generate these key-pairs (device of cloud), and where do you store the private portions of these keys?</strong>
-Keys are generated in the device.
-Stored in the device.</blockquote>