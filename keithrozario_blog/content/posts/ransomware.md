+++
title = "Ransomware"
date = "2015-10-12T11:44:34"
draft = false
tags = ['Spyware']
categories = ['CyberLaw', "Keith's Favorite Post", 'Security &amp; Privacy']
+++

<img class="alignleft wp-image-5215 size-full" src="/uploads/ransomware.jpg" alt="ransomware" width="259" height="194" />By now, you either know someone that's been a victim of nasty malware or have yourself been on the business end of nefarious software. The perpetual duel between security companies and malicious elements in cyberspace has changed dramatically over time, and no change has been so dramatic as the rise of a new type of threat, a threat we call...ransomware!!
<h2>...but what is Ransomware?</h2>
Ransomware is piece of nefarious code that infects your machine the same way any ordinary virus or spyware would. But what differentiates it from other threats is what it does after its infected a system.

Ransomware immediately seeks out specific file types like Microsoft Documents, Excel Spreadsheets, digital pictures, all for the purpose of encryption. Different Ransomwares target different file types, but the idea is behind it is to seek out these files that are considered particularly valuable to the user, and one that a user would pay lots of money to retrieve if ever lost. These files are then quickly encrypted using 'bank-level' encryption ciphers making them un-readable to the user.

Once the files are 'safely' encrypted, the user is usually prompted with the--Pay us money or never see your files again!!

The famous (or infamous) cryptolocker, would request payments only in bitcoin, before the decryption key would be released to the user, the malware has kidnapped your files and the only way to get them back is to pony up the cash.

In essence, cryptolocker held your files from ransom, in much the same way kidnappers hold kids for ransom in those hollywood movies, but unlike hollywood this is real, and the one and only way to get back the files is either pray for a miracle, or make the payment.<!--more-->
<h2>The origins of Ransomware</h2>
Believe of not, the roots of Ransomware trace all the way back to spam. Sapmmers realized sending unsolicited e-mail to millions of addresses about mundane things like viagera was a very lucrative business. So lucrative that the biggest players on the scene, a group called the Russian Business Alliance, were millionaires who drove expensive cars and drank fine champagne.

Brian Krebs wrote an amazing book,<a href="http://www.amazon.com/gp/product/1492603236/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1492603236&linkCode=as2&tag=keithrozarioc-20&linkId=HPD42FQKYK4ITXGW">Spam Nation: The Inside Story of Organized Cybercrime-from Global Epidemic to Your Front Door</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=keithrozarioc-20&l=as2&o=1&a=1492603236" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />, about spam that I cannot recommend enough, but the cut the long story short, the only way spammers managed to send out Billions of e-mails everyday was through something called a botnet.

A botnet is a large number of infected machines, comprising computers of everyday users who were implanted with a malicious code that would do the bidding of a control server, run by the aptly named botnet master. Basically, sending out billions of e-mails requires massive infrastructure in terms of computing power and bandwidth, and what better way to get that infrastructure than to steal it. A botnet is basically someone stealing cpu cycles and bandwidth from unsuspecting computer users throughout the world.

Botnets are hard to kill, because they are usually global in nature, and spread out among regular users who were innocently infected after they clicked links in e-mail. In fact, they're so rare, a botnet takedown is usually big news in the security community. It also didn't help that the Russian government usually turned a blind eye on activities of the botnet masters.

So authorities changed their tactics, rather than try to kill the botnets head on, the decided to take a more back-door approach. Authorities begun clamping down on credit-card payments made to the pharma spam lords, if the spammers couldn't charge customers for the drugs, they couldn't make money, and it didn't matter how many billions of e-mails they sent out if they could never charge the customer.

As each pharma spammer was denied the ability to accept payment, something authorities found much easier to do, than to take down the 'bullet-proof' servers or the botnets themselves, the spam soon stopped, and for a brief period we experienced a small victory.

But the victory was short-lived.

