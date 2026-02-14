+++
title = "Jho Low uses Gmail? Why emails can't be considered evidence"
date = "2015-03-07T15:11:26"
draft = false
categories = ['CyberLaw', 'Security &amp; Privacy']
+++

<img class="alignleft wp-image-4775 size-full" src="/uploads/15197804185_d4a1f3d9b3_m.jpg" alt="15197804185_d4a1f3d9b3_m" width="240" height="205" />As the 1MDB fiasco begins to simmer over the political stove, I wanted to inject some technical information into this discussion, specifically around emails and how they're almost useless pieces of evidence.

Just to make sure everyone's on the same page, here's some context.

In early March 2015, sarawakreport.org, a website run by investigative journalist Clare Rewcastle-Brown together with the London Sunday Times, published an article on controversial deal done by the 1MDB fund. At the centre of the deal was a man named Jho Low, who masterminded a sophisticated 'wheeler-dealer' that pocketed him $700 Million, all of which (at least according to sarawakreport.org) was siphoned from 1MDB, a Malaysian sovereign wealth fund.

Honestly, I don't understand the financially complex deals that sarawakreport.org was trying to explain to lil ol' me. So I'm just going to take her word here, that all the documentation that was produced leads to the conclusion that Jho Low masterminded the "Heist of the Century" by stealing $700 million through shady back door deals involving 1MDB and a company called PetroSaudi. But then of course, the question becomes, can you trust the documentation.<a href="/uploads/Layers-of-the-Internet.jpg">
</a>

Reading the article you get the sense that the e-mail trail presented forms the backbone of the entire story, and if the emails themselves are not true then the entire story is untrue as well.

In either case though, let's get straight to the point, and say that e-mails by themselves are quite useless.<!--more-->
<h2>What? Emails are useless?</h2>
To understand that we have to understand the Internet Protocol, or IP. It's the set of rules that govern how computers on the internet communicate with one another, and forms the fundamental basis of how the entire internet works. Unfortunately, this protocol was developed way back when we didn't need any form of security online, it was designed for information to be passed on efficiently and effectively, not securely.

Which means that at a very fundamental level, the internet provides no security to its users--at all. The security we get when we do our online banking or shopping comes from technologies that came very much after the internet was already established, and the Internet Protocol was already the defunct standard. For example the authentication and encryption that protects your online banking with Maybank is provided by a technology called SSL, which came about much later.

SSL is built on HTTP which is built on many other things, but ultimately rely on the IP layer of the internet.

In this analogy the internet is composed of 'layers', technology that is built on technology that came before it--much the same way as rock layers in geology are laid upon layers that came before them<em> (WiFi is a perfect exception, but this is generally true)</em>. The general rule of thumb is that a rock layer at the top is younger than a rock layer at the bottom. In the same way, we've built all the stuff you see in web 2.0 over layers that came in web 1.0, and most of those layers were unsecured.

Even if layers like WiFi or 3G/4G have security, and they reside on the what we call the physical layer, the security on these layers are usually stripped out before being passed onto the general internet. So WiFi has encryption that protects your data transmission from your phone or iPad to your router, but traffic from your router to the general internet no longer carries this encryption, and thus has to rely on other technologies to secure it.

<img class=" wp-image-4771 aligncenter" src="/uploads/Layers-of-the-Internet.jpg" alt="Layers of the Internet" width="550" height="309" />

Every layer of the internet corresponds (more or less) to the time it was created--and addressed the needs of users at the time. Security only became a requirement when online shopping was popular, which when viewed over the course of the history of the internet--wasn't too long back.
<h2>Which brings us to E-mails.</h2>
E-mails are a remnant of the internet past, built at a time when the internet was young, and resides in the layer of the internet that provide no security at all. The protocol that governs how e-mails flow from one point to another does not involve any authentication in much the same way as its contemporary protocols didn't either, but unlike it's contemporary protocols that have since passed on, Email is not only surviving in an era when it should be consigned to the history books, it's actually thriving.

Think of it this way....would you be able to 100% conclusively prove that the letter you got from your grandmother over Christmas was indeed from your Grandmother? How hard (or easy) would it be for someone to forge a letter from your grandmother? E-mail is exactly the same, it was built to mimic the postal service, and unfortunately the postal service doesn't validate the sender of the mail before it sends it out, which means anyone can send a mail pretending to be someone else--just like e-mail. The 'e' doesn't provide any magic.

