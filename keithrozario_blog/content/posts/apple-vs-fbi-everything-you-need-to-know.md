+++
title = "Apple vs. FBI: Everything you need to know"
slug = "apple-vs-fbi-everything-you-need-to-know"
date = "2016-02-20T09:26:04"
draft = false
categories = ['CyberLaw', "Keith's Favorite Post", 'Security &amp; Privacy']
+++

<a href="/uploads/broken-fence.jpg" rel="attachment wp-att-5526">![broken-fence](/uploads/broken-fence.jpg)</a>A judge in the US has ordered Apple to provide 'technical assistance' to FBI, in creating what some (but not all) cybersecurity experts call a backdoor. In the few years I've written about these issues, I've never seen anything as hotly debated as this one, across the folks from digital security to foreign policy all coming down on both sides of the debate.

On one hand it seems a bit snarky of the FBI to use this one particular case, that looks to have the highest possible chance of success to set precedent, but on the other hand it seems mighty nasty of Apple to refuse to comply with a court order, to crack into a terrorist phone.

So here's some facts of the case.

The phone in question belonged to Syed Rizwan Farook, a shooter in the <a href="https://en.wikipedia.org/wiki/2015_San_Bernardino_attack" target="_blank">San Bernadino shooting</a>, which caused the deaths of 14 people. America has numerous mass shootings, but this one involved two Muslims aligned to ISIS--and hence more easily labeled terrorism, without the need for adjectives like 'domestic'.

As I blogged about last week, <a href="https://www.keithrozario.com/2016/02/being-terrified-the-price-of-terrorism.html" target="_blank">self-radicalized terrorist don't get funding from headquarters</a>, and without that glorious ISIS-oil money, all these guys could afford for was an iPhone 5C, an entry-level phone with hardware identical to that of the iPhone 5, a phone launched waaaayy back in 2012 <em>(you'll remember that as the year Manchester United last won the Premier League)</em>. As an older phone, the security architecture of the 5C lagged behind the current generation iPhones, all of which have a secure enclave, but make no mistake, it's still pretty secure.

By pretty secure, I mean that the phone has all of its contents encrypted, and un-readable to anyone without the encryption key. The key is derived from both the user passcode, and a randomly generated hardware key that is unique to the specific iPhone. It is generally understood that Apple doesn't keep track of the hardware key, and therefore unable to provide it, as you might expect the hardware will also never give up it's key under any circumstance. Without the hardware key, the encrypted  data is unreadable, even with the passcode. Which explains why the FBI can't suck the data out of the device for decryption on a more powerful computer, or load the data into 1000's of iPhones for parallel cracking.<!--more-->

But even with the phone, things remain tough. To decrypt the phone, both the hardware AND the passcode is required. And if you don't know the passcode, things don't look good. iPhones are hardened against passcode guessing, just like ATM cards. If a thief managed to obtain your ATM card, they could take it to any ATM and try to guess your PIN Code, but they only get 3 attempts before the ATM sucks in the card, and ends the attack. The odds of guessing a 6-digit passcode with just 3 attempts is worse than striking the lottery--that's why losing your ATM card isn't that big a deal, and from a  strictly data perspective, losing your iPhone isn't a big deal either--provided you secured it with a long enough passcode. <em>(of course no one likes losing a RM3000 phone)</em>

Similarly, iOS works to limit an attackers ability to guess its passcode, either by slowing-down the  rate of guesses (through artificially delaying retry attempts, sometimes by hours), or by just erasing the entire contents of the phone after 10 incorrect passcode entries. The latter being a feature the user has to actively switch on.

All these protections against brute-force passcode guessing are baked directly into iOS, Apple's iPhone operating system, and even though this was an older generation phone it still had the latest software (yet another reason to admire Apple). Which also means that <a href="https://www.keithrozario.com/2015/04/worked-example-iphone-pin-hack.html">previous hacks which bypassed the protections</a> have also been patched. Like I said...pretty secure.

