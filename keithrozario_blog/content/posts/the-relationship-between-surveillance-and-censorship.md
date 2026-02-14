+++
title = "The relationship between surveillance and censorship"
date = "2016-03-27T16:01:30"
draft = false
categories = ['Misc']
+++

<a href="/uploads/314989744_5b5a852b47_z.jpg" rel="attachment wp-att-4940"><img class="alignleft wp-image-4940 size-medium" src="/uploads/314989744_5b5a852b47_z-300x200.jpg" alt="Spying Program" width="300" height="200" /></a>In the online world, surveillance and censorship are two sides of the same coin, you can't have one without the other.

When the government moots a 'blogger registration' act , we automatically infer it to be part of a wider censorship initiative, an attempt to control the narrative by subtlety telling bloggers <em>"we know who you are, so watch what you say".</em>

We intuitively get that putting a whole community under surveillance is a bid to control expression within that community, and if someone was even 'potentially' watching you--your behavior would change.

But the internet has made the connection between surveillance and censorship work in reverse, not only does surveillance lead to censorship,  but censorship leads to surveillance as well.<!--more-->

When the government censors SarawakReport or Medium.com , they do not specify the technical methods to the ISPs, all that they require is that the websites be 'difficult'  to access over their networks.

Most ISPs choose to implement this by poisoning their own Domain Name Servers (DNS). Think of DNS as the telephone directory your ISP operates, every time you want to visit Google or Facebook, you perform a lookup on the DNS server to get the IP addresses of the websites you want to visit. IP addresses work essentially the same way as phone numbers, once you have one you can 'dial' the server and create a connection.

What ISPs like Telekom Malaysia, Digi and Maxis do is simply corrupt their own directories to give you the wrong addresses for blocked sites. So instead of getting the legitimate IP addresses of Medium.com or SarawakReport.org, you'll get the address of a specially crafted server hosting a single page telling you that the website you want to visit has 'violated' Malaysian Law.

It would be trivial for the ISP to log which of its users was trying to access these block websites, and then provide a detailed list to the authorities when asked, and that's because every DNS request to their servers is uniquely identifiable. Simply put, your ISP is already looking into what websites you're visiting, and it is this surveillance makes censorship possible (even easy!).

Of course, I would be re-miss not to tell you that by simply <a href="https://www.keithrozario.com/2013/05/how-to-access-blocked-websites-malaysia.html">switching your DNS server</a> to other freely provided DNS services like OpenDNS and Google, you'd bypass this rather trivial blockage.

But let's dig deeper into more nefarious activities. In the run-up to the 2013 general elections, a popular user on the the Lowyat forums reported that <a href="https://forum.lowyat.net/topic/2794929/all">Telekom Malaysia was blocking access to certain Facebook pages and YouTube videos</a>, not all videos mind you--only specific 'politically' connected content.

Telekom Malaysia used a technique called Deep Packet Inspection (DPI), which involves not just  looking at connections as they whizz by their networks, but requires for them to <span style="text-decoration: underline;">look specifically at the content being requested</span>. It wasn't enough to TM to figure out that you were going to SarawakReport or Youtube, they had to know <span style="text-decoration: underline;">which specific page</span> you were visiting.

The reason was simple, blocking all of YouTube or Facebook would be political suicide. I guarantee you, that a government that blocks Facebook--won't be government for long.

So Telekom Malaysia <a href="https://www.keithrozario.com/2013/05/telekom-malaysia-t-is-censoring-the-internet-prior-to-ge13.html">deployed DPI</a> to dissect the requests that were made to YouTube and Facebook, determine if those request were for  'unsavoury' pages, and kill those specific connections. All other connections to Facebook and YouTube were left untouched. Goes without saying that even though they were primarily interested in specific pages, they were scanning all requests to YouTube and Facebook--effectively putting all their users under surveillance.

Once again, <em>in order to censor they needed to surveil</em>. Fortunately, things like DPI don't work anymore.

You see, even prior to our general election many websites were beginning to deploy <a href="http://www.slideshare.net/keithrozario/introduction-to-ssltls">TLS encryption</a>, that's the protocol that puts the 's' in 'https' and that little lock icon next to the url in your browser window. TLS signified that the connection to the server you were visiting was both authenticated and encrypted, and since these were good things , and the price of deploying TLS was approaching zero, most websites started implementing it.

But in June of 2013, a little kerfuffle concerning one <a href="https://www.keithrozario.com/2015/04/the-snowden-revelations.html">Edward Snowden</a> pushed many internet platforms to begin full adoption of end-2-end encryption for their websites. Google even began to penalize sites that didn't have encryption (or reward sites that did depending on who you talk to), organizations like the EFF began offering free TLS certificates, and now even mundane connections to sites like keithRozario.com enjoy full end-2-end encryption that is sealed from the prying eyes of your ISP (or anyone else for that matter).

