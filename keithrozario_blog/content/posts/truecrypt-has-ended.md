+++
title = "TrueCrypt is dead, long live ....bitlocker?!?!"
date = "2014-05-30T09:00:18"
draft = false
tags = ['TrueCrypt']
categories = ['Security &amp; Privacy']
+++

&nbsp;

The understatement of the month would be calling this a peculiar moment. This is far from peculiar--this is straightup WTF?!

My favorite encryption software, TrueCrypt, has been abruptly and mysteriously shut-down<strong><em>(que dramatic music!!!)</em></strong>. The official TrueCrypt website now only has some information on 'alternatives' and offers the following advice.
<blockquote><span style="color: #ff0000;">WARNING: Using TrueCrypt is not secure as it may contain unfixed security issues</span></blockquote>

TrueCrypt was really awesome, it had features like full-disk encryption and even encrypted volumes within encrypted volumes for 'plausible deniability'. The anonymous authors of the software have apparently thrown in the towel on what was the best free encryption software on the web.Yes, TrueCrypt was free just like Apache and OpenSSL, and just like them was pervasively used by tech-savvy web users. So any vulnerability on TrueCrypt would have severe ramifications--just like <a title="Heartbleed explained in under 2 minutes" href="http://www.keithrozario.com/2014/04/heartbleed-explained-in-under-2-minutes.html">Heartbleed had for OpenSSL</a>.

To avoid any 'heartbleed-like' issues with TrueCrypt--an initiative from within the security community was kicked off to <a title="Is True Crypt Audited Yet" href="http://istruecryptauditedyet.com/" target="_blank">perform a full security audit on TrueCrypt</a>. Support for the initiative wasn't hard to come by in the wake of recent developments like <a title="What is PRISM?" href="http://www.keithrozario.com/2013/06/what-is-prism.html">PRISM,</a> specifically the revelations that the US government was intentionally making encryption software weaker to allow exploitation further down the road.

But just when the audit was making good progress the TrueCrypt team dropped their bombshell. Brian Krebs suggest <a title="KrebsonSecurity" href="http://krebsonsecurity.com/2014/05/true-goodbye-using-truecrypt-is-not-secure/" target="_blank">that the shut-down is legit</a>, and this isn't some web-site hack or hoax. The speculation churning machine (a.k.a the entire internet) has been rife with guesses as to what really occurred, but honestly no one has the answer, except the authors of TrueCrypt--who are anonymous.

The problem for people who are using TrueCrypt--is what to do? TrueCrypt recommends bitlocker, but BitLocker isn't available for basic version of Windows--the version most people use? Also, Bitlocker hasn't been audited either and forgive me if I'm still a bit edgy about using Microsoft products. What with them <a title="Microsoft is eavesdropping on your skype conversations" href="http://www.keithrozario.com/2013/05/microsoft-eavesdropping-skype-messages.html">spying on my Skype </a>conversations and all.

I'm sticking to TrueCrypt for now, and wait till the dust settles before I decide to re-encrypt my drives with a new piece of software.After all the audit hasn't found any serious flaws, and even if it did I'm betting someone will fork the code as soon as it happens<!--more-->
<h2>Why do I use TrueCrypt?</h2>
Just so you know, The Malaysian Copyright Act of 1987 states that any Police Officer with the rank of Inspector (or higher) may enter your house to search for illegal copyrighted material without a warrant!!

Now I don't know a single Malaysian household that doesn't have an illegal DVD, some illegal software or just a fake t-shirt from Bangkok--except my house,because I'm a law-abiding citizen that loves Copyright laws. Rest assured though, the act has controls in place to limit these warrantless searches, for example the Police officer can y enter your house only if he--<strong>really feels like it</strong>!!

To be safe, I've encrypted my entire drive, which protects my data from prying eyes, and even if my laptop were stolen due to a house break-in, I can be 'reasonably' assured that my data was protected. It's just good practice to encrypt your drive, it makes sure your data is encrypted <strong>at rest</strong>, and provides far more security for your data than a standard windows password (which is easily bypassed).

Of course none of the encryption I implement would protect my data, if the application I used to encrypt it had  "unfixed security issues".
<h2>Conclusion</h2>
Should we trust TrueCrypt and other free software? Yes, this is a one-off situation and it shouldn't in any way change our trust level of open-source free software.

Correction:

*TrueCrypt was never OpenSource, it was more Source Available. The Source code to Truecrypt has always been available for viewing on sourceforge, however the project was never opened to the public to make additions of code. Unlike  OpenSSL, where the source was available and people could add code to it, which resulted in things like Heartbleed, all the code from Truecrypt has been written by a closed community.

It also means that the anonymous coders are the only guys that truly understand the entire code, and any modification may introduce some bugs or exploits--so a new TrueCrypt from some other authors may be potentially flawed.