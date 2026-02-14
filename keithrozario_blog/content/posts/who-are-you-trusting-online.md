+++
title = "Who are you trusting online?"
slug = "who-are-you-trusting-online"
date = "2014-07-20T22:44:53"
draft = false
categories = ['Misc', 'Security &amp; Privacy']
+++



![Trusting in an online world](/uploads/Trust.jpg)



When you get behind the wheel of your car, and hit the road--you're implicitly trusting ever other road user to play by the rules.  You trust no one will go out of their way to crash into you, or that no one would swerve into you for an insurance claim, you even trust that pedestrians won't hijack your car as you stop at the red light.

Sometimes you mitigate these risk, by locking your doors and keeping your distance, but fundamentally you're placing a lot of trust on your fellow road-user. You have no way of knowing for sure that they'll be good boys and girls--but you go about your daily car ride trusting that they'll do what is right. In cases where you don't trust anyone, you don't use the road. I know a lot of people who won't drive in India because they don't trust road users there--and some foreigners refuse to drive in Malaysia for the same reason.

Society works on trust, and without it--society just wouldn't work.

Think about it--you might not trust the restaurant waiter with your credit card--but you just ate at the restaurant without viewing the kitchen. Dying from poisoned food is far more serious than credit card fraud, yet you've trusted the restaurant not to poison you, but not with 16 digits from your bank. Sometimes you're trusting people without even knowing it.

And the same is true for the internet, The Internet Protocol(IP) that governs the whole internet till this day, is a highly 'trusting' protocol that prioritizes <span style="text-decoration: underline;">speed and simplicity</span> over <span style="text-decoration: underline;">security and privacy</span>. In much the same way that it's faster and simpler just to trust the restaurant not to poison you than it is to inspect the kitchen and verify the ingredients--the Internet Protocol accepts everything as true and routes data accordingly. Other protocols like SMTP and POP3 that are used for email employ the same levels of trust, that's why you can never trust an email--it's just too easy to spoof.

Essentially everyone on the internet trust everyone else to play by the rules. For example when Pakistan decided to block youtube in their borders, a mistake made by their local telecoms managed to take youtube down for several hours worldwide simply because everyone trusted the information Pakistan was sending them. Nowhere else in the world does such a high level of trust exist as on the internet--and nowhere else is it more dangerous.<!--more-->
<h2>The loss of Trust</h2>
![Padlocked car door](/uploads/131525153_0ed82a50e1_m.jpg)As the internet evolved for more than sharing cat pictures, the lack of security in the Internet Protocol became an issue. We soon realized that the internet had bad guys willing to exploit users trust--and we had to fundamentally re-engineer the internet. Unfortunately, you can't change the internet over-night, we're still using the very first version of the Internet Protocol for crying out loud! So instead of changing the internet protocol we've bolted on security as add-ons to the system, things like SSL/TLS now protect your data in transit over the internet. It's like placing a pad-lock on your car door because your car didn't come with a lock from the dealer. The underlying protocol isn't secure, so we've placed protocols on top of it to make it so.

These bolt-ons increase your security and privacy, but it doesn't eliminate your need to trust someone. You'll still need to trust 'some' people in order to reliably use the internet, and in most cases the number of people you need to trust is more than 1. The underlying premise is that in order for you to be sure this is a genuine Maybank website--you'll need to trust multiple parties along the way--forming a chain of trust. Chains of trust are practical, because if you trust Microsoft and Google, then you can trust who they trust without having to form individual relationships with every website or bank. But like any chain, if any link on that chain is un-trustable, the entire system is untrustable.

So for example you trust Rosmah (and really who wouldn't...she's such a nice lady), and Rosmah trust Ali--therefore you trust Ali. So when Ali says this website is well and truly Maybank, you believe it. But if either Rosmah or Ali betrayed your trust, then the entire system breaks down.

Philosophically you can have ask, how do you know Rosmah is who she says she is anyway? Which is the problem of the initial trust, and then of course once you trust Rosmah, how does the chaining of trust from you to Rosmah to Ali to Maybank work?
<h2>Step 1: Buying your machine (trusting the salesman)</h2>
[caption id="attachment_4501" align="alignleft" width="263"]

![You](/uploads/3345057291_cc0810b21a_z.jpg)

 You'd think twice before you trust this guy with your online banking.[/caption]

