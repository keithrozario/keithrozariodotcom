+++
title = "So you got hit by Ransomware"
slug = "so-you-got-hit-by-ransomware"
date = "2017-02-23T21:28:54"
draft = false
tags = ['Ransomware']
categories = ['Security &amp; Privacy']
+++



![](/uploads/Petya.jpg)

Last Monday, I got a text message from my uncle saying his office computer was hacked, and he couldn't access any of his files. Even without probing further, I already knew he'd been hit with ransomware and was now an unwitting victim in a criminal industry estimated to be worth Billions of dollars.

After learning a bit more, I found out that the IT guys at the company backed up their data (which was good), but stored all backup files on the same computer (which was bad). I guess they kept it on a different hard-drive which mitigated the risk of hard-disk crashes, but didn't effect any other type of risk. What if someone had broken into the office and stolen the whole computer? What if the Office was burnt to the ground or flooded? With all the backups on the same computer these risk would completely wipe out all their data--even if the files were stored in separate drives.

Ransomware is particularly interesting, the 'industry' has experienced tremendous growth the last 2 years, and it's now the number one cyber-threat small business owners face. But before going into ways of addressing the threat, it's important we understand cyber-threats in general, and for that we need the CIA.
<h2>Confidentiality, Integrity and Availability (CIA)</h2>
No, not the spy agency, but the acronym that stands for Confidentiality, Integrity and Availability.The three pillars make up the InfoSec Triad, and a threat is something to affects any one of the them.
<ul>
 	<li>Confidentiality means keeping the data confidential only to authorized users</li>
 	<li>Integrity is assuring the accuracy and completeness of data and that it hasn't been tampered with</li>
 	<li>Availability refers to the ability to make it available on request</li>
</ul>
People often focus on Confidentiality, going all out on setting strong passwords, file encryption and firewalls to protect data for being siphoned out. But security threats, like Ransomware and DDOS attacks, do not affect the confidentiality or integrity of data--and the protections you put in place to help with confidentiality and integrity are useless against them.

File encryption, a necessary tool to protect  the confidentiality of your data, does not protect against ransomware attacks (you can still encrypt and encrypted file), and setting strong passwords does not protect your website from being hit by a DDOS.

There is no panacea in cyber security, only specific actions to address specific threats, and unless you're addressing availability threats like ransomware and DDOS attacks, your general anti-virus is quite useless against it. So let's breakdown the Ransomware threat and see how its evolved to become the darling of cybercriminals everywhere.<!--more-->
<h2>Ransomware : An Introduction</h2>


![](/uploads/20012126873_c644607795_m.jpg)

Typically ransomware finds some way of entering your system, and then starts encrypting files based on specific extensions (.doc, .xls, .pdf..etc) Once all the files are encrypted, a prompt for payment is displayed, stipulating that failure to pay will result in you losing your files forever. The attackers have a secret decryption key, known only to them that will allow for the decryption of files back to their usable state, without this key your data is useless.

Clever criminals only use standard encryption (and so should you), which means the encryption is practically unbreakable. It's ironic that the same encryption used to protect your online banking, is used by criminals to enable their ransomware operation. Which also means the ransomware has the same 'quality' of protection as online banking (very simplistic but you get the point)

It's like the same guns used by police to protect you are also used by kidnappers and robbers. Ransomware, as the name suggest, is akin to kidnappers taking your child and extorting a ransom, only instead of children they're using data.

But unlikely kidnapping, your files never leave the network. They are encrypted, in place, and left on your computer where they were found. No data is ever sent back to the criminals because they don't want to host expensive servers to receive files, most of which are mundane documents. boring powerpoint slides, or (God forbid!) family photos.This lowers their exposure to the outside world, the only contact you make with them is when you got infected, and when you pay the ransom, everything in-between that taken care of by software.

That piece of software is what we generally refer to as Ransomware, and boy has it grown over the years.
<h2>Ransomware evolution</h2>
Ransomware has evolved over the years, not only are they now able avoid detection from most anti-viruses, they also have innovative approaches on what to encrypt and how the encryption takes place.

<a href="http://www.securityweek.com/petya-ransomware-encrypts-entire-hard-drives">Petya</a>, a ransomware that emerged last March, encrypted the master boot record (MBR) of the disk, a tiny but vital piece of data that enables your computer to boot up. Think of the MBR as the ignition on your car, it may be much tinier you car, but your car doesn't work without it. By aiming for the MBR rather than individual files, Petya could ransom 100's of Gigabytes of data in mere seconds, something traditional ransomware that encrypted each file would take hours to accomplish.

Innovations like Petya, are littered all over the world of ransomware and because these are all criminals, these innovations can't be patented. Hence, every innovation is then <a href="http://www.securityweek.com/upgraded-petya-malware-installs-additional-ransomware">built upon</a> and<a href="http://www.securityweek.com/satana-ransomware-encrypts-mbr-and-user-files"> expanded</a> by other criminal groups running their own operations. Eventually though this led to a logical conclusion, something that is a typical for any IT operation--ransomware was outsourced!

This trend is called <a href="http://blog.trendmicro.com/outsourcing-crime-how-ransomware-as-a-service-works/">Ransomware-as-a-Service</a>, and involves operators <a href="http://www.businessinsider.sg/ransomware-as-a-service-is-the-next-big-cyber-crime-2015-12/">selling ransomware software for other criminal operations to use</a>. That way, organizations with specialize spam and phishing skills, can focus on blasting emails and creating fake websites to infect victims, while leaving the coding of the ransomware to a 3rd-party. It also means that skilled programmers who have little knowledge running a extortion racquet, can focus on writing their programs instead of getting involved with business operations.

