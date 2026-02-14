+++
title = "The safest place for your money is under the mattress"
slug = "the-safest-place-for-your-money-is-under-the-mattress"
date = "2016-09-12T08:38:24"
draft = false
categories = ['CyberLaw', "Keith's Favorite Post", 'Security &amp; Privacy', 'Singapore']
+++

<a href="/uploads/Money-Under-Mattress.jpg">![money-under-mattress](/uploads/Money-Under-Mattress.jpg)</a>

When I was in school, we joked about people who kept their money under the mattress, that somehow those who didn't use banks were less intelligent than people who did.The general thinking was that smart people kept their money in the bank, where it was safe from theft, fire and flood, while still collecting interest.

In the 80's this was a compelling argument, when interest rates were high and banks really did provide security,but is that thinking still applicable today?

In June of 2000, Maybank <a href="http://www.maybank2u.com.my/mbb_info/m2u/public/personalDetail04.do?channelId=Personal&amp;cntTypeId=0&amp;cntKey=AU00.06.09&amp;programId=AU02.02-ArchiveNews&amp;newsCatId=/mbb/AU-AboutUs/AU02-Newsroom/2000/06&amp;chCatId=/mbb/Personal">launched their 'new' internet banking platform</a>, Maybank2u, which allowed their customers to do their banking online, outside of traditional branches or even ATMs. Few years later, it begun offering online purchases and soon after the mobile <a href="http://www.maybank.com/iwov-resources/corporate_new/document/my/en/pdf/corporate-news-release/2014/Press_Release_maybank2u_app.pdf">app was launched</a>.

But while online banking platforms brought convenience, they also introduced new security threats -- and it wasn't clear whose job it was to secure against those new threats, and who would be liable for inevitable financial losses.

Was it going to be bank who assumed liability, just like they did before, or would it be the account holder, or possibly a mixture of both?

The answer depends on who gets attacked, because not all attacks are equal.
<h2>Not all attacks are equal</h2>
There's two types of attack, one where the bank itself is attacked, and another where the account holder is targeted instead.

When someone walks into a bank  with the threat of violence, and walks out <a href="http://www.straitstimes.com/singapore/suspect-on-the-run-after-30k-bank-robbery-in-holland-village">with $30,000 of the banks cash</a>, the bank absorbs all the loses. After all, that's why your money is in their safe and not under the mattresses.

<a href="/uploads/507d7acb92f46ed8d8779be14e3f2051.jpg">![507d7acb92f46ed8d8779be14e3f2051](/uploads/507d7acb92f46ed8d8779be14e3f2051-300x188.jpg)</a>But there exist another class of attack--customer impersonation, where the attacker isn't threatening violence or even 'attacking', but trying to fool the bank into believing they are the rightful account holders. In other words, the attacker is trying to impersonate you, to get to <em>your</em> money.

And in the digital world, customer impersonation is far more common. Consider the case of ATM fraud.

ATMs identify a user by verifying their ATM cards, and then prompting them for the PIN. More specifically, the ATM first authenticates the inserted ATM card (<em>is this card real?</em>) and then proceeds to ask the user for the PIN (<em>is the person the accountholder?</em>), once an ATM is satisfied, it then proceeds to grant the user access to the account.

Hence if an attacker managed to steal <em>your</em> card and knows <em>your</em> PIN, the ATM has no way to differentiate between you and the attacker. Anyone could take <em>your</em> money from <em>your</em> account, by just having your ATM card and PIN, in contrast robbers attacking a bank would simply be taking the bank's cash...not yours.

Credit Card fraud is another prime example, but at least in Malaysia <a href="http://www.consumer.org.my/index.php/personal-finance/bank/175-pay-only-rm250-for-lost-or-stolen-card-transactions">end customers have their liability capped at RM250 provided they report their lost cards in a 'reasonable' amount of time</a>. For debit cards and ATM cards are not protected in the same way. Which is strange because the poorer sections of society who need more protection usually have debit instead of credit cards.

But even credit card users need to be wary, because changes in the liability model are bound to happen when we <a href="https://www.keithrozario.com/2015/10/chip-and-pin-an-intro-for-malaysians.html">introduce Chip and Pin</a>. (read more <a href="http://www.loyarburok.com/2010/01/16/those-bloody-banks-credit-card-companies-and-bank-negara/">here</a>)

To summarize, customer impersonation isn't the same as a bank robbery, when the bank issues you credentials (like PINs, passwords or ATM cards), the responsibility to secure those credentials are yours--and if those credentials are compromised, then you'll have to shoulder some of the financial losses as well.

<!--more-->
<h2>ATM security</h2>
But an ATM transaction requires a bank issued card, a customer chosen PIN, and it's all executed on the secure bank hardware. The bank is responsible for securing the ATM (which is a computer), while the customer has to protect their ATM card, and keep their PIN a secret. While this was still a major change, the overall effort required to secure the ATM system is remarkably simpler than securing an online transaction.

After all, people know how to keep a physical ATM card safe--we've been trained all our lives how to protect a physical asset. Unfortunately, human beings aren't so good at keeping secrets.

But what happens when we move from ATMs to the Internet?
<h2>Online banking security</h2>
With online banking, the bank is merely hosting a website. Account holders are using their own computers to access the website, which means that the onus is on them to ensure that the computers their using are secure.

More importantly, it's also your responsibility to keep your password a secret, because that's the only way the bank identifies you. Losing it, would mean anyone could impersonate you and access your account information.

