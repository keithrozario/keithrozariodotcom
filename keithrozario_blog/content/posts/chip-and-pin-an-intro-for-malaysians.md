+++
title = "Chip And Pin : An intro for Malaysians"
date = "2015-10-29T11:59:54"
draft = false
categories = ["Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

In 2016, Chip and Pin will gradually be introduced in Malaysia, that means your Credit Cards now will prompt you for a PIN instead of signature during purchases. This will be a bit of a hassle, but it will be worth it,  here's what you need to know about it and credit card transactions in general.
<h2>The 5 people you meet in card transaction</h2>
<a href="/uploads/19205891971_2abaa89036_z.jpg"><img class="wp-image-5281 size-medium alignleft" src="/uploads/19205891971_2abaa89036_z-300x300.jpg" alt="19205891971_2abaa89036_z" width="300" height="300" /></a>First off, a short primer on credit card transactions. In any business transaction, there are at least 2 actors involved, a buyer and a seller. In industry lingo we call them <strong>Merchants </strong>and <strong>Cardholders</strong>. These are important terms to remember, as we'll use them extensively .

But a card transaction is far more complicated and involves at <span style="text-decoration: underline;">least</span> 3 more actors, some of which you may not even be aware off. First, we have the party that issued the cardholder their card, the '<strong>Issuer</strong>'. If you have a credit card, chances are that credit card is tied to an line of credit issued by a bank, whether it's HSBC, or Maybank, these are issuers, who have a relationship with the card holder.

Then we have the '<strong>Acquirer</strong>'. This is the financial institution that provides the merchant the ability to accept card transactions. Sometime this is as simple as just placing a card terminal on the merchant premise. The acquirer has a relationship with the merchant, and that's why when you look at credit card receipts, they usually have a banks logo on them--that's the acquirers logo.

Both the issuer and acquirer are usually banks, because credit cards deal with debt, and only registered financial institutions are authorized by law to perform such transactions (think of interest rates, and loan functions..etc)

So far, we have the <strong>Issuer</strong> that issues the card to the <strong>cardholder</strong>, and the <strong>Acquirer</strong> that provided the infrastructure to the <strong>merchant</strong>, but how do we tie all of them together. Here the final actor provides a network that <span style="text-decoration: underline;">connects all acquirers to all issuers</span>, they're called <strong>Card Schemes</strong>. You know them by their names, VISA, Mastercard, Diners, JCB, Discover..etc. The schemes provide the ability to connect acquirers and issuers, so when you go a merchant, you only ask them if they accept Master or Visa, and not worry about the specific acquiring bank. Similarly the merchant places a "Mastercard accepted" logo on their premise, because if they can accept one Mastercard, they can accept them all.

These 5 actors, the <strong>Cardholder</strong>, the <strong>Merchant</strong>, the <strong>Acquirer</strong>, the <strong>Issuer</strong> and the <strong>Scheme</strong> work seamlessly together to allow you to purchase goods and services using only a single piece of plastic we call a card.

But what is a card?<!--more-->
<h2>What is a Card?</h2>
A card a method of authentication. It allows the payment system to identify you, and then tie your identity to a line of credit, which is then used in a very complex debt transfer mechanism. <em>(you need to buy me a beer for me to explain debt transfers to you)</em>

A card proves you are indeed yourself, and once that identity is confirmed, other checks like your credit limit are used to approve or decline a transaction.

It's quite amazing that you can go into a machines store in MidValley, walk out with a brand new iPad, but only actually pay for the iPad at the end of the month--not to the merchant, but to the issuing bank. Merchants are consistently told that accepting credit cards pushes sales up, because the psychological impact of purchasing with a card is far lower than with cash. A lot of people would have much smaller TVs if it weren't for 0% interest rate payments.

But I'm getting off-point.

The point is that credit card transactions are phenomenally convenient, but like all other conveniences they also pose a security challenge. If the only thing protecting your line your credit <em>(which can be much higher than your monthly salary)</em> is just a piece of plastic, then you better be sure that the technology that protects it is going to be pretty much unbeatable.

And what exactly <strong>is</strong> the technology that protects your identity?
<h2>EMV vs. Magstripe, FIGHT!!</h2>
Putting the <strong>Chip</strong>, in <strong>Chip and Pin</strong>.

In the past cards were purely based on Magnetic Stripe technology. These cards had a stripe of data on their back, which contained all the information needed to identify the cardholder. This was a really bad idea as all the data was in plaintext which made it easily read and duplicated.

You can buy really cheap magstripe readers and writers in the market today, and start cloning you own magstripes cards, but fortunately it won't get you far.

In the mid 2000's the Association of Banks Malaysia (ABM), decided to migrate all cards in Malaysia to a standard called EMV. EMV is an acronym for Europay, Mastercard, Visa and is essentially a technology standard for a generation of credit cards based on chips rather than stripes.

The main driver for the change was the massive amount of fraud in the country, in true Malaysia boleh spirit, we had one of the highest fraud rates in the world, and local issuers and acquirers were pushing for a technological solution to our fraud problem.

EMV offered a solution by promising that the cards were un-cloneable. The EMV cards in circulation locally today still contain magstripes to ensure they are 'backwards compatible' with foreign countries. In some countries like Thailand and Indonesia a lot of businesses still run on pretty old card infrastructure that only works on magstripe, I remember paying for a 5-star hotel stay in Bali that used a zip-zap machine to read my magstripe. Be assured though that if you swiped your magstripe locally in Malaysia, the transaction would be declined.

EMV cards (sometimes called Chip cards) are almost mini computers you carry in your wallet. The chip on the card can perform complex cryptographic calculations, the keys for which are impossible to obtain from the card directly.

For the more technical savvy among my readers, at the root of EMV security is a private-public key pair on the card. The private key is never revealed to anyone, and is can never be extracted from the chip(at least that's the assumption). When a card is inserted into an EMV reader, it sends two chained certificates to the reader, one is an scheme signed certificate of the issuer, and another issuer signed certificate of the card. The second certificate contains the public key of card, which the reader can then verify.

Loaded onto every card reader is a Scheme certificate, which is used to verify the issuer and card certificates. Essentially, a Visa certificate is chained to Issuer certificate, which is then chained to an individual card certificate. You can google the public Visa and Mastercard certificates to have a look.

If you didn't understand the last 2 paragraphs, no worries. What you need to know is that it's MUCH harder to clone a chip card then it is to clone a magstripe cards.

But cards alone aren't enough are they?
<h2>2 Factor authentication</h2>
Of course not, if all the security relied on the card, then anyone with a stolen card could execute a whole load of transactions.

So all cards come with 2 factor authentication.

When we talk about authentication, a 'factor' is either
<ol>
	<li>Something you Have (like a card, token, thumbprint..etc)</li>
	<li>Something you know (like a password, or passphrase)</li>
	<li>Something only you can do (like a signature, or answering security questions)</li>
</ol>
When you have just one factor, that's considered poor security. Modern systems usually have a combination of more than one factor, hence the term 2-Factor authentication.

For example, a cash withdrawal at the ATM uses 2 factor authentication. To withdraw money from your account you must first have the ATM card<em> (something you have)</em> and enter the PIN<em> (something you know)</em>. Hence losing your card isn't so worrying because criminals still need the 6-digit PIN, and if you're protected it sufficiently, you've got no worries.

By the way, there's a myth going around that if you enter your PIN backwards, the Police will be alerted---that's bullshit!!. The bank doesn't even know your PIN, and logically wouldn't know the reverse of it either. If you're wondering how the Bank can authenticate a PIN without knowing it--<a href="https://www.keithrozario.com/2015/10/the-problem-with-bio-metrics.html">read this</a>.

But what does 2-Factor authentication have to do with Chip And PIN?
<h2>Signature vs. PIN</h2>
<img class="alignright wp-image-5279" src="/uploads/signature.jpg" alt="signature" width="300" height="212" />Technically even today all credit transactions are two-factor authenticated. You must have the card, and you must be able to sign according to the signature behind the card.

But all of that assumes that a signature is hard to forge, and that cashiers verify the signature--both of which aren't true. The main problem with signatures is that it relies on a human (the cashier) to verify the transaction, that's weak in every sense of the word.

Malaysia was one of the first countries to implement EMV, and we chose the Chip and Signature variant--at the time most countries were still on Magstripe, and our local fraud dropped to near zero because we used better technology than the rest of the world. It wasn't that criminals couldn't crack it, it was just that it was easier to shift their operations elsewhere in the world than invest resources to crack EMV.

Criminals are opportunist, why spend $10 to crack 1 EMV card, when you can crack 100 magstripe cards for the same amount. Hence they just moved to countries with the lower tech, and eventually ended up in America where those poor souls have only just moved to EMV Chip and Signature.

So if we want to keep fraud low, we need to upgrade the tech, and the logical step is to move from EMV Chip and Signature to EMV Chip and PIN, which is almost the defacto standard in all but a handful of countries.

But Why are Pins more secure?

<img class="alignleft wp-image-5280" src="/uploads/7212980434_e0b58bd5d2_m.jpg" alt="7212980434_e0b58bd5d2_m" width="300" height="300" />A PIN is fundamentally more secure than a card, because it is verified by the issuing bank (<em>or sometimes on the terminal by the card itself, but I don't have time to explore offline and online PIN here--again that needs a beer</em>), and the verification process is automatic. So we don't have to rely on cashiers and human judgement, it also frees up the cashier, because no decision is reliant on them.

An extra benefit of Chip and PIN is there are less opportunities for downgrade attacks. Because Signatures need human verification, there are special circumstances where card transactions don't require signatures. When you pump petrol in Malaysia and swipe your card at the pump, no signature is requested from you--because there would be no way to verify it. So a petrol purchase, specifically one done at the outdoor pump, is a pure Single Factor authenticated transaction--you only need the card <em>(something you have)</em>

In the future with Chip and PIN, we will have 2 factor authenticated transactions at the petrol pump because cardholders would need both their card AND their PIN. It's pretty great, but Chip and Pin won't always come to rescue.
<h2>Where Chip &amp; Pin won't help</h2>
Earlier I made the distinction of physical card transactions at stores, where you swipe your card and online transactions where no cards are swipe.Just how do you secure the latter?

Online purchases are pretty complex, they involve you entering your card number, expiry date and CVV2 code (that's the 3 or 4 digit code printed somewhere on your card). While you're entering more information than if you just swiped it at a reader, you never enter your PIN online. There's a good reason for that, because PINs are to be protected like the holy grail of Jerusalem, and should never be entered into something as insecure as a web-browser.

Fundamentally, that makes online purchases a single-factor authenticated transactions...unless the issuer does some magic, Maybank sometimes prompts your for a special code sent to your mobile, while HSBC would occasionally ask for special 6-digit code provided by the 'dongle' they provided certain customers. There are the exceptions rather than the rule. Most of the time, with just a handful of numbers (23 to be exact), a criminal can purchase goods and services online with your line of credit.

As you can see Chip and PIN doesn't help in this online (card NOT present transactions) so is it worth it?

<em>*Technically Chip and PIN will reduce the chances of someone skimming your card details. When the migration to Chip and PIN is complete, waiters at a restaurant (or anywhere else) will have to bring a terminal to YOU  to enter the PIN, hence your card never leaves your sight. This is far more secure than you handing over your card to a waiter and hoping for them to return with receipt--in the moment when you lose sight of your card, the waiter could have copied the card number, expiry date and CVV2 information, and then subscribe to hardcore foot fetish porn sites using just those details.</em>
<h2>Where Chip &amp; Pin will help</h2>
Chip &amp; PIN is fundamentally more secure than Chip &amp; Signature...BUT it isn't <strong>absolutely</strong> secure. There's an entire group working at Cambridge University trying to crack it, and many cracks have already appeared. The encryption works in principal, but the protocol of communication between the terminal and card has some 'gaps' that need further addressing.

In security of the masses, you can never be 100% secure, but you can put in place systems that make you less of a target. Moving Chip &amp; PIN will elevate Malaysia out of the lowest rung in the technological ladder, and keep us away from 'most' of the criminals.
<h2>Conclusion &amp; a note about liability</h2>
<a href="/uploads/5654834876_3c5feb5678_z.jpg"><img class="alignleft wp-image-5278 size-medium" src="/uploads/5654834876_3c5feb5678_z-300x194.jpg" alt="5654834876_3c5feb5678_z" width="300" height="194" /></a>Even if you didn't understand what I just said throughout this ridiculously long 2000 word post, you need to at least understand this.

In Malaysia, we have a Law that limits the liability of a cardholder to Rm250 provided they reported the lost card in a 'reasonable' amount of time. Moving to Chip and PIN may impact that significantly, and increase your liability, simply because it wasn't just a lost or stolen card, but also a lost or stolen PIN as well. Losing a physical item is 'reasonable', telling someone a secret like a PIN is something else entirely.

My guess is that the banks are going to come down much harder on fraud, and try to shift that liability to customers as we've seen in other countries.Make sure you understand your agreement before signing up for a card, and make sure you understand how the law can (or cannot) protect you.

If you're a merchant, consider this. Chip and PIN isn't mandatory for everyone. The incentive given to acquirers and issuers is liability. The rules are simple, if there is a fraudulent transaction, the party with the lowest technology foots the bill. So if a card is a Chip &amp; PIN card, but the merchant only had a Chip and Signature terminal, the acquirer (or merchant) assumes liability. If the terminal is a Chip and PIN capable one, but the card can only support signature, the issuer assumes liability, and since nobody wants to be liable, there is an incentive to move to Chip and PIN quicker.

That being said, happy PINning.

&nbsp;