It's actually surprisingly complex system that starts out with you buying a new machine (whether it's a laptop, tablet or phone) and from that point of your purchase--you immediately trust the party you've purchased the laptop from. For instance you trust Amazon or Harvey Norman not to install keyloggers or malware on your machine when you buy it from them. Then of course you'd need to trust the actual manufacturer of the machine--whether it's Lenovo or Dell or Compaq, you trust that they dutifully installed original versions of Windows(or some other OS) on your machine without adding malware or keyloggers.

Finally you'll have to trust Microsoft, hoping that they didn't install back-doors in their OS for you.

This is why the Snowden revelations were so disturbing to the tech community--Microsoft it seemed was in bed with the NSA, <a title="Microsoft Zero Day Exploits Government" href="http://www.keithrozario.com/2013/07/should-malaysia-government-use-microsoft-products.html" target="_blank">Microsoft revealed 0-day exploits to the NSA before anyone else</a>, and the web-users who were using Windows had their trust in Microsoft betrayed. While there is debate as to how much information Microsoft shared with the NSA--there is no debate that every Windows users places a significant amount of trust in Microsoft (most of the time without even knowing it)

Trusting the salesman extends beyond computers as well--there's a huge controversy about US companies procuring Network equipment from Chinese companies like Huawei and ZTE, because when you buy a computer (and a router is a computer) you're trusting the manufacturer. The Pentagon reported that there could 'potentially' be backdoors in these equipment which is a bit hypocritical, considering the NSA has backdoor-ed many more things than China, some US officials were worried about a 'magic packet', a supposedly secret IP packet, that went sent to a router would immediately cause it to self-destruct, this is more fairy-tale than reality, but it just goes to show how much trust we place in the manufacturers of these equipment.

The point though is that even before you've booted up your laptop, you're trusting at least 3 people, the party that sold you the machine, the party that manufactured the machine and the party that manufactured the software--and if any one of these guys was untrustworthy your entire supply chain doesn't work. So if you've used pirated version of of Windows you're essentially trusting online pirates for your security, which is not a good thing!

The most important point of Step 1, it's the initial point of trust. You've trusted these parties, and therefore all your chains of trust originate from them. In other words, if they choose to screw you--you'll have no way to know. But if they truly are trustable, then the entire chains you build will at least have a solid foundation.
<h2>Step 2: Trusting the software</h2>
Your laptops don't normally come empty--they come installed with Operating Systems and Anti-virus, media playing software etc etc. All of that really is a waste of time. My advice is to delete everything except the necessary drivers and Operating Systems on your machine and get your own Anti-Virus and Media software.

In any case, at some point you'll have to trust the Anti-Virus to do it's job--these have proven less effective than before, and nothing replaces good judgement, not even the best Anti-Virus. However, people have come to trust Anti-Viruses to do their job, to the point where people with Anti-Virus software actually have more malware than people without them. Apparently having visible security like Anti-Virus software increases the risky behaviour of the users, they tend to visit 'dodgy' sites more hoping their anti-virus is some sort of silver bullet than can protect them from all threats--This is a case of too much trust placed on the Anti-Virus software, it's an ineffective placebo of sorts.

Then there's the other software you install, like media players and Office software, and Picture editors etc etc. When you download and install them--you're trusting them not to be malicious. Fortunately, you can chain the trust, Windows for example allows you to view the the Digital Signatures of the application you've downloaded, which means that at the very least the software originates from the Publisher it says it comes from.

If you right-click on an executable you download, there 'should' be a digital signature attributed to that, from that Digital signature you can glean if the AVG Anti-virus you've downloaded did indeed come from Checkpoint software (as it should) or whether it came from someone else. This isn't trivial and it has happened before, Gamma Corp, a dodgy as hell company that sells dodgy spyware to governments did this in our own country.

In the run-up to the Malaysian elections, Citizen Labs discovered a <a title="CitizenLab finSpy Malaysia" href="https://citizenlab.org/storage/finfisher/final/fortheireyesonly.pdf" target="_blank">booby-trapped word document that once opened would install spyware on the machine that would masquerade as firefox</a>. The document was titled "SENARAI CADANGAN CALON PRU KE-13 MENGIKUT NEGERI.” which of course meant that it was targeted at Malaysians, and since Gamma only sold software to governments--you can do the math as to who was behind the spyware installations.



