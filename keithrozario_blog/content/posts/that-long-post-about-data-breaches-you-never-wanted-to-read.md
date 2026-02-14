+++
title = "That long post about Data breaches (you never wanted to read!)"
date = "2017-12-20T11:14:03"
draft = false
categories = ['Misc']
+++

<h3><span style="color: #000000;">Part 1: An intro to Data Breaches</span></h3>
Let's start with some basics. What is a Data Breach?

According to <a href="http://www.verizonenterprise.com/verizon-insights-lab/dbir/2017/">Verizon</a>, a <strong>data breach</strong> is when you've confirmed that data has been lost to an attacker, while a <strong>data incident</strong> is merely something that 'may' result in a breach.

An incident is when a laptop goes missing from your company's office.

A breach is when the data on that laptop is published online.

Breaches can be negligent or malicious in nature. An employee accidentally sending staff details to a vendor, would be negligent, but when someone breaks into your office to steal your laptops, that's malicious. Usually breaches require both negligent and malicious elements, and rarely do we see cases of elite nation-state actors hacking into orgazations.

But just because incidents happen before breaches, it doesn't mean we learn about them in that order. Sometimes we find the lost data first, and then scramble backwards to determine the incident.

Imgur, a popular image sharing site <a href="https://threatpost.com/imgur-confirms-2014-breach-of-1-7-million-user-accounts/129006/">that lost 1.7mln records,</a> were made aware of data breach from Troy Hunt, and had to go into damage control, presumably before knowing of what incident caused it.

