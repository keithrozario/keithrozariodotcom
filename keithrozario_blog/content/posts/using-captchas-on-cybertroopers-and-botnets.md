+++
title = "Using Captchas on cybertroopers and botnets"
date = "2013-07-11T08:00:01"
draft = false
categories = ['Copyright and Censorship', 'Crowdsourcing', 'Malaysia']
+++

Last week I wrote about the <a title="The Malaysian cybertrooper phenomenon or is it Botnet?" href="http://www.keithrozario.com/2013/05/malaysian-political-cybertrooper-botnet.html">'rigged' EDGE poll</a>, that the EDGE had to eventually take down because they suspected someone was trying to bias the results. It was later revealed that a handful of IP addresses were responsible fro the bulk of the votes--presumably the fake ones. An IP address defines a unique internet connection, but not necessarily a unique device. You can try this yourself at home, and connect your PC, Laptop, Tablet and phone to your Wi-Fi router and then go online to check your IP from each--all of your devices will have the same 'external' IP address.

So in theory, the IP address could have belonged to a shared cybercafe where everyone was logging in and voting on this obscure Poll--but that's unlikely. What's more likely is that a single PC loaded with a simple script was logging into multiple times to the EDGE and continuously voting. There's no other way to get 6,000+ votes in a short space with a regular human being.

That of course, begs the question--how can you fix this. Well the answer to these automated scripts has been around for quite sometime now, its called a <a title="Why ReCaptcha works: The 4 requirements of Crowdsourcing" href="http://www.keithrozario.com/2011/12/recaptcha-4-requirements-crowdsourcing.html">CAPTCHA</a> and it looks like this:

<a href="/uploads/What-is-reCAPTCHA-.png"><img class="aligncenter size-full wp-image-3616" alt="What is CAPTCHA" src="/uploads/What-is-reCAPTCHA-.png" width="465" height="148" /></a>

You've seen this before, a Captcha is a simple test of human-ness,

A Captcha is a little bit of checking most websites do to make sure you’re a human. Now the reason they’re all jumbled up and ‘squigly’ is simply because the squigly-ness makes it impossible for a computer program to read. In fact no one has yet come up with a program that can read a Captcha, yet even my 6 year old niece can be able to identify most Captchas on the first try, which tells us a lot about the difference between man and machine.

<span style="font-size: 13px; line-height: 19px;">As far as vote rigging prevention methods go, a Captcha is more like a long line at the polling center, rather than indelible ink. A Captcha doesn't prevent anyone from double-voting but it does raise the effort required to place a vote to the point where one person submitting 6,000 votes would be practically impossible. It's a 'proof-of-work' that basically charges the user for whatever transaction was being performed, in this case the user is charged the time and effort it would take to solve the Captcha before placing their vote. The fact that the transactions cost something, means that at some point it becomes economically infeasible to repeat the transaction over and over again--whether that transaction was a vote for an online poll, or a comment on a blog or even sending out an email. </span>

So the proof-of-work actually helps address the bot-nets or even cybertroopers, I wonder why the EDGE didn't implement it?