![Fake vs. Real Firefox](/uploads/Fake-vs.-Real-Firefox.png)



The point of course is that the fake Gamma Corp Firefox, didn't have a digital signature, while the real Firefox did--but how many of you actually verify the signatures of applications you install? How many people know it's there?

The digital signature though relies on a chain of trust that starts from your OS (Microsoft, Apple or Linux..etc) to verify the authenticity of the application you're installing. But how does that chaining work?
<h2>Step 3: Trusting the Certificate Authorities (and their chains)</h2>
When you buy a copy of Windows, it comes pre-installed with a bunch of root-Certificates. A root-certificate is nothing more than Public Key of a trusted authority--aptly called certificate authorities (CA).

When you download a piece of software, that software (usually) has a certificate of its own, it's easy to verify if that certificate is genuine. At a very high level--the analogy is that the certificate of the software has been encrypted by the Private Key of an Authority you trust. Now all you need to do is decrypt the certificate using the Public key of that authority--which is in the root-certificate  pre-installed on your machine, and this allows you to trust the certificate of the application. This isn't exactly what happens (some hashing goes on etc etc) but it's a good enough analogy for now.

Only the CA has the private key to the public key installed on your machine--and if the application is encrypted with the correct private key, you can safely assume it's been vetted through by the CA you trust before they encrypted it.

This merely authenticates the software--the software comes from the right publishers--it doesn't mean that the software isn't a virus or malware.