When the Philippines Election <a href="http://www.wired.co.uk/article/philippines-data-breach-comelec-searchable-website">Commission (COMELEC) website was hacked</a>, it was apparent what had happened, hackers defaced the entire site, hence the incident and breach happened <a href="https://en.wikipedia.org/wiki/Commission_on_Elections_data_breach">simultaneously</a>. For Equifax, the time between incident and breach was a few months (at least that's what Equifax say), and for the Malaysian Telco breach, the gap was years.

I'm not here to talk about criminal investigations, but cut the Malaysian police some slack, its difficult to investigate a 3 year old crime. Sometimes IT pros can't investigate bugs that occurred 3 days ago, because logs were already purged, what more 3 years.
<h4>The new normal</h4>
Data breaches are the new 'normal', an accepted risk of living in today's hyper-connected world.

The price of our shiny new toys, like iPhones, Uber, and foodpanda, is the risk of data breaches. For all the <a href="https://www.bloomberg.com/news/articles/2017-11-21/uber-concealed-cyberattack-that-exposed-57-million-people-s-data">hullabaloo around Uber</a>, people are still going to use their service, because let's face it, Uber is still better than no Uber.

All the new online services, that make our lives better, require us to share some personal data with them. And that implicitly means, that there is a risk that data is lost.
<h4>Impact to companies</h4>
But just because Data breaches are normal, doesn't mean they don't impact the companies that experience them.

Last year, the Journal of Cybersecurity (yes, there is such a thing), published <a href="https://academic.oup.com/cybersecurity/article/2/2/121/2525524?searchresult=1">a study suggesting damage from data breaches to companies were minimal</a>:
<blockquote>Specifically, we find that the cost of a typical cyber incident in our sample is less than $200 000 (about the same as the firm’s annual IT security budget), and that this represents only 0.4% of their estimated annual revenues.

... much lower than retail shrinkage (1.3%), online fraud (0.9%), and overall rates of corruption, financial misstatements, and billing fraud (5%)</blockquote>
Still, while the initial cost is paltry, the long term consequence isn't.  <a href="https://www.comparitech.com/blog/information-security/data-breach-share-price/">Comparitech did an analysis of data breaches and the effect it had on share prices:</a>
<blockquote>Breached companies tend to underperform the NASDAQ. They recover to the index’s performance level after 38 days on average, but after three years the NASDAQ ultimately outperforms them by a margin of over <strong>40 percent. </strong><em>(emphasis mine)</em></blockquote>
In other words, the effect of a breach causes stock prices to immediately drop, then recover, but subsequently get pummeled.

However, almost all studies reveal that the damage from data breaches to companies are <span style="text-decoration: underline;">reducing</span> over time!

From comparitech:
<blockquote>The most notable result is older breaches met with a stronger initial reaction than newer breaches. One theory is that ... they become more common. This causes a “breach fatigue” ... in which investors are less shaken by data breaches as time goes on.</blockquote>
And the journal:
<blockquote>The litigation rate for all cyber events has been generally decreasing...the litigation rate for data breaches was around 20% in 2004, but has fallen to about 5% in 2014.</blockquote>
Conclusion?

Both the market, and the general population have become more accepting of breaches.

So if breaches are bad, and they're the new normal, can we at least contain them. As we'll see next, the answer is a resounding no.
<h3><span style="color: #000000;">Part 2: Data Breaches cannot be contained
</span></h3>
Just because they're normal doesn't mean data breaches are harmless, modern breaches share 3 common traits that make uncontainable.
<ul>
 	<li>They last forever</li>
 	<li>They're very common</li>
 	<li>They have little re-sale value</li>
</ul>
Sort of like diamonds, so let's take these one at a time.
<h4>They last forever</h4>
Once a breach data is published on the internet, there's no containing it.

This isn't unique to data breaches, all digital content has the same issue. It's the reason why online piracy is a big deal -- it's impossible to contain the distribution digital content once the internet gets a hold of it.

When a DVD-quality version of <a href="https://torrentfreak.com/scared-pirates-delayed-release-of-expendables-3-140728/">Expendables 3 was leaked online</a>, Lionsgate was powerless to stop it. The most they could do was <a href="https://www.cinemablend.com/new/Remember-Expendables-3-Got-Leaked-Someone-Just-Got-Arrested-70808.html">arrest the perpretrator,</a> and absorb a $10mln loss. This is a powerful hollywood studio, with millions to lose, and they couldn't stop the dissemation of their content.

The whole point of digitizing information, is to allow easier duplication and transportation of data. So when you try to 'contain' a data breach , you're not so much trying to out-wit the attackers, as you're trying to fight the nature of the internet itself.

And if the breached data are immutable (un-changeable) attributes like date of birth, MyKad numbers or blood type, breach victims remain victims -- forever.

Given how pervasive the impact of a breach can be, you'd expect them to be rare. But boy, would you be wrong.
<h4>They're common</h4>
Nobody has a definitive answer, but Gemalto estimate <a href="http://breachlevelindex.com/top-data-breaches">918 reported breaches</a> in the first half of 2017, while Verizon count nearly<a href="file:///home/keith/Downloads/rp_DBIR_2017_Report_en_xg.pdf"> 2,000 breaches in 2016,</a> and none of these are exhaustive list.

If you're reading this, chances are you're already part of <strong>multiple</strong> reported breaches, and possibly even more un-reported ones. Check out <a href="https://haveibeenpwned.com/">haveibeenpwned</a> to see if your email has been in other breaches.

They more services we consume, the more databases our data exist in, the more likely we are to be victims of breaches.
<h4>They have little re-sale value</h4>
But who's carrying out these breaches? and what are they using the data for?

The breached data are often traded on internet forums. If credit card data involved, they often go to carding forums that specialize in their trade. Depending on the type of the card, these numbers can go for <a href="https://krebsonsecurity.com/2014/02/fire-sale-on-cards-stolen-in-target-breach/">as low as $8</a>.

And that's credit card data which can be monetized (relatively!) easily. Personal account data, like MyKad Numbers and home addresses, require more effort to monetize, and hence, worth less.

So much less, that in cases like the Malaysian telco breach, they've been published online for free!

But why would attackers go through the trouble of 'hacking' only to publish it for free?

One word -- reputation.

Just because the online forums are anonymous, doesn't mean reputation doesn't count. All forums support a pseudonym, and that online identity can gain reputation for uploading leaked database. Some sites even have a point system based on how many leaked databases you uploaded.

Some users just copy the data from one forum and post it on another, gaining reputation on forums, but in the process guaranteeing the leaked data remains on the internet forever, and not dependent on a single forum or user.

You might be willing to pay thousands of dollars to protect MyKad number, but it's traded like pokemon cards online.

This tri-fecta of factors, means that trying to contain breach is a fools errand, and a non-starter of a solution.

But what happens if the breach occurs, but isn't yet on the internet? Do companies have still have a chance of containing it? As Uber learnt quite recently, the answer is still NO.
<h3><span style="color: #000000;">Part 3: The peril hiding data breaches</span></h3>
In 2016, Uber got hacked, and it was a classic case of a <a href="https://www.bloomberg.com/news/articles/2017-11-21/uber-concealed-cyberattack-that-exposed-57-million-people-s-data">single careless error</a> leading to a massive problem. Happens <a href="https://awsinsider.net/articles/2017/07/19/dow-jones-leak.aspx">all</a> <a href="https://www.engadget.com/2017/11/28/classified-us-army-nsa-data-stored-unprotected-server/">the</a> <a href="https://awsinsider.net/articles/2017/10/10/accenture-data-exposed-amazon-s3.aspx">time</a>, <em>this I.T thing is hard man, that's why you pay us the money!</em>

But the controversy wasn't about the breach, rather Uber's response to it.

Instead of reporting this to regulators and users, Uber signed up the attackers with an NDA (yes, a legal non-disclosure contract) and reported the extortion as a bug-bounty payment of $100,000.

<em>[<strong>Note to companies:</strong> Signing up extortionist with legal NDAs isn't a good breach response]</em>

The contract had specific personal details of the attackers, and once signed, put both Uber and the attacker  in a Mutually Assured Destruction (MAD) scenario.

No regulator, driver or rider was informed. There's a deep philosophical question here, if a breach doesn't happen on the internet, is it really a breach?

Turns out, the answer is still YES. Because Uber seemed had weathered this breach, for about a year -- Until they got a new CEO.

When Dara Khosrowshahi took over Uber, he decided to release a statement informing everyone of the breach. Only problem was that it took him months to do it

In a strongly worded letter, one US Senator made the <a href="https://www.scribd.com/document/365661732/11-27-2017-Letter-to-Uber">following statement to Uber's new CEO</a>:
<blockquote>While Uber reportedly learned of the breach in November 2016 -- and reports indicate you subsequently learned of the breach ... in September 2017 -- Uber decided not to inform passengers and drivers of the breach until last week. Even more disturbingly, Uber is reported to have shared information concerning the breach with potential investors prior to alerting regulators or affected drivers and passengers, as required under numerous state data breach laws</blockquote>
Joe Sullivan, Uber's chief security officer was fired, with some members of his team quitting shortly after.

So remember, if you're covering something up for your company, one day you'll get a new CEO, and things might not look so good. Case in point, the VolksWagon coder who helped them cheat on the emissions test. <strong>[Spoiler alert: <a href="https://www.theregister.co.uk/2017/08/25/vw_engineer_gets_3yrs_for_emissionbusting_sw/">he's in jail</a>]</strong>

Engineers can no longer use the <em>"I just followed orders"</em> excuse, didn't work for Joe Sullivan, didn't work for the VW coder, and it won't work for you.

People can forgive a breach, after all breaches happen everyday,

What people find harder to forgive is a deliberate attempt to conceal the truth. That's unethical.

And while most lawyers in Malaysia,<a href="http://www.malaysianbar.org.my/press_statements/press_release_|_personal_data_breach_reported_on_19_october_2017.html"> including the Bar Council</a> are of the opinion that the breach notification isn't part of Malaysian law, I beg to differ, I think the PDPA does mandate breach notifications (just not explicitly), and that's what we cover next.
<h3><span style="color: #000000;">Part 4: The Ethics of Breach Notifications</span></h3>
Few lawyers give much thought to data breaches, and hence the legal literature around them is sparse. But I did find this gem of an article from <a href="http://pwc.blogs.com/cyber_security_updates/2014/11/ethical-positions-in-breach-handling.html">PWC</a>:
<blockquote>...the question of giving of notice to regulators and individuals, the narrow legalistic view would be that the Data Protection Act does not contain an express requirement for notice...

But how does an ethical view alter the situation? The answer might be ... the ethically correct thing to do is to give notice, perhaps based on the rationale that notice will reduce the risks of harms...

But surely that can't be right? The law and ethics cannot deliver conflicting judgments on matters of fundamental importance? Surely the bigger picture requires convergence of results?...

Unlike printed words in legislation, the people who oversee us and sit in judgment over us have ethical content and context....they apply a purposive approach to the interpretation of the law when that is required to deliver just results.  Thus, they can take the view that the legally correct thing to do is the ethical one. At that point <strong>breach disclosure is seen as being part of the law, regardless of the narrow picture within the text of the Data Protection Act</strong>.</blockquote>
If you're a victim of a data breach, as nearly all Malaysians are, no provision in the PDPA explicitly grants you a right to be informed. But if we define Data Breaches as "Involuntary Data Disclosures" the picture clears up.

The PDPA states that if someone discloses your data to a 3rd-party, they have to inform you, and seek your consent prior to disclosure. Seems logical, that if they lost (instead of disclosed) that same data, to a malicious 3rd-party, those same principles apply. Obviously consent is moot when it comes to breaches, but the notice and choice principle is meant to inform the data subject, and that principle should still stand.

But I'm no lawyer, so let's ask a simple question.

Are other jurisdictions, who've thought about this long and hard enough, coming to a conclusion that breach victims should be informed, and is there a general trend towards breach notification?

YES and YES!

In the US, such laws exists in most states, and a Fedaral law is in motion.

In Europe, the GDPR will mandate notifying victims within 72 hours, on top of the existing<a href="https://en.wikipedia.org/wiki/Telecoms_Package"> telecoms package, which already mandates breach notification</a>.

Even in the Philippines the Data privacy commission ordered <a href="https://www.rappler.com/newsbreak/in-depth/165398-lessons-learned-one-year-since-comelec-voters-data-leak">the Election Commission (COMELEC) i</a>nform breach victims, in the wake of their 2016 data breach. The privacy commission also recommended that the <a href="https://privacy.gov.ph/privacy-commission-finds-bautista-criminally-liable-for-comeleak-data-breach/">chairman of the COMELEC be criminally prosecuted</a> (Criminally!!)

When a company takes my data, they have a moral, ethical and legal obligation to inform me of who they're giving that data to, and what that 3rd-party is doing with it.

That responsibility cannot vanish just because the data was 'hacked'.

We cannot reduce the responsibility of data collectors when data is lost to malicious 3rd-parties, if anything we need to increase their responsibility, to incentivize them to more fervently protect data.

I'm particularly disappointed that no one from the telcos have leaked anonymously to the press, or spoken off the record to reporters. I don't understand how an entire industry can collective lack conscience on the issue. Under normal circumstances, the telcos fall over themselves to assure us that customers are the most important thing to them, and that they <a href="https://youtu.be/P-MUABLEcWw?t=7s">commit to transparency</a>.

Customers are important to telcos? Transparency?! Really?!

Because in this instance -- the customers were not important at all, and there certainly isn't any transparency from the telcos. If customers were as important as telcos claim, they'd have informed each and every victim by now, and compensated them in some form.

So I don't think telcos care about their customers, and I certainly don't think their transparent.

But informing the victims are just the first step in handling a data breach. Next, we explore ways of mitigating the impact to Malaysians from our massive breach.
<h3><span style="color: #000000;">Part 5: Reducing the impact of breaches</span></h3>
As we discussed in previous posts, eliminating or containing breaches are impossible, instead the focus should be mitigation, and that needs to happen at a policy level.

Individually, there's little you can do to tackle the breach, but the government needs to setup policies to mitigate the impact of the Telco breach, and prepare us for future breaches <em>(and oh yes, there will be more!)</em>

But before that, we need to tackle some flaws in with our MyKad, specifically their numbers.

Having a single identifier, like the MyKad number, is a good thing, the Government needs something that uniquely identifies you. It helps ensure don't vote twice, or allow tax authorities to audit all your bank accounts.

But an identifier, should just identify your, not reveal information.
<h4>MyKad as Identified</h4>
Today, MyKad numbers reveal your age, gender and state of birth. Identifiers are usually public knowledge, and hence shouldn't contain revealing data. If MyKad numbers are designed to be shared, then people should feel comfortable sharing them (like duh!) How many people are comfortable sharing their age?

A good example are bank account numbers, just browse Lelong, where sellers openly publish their bank account numbers -- because the only thing anyone can do with them, is give them money.

Let's re-design MyKad numbers to be good identifiers by removing information from them and then let's stop using them as authenticators.
<h4>Autheticators? WTF is that?</h4>
An <strong>identifier</strong> makes a claim of who you are, and <strong>might</strong> be public knowledge.

An <strong>authenticator</strong>, proves that claim, and <strong>must</strong> be secret.

Think of identifiers as usernames, while authenticators are the passwords. Unfortunately, we've made MyKad numbers both -- and obviously something can't be public knowledge and secret at the same time.

Many organizations assume I'm Keith Rozario, just because I know Keith Rozario's MyKad number. When I call my bank for information like my account balance, they will usually 'verify' me by asking questions like:
<ul>
 	<li>What's my MyKad Number</li>
 	<li>What's my Address</li>
 	<li>How do I usually pay your Credit Card Bill, etc etc.</li>
</ul>
The answers to the first 2 questions are in the Telco Breach, and freely available online for anyone. And there are  an uncountable number or organizations that already have my MyKad number and address. MyKad numbers are NOT secret, they were never designed to be, let's stop pretending that they are.

A possible alternative is to use a Phone Pin, or a voice password but let's move on away from MyKad numbers, and onto identity freezes.
<h4>Identity Freezes</h4>
Today, If you fail to pay your Digi bill, you end up on a blacklist, and no telco will give you a post-paid line.

Systems like CTOS and CCRIS, are in place to protect corporations from giving credit to the 'wrong' people.Let's take those same systems, and use them to protect data breach victims as well, which at this point is every Malaysian.

I propose the concept of an identity freeze, where you can freeze your identity from being accessed by anyone. This automatically means banks won't give you credit, but can also prevent telcos from issuing you accounts (even prepaid ones). Very similar to credit freezes in the US.

Once you freeze your identity, you'd be safely assured that no one can take out loans, credit cards, or phone lines in your name. Today, the only people with that assurance, are people on the blacklist.

The process for unlocking an identity should be painful (relatively speaking), very verbose, and temporary. The default should be frozen unless otherwise requested -- and the entire system should be provided for free.

This mitigates the impact of data breaches, giving victims some control of their data, and ensuring the damage of the breach is limited. It reduces the value of data breach information, because it would take a lot more to monetize the data, which in turn would probably(!) reduce the number of breaches themselves.

Though again, once that breach data hits the internet, there's no stopping it.

But mitigating impacts to victims is one thing, many are interested in holding companies accountable for this breach. Data breaches are the new normal, but companies shouldn't be let off scot-free. In the next post, we explore how to determine if the company has taken reasonable steps to protect your data.
<h3><span style="color: #000000;">Part 6: Practical Steps for Security</span></h3>
When it comes to security, the PDPA is rather light. I won't waste space quoting it , but the crux is that companies that have personal data must take<span style="text-decoration: underline;"> practical steps</span> to secure the data. Fortunately, those practical steps are not defined, because technology always outpaces legislature.

The PDPA instead outlines principles, and leaves it to judges and regulators to constantly redefine what is practical (or not). It's unfair to judge a security incident from 4 years ago, using the knowledge we have today, the risk profile and technicalities surrounding data breaches have evolved immensely.

It's yet, another reason, why disclosing a breach as soon as it's discovered is in the organizations own interest. It means you get judged 'in your own time' , and not 3 years down the road, when people are more paranoid, and security levels are much higher.

But that still begs the question of what are practical steps?

Instead of focusing on firewalls, and anti-virus, and block-chain (gasp!), the focus should be on simple questions that any layman can understand.
<ol>
 	<li>What is the gross revenue and profit of the company?</li>
 	<li>What's the highest ranking officer in the organization that looks purely at security?</li>
 	<li>What are the resources (budget and people) allocated to to that ranking officer?</li>
 	<li>What were the recommendations of that team prior to the breach, and which of them were (or were not) followed?</li>
</ol>
If the highest ranking security officer is Freddy who just graduated in marketing last year, then that's not very practical, or If the team the security officer team consists of two interns, both of whom were aspire to be copy-writers, that's not very practical.

You get the picture.

It's only AFTER we've established that the security officer had sufficient rank, and that a reasonable amount of resources and budget were allocated, do we need go into the specifics.

And, we will rarely need specifics. (trust me!)

Equifax , a company whose revenue runs into the Billions (!) , laid the blame for their massive breach down to a single employee, <a href="https://techcrunch.com/2017/10/03/former-equifax-ceo-says-breach-boiled-down-to-one-person-not-doing-their-job/">Tech Crunch reported</a>:
<blockquote>“The human error was that <strong>the individual</strong> who’s responsible for communicating in the organization to apply the patch, did not,”

The notion that just one person didn’t do their job and led to the biggest breach in history is quite an amazing claim and shows a fundamental lack of good security practices.</blockquote>
If a billion dollar organization, left patching of critical software to Bob from accounting, we don't need to ask about firewalls now, do we?
<h3><span style="color: #000000;">Part 7: Conclusion</span></h3>
This was a 7-part post, with a total word count exceeding 3700, and if you've come this far you deserve nothing less than a solid hand-shake, pat on the back, and a freaking 5-star medal. Unfortunately, I can only afford first two, if you ever see me in the person, come on over and claim your prize.

So let's wrap this baby up.

Data breaches are the new normal, and people have accepted that. But it doesn't mean they aren't damaging both to victims and the organizations involved. Once a breach happens, there's no containing it, affected organizations involve should quickly move to inform the victims.

And even though current laws in Malaysia don't explicitly require breach notifications, applying the principles in the PDPA, will lead us to conclude that breach notification is indeed mandatory and that is inline with the global trend.

To mitigate the impact of data breaches, regulators need to revamp the mechanism and systems we have in place. Specifically the MyKad numbering system which desperately needs a revamp, and implementing a robust identity freezing system, that will allow average citizens better control of their data.

In the end, we will eventually learn to build systems that handles breaches effectively, but until then victims will continue to suffer. Here's hoping we reach that point sooner rather than later.

THE END. (phew! that was a long one)

Got any thoughts around breaches?

Hit me up on email keith [at] keithrozario.com , or find me on twitter <a href="https://twitter.com/keithrozario">@keithrozario</a>.

<em>As a bonus, here's a short piece about <a href="https://www.keithrozario.com/2017/12/part-8-false-prepaid-registrations.html">false prepaid registrations</a> you might want to read, to help untangle the giant hairball that is the Malaysian Telco breac</em>h.