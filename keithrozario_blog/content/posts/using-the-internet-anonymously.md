+++
title = "Using the internet anonymously"
slug = "using-the-internet-anonymously"
date = "2015-09-11T12:25:53"
draft = false
categories = ['Misc']
+++

<a href="/uploads/314989744_5b5a852b47_z.jpg">![Spying Program](/uploads/314989744_5b5a852b47_z.jpg)</a>While anonymity on the internet is slowly dying, there remain legitimate reasons for wanting to keep your online identity a secret from <del>those meddling kids, </del>governments or snooping criminals. From e-mailing leaked documents to commenting on blogs using pseudonyms or even just casual online chatting, utilizing the internet without leaving digital bread-crumbs behind you is a task that is getting more difficult over time, particularly when the big bad wolf that's chasing you down is a rich and powerful government agency.

But to secure yourself online, you first need to understand whose attacking you, and what techniques they're using. Adjusting your defense to suit your attacker is not just common sense, it is the only practical way to achieve a semblance of security and anonymity online without losing your mind and going into tin-foil hat wearing paranoia.

For example, if your adversary is the NSA, there's nothing much you can do. This is a Federal agency so well resourced, they're building a data-center in Utah that's bigger than 5 Ikeas.Add to all this, the fact that it hires the cream of the crop from the Ivy-league maths programs, and you have brains and brawn that are orders of magnitude higher than the average person. If the NSA wants to target you, it's game over. The only reason you're not targeted by the NSA is that you didn't factor high enough on the wanted list to merit their attention and taxpayer dollars.

But how about the Malaysian Government? How sophisticated are they and is it Game-over if the Malaysian government were targeting you?

Fortunately, our Governmen isn't building a Utah data-center, or a Great Firewall and they're no where close to the NSA, but they're still a well-resourced organization that has the technical capability and financial muscle to do some serious harm against an ordinary citizen. And in order to secure yourself against them, you'd need to understand their techniques and tools.
<h2>Malaysian Government Surveillance 101</h2>
<a href="/uploads/4638981545_f0578a16fe.jpg">![Childrens Privacy](/uploads/4638981545_f0578a16fe-300x168.jpg)</a>Firstly, the government controls the ISP and Telcos, and hence the Government controls the network. The prevention of terrorism act (POTA) permits a P<a href="https://www.keithrozario.com/2015/05/the-technological-effects-of-sosma-and-pota.html">olice Officer to waltz into any ISP or Telco and compel them to grant him your communication details</a> without the need for any kind of judicial warrant, it also allows for the Police to place a digital wiretap on your communications (again without a warrant), but also without ever having to reveal the status of that wiretap to any court of law even if they convict of something. So anytime you're using a Malaysian internet connection, you have to assume that the connection is compromised.

Thankfully, whenever I go into a starbucks, or use the WiFi at KLIA, I already assume the network is compromised--and there's many ways to secure yourselves over a hostile network.

Secondly, the government has a record of <a href="https://www.keithrozario.com/2013/05/the-malaysian-government-is-spying-on-you-finspy-fisher.html">purchasing surveillance spyware</a> (<a href="https://www.keithrozario.com/2015/07/hacking-team-got-hacked-and-heres-what-malaysia-bought.html">twice!</a>),  These are specialized software designed to infiltrate your laptop or smartphone, and start sending all your communication data direct from source. Again, one has to assume there is no judicial oversight over the use of these things.

If your end-device is compromised, and the Government has already installed spyware on your phone, laptop, tablet or even smart TV, there's nothing you can do on the network end to secure things. So it's wise to start securing the device before you think about the network, and that's where we'll begin.