The spammers still had the large botnets operating to send spam, they just couldn't charge credit cards. So they turned to the one payment system that no government controls--bitcoin. But bitcoin usage is difficult and cumbersome, something very few end users would go through the trouble just to buy cheap Viagra,hence there needed to be something to 'encourage' the user to get down to using it. And what's more encouraging than holding all your precious files and photos for ransom?

The spammers, then re-tuned their botnets to send out spam designed to infect target computers with ransomware rather than sell generic cholesterol medication.
<h2>Can't I do tech-magic to get the files back?</h2>
Once users see that dreaded ransom page, most of the time the jig is up. The encryption used is usually too strong for any regular user to break on their own, and the few ransomware that have been broken are due to flaws in the implementation of the application rather than the encryption itself.

For example, Cryptolocker, which had such an elegant architecture, I can't help but admire it.

Cryptolocker would infect a machine, and use a special Domain-Generating-Algorithm (DGA), to connect to a command and control server. This DGA would be a sort forward rolling code, that made if difficult for authorities to identify what would be the next domain the criminals would use, hence allowing the malware authors to evade detection.

In any day, only 1% or so crypto-locker infected machines would be able to connect to a C&amp;C server, but that was good enough. Once logged onto the C&amp;C server, cryptolocker would retrieve the public component or a public-private keypair, to begin encrypting the files. This meant that the private key,<strong> the one needed for decrypting the files</strong>, never leaves the C&amp;C server, and hence once all the files are encrypted, there's no way the victim would be able to reverse the damage. The encryption used in cryptolocker is the same used to protect your connection to the bank, it's very strong, and technically unbreakable.

In layman's terms, if you think of a physical photograph album you have at home. Cryptolocker is like a burglar who sneaks into your house, and locks your photo-albums in a unbreakable box, while leaving the key to the lock secretly hidden away somewhere else. Even if you've caught the burglar, there's little you can do, as he's already locked the box, and now you have to pay him or risk losing the precious photo-album.
<h2>How do I protect myself?</h2>
Because ransomware infects the same way as viruses or spyware does, protecting yourself from it is the same as the others.

Use only original software, and make sure it's patched regularly. Install a good anti-virus, and preferably a firewall as well. Of course, the most important step to protect yourself is not to click on suspicious e-mails as that is the primary (though not only) source of infection.

But with cryptolocker, there's one step you can take to protect yourself even if you are infected, and have already lost all your files--and that's backup.

A properly executed backup process would make ransomware useless, as you could always go revert to the backup. There's one catch though, you have to ensure that the backup is <strong>off-site</strong> (meaning not on your local machine) and has <strong>versioning</strong>. A back-up on the machine is useless and next generation ransomware would probably seek them out and destroy them, and real-time backups are useless as the real-time backup would also be encrypted.You have to ensure you have the versions of the documents (before) they were encrypted.

The only true protection is a back-up with versioning, such as dropbox for business. When using a backup solution that has versioning, not only is your latest copy of a document is saved, but all previous copies are saved as well. Meaning you can view your document as it was 2 weeks, or 1 week ago, or even 1 day ago, to see how it's changed over time--but more importantly, if you have this, then all you'd need to do is to revert to a version before the ransomware got a hold of it.

A cloud backup solution that has versioning is the one and only true protection you have against things like cryptolocker. Of course most cloud based solutions like flickr for photos are also quite isolated and protected from these attacks.
<h2>Conclusion</h2>
There will always be bad guys and good guys on the internet, and while minor victories are possible, it's hard to imagine an internet that is both free and crime-free. I argued before that the price of freedom is the possibility of crime, the only way we will eliminate crime is to live in a police state, and in my mind, tolerating 'some' crime is better than an internet policed by the government.

Which means in a free society, criminals will always cook up new ways to extract money form you, while you have to either fend for yourself, or enlist the help of a private enterprise 'good guy'.

Many people think an anti-virus is a silver bullet solution to infections, they're not. A an anti-virus protects you from 'some' viruses, while a GOOD one may protect from 'most', but no anti-virus protects you from ALL of them.

As always exercise good judgement online, and if you're back-up your stuff. You gotta back it up to get it back.