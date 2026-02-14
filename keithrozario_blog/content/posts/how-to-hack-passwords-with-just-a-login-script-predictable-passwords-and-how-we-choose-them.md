+++
title = "How to hack passwords with just a login script: Predictable passwords and how we choose them."
slug = "how-to-hack-passwords-with-just-a-login-script-predictable-passwords-and-how-we-choose-them"
date = "2011-07-19T11:03:57"
draft = false
categories = ['Misc']
+++

<a title="Troy Hunt" href="http://www.troyhunt.com/" target="_blank">![](/uploads/362527788_a603f4195b-199x300.jpg "Hacked Accounts")Troy Hunt</a> a Software Engineer, Microsoft MVP and the genius behind the website <a title="Troy Hunt" href="http://www.troyhunt.com" target="_blank">www.troyhunt.com</a>, did a huge analysis on recent password hacks on Sony and Gawker to come up with a pretty daunting conclusions on how people choose passwords and why email accounts are easily hacked.<!--more-->

First, let's take a step back and highlight that there are a couple of ways to hack and email account, one is through a method called phishing where an attacker tries to get your password by pretending to be a person from Gmail/Hotmail/MSN, etc etc and then tells you your account has been compromised please do the following..etc etc. Then you'd inadvertently give them your password and voila, your accounts been hacked.

The next method is the more interesting one, it's where an attacker knows nothing (or almost nothing) about you and then just tries to guess your password. Once the attacker has your password, he logs on your account, and changes your password (thereby locking you out), and then proceeds to wrecking havoc with your email. You'd think that would be a waste of time, considering your password is secure, well yours may be secure but a lot of people use passwords that are either easily guessed or just downright dumb.

According to Troys research 3% of people use their username as their password. So if your login was <strong>racecar73@facebook.com</strong>, your password would be <strong>racecar73</strong>. What that means is that if I have a script and the 300,000 accounts that Troy used in his data set, I would be able to access 9,000 accounts by just using the username as the password. You read that right...9,000. Who needs to send multiple emails or scam someone, I could get 9,000 accounts with publicly available data.

Then I could re-run the script and this time instead of using the username, use the word "<strong>password</strong>" as the password. According to Troy, "<em>My password source of several hundred thousand accounts had nearly two and a half thousand “password” passwords which is not only a pretty poor choice given its clearly available in a dictionary, it’s also an insanely obvious one." </em><em>
</em>

So if you had a script to just continuously attempt logins into Facebook/Hotmail/Gmail, and you just set to attempt either the username or the word "password" , you'd be looking at about 3,000-4,000 hacked accounts for every 100,000 accounts you attempt to hack. This without knowing a single thing about your victim.

Troy research is well written and quite extensive and I definitely recommend you read it <a title="Troy Hunt" href="http://www.troyhunt.com/2011/07/science-of-password-selection.html">here</a>. He also talks about most people using their names with a number suffix, and how 14% of people use a password comprised of only numbers...what's the most popular numbered password? <strong>123456</strong> of course. DAMN!

So if you're using a common password, I suggest you change. Troy also has a recommendation for that <a title="Troy Hunt" href="http://www.troyhunt.com/2011/03/only-secure-password-is-one-you-cant.html" target="_blank">here</a>.

The great piece of news brought to you via <a title="Slashdot" href="http://it.slashdot.org/story/11/07/18/2327208/The-Science-of-Password-Selection?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+Slashdot%2FslashdotIt+%28Slashdot%3A+IT%29" target="_blank">Slashdot</a> via <a title="Troy Hunt" href="http://www.troyhunt.com/2011/07/science-of-password-selection.html" target="_blank">Troyhunt</a>

That great picture brought to you via flickr: <a title="Flickr" href="http://www.flickr.com/photos/harmony19490/362527788/sizes/m/in/photostream/" target="_blank"><em><span style="color: #888888;">http://www.flickr.com/photos/harmony19490/362527788/sizes/m/in/photostream/</span></em></a>