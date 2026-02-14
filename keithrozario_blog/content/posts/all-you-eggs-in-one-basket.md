+++
title = "All you eggs in one basket"
slug = "all-you-eggs-in-one-basket"
date = "2016-10-02T20:45:49"
draft = false
categories = ['Misc']
+++

Is it wise to use an online password manager? After all, putting your passwords on the cloud seems like a really dumb idea.

But I use password manager because while storing stuff on the cloud may present risk, it's far riskier and dumber to re-use passwords.
<h2>Why you need a password manager?</h2>
Despite the sexiness of zero-day exploits and hardcore state-sponsored hacking groups we see on the news, the number one way the average person gets hacked is <a href="https://www.schneier.com/blog/archives/2016/05/credential_stea.html">through password compromise</a> (boring!). That's when hackers guess, or somehow figure out your passsword, and then use it to access the various online services you subscribe to.

Most people downplay the risk of this happening, ebcause they think they're not rich enough, or famous enough to be the target of hackers. But in an era, where hacks <a href="https://www.theguardian.com/technology/2016/sep/23/yahoo-questinos-hack-researchers">compromise millions of accounts</a>, and hackers can automate exploits to run on cheap cloud servers from Amazon--you'd be surprise what hackers consider a worthwhile target.

But how do hackers get your password?

On occassion they actually guess it, ala <a href="https://en.wikipedia.org/wiki/ICloud_leaks_of_celebrity_photos">'the fappenning'</a>, but more commonly they get your passwords by hacking other services. Shockingly, sometimes the easiest way to get your Google password is to hack dodgy forums, and insecure chat rooms that litter the internet.<!--more-->

<em>Say what now?!!</em>

Because most people <span style="text-decoration: underline;">re-use the same password across all their online accounts</span>, a hack on a dodgy forum or chat room online can sometimes lead to people's Paypal accounts and Gmails getting compromised. If you re-use your Paypal password on a dodgy online forum with shitty security, then your Paypal account has shitty security--and there's nothing Paypal can do about it.

So in order for you to be safer online, you need to practice good password hygiene, and that requires you to do 3 things.
<ul>
 	<li>Use strong passwords <em>(so they can't be guessed)</em></li>
 	<li>Don't re-use your passwords <em>(so that compromised passwords on one service, doesn't affect others)</em></li>
 	<li>Use two-factor authentication whenever possible</li>
</ul>
But we're all human, and there's no way we can remember hundreds of passwords (I have 200+ of them on LastPass), let alone hundreds of 'strong' passwords. I can't even remember all the names of the obscure relatives I meet on Christmas.

And that's where password managers come in, they allow you to remember just one strong password, and it'll take care of the rest. And since the password manager is storing the password for the services, your passwords can be secure enough to be practically irreversible even if hackers broke into a service you subscribe to. <em>(<a href="http://www.bfm.my/keith-rozario-internetless-public-service#">listen to my podcast on how Mark Zuckerberg got owned here</a>).</em>
<h2>Are password managers safe?</h2>
<em>Right now, you're thinking that a password manager is going to make you safer online--but isn't it putting all your eggs in one basket? And what happens if the password manager was hacked?</em>

Lastpass servers can get hacked, but your passwords aren't stored there.

I'll take a minute for you to re-read that last sentence, your passwords are <strong>NOT</strong> stored on Lastpass servers.

Instead they store your encrypted password, and that encrypted data is useless without the key.

<em>So where's the key?</em>

The key used to decrypt/encrypt your passwords on LastPass is the <em>master password</em>. It's the only password you have to remember--your Last Password if you like. The master password never leaves your device and is never stored.

Yes, LastPass isn't hack-proof. But there's nothing of value on their servers to justify hackers spending effort trying to break into them.

Essentially what Lastpass do is use your master password to derive a master encryption key, and that key never leaves your device. All passwords are encrypted before being stored on LastPass servers, and because they don't know the key, those passwords are useless.

[caption id="attachment_5844" align="aligncenter" width="550"]

![lastpass-encryption](/uploads/Lastpass-Encryption-1-820x175.png)

 How LastPass store &amp; retrieve your passwords[/caption]

LastPass may not be absolutely secure, but they do have strong architecture in place, for a solution to give you access to your passwords on the cloud.
<h2>LastPass isn't panacea</h2>
But as always are are caveats of course, and here's the 3 main ones.

Caveat 1, the 'master' password you use has to be strong enough to prevent anyone from guessing it. If your master password was 'Password' or '123' or 'dadada' , then all bets are off, and you've pretty much screwed yourself.

Caveat 2, you must trust Last Pass. In theory you could verify what they do, but in general, you must trust that the Lastpass application you install on your browser or use on your phone isn't siphoning your master password away somewhere.

Caveat 3, even with LastPass, if someone hacked your local machine (phone or laptop), then Lastpass won't protect from those attacks either. Lastpass only protects you from certain attacks, not all.
<h2>Conclusion</h2>
I'm a big fan of Password managers and LastPass in particular, if there's one piece of advice I'd give regular folks to improve their online security, it's to start using a Password manager.

Although you're 'sort' off putting all your eggs in one basket, it's still a pretty strong basket, and one that leaves you less vulnerable to password compromises on the internet.
<h2>Worked Example</h2>
A worked example is when Mark Zuckerberg got hacked a few months ago. Mark used a weak password, 'dadada', and he re-used that password across multiple services (LinkedIn, Twitter, etc). So when LinkedIn was hacked, hackers got his password (easily), and then used it to access twitter.

If Mark had used a password manager, he could have used a stronger password (instead of 'dadada') and he could have had individual passwords for each service (instead of sharing).

Mark should also have used two-factor authentication...

If you want to be more secure online--here's a <a href="http://Lastpass.com">lastpass link</a>. Good luck.