But there's a last and final attack-vector that a government can employ. Simply breaking into your home, and taking your laptop and smartphone away from you. Which means that you don't just need to secure your device and network when you're using it, but also when you're NOT using it. In computer-geek circles we call this securing your data at rest, which protects your data while it's just idling somewhere, and it turns out that's not entirely easy to do either.<!--more-->
<h2>Device Protection</h2>
<a href="/uploads/Secured_VPN.jpg">![Secured_VPN](/uploads/Secured_VPN-300x199.jpg)</a>From all the documentation I've read about the <a href="https://www.keithrozario.com/2015/07/hacking-team-got-hacked-and-heres-what-malaysia-bought.html">Hacking Team breach</a>, it's clear that hacking team had the ability compromised Windows and Mac devices, and rooted android phones. Our government buys a lot of their surveillance software from an open market, and the open market is dictated by supply and demand, and since the demand for Windows and Mac vulnerabilities far exceeds that of Linux vulnerabilities, you're far safer using Linux. The open market dictates this, which makes the governments purchase of surveillance software for Linux economically and financially unsustainable (not technically impossible).

Also never root your phone, or trust un-verified sources. Download all your software from the official appstores of the platform you're using, whether it's the Apple appstore, or Google Playstore, or even Windows and Macs, getting your downloads from verified and trusted sources severely limits your chances of getting infected (though again it's not impossible). By the way, Apple iOS devices seem to be the most secure devices around--which may justify their high price tags for those who can afford them.

Rooted &amp; Jailbroken are synonyms for 'insecure'. Securing a device requires some specific advice which I won't go into here, but suffice to say if you use Ubuntu from a USB-Drive, with no persistent memory, you're probably 99% secure from an adversary like the Malaysian Government. By not having persistent memory you ensure that malware on the device gets wiped out on the next reboot, and by not using the hard-disk your RAM gets wiped-out on the next reboot as well.

So if you're busy writing an e-mail to a journalist, and the police are barging in your front door, simply hitting the restart button on your machine, ensures all the data is safely and securely wiped out.

However, Ubuntu is beyond the reach of most. It's free software, but the general public probably isn't used to it, so asking people to use it would be quite useless advice. A practical alternative is a Chromebook, which runs on Linux, and is quite good as well.However, be wary not to over-rely on the usage of a non-mainstream operating system, securing yourself requires effort and knowledge, and just fully relying on a computer system isn't going to cut it.
<h2>Uses of service</h2>
Now there's no point using Ubuntu and securing your device, if you then go out and use a Malaysian E-mail provider or some other locally paid service. The government has too much power over local businesses, and a paid service leaves a money-trail.

As counter-intuitive as it sounds, if your adversary were the Government of Malaysia, simply using G-Mail and Dropbox on a secure device is probably enough to thwart any effort to spy on you. G-mail has the added benefit in that so many people use it--which blurs the battel-field for your adversary because there's so many innocent targets in the way.

Of course if your adversary were the NSA, it's a different story, and if you think that our local kerajaan is working in cahoots with the NSA, this wouldn't work--and you'd have to be some really bad-ass terrorist.
<h2>Network Protection</h2>
Once your device is secured, and you're sure about the confidentially and integrity of the services you're using, the final bit is securing the network traffic.

As I mentioned before this is quite easy to achieve. The easiest and simplest way to achieve this is via encryption--that's when the data you transmit over the network is scrambled up in a way that no one except the intended recipient can un-scramble. Your connection to this blog is encrypted, via a technology known as TLS (or sometimes called SSL or https), which means that all the data from my site to your computer is un-readable to anyone in between.

But there is still meta-data. Someone on the network can still figure out that you're visiting my site, they just don't know which post it is, or which topics you're browsing, they know how long you're spending on my site, and how often you visit. Meta-data is still a pretty strong indicator of certain things, and encryption doesn't hide meta-data.

If you want to make sure that the government can't even see what websites or pages your visiting, then you need to anonymize your data (which isn't the same as encrypting). And the one encryption tool that comes to mind is TOR. But there's good reason to a be bit skeptical about TOR, about a year back two researchers were promising a talk about how they broke TOR anonymization for less than $3000. That talk was <a href="http://www.theguardian.com/technology/2014/jul/22/is-tor-truly-anonymising-conference-cancelled">cancelled</a>, and subsequently the US Government 'suddenly' manage to catch the <a href="https://en.wikipedia.org/wiki/Dread_Pirate_Roberts_%28Silk_Road%29">operator of the biggest online black-market </a>inside the TOR network.

