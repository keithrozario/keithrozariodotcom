+++
title = "The problem with bio-metrics"
date = "2015-10-18T15:59:49"
draft = false
categories = ['CyberLaw', 'Security &amp; Privacy']
+++

<a href="/uploads/8229504229_47a07ff41f_z.jpg"><img class="alignleft wp-image-5237 size-medium" src="/uploads/8229504229_47a07ff41f_z-300x200.jpg" alt="8229504229_47a07ff41f_z" width="300" height="200" /></a>Passwords have always been a problem.

For a password to be adequately secure, you need a certain amount of randomness <em>(or entropy in geek)</em> associated with the password to ensure it can't be easily guessed. The password <strong>monkey</strong> is less secure than the password <strong>k3ithI$one$3xydev1l, </strong>but the latter is inherently harder to remember (although still very true).

Remember you should use a different password for each online service you subscribe to, Your Jobstreet credentials should be different from your banking credentials. This way, if someone hacks into Jobstreet and compromises their passwords, your banking credentials remain secure.

What people often do is re-use one password across all their services, so that a compromise on one service is as good as a full-blown compromise across their entire online identity, a hack on that nutrition forum you visited two years could cause you to lose your life savings.

There in lies the trade-off, a easier to remember password is also easier to guess, and hence easier to hack (<em>Google 'the fappening' if you need more convincing</em>), while a hard to guess password is harder to remember, and near impossible to execute if you need remember a different password for each your online services.

Which suggest that the problem isn't passwords per se, but rather our human inability to remember long un-guessable passwords. Computers have long out-stripped us in this arena, and trying to overcome that is pretty much unthinkable at this point.

But what is the solution then? Well, in general we have 2 partial solutions.<!--more-->
<h2>Password managers</h2>
<a href="/uploads/17046271105_2b6a5a619f_z.jpg"><img class="alignright wp-image-5235 size-medium" src="/uploads/17046271105_2b6a5a619f_z-300x300.jpg" alt="17046271105_2b6a5a619f_z" width="300" height="300" /></a>One is to use a password manager, like LastPass. LastPass stores a unique password for each of your online services, while requiring you to remember only one. Basically, it securely stores your password in a 'vault' that is encrypted by a secure key known only to you. When you use LastPass, you download the encrypted vault from the lastpass servers, and then decrypt it with your (hopefully) hard to guess secret key. This way you can have unique, hard to guess passwords for all your services.

But there's a catch, LastPass itself then becomes a high value target for attackers. Thankfully LastPass is pretty secure and provides the option for 2 factor authentication. Now, LastPass just happens to be the password manager I use, most other password managers would do just fine.

The one strongest piece of security advice I could give you is to use a password manager, it will reduce a lot of your headaches.
<h2>Bio-metrics and Permanence</h2>
<img class="wp-image-5234 size-medium alignleft" src="/uploads/16250748818_b1f9bc160e_z-300x169.jpg" alt="Biometric validation" width="300" height="169" />The 2nd option is to use a bio-metric authentication. Your thumbprint or retina scan is unique only to you, and is quite hard to guess. So obviously that's a good place to start.

But there is a problem with bio-metrics that makes me shudder at the thought of ever using it as an authentication mechanism--it's PERMANENT.

Passwords and credit cards are mostly temporary. A new credit card, with a new number can be issued to you in days, a password can be reset in minutes, but a thumb-print is forever.

You're vulnerable when your credit card gets stolen, but that vulnerability disappears the moment you cancel the card.If you bio-metric data was stolen, the vulnerability continues in perpetuity because your thumbprint and retina scan are yours for perpetuity. If the bank lost your thumbprint data, if can't issue you a new thumb...and that's a problem.

This isn't a theoretical scenario either. The United States, Office of Personal Management (OPM) was hacked recently, and hackers carted away the biometric information of more than 1.1 million US military personnel, and as Technology moves more and more into bio-metrics, that stolen data only grows in value.

Many in the Obama Administration think the Chinese government was responsible for the hack, which is a double edge sword for the victims. After all, having a government steal your data is probably better than having a Russian crime syndicate steal it, but then again these are American Government employees, some of whom may have had a bright career ahead of them--cut down because a foreign government now has their data.

If your fingerprints are known to the Chinese Government, you're not going to be one authorizing nuclear launches in the foreseeable future. In fact, in an ironic twist, CIA operatives in Beijing were recalled, precisely because their names were NOT on the list of victims, singling them out in what was supposed to be a covert operation. Hence these CIA operatives, who were not part of the OPM breach, were sort of secondary victims of a primary crime.
<h2>One Way functions to the rescue</h2>
There are some ways to limit the damage associated with bio-metrics while still enjoying the benefits and ease they provide.

