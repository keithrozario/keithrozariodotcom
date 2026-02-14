+++
title = "Relax dear-citizen your contactless card is relatively safe---ish"
slug = "relax-dear-citizen-your-contactless-card-is-still-relatively-safe-ish"
date = "2016-12-31T10:37:17"
draft = false
tags = ['Card']
categories = ["Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

<p style="text-align: left;">![](/uploads/19205891971_2abaa89036_z-300x300.jpg)As Malaysia slowly (but surely) migrates to Chip and Pin, some banks have taken the opportunity to issue not just new Pin-enabled cards, but contactless-enabled ones as well.</p>
To be clear, Banks are only mandated to issue new Pin cards <em>(replacing the signature cards you had before),</em> but are taking the opportunity to also embed contactless capabilities into them as well. After all they're already issuing new cards to every (single!) card holder, might as well get them on the contactless bandwagon while they're at it.

The reason for being so gung-ho about contactless is purely economical. Research suggest that the easier payment methods become, the more money people are willing to spend. People with credit cards spend more than people with just cash, and 0% interest schemes have been a godsend to retailers. Contactless payments, which don't involve cumbersome Pins or signatures, are clearly the next evolutionary step, with <a href="http://www.iises.net/download/Soubory/IJOES/V3N4/pp70-98_ijoesV3N4.pdf">one research paper suggesting they increase customer spending by nearly 10%</a>.

Banks make money from small percentages per transactions, the more transactions at higher amounts, the more money they stand to make. So if an extra dollar worth of electronics in a contactless card increases revenue by 10%--why not?!
<h2>Pins are for security, Contactless is for convenience</h2>
But while PINs are a security feature, contactless is all about convenience. And conveniences trade-off security, so it stands to reason that contactless cards are less secure than regular 'contact' ones.

The question is whether that trade-off is worth the increase in convenience. After all, nothing is absolutely secure, and in today's criminally infested internet, <a href="https://www.keithrozario.com/2016/09/the-safest-place-for-your-money-is-under-the-mattress.html">keeping your money under the mattress is safer than keeping it in a bank</a>--but nobody does it because the mattress would be too inconvenient.

So what convenience are you getting with a contactless cards?

For one thing, no more waiting for a receipt printout to sign on, or bending down to an inconveniently placed pinpad to type in your PIN. Plus, for someone with gigantic fingers like me, I jump on the opportunity to avoid having to fidget with pinpads that must have been designed for dwarf children after they've been struck by the ray gun from <em>Honey I shrunk the kids</em>.

But that's about it--the only convenience contactless cards provide is that you can do contactless payments--up to a specified amount.

The question now is what security trade offs are you making for this <em>remarkable</em> feature?<!--more-->
<h2>The security considerations</h2>
Well contactless cards are by nature -- contactless!

While regular ol' <em>contact</em> cards need to be physically inserted into a terminal to be read, contactless cards can be read 'over the air'. I've seen people tap their entire wallets at the readers to make payments,  which means anyone <a href="https://thomascannon.net/blog/2012/03/bbc-watchdog-contactless-cards/">can build a reader capable of extracting information from your card, while it's in your wallet or bag</a>.

The electronics to build such a reader is remarkably cheap and simple to build, after all, the specifications for something as pervasive as credit cards aren't exactly state secrets. Just watch <a href="https://www.youtube.com/watch?v=elBWoMXt3WY&amp;t=73s">this video</a> to see how easy it is to do--this one even does it with a <a href="https://www.youtube.com/watch?v=eJQvnRMQkgo">rooted android phone</a>.

And what data do criminals get from these readers? Your name, credit card number and card expiry date, a remarkable amount of data for very little effort.

So the cards are easily read, even while still in your wallet or bag. The bigger question though is what can they do with the data?

The answer is not much. <em>(meh!)</em>
<h2>How Credit Cards protect themselves</h2>
Credit card transactions are divided into two broad categories, card not present (CNP) and card present (CP) transactions.

Card Present (CP) transactions are the general in-store purchases you make with your credit card present. In these cases, the credit card terminal uses cryptography to authenticate the card, in other words the terminal has ways of making sure the card is genuine. And the general consensus is that any Chip card (whether it's a PIN or Signature one) is un-cloneable.

The method used to protect the secret-key on these cards is comparable to the method used to secure iPhones. So rest-assured that just having name, credit card number and expiry date is insufficient to clone a credit card. You need the card's secret-key, and that's going to take more than a rooted android phone to extract.(a lot more!)

In other words, while criminals may be able to read your contactless card while its still comfortably in your pocket, they'll be unable to clone it.

But what about those transactions that don't require a card at all? What about the card not present (CNP) transactions?

CNP transactions generally refer to online transactions where the physical card isn't present. The cardholder (or a criminal impersonator) is merely entering numbers into a web browser. I could call my wife today, give her the relevant details of my card, and get her to book me a flight to Bora-Bora, and no one would know whether she had the card or not--but the transaction would be approved.

<a href="/uploads/CVV2.jpg">![](/uploads/CVV2.jpg)</a>To combat fraud for CNP transactions, cardholders are forced to enter their CVV2 number to authenticate a transaction. The CVV2 number is the 3 (or 4) digit number printed at the back of your card (or front if you're using American Express). CVV2 is not stored electronically on the card, only printed on the back, since it's designed for humans to read and enter manually into web browsers. Because it's not electronically <em>stored</em>, it can't be electronically <em>read</em>.

Which means the data read by a malicious drive-by contactless card reader <strong>isn't sufficient</strong> to perform either offline or online transactions.

Phew!

Bank Negara's official statement, <a href="https://www.facebook.com/bnm.official/photos/a.492310539871.272673.83552599871/10154571535289872/?type=3&amp;theater">which was released on facebook</a> <em>(because it's 2016, and official statements from central banks now go on Facebook) </em>stated long-windedly that:
<blockquote>• Contactless cards have an embedded chip...renders a contactless card almost impossible to be cloned or counterfeited; and

• Malaysia has adopted a stronger authentication method...To authenticate an online card transaction, cardholders are required to enter a transaction authorisation code (TAC) that is sent to their mobile phones or security device. In the event the card details are misused to conduct a transaction at an overseas merchant’s website that <strong><em>has not implemented a stronger authentication method</em></strong>, Malaysian cardholders are protected by the liability shift rules introduced by the international card networks which require the overseas merchant to bear the liability of any fraudulent transaction</blockquote>
The last line of the quote simply says that if someone stole your card details and shopped at sites that don't implement two-factor, such as Amazon, or subscribed to porn websites, the merchants would foot the bill and not you. Which means that there is a policy solution to this as well--not just technologically. This sort of liability shift is how banks incentivize parties to upgrade their infrastructure.

Oh, and by the way, <a href="https://www.schneier.com/blog/archives/2016/08/nist_is_no_long.html">SMS two factor has already been deprecated by NIST</a>--so probably wise not to start your press statement with words like <em>"stronger authentication method</em>" only to be follow that up by <em>"TAC that is sent to their mobile phones". </em>So far the best solution I've seen for CVV2 codes was <a href="http://www.thememo.com/2016/09/27/oberthur-technologies-societe-generale-groupe-bpce-bank-this-high-tech-card-is-being-rolled-out-by-french-banks-to-eliminate-fraud/">this one</a>, where the code changes every hour. A slightly more problematic solution is a separate dongle, but those are cumbersome.

As a side note, since Visa uses a short 3-digit CVV2 code,<a href="http://eprint.ncl.ac.uk/file_store/production/230123/19180242-D02E-47AC-BDB3-73C22D6E1FDB.pdf"> researchers have found</a> a way to brute-force guess the code by simply<a href="http://thehackernews.com/2016/12/credit-card-hacking-software_5.html"> trying every possibly combination across multiple websites</a>. A distributed brute-force attack, which only require that the criminals know your card number and expiry date--the two very things they can read from your contactless card with ease.

By comparison, Mastercard blocks brute-force attacks, while American Express uses a 4-digit CVV2 code (that's 10 times harder than 3-digits to brute-force).

However, it's easier to buy card numbers and expiry dates from shady characters online (<a href="https://krebsonsecurity.com/2016/04/all-about-fraud-how-crooks-get-the-cvv/">$5-$10 a piece</a>) than it is to read them off contactless cards in public. Just how long could you walk around a busy city with a card-reader in your pocket, before someone eventually finds out?! So .
<h2>Contactless can be more secure?</h2>
![](/uploads/1415020421171_wps_49_Visa_contactless_jpg-300x169.jpg)As a final thought, is there is some security advantage to using contactless cards. <em>(yes, I know I said all conveniences traded off security, but hear me out)</em>

Since contactless cards are meant to be tapped, they usually never leave the cardholders hands--which means there's less of a possibility of someone stealing your card info by taking a photo, or even just memorizing the numbers while you're not looking. And as we discussed, the all important CVV2 is printed, and if no one can see it (because the card is in your hands), no one can steal it.

To be sure, contactless cards aren't perfect, but they're just the natural evolution of payments--so get with the program. You're more likely to lose your card details, because some dumb-ass merchant decided it was a good idea to to write down your credit number and CVV2 details in their Point-of-Sale ... and that same dumb-ass merchant gets hacked. Even in Singapore, I've had merchant insist on writing down my card details in their POS--a definitive no-no when it comes to securing your card details.

And most of the other attack vectors that contactless cards pose, are equally likely for regular 'contact' cards as well.

Here's wishing Malaysia a successful Chip and Pin migration, and Merry Christmas everyone.
<h2>Conclusion</h2>
Overall, contactless cards offer a little convenience for just a slight security trade-off. I wouldn't turn a card down just because it wasn't contactless, they're still pretty good.

Just make sure you don't get debit cards (whose liability is unlimited on your part), and choose a good PIN, and always cover the pinpad with your hands when you're typing in your PIN.

Other than that, I for one, welcome our new contactless overlords!
<h2>TL;DR</h2>
Researchers in the UK have managed to successfully 'impersonate'  a card before, even giving a <a href="https://www.youtube.com/watch?v=JPAX32lgkrw">demonstration online</a>. While this is true, the difference is that the UK uses Offline Pins, while Malaysia will implement (hopefully!) Online Pins, and in the <a href="https://www.cl.cam.ac.uk/research/security/banking/nopin/oakland10chipbroken.pdf">published paper</a> (which many members of the press choose to ignore), they specifically mention:
<blockquote>we have tested cards from Switzerland and Germany whose CVM lists specify either chip and signature or online PIN, at least while used abroad. The attack described here is not applicable to them. However, because UK point-of-sale terminals do not support online PIN, a stolen card of such a type could easily be used in the UK, by forging the cardholder’s signature.</blockquote>
Offline Pins are stored on the cards themselves, and are verified by the card--as you can imagine this isn't a great solution. A pin enabled card is still better than a signature one, but because the Pin is verified by the card, if you can successfully compromise the connection between the card and the terminal you can beat the protocol. This isn't 'cloning' the card, because you still need the original card, and some electronics, but it's awfully close. With a stolen card, you'd be able to perform some Card Present transactions and net yourself some serious bounty--again this isn't something a sustainable criminal enterprise would do, spending money in physical locations is a definite no-no.

The UK was one of the first countries to implement Chip and Pin, and hence the choice for offline pin. Modern implementations of chip and pin usually use Online Pins, and this means that the Pin is verified by the banks online systems (and not the card). Impersonating an online Pin card is far harder to do (at least to my mind!)

Finally, because the usage of Pin depends on the card and terminal--chances are that when you go to foreign country, you'll still be asked for signature. That's because these countries haven't implemented online PIN yet, and their terminals can only do offline pins, so both the terminal and card 'fallback' to use signature--the only verification method both terminal and card agree on.
<h2>Further reading</h2>
<ol>
 	<li><a href="https://www.keithrozario.com/2015/10/chip-and-pin-an-intro-for-malaysians.html">My initial post on Chip and Pin</a> ( a real dummies version)</li>
 	<li><a href="https://www.youtube.com/watch?v=ET0MFkRorbo">Youtube video of professor Ross Anderson explaining the fundamentals of Chip and Pin</a></li>
 	<li><a href="http://www.thestar.com.my/news/nation/2016/12/08/bnm-you-wont-pay-dearly-for-contactless-cards-these-plastics-come-with-security-features-that-are-im/">BNM just completely screwing up the explanation to Sin Chew</a> (from TheStar)</li>
 	<li><a href="https://www.youtube.com/watch?v=Ks0SOn8hjG8">A Computerphile video from Ross Anderson</a> (the guy is brilliant)</li>
 	<li><a href="https://www.facebook.com/bnm.official/photos/a.492310539871.272673.83552599871/10154571535289872/?type=3&amp;theater">Official Bank Negara Statement on Contactless cards</a></li>
 	<li><a href="http://www.abm.org.my/index.cfm?sc=press_releases&amp;ar=1175">Statement from ABM</a> (Associations of Banks Malaysia) on roughly the same topic, with exactly the same wording :).</li>
 	<li><a href="http://money.cnn.com/2015/03/26/technology/security/credit-card-dynamic-cvv/">CNN article</a> for a credit card where the code changes every hour</li>
</ol>