This criminal supply-chain is both sophisticated and efficient, and a win-win for everyone...except the victims. But innovation doesn't stop there, it extends much further into places you least expect.
<h2>Marketing innovations in Ransomware</h2>
If you can't build a better Ransomware, maybe you can market the one you have better.

We've had ransomware that promised to <a href="http://www.digitaltrends.com/computing/ransomware-claims-to-donate-money-to-charity/">'donate' a portion of their proceeds to charitable organizations</a>, appealing to their victims sense of charity, and yet another that promised to decrypt your files <a href="https://www.theregister.co.uk/2016/12/11/ransomware_offer_pay_us_a_770_ransom_or_infect_two_friends/">if you helped them infect two other computers</a>. The<a href="https://nakedsecurity.sophos.com/2017/01/16/spora-ransomware-goes-freemium-with-four-different-payment-options/"> Spora ransomware</a> that hit my uncle's office, actually promised 'immunity' from future infection, for roughly RM5000. The best part is, the same IT guys that thought it was a good idea to backup everything onto a single computer, recommended they not just pay the ransom, but get the 'immunity' package as well. <em>*face* meet the *palm*</em>

Spora even goes further, by offering discounts for people who were willing to leave a review of their 'support' service on the <a href="https://www.bleepingcomputer.com/forums/t/636975/spora-ransomware-support-and-help-topic/" target="_blank">Bleeping Computer Spora ransomware thread</a>. A bleeping computer article goes on to say:
<blockquote>the Spora gang has offered a 10% discount to a company that suffered Spora infections on more than 200 devices. The researcher calls Spora's customer support <strong>more user-friendly and helpful than the customer support service provided by many tech companies today</strong>. On the other hand, we call it "smart PR" instead, since crooks have everything to gain from "being nice" to their customers. - <a href="https://www.bleepingcomputer.com/news/security/spora-ransomware-sets-itself-apart-with-top-notch-pr-customer-support/">BleepingComputer</a></blockquote>
If this were any other industry, donating proceeds to charity, or offering free services in exchange for referrals would be standard marketing gimmicks, but these are criminals--with customer service!!! What gives??!!

What gives is that this isn't your average criminal organization, standard operating procedure for drug lords  is to ensure that they control specific 'turf', and that competition in their turf wouldn't be tolerated. But on the internet, there's no such thing as turf, and there's no way to eliminate the competition. Crime lords have accepted this and evolved into the new competitive environment on the internet.

In the end, we have criminal organizations committing crimes, but behaving like multinational organizations, with sophisticated supply chains, marketing departments and even customer support. It's a new breed of criminal, and one that targets small business owners, private citizens and even <a href="http://www.bbc.com/news/technology-35880610">hospitals</a>, while law enforcement can only look on.

So what can YOU do if you come face-to-face with this new threat?
<h2>How to respond to Ransomware</h2>
If you get hit by ransomware, the chances of getting back your data without paying the ransom is slim (but not zero).  All forms of ransomware have their own branding around it, with cool names like Spora or Petya, try googling the name to see if anybody has released a fix/restore for the ransomware in question. It'll at least give you an indication of how you got infected.

The next question is whether you should pay? I suggest you don't.

There's no guarantee you'll get your money data back once you pay them. Most of the time you probably will, it's bad publicity for the ransomware to not give you the data back, but there's no small claims tribunal you can go to for protection or consumer affairs department. Once the money leaves your hands, you're at the mercy of common criminals.

Finally, paying a ransom, legitimizes their business. If nobody paid ransoms, nobody else would get hit by these things, because criminal gangs still need money. The boom in ransomware is because victims pay, and these guys can smell cash a mile away.

It's a vicious cycle, as more victims pay, more criminals join in the fun, creating more ransomware, which creates more victims. which means more victims pay.

So if you get hit with ransomware, you should probably take one for the team, and swallow your loses and move on. Just bear in mind that if you don't pay, you won't get your data back, and you should probably take steps to protect it while you have it. So how do you avoid being victim?
<h2>How to avoid getting hit by Ransomware</h2>
First, get an off the shelf anti-virus. I don't do recommendations for anti-viruses here, but any 'reputable' vendor would be fine, this mitigates the chances of you getting hit.

Second, get a cloud backup solution that has versioning. Remember, it must have versioning, repeat after me, ver-sion-ning!

Real-time backups alone don't work, because as soon as the ransomware encrypts your files, the encrypted version is backed up to the cloud, destroying the 'good' copy. Instead what you want is something like Dropbox, that stores not just the current version of your file, but every version you made for the last 30 days.

If you get hit by ransomware, you just revert everything to the previous version (prior to the encryption) and you'd be good to go. Dropbox cost just $99/year. A ransomware hit can cost you 5 times that amount. A cloud backup solution with versioning is the only true way to address the ransomware threat--everything else is a matter of probability and chance.

Plus if your office gets robbed, or flooded or burnt to the ground, all your data is still secure.
<h2>Conclusion</h2>
Ransomware is pretty interesting, of course not to the victims, but from a outsider perspective it's interesting to see the amount of innovation happening in the ransomware space.

Hopefully you have a better indication of what it is, and how you can protect yourself.