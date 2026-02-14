+++
title = "Hack TM Unifi: In case you've lost your default password"
slug = "hack-unifi-default-password"
date = "2013-08-12T08:00:21"
draft = false
categories = ['Malaysia', 'Security &amp; Privacy']
+++

<a href="/uploads/dir-615.jpg">![dir-615](/uploads/dir-615.jpg)</a>There's a lot of documentation online on how to <a title="Unifi WiFi Hacking tutorial" href="http://godamwifi.blogspot.com/p/tutorial-unifi-hacking.html" target="_blank">hack your neighbours Wi-Fi</a>, but sometimes you need to hack your own system. Usually its because you've change your router password and forgot it completely, leaving you in the cold desolate place we like to call "No router land".

Don't fear though, its actually pretty darn easy to hack your standard Dlink Dir-615 router <em>(pictured above)</em> that came stock with your Unifi subscription. Make no mistake, the router actually has some pretty sleek features, but Telekom Malaysia has a lackadaisical approach to security that makes hacking this router merely google searches away.

The default Unifi access credentials are:
<pre><strong>Username</strong> : admin
<strong>Password :</strong></pre>
Where the password field is literally left blank, (as it is).

However, if you're locked out of your Unifi router, here's a couple of things you could do to get your connection back:<!--more-->
<h2>Option 1: Logging in with the Operator account</h2>
Most of the time, I recommend you use the admin account to change your Unifi settings, TM themselves admit that they don't even set a password for this account on their <a title="TM Unifi Dlink Dir 615 user guide" href="http://www.tm.com.my/publishingimages/unifi/pdf/rg%20dir-615%20user%20guide.pdf" target="_blank">user guide</a> (page 9, 2nd bullet). However, if you've changed the password to this account and forgot it, there's still a 2nd account that is left lurking in the system.

This is the 'Operator' account, and actually has more features than the standard 'Admin' account. TM have left this here, presumably for support purposes, but quite frankly, they shouldn't. It's like your house contractor, keeping a spare key to your home for 'support' purposes, it's just not good security.

Fortunately though, if you've just changed the 'Admin' password, you've still got a chance to go back into your router and set things up correctly, just logon with the Operator account using one of the following credentials:
<pre><strong>Username:</strong> Management
<strong>Password:</strong> TestingR2</pre>
<pre><strong>Username :</strong> operator
<strong>Password :</strong> h566UniFi</pre>
<pre><strong>Username</strong> : operator
<strong>Password :</strong> telekom</pre>
<pre><strong>Username :</strong> operator
<strong>Password :</strong> <em>&lt;your Unifi username in reverse order&gt;</em></pre>
Needless to say, please change the operator password once you've logged on, and remember it wisely this time.
<h2><strong>Option 2: Hack the Dlink Dir 615 router</strong></h2>
This options isn't as hard as it might seem. For those running a router with a firmware version of 7.09 and below, there is a well documented vulnerability on the Dlink Dir-615 router that enables you to access your router without even knowing the username or password. To do so, just enter the url below;
<pre><code>http:</code><code>//192.168.0.1/tools_admin.php?NO_NEED_AUTH=1&amp;AUTH_GROUP=0</code></pre>
For more info on the vulnerability check out this link <a title="Dlink Dir-615 forgotten password" href="http://1337day.com/exploit/15033" target="_blank">here</a>. The vulnerability is called an authentication bypass, and literally allows you to access the router with no credentials at all! You can visit any page from the router menu, by just adding the "?NO_NEED_AUTH=1&amp;AUTH_GROUP=0" to the end of the link.
<h2>Option 3: The one that will always work</h2>
<blockquote><strong>*Edited 5-Dec-2013*</strong></blockquote>
I'm really scared of this one. As from my checks with a couple of Shodan searches <span style="text-decoration: underline;"><strong>ALL Unifi routers are susceptible to this attack</strong></span>. All you need to do this is visit this link:
<pre><a title="Unifi router password" href="http://192.168.0.1/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd" target="_blank">http://192.168.0.1/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd</a></pre>
And you'll see in plain-freaking-text, your unifi routers username and password, for both the admin and operator/management accounts.

Thanks to use_the_source_luke from <a title="Hack Dlink routers" href="http://seclists.org/bugtraq/2013/Dec/11" target="_blank">this bugtraq post</a>.

This is all public information at this point and you deserve to know that your unifi router is insecure. So get out there and buy a new router already.
<blockquote><strong>*end edit*</strong></blockquote>
<h2>Out of Options</h2>
There are other vulnerabilities on the Dlink router, including the famous config.bin password hack, however, from my checks, most Unifi routers are already patched with the fix for that. Leaving the above two options your only hope. If you really are out of options, you can always purchase a new router for your Unifi connection (I recommend the Asus RT-N12C1 or the Asus RT-N12HP)

However, you made need to call TM for your Unifi Password.
<h2>How to secure your Unifi router</h2>
It's also important to learn how to secure your router, the first bit is easy. Change the passwords, TM have a really bad habit of setting the router password to blank, meaning there literally is NO PASSWORD!!

Needless to say, that's bad security. What's even worse is the average customer isn't aware of the operator account which is left on the system with default passwords as well. From my quick checks, about 50% of people don't change they're router Admin passwords, and nearly 99% of people haven't changed their operator password. You can't really blame them, they didn't know the operator account was there in the first place. So basically 99 times out of a 100, you'll be able to 'hack' your unifi router using nothing but default passwords.

Securing the router, first and foremost requires that you change the passwords from their default values.

Secondly, if you're using a firmware version of 7.09 and below, it's time to upgrade your firmware. Upgrading your router firmware is actually pretty common stuff, there are entire websites that are dedicated to documenting router vulnerabilities, not for hackers, but security research--and this concept actually <a title="How Computer Security Research works: Facebook 20,000 prize" href="http://www.keithrozario.com/2013/07/computer-security-research-works-facebook-20000.html">helps make our everyday appliances more secure.</a>
<h2>Conclusion</h2>
A lot of people have locked themselves out of their home routers, so hopefully this post helps. However, because TM have such a bad stance against security, it also means that if you don't take the necessary precautions, you could be on the wrong end of an attack.

Remember to stay safe and secure, securing your router is as important as securing your front door.