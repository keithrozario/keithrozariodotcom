+++
title = "ATM Hacks are so bloody boring"
slug = "atm-hacks-are-so-bloody-boring"
date = "2014-10-01T22:31:11"
draft = false
categories = ['Malaysia', 'Security &amp; Privacy']
+++

![KLIA computer infected with Virus](/uploads/10710694_10152497851406888_323063805424206601_n.jpg)Last week, while I was flying from KL to London, I noticed a strange anomaly on the screen of the boarding gate at KLIA. Closer inspection revealed that it was an anti-virus warning that signaled the computer had been infected by a Virus (almost 2 days ago!!). As a techie, I quickly deduced 3 things from the screen.

<strong>One</strong>, the computer was running Windows, and probably an outdated version of Windows.
<strong>Two</strong>, the computer had been infected with <a title="conficker" href="https://en.wikipedia.org/wiki/Conficker" target="_blank">Conficker</a>--<a title="Conficker Worm" href="http://www.symantec.com/connect/articles/killing-conficker-how-eradicate-w32downadup-good" target="_blank">Conficker was a pretty infamous threat, back in 2008</a>!! And yet, here we are, at Malaysia's most prestigious airport, and we have a computer infected by a virus that pre-dates the iPhone 3G.
<strong>Three</strong>, the computer is probably part of a larger network, and never gets patched or updated--probably. If it were patched, it wouldn't be infected with a ol' grandmother of a virus.

As an added bonus--I could easily see the user of the system. That's a delicious bit of information for any hacker to have.

Heaven forbid, the virus on the computer screen at KLIA not spread to something important--like control tower or Sky Train controls.

These days, everything is a computer. Your phone is a computer, your watch will one day be a computer, so too is your car. But when was the last time you patched and updated these systems? When was the last time you updated the firmware on your router--or even when was the last time you updated the software on your laptop? Some of you probably haven't done this before--I'm looking at you Android JellyBean and iOS5 users.

So the display screens at the airport are computers--but so are the Automated Teller Machines (ATMs), and trust me when I say this, some of them run on windows....gasp!!<!--more-->
<h2>Unpatched systems are bad systems</h2>
When you don't keep IT systems up to date--they tend to be less secure. So it really comes as no surprise that old ATMs in Malaysia are now the target of a sophisticated hack that allowed them to dispense millions to south american gangs. If you're an IT guy that has listened to the constant news of much MUCH larger attacks at US supermarket chains, this is absolutely boring stuff. I mean boring with a Capital Z'.

First of all, ATM cash is cold hard cash--which may sound appealing, but that's a lot of cash to be lugging around. Digital cash, like credit card numbers can be sold on Russian black market forums for between 15-30 US Dollars each. So criminals these days are more interested in digital stuff than they are in cold hard cash.

Secondly, these involved physical machines, the criminals had to go to the ATMs to withdraw the money and expose their faces. Digital hackers that broke into Target, PF Changs and Home Depot have yet to been photographed let alone caught.

Finally, there's no way the criminals can automate this, they're required to go to each individual ATM and perform the Hack themselves. And now that Police are on their trail, it's likely the Police have staked out the ATMs and the gang is likely to be laying low. So really the total damage these guys caused is probably is probably the reported Rm2-RM3 million--that's boring.
<h2>![Latin_American_ATM_robbers-police-300914](/uploads/Latin_American_ATM_robbers-police-300914.jpg)Not a big deal</h2>
If you've worked in the IT department of a bank, Rm3 Million is a medium sized IT project--<a title="CIMB Core banking upgrade" href="http://www.thesundaily.my/news/962182" target="_blank">CIMB's core banking system upgrade cost them nearly RM1.1 BILLION</a>, what's a few million here and there. You might even argue that it cost less than actually updating these ATMs. So what's the big deal?

It's a victimless crime (unless you consider banks and insurance companies 'victims'). Yes, the police computer crimes unit is on top of it, but really, what are they going to do.

If you're all hung up about this, as <a title="Tan Eng Bee IT security" href="http://www.themalaysianinsider.com/sideviews/article/banks-should-enhance-their-it-security-tan-eng-bee" target="_blank">Tan Eng Bee from the MalaysianInsider</a> is--I must say, you haven't been reading the news lately. In her article she equates African black money scammers to these guys, even though the two crimes are completely different things. To be honest, the Malaysian banks have great IT infrastructure--I know. We're one of the first countries to move to EMV credit cards which reduced our card fraud to almost zero. The reason so much hacking is going on in America is because they still use Magstripe, <a title="Malaysia moves away from Magstripe to EMV" href="http://articles.economictimes.indiatimes.com/2005-07-14/news/27500609_1_emv-migration-malaysia" target="_blank">a technology we moved away from almost 10 years ago</a>. So just because a couple of ATMs get hacked doesn't mean our IT industry is inadequate or ignorant (her words!)--it just means a couple of ATMs got hacked.

If you want to look at IT security done wrong, look to Canada, where in January this year, two teenagers hacked into an ATM, by <a title="Teenagers hack into ATM" href="http://www.theinquirer.net/inquirer/news/2349210/teenagers-hack-atm-by-reading-the-instructions" target="_blank">following steps from the instruction manual</a>!! Apparently, the IT vendor didn't change the default password of the ATM, something most Unifi users don't change on their router either--so let's not point fingers so fast shall we.

Of course in the spirit of Malaysia boleh--I will remind everyone that Malaysia also has<a title="Malaysia boleh: 3 countries, 3 card-skimmers, all Malaysian" href="http://www.keithrozario.com/2014/06/malaysia-boleh-3-countries-3-card-skimmers-all-malaysian.html" target="_blank"> it's own criminals doing us proud abroad</a>.

Finally I want to draw your attention to this last photo. Look at the one on the bottom right--if you squint you can almost make out the pinpad of the ATM, this means that whoever has control of this CCTV also has visibility of you while you're entering your PIN on the ATM, which leads me to the most important piece of advice you'll get today. ALWAYS cover your PIN when you're entering it into the ATM--who never know who might be watching

For those still curious, Kaspersky Labs did a really great in-depth analysis of the malware used to infect the ATMs. This device originates from Russia and used all around the world, the malware was possibly created by someone and executed by someone else (there's a challenge-response halfway through the process, the crooks weren't calling an insider, they were calling the author of the malware). And true enough the ATM ran Windows...gasp!!! Link <a title="Kaspersky Blog take on the ATM hacking" href="https://securelist.com/blog/research/66988/tyupkin-manipulating-atm-machines-with-malware/" target="_blank">here</a>.