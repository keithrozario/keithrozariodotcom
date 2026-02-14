+++
title = "Phishing by the Bank--Maybank that is"
date = "2014-10-31T23:30:30"
draft = false
categories = ['Misc']
+++

Recently I received a phishing email from konzie2@usm.edu telling me that Maybank had installed new security features and that I need to validate my details on the Maybank2u web portal. The email was marked as SPAM by Gmail, and trying to visit the site further sparked more warnings from Firefox AND my anti-virus.

But I was curious as to what the link would entail, in much the same way I was curious about the RHB phishing emails I received some months back.

Hopefully this post gives you an indication of just how sophisticated these attacks are, and manages to educate you on the one true way to establish if the site you're visiting is genuine.

<a href="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-18-45.png"><img class="wp-image-4644 aligncenter" src="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-18-45.png" alt="Fake Maybank2u login page" width="550" height="400" /></a>

The fake login page for Maybank2u looks exactly like the REAL login page of Maybank2u, there really is no difference from the victims perspective. What's more interesting is when you go deeper, by just enter in 'a' username and a password you get to the following page (please don't enter 'your' username and password, just 'a' username and password)<!--more-->

First it will ask you to change your Maybank2u challenge questions--these are questions you use in order to get back control of your account in case you've lost your password.

<a href="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-21-04.png"><img class="wp-image-4633 aligncenter" src="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-21-04.png" alt="screenshot-cabohealthtravel com 2014-10-28 10-21-04" width="550" height="379" /></a>

&nbsp;

Then they ask you to change your withdrawal limits (those slimy sneaky fellas...)

<a href="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-22-25.png"><img class="wp-image-4635 aligncenter" src="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-22-25.png" alt="screenshot-cabohealthtravel com 2014-10-28 10-22-25" width="550" height="396" /></a>

&nbsp;

Then it ask you to change your email--presumably so no warnings reach your email;

<a href="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-24-08.png"><img class="wp-image-4638 aligncenter" src="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-24-08.png" alt="screenshot-cabohealthtravel com 2014-10-28 10-24-08" width="550" height="394" /></a>

&nbsp;

&nbsp;

At each step of the way---the site request for your TAC, and performs an almost flawless man-in-the-middle attack on the would-be victim. The site was professionally coded (at least from the display perspective), and worked to get the user to change certain key elements of their account information to facilitate large withdrawals of money.

Finally they end with this:

<a href="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-27-23.png"><img class="wp-image-4643 aligncenter" src="/uploads/screenshot-cabohealthtravel-com-2014-10-28-10-27-23.png" alt="screenshot-cabohealthtravel com 2014-10-28 10-27-23" width="550" height="353" /></a>Real sneaky guys,  it reads that your details are being processed and advises you "NOT" login for the next 2 hours to "avoid errors in their database"---presumably so that they can rob you blind in those 2 hours.

The commonality between this and a past post I wrote about a <a title="RHBNOW Email: Intricate details of a Phishing scam" href="http://www.keithrozario.com/2014/07/rhb-phishing-scam-details-phishing-scam.html">RHB phishing scam</a> is remarkable.

1. They both use hacked wordpress sites to host their page

2. They both use fake emails to start the phishing scam

3. They both look identical to the real bank websites.

So how can you make sure that the bank website you're visiting is genuine and not these fakers. The one sure fire way, is too look for the green bar of SSL. If you use Chrome or Firefox you can see a green bar  where you type the address of your banks website. The only way a criminal can fake a green bar is either by controlling your machine altogether ( in which case everything you do is already compromised) or by solving a really hard maths problem which is infeasible today--and I would argue if the criminal figured out how to that, he's not coming for you.

Remember folks, if it ain't green--don't login. And if your bank doesn't have a green bar website, my recommendation is to get a new bank.
<h2><a href="/uploads/RHB_Real.png"><img class="wp-image-4473 aligncenter" src="/uploads/RHB_Real.png" alt="Real RHB Website" width="550" height="400" /></a>Conclusion</h2>
I was really impressed by the sophistication of this attack, and downright amazed at the "Do not login for the next 2 hours to avoid errors in the database" message--that one was just slimeball move.

I can't help but feel sorry for the people who did this, a lot of people I know don't get IT at all--and they're afraid of most things tech, so when a seemingly genuine email somehow breaks the barrier to their inbox, they just do as they're told, and for the average person trying to figure out what's real and what's not is really hard.

If you're going to take just one thing away from this post, take this--if it ain't green, don't login.

&nbsp;

&nbsp;