One of them is to use one way functions on the digital data. A one-way function is a mathematical function that goes only one way, sort of like a pressure valve that lets water flow in one direction but not the other.

In primary school arithmetic, we're used to seeing two-way functions that can be easily reversed. Addition one way, Subtraction in the other, or Multiplication one way, and Division the other. In each of these cases the effort is almost equal in either direction.

But consider a square function, one where a number is multiplied by itself. So the square of 5 is 25, and conversely the square root of 25 is 5. Now, if I asked you to calculate with just a pen and paper the square of <strong>9,876,293,232,980</strong> it may take you some time, but it's possible. If instead I asked you to calculate the square root of <strong>97,541,168,023,806,540,559,680,400</strong> with just a pen and paper, you might as well not even start. The effort required to get a square root of a number is far harder than to square a number. One way functions are the extreme of these, where once the function is completed, there is absolutely no way to go back.

But what do one way functions have to do with it?

Well if instead of storing your fingerprint, I stored the resulting one-way function of the digital output of your scanned fingerprint <em>(remember digital means digits, hence numbers)</em>, it means that I can authenticate your fingerprint without ever needing to store your biometric information (which is the proper way of storing passwords as well). This reduces the effect of a hack, as the hackers can't get your fingerprint from the hacked data.

To keep the analogy, instead of storing you actual password <strong>9,876,293,232,980 </strong>I would store the square of it, knowing that even if the attacker knew the square they wouldn't be able to square root the number to get the password (it's a poor analogy, but one that works).

The problem with this approach is that it can't do approximations, and you couldn't determine if a partial fingerprint was taken because the fingerprint has to be treated as a whole.One way functions are also pretty unique, and even a small change in the input results in a drastically different output, which means a slight alteration in your fingerprint, because you burnt your finger while cooking some chicken curry, will force you to re-authenticate yourself. Something you could get away with if you were just comparing a scanned fingerprint to a stored fingerprint and allowed for a certain threshold of variability.
<h2>Central storage</h2>
Finally we have the central vs de-centralized hosting. If your bio-metric information were stored only on your phone, it could still be a problem, but a smaller one than a central server that hosted 1.1 Million fingerprints inside.

A phone with just one thumb-print also presents a less desirable target to criminals, hence reducing the likelihood of an attack.

The reason I bring one way functions and central storage up, is because I think that if anyone wants to store your biometric data, then need to be up front about how they store that data, and then the user has to make a conscious decision about whether to proceed or not.

Most regular users are probably not aware of the dangers of using biometrics, and could wind up losing more than they bargained for. Knowing if a service that uses bio-metric authentication stores hashes (rather than scans) and knowing where that data is stored is something everybody needs to be aware of, and if my laymen reading of the Personal Data Protection Act is correct, it is actually a legal right you have.
<h2>Are Bio-metrics secret?</h2>
There's an added weakness to biometrics as well, they're not entirely secret. You're leaving your fingerprints on literally everything you touch, if your car was stolen chances are your the thieves have your biometric details as well.

What's worse is that criminals know exactly where your thumb and retina is at any time. There's a scene from the movie Demolition Man where in order to open a prison door, the criminal (played by Wesley Snipes) plucks out the victims eyeball to pass a retina scan. Closer to home, an owner of a brand new Mercedes S-Class had his thumb cut-off by carjackers because they needed it to disarm the immobilzer.

Still think bio-metrics are a good idea? Imagine if the Mercedes used Retina scans to disarm the car?
<h2>5th Amendment rights</h2>
There's also little protection offered by bio-metrics if the Government gets involved. In the US, the 5th amendment protects a citizen against self-incrimination, meaning that the Government cannot compel you to testify against yourself. This is why the first thing a Police Officer says when he's arresting you is that you have the right to remain silent, which means you can choose not to answer any questions--at all.

Those questions could be, what's the password for your iPhone.

But if you protected your iPhone with a touchID, then all bets are off. Because a fingerprint is something you have, instead of something you know it doesn't get the 5th Amendment protections as passwords. The Government can't compel you to unlock a password protected phone, but they can compel you to open a bio-metric secured one.
<h2>Conclusion</h2>
<img class=" wp-image-5236 alignleft" src="/uploads/10643204815_655b8e60c8_o-300x300.jpg" alt="10643204815_655b8e60c8_o" width="270" height="270" />So between the permanence of bio-metrics, their lack of 5th Amendment protections and the chance that they can cause you some serious physical harm, I'd be very very worried about using a bio-metric to protect anything, let alone something as important as my bank account.

Plus they're not even secret, you're leaving your fingerprints on everything you touch--that doesn't apply to your ATM PIN which never leaves your head. Biometrics aren't all that good.

Because if the Office of Personnel Management for the worlds most powerful nation can be hacked, I'm sure a bank in Malaysia could be as well.