+++
title = "Unifi D-Link Routers are now officially completely hacked"
slug = "unifi-d-link-routers-hacked"
date = "2013-12-07T09:56:17"
draft = false
categories = ['Malaysia']
+++

I'm a big fan of the D-Link DIR 615 router, I think Telekom Malaysia made a pretty good choice selecting it as the default router for Unifi accounts. To be fair, TM have made some bad choices as well, but we won't go into that here, overall the router isn't top notch, but it gets the job done.

Unfortunately, D-Link as a company has come under the spotlight for some rather funky security practices. First, there was a rather <a title="Questionable backdoor" href="http://nakedsecurity.sophos.com/2013/10/15/d-link-router-flaw-lets-anyone-login-using-joels-backdoor/" target="_blank">questionable backdoor</a> that D-Link installed on a couple of older versions of their routers, the router basically granted anyone access to D-Link routers by just changing the user agent string of their browser--worse still the back door carried the name of the author....it was <a title="Edit Backdoor by Joel" href="http://nakedsecurity.sophos.com/2013/10/15/d-link-router-flaw-lets-anyone-login-using-joels-backdoor/" target="_blank">Joel</a>.

Fortunately, for Malaysians, the backdoor didn't affect Unifi routers--as far as I could tell anyway, and D-Link have since fixed the issue.

Just last week, though a rather obscure post on <a title="Bugtraq Dlink root access" href="http://seclists.org/bugtraq/2013/Dec/11" target="_blank">bugtraq</a>, which was then quickly re-posted to a couple other forums, detailed a more intrusive exploit, one that Unifi Dlink routers <strong>were</strong> susceptible to. This one, didn't grant you access, but it would grant you the username and passwords of all users of the routers--literally giving you the keys to the gates of your router. As far as I can tell--this impacts EVERY D-Link Unifi router there is.

The hack is so simple, it requires no additional tools other your browser and quick copy-n-paste. All the attacker is required to do is to enter the following url:

<blockquote>
<pre><a title="Check your Unifi router password" href="http://192.168.0.1/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd" target="_blank">http://XXXXX:YYYY/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd</a></pre>
</blockquote>

Where XXXXX is the router IP address, and YYYY is the port on which it's operating on. Then the router will miraculously display it's security credentials to you, and you're good to go. Using Shodan, I've verified that this works with nearly every firmware <em>(pictures are blurry, click to open the full image)</em>
<p style="text-align: center;"><a href="/uploads/7.13-firmware.png">![7.13 firmware](/uploads/7.13-firmware.png)</a></p>
<p style="text-align: center;"><a href="/uploads/7.17-firmware.png">![7.17 firmware](/uploads/7.17-firmware.png)</a></p>
D-Link have yet to release a patch for this, and the guy that published the bug didn't really follow the rules. Usually D-Link should be alerted of such a bug and given time to fix it before the vulnerability is published.

However, since literally hundreds of thousands of Malaysian households are now susceptible to this attack, you need to know. More importantly, there's nothing you can do about it with your current router firmware. No counter-measure is possible, it's like living in a house where the door won't lock, or the gate won't close--how will you sleep at night?

Don't despair you have two options to fix this:

1. Upgrade your router firmware to DD-WRT, Unfortunately, the guys over at Unifi Athena have been on a really long hiatus--and all the websites you search for information on this refer to them. Hopefully I'll have time to publish a tutorial on that soon.

2. Change your router to a new Asus/Tp-Link router. I personally use the N12, but any of the Unifi compatible routers work pretty much out of the box.

3. That may fix the short-term though, in the long run, you'll need to pay attention to security practices and upgrade your router firmware accordingly--provided the manufacturer actually releases patches. It's inconvenient, but security requires effort.