To bypass these obstacles, the FBI is asking Apple to provide them with a special <em>tailor made</em> version of iOS that would eliminate these protections, specifically:
<ul>
	<li>The<strong> removal of the Auto-Erasing feature</strong>, which would otherwise erase the contents of the phone after 10 incorrect passcode entries.</li>
	<li>The<strong> removal of the  artificial delays</strong> in attempting the passcodes, allowing the FBI to try passcodes at the fastest rate the hardware will allow.</li>
	<li>The <strong>ability to submit passcodes electronically</strong> to the iPhone which eliminates the need of a human person manually entering the passcodes by hand</li>
	<li>And, the special software could be further <strong>customized to work on only this one iPhone</strong>, down to the serial number etc..</li>
</ul>
In essence, the FBI is asking Apple to create a 'special' ATM, that would allow them to try PIN codes for a specific ATM card without sucking in the card after 3 failed attempts. That 'special' ATM would also have a ability to attempt the PINs electronically rather than having someone manually enter the PINs.

If a terrorist told you that the co-ordinates for a bomb was the PIN to his ATM card, and neither the Bank nor the Police had anyway to ascertain the PIN, other than creating that 'special' ATM--do you think the Bank should do it? Would it be considered a 'back-door'?

All in all, it seems like a pretty reasonable request, but what makes this so controversial (at least in cyber security circles) is whether the 4 items above are considered a 'back-door'. Some experts say it is, others say it isn't.

What isn't controversial is Apple's ability to do this. Experts all agree that <a href="http://blog.trailofbits.com/2016/02/17/apple-can-comply-with-the-fbi-court-order/" target="_blank">this is possible</a>, and even <a href="http://withoutbullshit.com/blog/apples-tim-cook-shows-how-to-communicate-in-a-crisis/">Tim Cook's brilliant PR response</a> didn't deny their ability to do so. So it is whether Apple 'should' do this, that is the question.

'Should' is a strange word, this is after all a phone that belonged to a <em>terrorist</em>, and shouldn't Apple do everything in its power to help law enforcement? What if the phone has contact details of other ISIS operatives in the US, or what if it had more details of ISIS operations in Syria, wouldn't we want that, regardless of how 'burdensome' it might be to Apple. This has nothing to do with the 4th amendment, after all the owner of the iPhone is dead, and a court warrant is available--so what's stopping Apple?<em> [update: Actually the 'owner' of the iPhone was the San Bernadino county, which meant it belonged to a government, not the individual, definitively ending any 4th amendment protections]</em>

To be fair, there's only a very small chance that these 'self-radicalized' lone wolves have anything of grave importance on their old iPhone, but when words like terrorism are bandied about, a 1% is more than enough.

Which is why I feel it's a bit snarky for the FBI to use this case, it seems the perfect case. It involves terrorism (which pushes everyone's emotional buttons), an old iPhone that can be cracked and violates no constitutional protections. But you can bet, that if it succeeds on a legal level, that the precedent set by this case, will be used for other cases that don't involve terrorism and affect more recent versions of iPhones.

And that's what scares Apple.

That if it sets a precedent by complying with <em>this</em> court order, then it will have to comply with all <em>other</em> court order, potentially thousands more, requesting the very same thing, and the perception of iPhone security will take a severe beating--after all there's a reason drug lords and terrorist use iPhones. Let's also accept, that if one Judge rules for Apple to comply for this iPhone, explaining to futures court Judges the technical intricacies of the secure enclave, RAM Disk implications, and digital signatures of future iPhones would be a task so monumental that from a legal standpoint <span style="text-decoration: underline;">this iPhone 5c is all iPhones</span>.

The question of 'should' must also take into account the precedent this might set, and look beyond the specifics of this one case.

Plus it really <em>would</em> be burdensome on Apple to replicate what they might do in this one case, thousands of times. Everytime they do so, they'd have to sign the new operating system, which means they'd have to get their super-secret iOS signing key and digitally sign the software. Apple's entire iOS security is premised on keeping that key secret, and since iOS operates on all of their iPhones, and iPhones are a $50 Billion dollar a year business, the signing key is quite possible the <strong>most valuable secret in the world</strong>. If you have it, you would have broken all of iOS security, plain and simple.

If you were a shareholder, would you like Apple to get out this secret key, every time the FBI, DEA or NYPD come knocking? And what's to stop this precedent from being enforced internationally? Why would China, Apple's largest growing market, feel that their law-enforcement isn't entitled to the same privilege as the FBI?

How would you feel if Apple complied with the request to the FBI for this terrorist case, and then complied with other request from Israel, China, Australia...or Malaysia?