I still think TOR provides anonymity (though not secrecy), but the reason I don't recommend it is that it's easy to miss out and get wrong. The Vidalia browser most people use for TOR looks identical to Firefox, and sometimes you just forget which is which. Also, Vidalia doesn't send all network traffic through TOR, only its traffic.

A simpler solution would be a VPN, and unfortunately VPNs require you to pay money (which leaves a money trail). It's a compromise, but in a world with no perfect solution, a compromise is necessary.

So after you've installed Linux on a USB-Drive with no persistent storage, and encrypted your connection using a VPN, how do you now transfer data to your journo-buddy or get data from your source?
<h2>E-mail</h2>
<a href="/uploads/15197804185_d4a1f3d9b3_m.jpg">![15197804185_d4a1f3d9b3_m](/uploads/15197804185_d4a1f3d9b3_m.jpg)</a>As archaic as it sounds e-mail is still the defacto method of communication for most people. Unfortunately, e-mail is terrifyingly insecure, it's not encrypted and in most cases not authenticated either. People can mistake e-mail addresses that were maliciously made to look similar, like keith@micros0ft.com and keith@microsoft.com may look identical, but one had microsoft spelt with a zero '0' instead of the letter 'o'.

How do you secure this? First off using your own e-mail server is a definite no-no, you're not <a href="https://en.wikipedia.org/wiki/Hillary_Clinton_email_controversy">Hilary Clinton</a> and even she got it wrong.

Secondly, using a e-mail provider that claims to 'respect your privacy' might help, but there is a way to securely use g-mail without having to trust Google. Which means you can rely on the Google infrastructure, and the fact that everyone in the bloody world using G-mail to secure your communications, but then encrypt your data using your personal keys to the point where even Google can't decrypt it.

It's a technology called PGP, and the setting of it is quite difficult for a lay-person. Edward Snowden struggled to get Glenn Grenwald to use PGP, because Greenwald was a great journalist but pretty much a tech-illiterate.

In any case, the concept relies on public private key pairs, when both sides can generate their own public-private key pairs and exchange only their public keys with each other. Thereby every e-mail encrypted with the public key of one party, can only be decrypted by the private key of that party.So even though you're relying on Google Servers to send this info, and Google can see the e-mails, they'll only be seeing a jumbled-up encrypted message.

If you want to contact me securely, send me an e-mail using this <a href="https://www.keithrozario.com/2015/04/keiths-pgp-key.html">PGP key</a>.

But here again we run into the classic 'meta-data' vs. 'content' discussion. When you register for a Gmail account, Google verifies your phone number, which means that they know who you are (no burner phones in Malaysia). But the same principle applies, and you can use PGP on any e-mail provider.
<h2>Securing Data-at-rest</h2>
Finally we land on securing your data at rest. You may have done everything correctly, but then you left your files on USB drive at home, and while you're out for dinner an attacker breaks into your home and copies it, or steals it. Worse still, what if the attacker breaks into the home while you're still in?

If you're hoping to leak out Gigabytes of data, ensuring that data is protected while it's sitting on a USB drive of your hard-disk is absolutely paramount. Securing the data while its in transit is not enough.

Fortunately, there are a few disk level encryption software that protect this, but even if all else fails using something as simple as WinZip and encrypting the payload with AES-256 and a strong password is most often enough to thwart an attacker.
<h2>Conclusion</h2>
Hopefully you'll never have to feel that your Government is out to get you, and be forced to take these pretty 'extreme' steps. But if you are, at least you can take comfort in the fact that the universe wants you to keep secrets.

We've built encryption technology that is so asymmetric, that a 5 year old laptop can encrypt a message so securely that even the US government wouldn't be able to break it. There is no physical world equivalent here, as nothing you build or construct could withstand the might of the US Military--fortunately secrets aren't traded in physical world.

But we need to be clear that Device Security, Network Security and Data security, are 3 different things that need to be tackled. A lot of 'security' software usually only achieve one of these but advertise themselves as a panacea for securing yourself, don't be fooled online anonymity is hard to accomplish, but not impossible, and if you're hoping to leak out government secrets, its important you take all the steps necessary.

Don't be fooled by gimmicky software offering 'military-grade' encryption, implementing the encryption correctly is usually quite hard.