The same concept works for Online browsing, when you visit Maybank or CIMBClicks for example, they will provide you a SSL/TLS certificate, which you can verify using the one of the root-certificates installed on your machine (Chrome and IE use the root-certificates of Windows, Firefox uses it's own set of root-certificates, choosing not to trust windows). but when you trust a certificate, it doesn't mean you trust the website--it just means you validated the certificate.

The next step is to verify that the website really does possess the certificate--because anyone who visits Maybank gets the same certificate, and can easily spoof the certificate on some other website. The trick here is, that the in the Maybank certificate lies a secondary public key--and because you trust that certificate you trust the public key. And all you need to do now, is encrypt something with the secondary public key, and challenge the website to decrypt it. If they succeed it means that they have the Private key and you can trust them--if they can't, you know that they're lying about who they say they are. The private key to the Maybank2u.com.my login is quite possibly the most important number in Malaysia, and it guards the millions of Maybank2u account holders from fraud and theft--imagine our entire financial system is protected by nothing more than a secret that's 'just' 600 digits long.*

[caption id="attachment_4499" align="aligncenter" width="500"]

![Maybank-Certificate](/uploads/Maybank-Certificate.png)

 The Actual Maybank2u.com.my certificate, with the chain of trust originating from the VeriSign Class 3 Root Certificate, all the way to Maybank2u.com.my, underneath is the 2048-bit Public Key (which is just 600 decimal digits long).[/caption]

However, the only reason you trust that 600 digit long number is because the Certificate authority on your machine formed a chain of trust to Maybank's certificate. And the only reason you trust that Certificate Authority is because it came pre-installed with Windows (or Firefox).

Now you see why having an illegal copy of Windows is not just bad morally, but it's bad security--because what's to stop the pirate from shipping the illegal DVD with additional root-certificates. Selling you an RM10 illegal copy of Windows is nothing compared to stealing your bank account.

Problems with certificates authorities are still common though--recently an I<a title="Indian Agency issues fake certificates" href="http://www.zdnet.com/indian-government-agency-issues-fake-google-certificates-7000031396/" target="_blank">ndian Certificate Authority decided to issue fake certificates that would have allowed malicious hackers to spoof Google websites</a>. That Indian certificate authority was one of the root-certificate holders in Microsoft Windows--meaning that all Windows users would have been susceptible to that attack, and even the most security savvy user wouldn't notice a difference--because there wouldn't be one.

So you trust Microsoft, who then trust these CAs, who then tell you that a website if genuine--and you have no reason to doubt them. Unless of course Microsoft turns around and tells you that the CA they used to trust, is no longer trustable--as in the case of the Indian Certificate Authority.

Which of course leads us to the last part of this very long post--how do you revoke trust? Trust like anything must not only be earned--it must be continually earned. Any system that perpetually trust someone (or something) is likely to have that trust violated at some point, instead there must be some mechanism to revoke trust, particularly in a chained world of trust that the internet operates on. The surprising thing is that while the mechanism to trust is straightforward and mutually agreed on--the mechanism to revoke trust is a huge controversy online, with different experts having different views. How certificates are revoked online is a strange process that differs by browser--but the fact of the matter is, there must be a way to revoke trust, because trust needs to be 'current'.
<h2>Step 4: Revoking Trust</h2>


![234217869_8ce0ad92ec_z](/uploads/234217869_8ce0ad92ec_z.jpg)



As we saw in step 3, as long a root-certificate on your machine validates a online certificate, that online certificate is deemed safe and secure. However, what happens if the bad guys manage to find the private key of the online certificate--how would the CA revoke that online certificate?

Now we have the final piece of the puzzle, an Online Certificate Status Protocol (OCSP) server. A server whose one and only job is to provide a real-time response to queries for the status of a certificate. So for example if you had a website that had a certificate issued by a trusted CA, but then one day you discovered your website was hacked and someone compromised your private keys tied to that certificate. What would you do?

You'd report the issue to the CA, and the CA in turn would update the status of the certificate in their OCSP server to 'revoked'.

Then when any visitor that was maliciously presented with your revoked certificate does and OCSP request--they'd find that the certificate was revoked and would then know that the site they're visiting was comprimised. Firefox checks the OCSP status for all certificates its presented--Google Chrome never checks for OCSP status. This is where the controversy around certificate revocation starts--and it hasn't ended. Google Chrome instead has something called CRLSets (Certificate Revocation List Sets), that simply default store all the revoked certificates within the browser itself--which is faster in operation but less secure because it no longer is in real-time. Also Chrome doesn't store all the revoked, just the 'important' ones--which isn't good.

You can check if your browser supports revocation by visiting <a title="Revoked Certificate GRC" href="https://revoked.grc.com/" target="_blank">revoked.grc.com</a>.

So that's why I use Firefox and no longer use Chrome. When you use Firefox you trust Firefox root-certificates (not Windows) and you get real-time OCSP checking. When you use Google Chrome you trust Windows root-certificates (which have issues) and you don't have real-time OCSP checking. In either case, you should never use IE.

The point though is that this last-bastion is what completes the chain of trust:

You Trust the Laptop salesman, and you Trust the laptop manufacturer and you Trust the OS manufacturer (for example Windows). Then you Trust Windows, who trust a whole bunch of root-certificates, and those root-certificates have trusting relationships with almost the entire internet. However, to cover your ass, you finally check that chain of trust against an OCSP server, before you finally trust that the website you're visiting is a genuine one.

OCSP is really important, if someone manage to compromise that 600-digit key that protects all of Maybanks customers, at the very least, the OCSP server would serve as a last defense against any attack. It would prevent hackers from creating phony Maybank websites, because browsers would immediately detect the revoked certificate.
<h2>Conclusion</h2>
To be honest, I had no idea how complex the chains of trust we use everyday really were until I researched them for this post. There's so much going on when you visit a website to most people it's almost like 'magic', and just like magic, they'd rather not know how it works.

But unless you really know who you're trusting online to protect you from the bad guys, you can't make informed and good decisions about your own personal security while browsing the nasty vicious shark tank we call the World Wide Web. This post is long-winded and a bit on the 'bla bla bla' side, I hope to concise it over the coming months, but hopefully you read it to the end and really understood who you're trusting online.

Until then, stay safe, and remember--if it ain't Green, don't login.

<span style="color: #999999;">Picture courtesy of <a title="Fiddledydee" href="https://secure.flickr.com/photos/fiddledydee/" target="_blank"><span style="color: #999999;">Fiddledydee</span></a>,<a title="Vertigogen flickr" href="https://www.flickr.com/photos/vertigogen/234217869/in/photostream/" target="_blank"><span style="color: #999999;"> vertigogen</span></a>, <a title="Computer Salesman" href="https://www.flickr.com/photos/mc_sensei/3345057291" target="_blank"><span style="color: #999999;">Michael Stout</span></a></span>,

<em> *I used digits to mean regular decimal digits. The real Maybank Public Key is 2048 Binary Digits (or bits) long, which converts to roughly 600 decimal digits.</em>