This is the key reason why e-mail is the preferred channel of communications for Nigerian Princes who want to give your inheritance (for a small fee) , bank phishing scams. and viagra resellers. E-mails can easily be spoofed and provide no clear trail to the guys running the scam, They can also be forged to appear real, unlike Facebook messages, or even Twitter Direct Messages that are far harder to spoof, and are usually only compromised if the user account has been hacked.

For completeness sake though, I have to inform you that there are certain technologies that do allow us to attribute an email to a specific sender, namely digital signatures--but hardly anyone uses them, and almost no lay person understands how it works. Other technologies that are built to work in the background like SPF, DMARC...haven't really taken off.

The point of course is that email is great for communication but provides no form of authenticating the sender--which is why your bank will never send you an important e-mail, it always does so by snail-mail. Snail-mails are also easily spoofed, but they're far more expensive to send, and most scammers may know your e-mail, very few will go through the trouble of finding your actual physical address.
<h2>What about those Prism documents eh?</h2>
<img class=" wp-image-4776 alignright" src="/uploads/12224127613_9e6586dae1_z-214x300.jpg" alt="Snowden" width="300" height="420" />But Keith...you protest. Don't you believe all the Snowden documents, and can't those have been elaborately forged as well. Why hold SarawakReport to such a high standard, but let Snowden pass under the bridge, I hear you say.

That's true. All the Snowden documentation (which I believe is 100% genuine) could have been easily manufactured in much the same as the 1MDB emails could have been manufactured--although I'm not accusing anyone of manufacturing those emails.

The difference isn't technical, the difference is Snowden.

Snowden is the source of the information about the NSA, and he identified himself as a contractor working for the NSA out of its facility in Hawaii. Meaning there's actually a background story as to how The Guardian and The Washington Post got the information they published.

More importantly, the NSA hasn't denied the validity of the documentation, and the fact that the US is hunting him down seems to add credence to the fact, not to mention the other sources of information that have served to further re-inforce the notion that the Snowden documents are valid, including engineers from AT&amp;T who claimed that secret rooms were setup in their facilities to sniff on the traffic of ALL their users, which jives 100% with all the Snowden revelations.

Unfortunately, neither SarawakReport.org or The London Times have come forward with their source, although from the e-mail trail it seems clear that it was Patrick Mahony whose emails were exposed, since all the emails are viewed from his perspective....and he is the one name present it all e-mails.

Without a source to validate the claim, the story that she miraculously came into possession of these emails seems a bit too convenient. I know there exist a code of journalism about revealing sources etc, but emails by themselves are a dime-a-dozen and really prove nothing. Even if the e-mails were given by a 'reliable' source, by their very nature, e-mails can be fabricated and forged, which make them useless as proof.

In any case, as much as I'm convinced Jho Low is crooked as a politicians spine, all I'm saying is that emails aren't proof--and they never will be.

And Maybe there is a backstory that I haven't read, and maybe even some have accepted the validity of the emails including the accused.
<h2>Other interesting facts</h2>
Which brings us to some other interesting facts--Jho Low, the man at the center of this controversy, accused for siphoning $700 Million dollars from Malaysia, the evil-genius with a chubby face....uses GMAIL as his primary email address!!!

You would think, a man of mystery and wheeling-dealings such as him wouldn't be using free email services, and you'd also think that a man like Patrick Mahony would begin to question someone making him offers in the Billions of dollars but can't afford a custom domain email address, like jho.low@sayatipumalaysia.com??

I'm just at a lost of word for why a guy architecting a multi-billion dollar deal, uses Gmail as his primary email. I really am, it's like would you trust a guy claiming to represent Malaysia in a multi-billion dollar deal if he drove a kancil?? Using Gmail is the e-mail equivalent of driving a kancil.
<h2>Conclusion</h2>
In any case, I'll just end by concluding that Email isn't really a good source of information. Everything said and written in emails, can be easily disputed and refuted, they do not have a property of non-repudiation.

Which isn't to say we shouldn't trust them--it's just e-mail shouldn't be considered evidence in a court of law (especially if the other party contest their authenticity).