And finally to circle back to the Bank analogy, the ATM has no personal data, and the data in the iPhone doesn't represent a clear and imminent threat, it was details of an event that had already happened.

If you were CEO of Apple what would your stand be?
<h2>Post Script</h2>
The iPhone has a hardware limit of 80ms per password attempt, which would take about 15 minutes to crack a 4-digit passcode, and 1 day to crack a 6-digit one. However, a sufficiently lengthy alphanumeric passcode (composed of both digits and characters)would still take years to crack even if the FBI obtained their special iOS, so you know what to do if you want to protect your future drug empire.

Apple has <a href="http://techcrunch.com/2016/02/18/no-apple-has-not-unlocked-70-iphones-for-law-enforcement/">never complied to similar requests before</a>, even though you've read that<a href="http://www.thedailybeast.com/articles/2016/02/17/apple-unlocked-iphones-for-the-feds-70-times-before.html"> it acquiesced 70 times prior</a>, that's just technically wrong. I love Shane Harris and his <a href="https://spaghettionthewallproductions.com/rational-security/">rational security podcast</a>, but he doesn't get the nuance of this issue. First of all the number 70 is a government estimate, not something Apple agreed with, and while we don't have the specifics of each case, some argue that this was much older iOS7 devices, which don't have built-in encryption--which meant data could be extracted without the need for a passcode.

But think about what that means, if Apple could extract the data from the phone without a passcode, what's to stop the likes of Russian cyber-criminals or Chinese State-Sponsored hackers from doing it as well? Hence, Apple improved the security of their software to ensure that no one without the passcode could access the contents--and what the FBI is requesting now is a tailor-made iOS that intentionally circumvents the protections, un-doing all of what Apple has engineered. This is the first time the FBI has requested this, and not the 70th time.

<strong>#Update 1</strong>: As it turns-out the iPhone actually belong to the owners employer, the county Health Department, and part of the reason we're in the mess is that<a href="http://www.politico.com/story/2016/02/apple-iphone-privacy-justice-department-219505"> they reset the password for the Apple ID account shortly after the attack</a>. Had they not done that, Apple may have been able to provide the data from the cloud back-up without all this kerfufle.

<strong>#Update 2:</strong> Cybersecurity 'Legend', John McAffee has come out and said that his team of elite hackers will be able to <a href="http://www.businessinsider.com/john-mcafee-ill-decrypt-san-bernardino-phone-for-free-2016-2">crack the encryption of the iPhone in 3 weeks</a>. Now we know this is legit, because if you Google <a href="https://www.google.com/search?q=cybersecurity+legend">'Cybersecurity Legend'</a> his name does come up--a lot! But McAfee is legendary for the wrong reasons, apart from having his name associated with a <a href="http://www.urbandictionary.com/define.php?term=McAfee">"A barely passable virus scanning program that updates at the worst possible times. "</a>, he's also famous for <a href="https://www.youtube.com/watch?v=bKgf5PaBzyg">producing youtube videos of him snorting drugs</a> with prostitutes, <a href="https://mcafee16.com/">running for president</a> and, believe it or not, <a href="http://www.amazon.com/s/?search-alias=stripbooks&amp;field-author-exact=John%20McAfee">writing books about Yoga</a>. But jokes aside, the offer that he makes to the Feds are that he will crack the iPhone 5C in under 3 weeks, and he'll use social engineering. Now unless he's able to psychologically<a href="https://www.grahamcluley.com/2016/02/good-luck-john-mcafee-socially-engineering-corpse/"> trick a dead person to reveal their passcodes</a>, or charm an iPhone into revealing its encryption key--this<strong> is a joke of an offer</strong>, more worthy of being reported in the Onion than on the countless media outlets who probably don't get it.

<hr />

 

For the best articles on the topic:

<a href="https://www.eff.org/deeplinks/2016/02/technical-perspective-apple-iphone-case">EFF Deeplinks blog,</a> that answers all your high level technical question

Jonathan Zdziarski's <a href="http://www.zdziarski.com/blog/?p=5645">amazing post</a>, which covers more deeply why this isn't only for one iPhone, and why legally Apple would have to make their 'broken' iOS available to the defence counsel.

A <a href="http://www.zdziarski.com/blog/?p=5714#more-5714">second Zdziarski post</a> on Bill Gates ribbon and ribbon-cutter analogy.