What TLS provides is secrecy, that while your ISP may know you're connected to Medium or keithRozario.com, they can't figure out which page within that site you're visiting, and that's a problem, because DPI requires that they identify in detail which page you were requesting. With DPI rendered useless, censorship became an all-or-nothing issue.

That's why the Government had to block <a href="https://www.keithrozario.com/2016/01/medium-blocked-collateral-censorship-vs-collateral-freedom.html">ALL of Medium.com instead of just the SarawakReport content</a>, and everyone else on the popular blogging platform become collateral damage in the governments action.

By encrypting our connections to websites like Facebook, we've reduced their ability to carry out surveillance on our activities, this indirectly affected their capacity to censor--two sides of the same coin.

The one 'real' solution that removes any capability from your ISP to censor is to resort to VPN services or TOR. In both these options, even the 'meta-data' of the connection is encrypted as it transverses your ISPs network, only to be decrypted somewhere else on the internet, outside the prying eyes of local authorities.

If you're looking for a VPN, I have a suggestion <a href="https://www.keithrozario.com/2013/09/best-vpn-malaysia-privateinternetaccess.html">here</a>, or use TOR. You can (and should) use these services even if you're just casually surfing, your use of it provides 'cover-fire' for those using them for more serious reasons. If TOR were only used by journalist reporting on governments, it would be trivial for governments to detect them.

However, the government has one more trick up its sleeve.

If the connection is encrypted end-2-end, they'll just past the end.

In June of 2015, I wrote extensively about <a href="https://www.keithrozario.com/2015/07/hacking-team-got-hacked-and-heres-what-malaysia-bought.html">surveillance software the government bought from a company called Hacking Team</a>, and highlighted the <a href="https://www.keithrozario.com/2016/01/no-the-prime-minister-doesnt-need-spyware.html">3 government agencies</a> who procured them. This stuff was less surveillance software and more akin to hardcore hacking tools, used to hack into the computers of victims and begin spying on them in a very intimate manner.

Your smartphone holds so much personal information, that at times it may know more about you than your spouse. By hacking into these phones, the government was able to obtain an intimate and personal picture of the user, regardless of the encryption software being deployed, since the hack was down upstream of any data encryption.

The technical details are unimportant (but can be gleaned <a href="https://www.keithrozario.com/2015/07/hacking-team-got-hacked-and-heres-what-malaysia-bought.html">here</a>), what's important is to realize that the existence of such software creates a <a href="https://en.wikipedia.org/wiki/Panopticon">panopticon effect</a>. The idea that you don't need to spy on everyone, just some people and everybody else will fall into line, that people will adjust their behavior as long as there is a 'chance' that they were being under surveillance.

Truthfully, software we procured from Hacking Team is used to spy on just a handful of people, not bulk surveillance of hundreds, thousands or millions of people, but even knowing that such tools exist and 'could' be used on you, would make you think twice before you visited redtube or pornhub. If you were a Muslim, you might be unwilling to search for things like Syiah, or 'I want to touch a dog', it might make you unwilling to like that page about Israel...and so on.

And you might say that such effects are good, that forcing someone to think twice before they visit a porn site is desirable, but we shouldn't be held hostage to a over-bearing government who watches our every move. People should be allowed to use the internet un-hindered to enjoy the tremendous marketplace of ideas it offers, rather than limit ourselves to the confines of spaces the government deems 'good and desirable'.

Nobody wants to use the internet with someone constantly looking over their shoulder, it's a matter of human dignity to use the internet freely and openly without worry.

The common theme among victims of Stasi surveillance, was the feeling of betrayal when they discovered that some of their best friends (even spouses) were recruited by the Stasi to spy on them--this tears at the very fabric of society, if we can't trust each other, society stops working. The same might be said of our technology, that if we begin to second-doubt Waze navigation, or the amount of money we have in our bank accounts, it could diminish the goo that technology can deliver.

At some point, we may feel betrayed by the technology that the government has 'turned' against us. When they abuse the use of local DNS servers, perform deep packet inspection or even hack our personal smartphones, they force Malaysians to question the technology they use on a daily basis, and in some cases completely neglect using them. That is definitely not a good thing.

Next week (2nd April 2016), I'll be at the arts for grabs event speaking about government surveillance and it's impact on society, if you're even remotely interested on this topic, I encourage you attend and we can have a very interesting discussion.

Details <a href="https://www.facebook.com/events/1722706634672119/">here</a>.