That's why phishing attacks to steal usernames and passwords are so common (I blogged about one for <a href="https://www.keithrozario.com/2014/10/phishing-by-the-bank-maybank-that-is.html">Maybank</a>, and another for <a href="https://www.keithrozario.com/2014/07/rhb-phishing-scam-details-phishing-scam.html">RHB</a>) So how do banks design their systems to overcome the weakness of passwords?
<h2>Username and Passwords are not enough</h2>
<a href="/uploads/2-factor-auth.jpg">![2-factor-auth](/uploads/2-factor-auth.jpg)</a>In Malaysia, most banks use sms' to send a One Time Password (OTP) to verify that the person making the online transaction is in possession of a phone number tied to the account. This way, even if a attacker knows the password to your Maybank2u account, they can't move money unless they can get a hold of the OTP (or TAC in Maybank terminology)

In cybersecurity jargon, this is 2 Factor authentication, where in order to access funds in your account, the attacker would need to know the Password (something you know), and have possession of the phone (something you have).

Password = 1 Factor. OTP = 1 Factor.

Password + OTP = 2 Factor.

Problem is that sms was never designed to be a secure channel and even if it <em>was</em> it's not anymore.
<h2>What happens when you get hacked</h2>
Consider what happened to Mr. Eric Chua, who lost nearly RM11,000 to hackers. He claimed hackers compromised his email addresses, then managed to get Digi (a local telco) to re-issue them his sim card, and then used his Maybank2u account to purchase multiple items from an online shopping site.

His Facebook post has since been deleted,but <a href="/uploads/Eric-Chua-ONLINE-BANKING-HACKED-This-is-a-public...-Facebook.png">here's a screenshot</a>.

Some parts of his story seemed odd, for example I doubt Digi would issue you a new sim without some IC verification, and if Digi does this then they need to stop--<em>like right now!!</em>

But here's the thing.

Assuming everything in his story were true, who would ultimately be responsible for the RM11,000 loss? Would it be Mr. Chua, who lost control of his e-mail account (nothing to do with the bank), or Digi for issuing a sim to someone else (again nothing to do with the bank). Or would it be the bank for designing a system that wasn't fullproof?

In the more <a href="http://www.straitstimes.com/singapore/man-in-row-with-bank-over-hacked-phone">straighforward case of Mr. Philip Loh</a> from Singapore, who lost $12,000 due to hackers, things may be a bit simpler. Mr. Loh claimed that hackers broke into his phone to execute malicious transactions. In this case, only one computer system was broken--his phone. Once hackers had control of his phone, they didn't need to have telco's issue them a new sim, or even compromise any e-mail accounts--all the information was sitting pretty on his Samsung Galaxy Note.

Mr. Loh's case didn't involve a 3rd-party like Digi, and lawyer Bryan Tan opined that "Is it fair for consumers to bear the liability when it is the system that has been compromised by hackers?", but of course in the case of Mr. Loh, the 'system' was the phone that belonged to him!

The more relevant question would be "Did the bank inform Mr. Loh of the risks of online banking on his phone before offering the service to him?"
<h2>SMS isn't secure</h2>
In both cases, the banks claimed their systems were not hacked (<em>true</em>) and they maintained that payments could not be waived because the transactions were authorized by One Time Pins (OTP). The thinking is since the OTP further asserts the identity of the users, these transactions should be considered more 'secure', and hence more difficult to reverse.

What is less acceptable though, is the more fundamental issue of banks who rely on sms to protect the end consumer. NIST (the most authoritative body on the topic), is urging people to move away from the use of SMS for one time passwords, not just because it relies on the mobile security, but because the protocols used to transmit SMS's is no longer considered secure. NIST explain further by <a href="http://nstic.blogs.govdelivery.com/2016/07/29/questionsand-buzz-surrounding-draft-nist-special-publication-800-63-3/">saying</a>:
<blockquote>security researchers have demonstrated the increasing success (read: lower cost in time and effort and higher success rates) of redirecting or intercepting SMS messages en masse. While a password coupled with SMS has a much higher level of protection relative to passwords alone, it doesn’t have the strength of device authentication mechanisms inherent in the other authenticators allowable in NIST draft SP 800-63-3. It’s not just the vulnerability of someone stealing your phone, it’s about the SMS that’s sent to the user being read by a malicious actor without getting her or his grubby paws on your phone.</blockquote>
In short, passwords with SMS are better than just passwords, but they're still no longer good enough for online banking. Not only are mobile phones horribly insecure when used by the general public, the underlying technology used for transmitting SMS's is already considered practically compromised.

And since banks rely on SMS security for their online banking, it's disingenuous to have such a high confidence in the security of their product, when a major component of the authentication is considered weak.

Hackers always go after the weakest link in the chain, sometimes that's the customer (phishing scams), sometimes that's the customers phone (e.g. Mr. Loh), but it looks like SMS will be the next target, and that's the day all hell may break loose :)

<em>For more info on how to crack the mobile phone network, read <a href="http://www.cbsnews.com/news/60-minutes-hacking-your-phone/">this</a>.</em>
<h2>Conclusion</h2>
And so we come full-circle. If you put your money in the bank, is it going to be more secure than having it under your mattress?

I honestly believe keeping your money at home is probably the better option--but it <strong>isn't</strong> an option, at least not anymore.To be a fully functioning member of society requires a bank account, if only to just receive your monthly salary, I can't operate without Uber or online shopping, and even my payments for the hosting of this website, all require online banking.

If you want your money to be safe, keep it under the mattress, because chances are, houses get robbed less than phones get hacked.

For the rest of us, to whom online banking is necessity, we're just going to have to learn how to secure our phones and passwords because he security of online banking is a shared responsibility between the bank and the consumer.