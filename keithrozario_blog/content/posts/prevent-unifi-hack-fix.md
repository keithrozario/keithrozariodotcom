+++
title = "How to prevent your Unifi account from being hacked"
slug = "prevent-unifi-hack-fix"
date = "2014-01-05T20:22:49"
draft = false
categories = ['Malaysia', 'Security &amp; Privacy']
+++

<p style="text-align: justify;">OK....I made a boo boo!</p>
<p style="text-align: justify;">Actually my method of <a title="How I hacked 4 Unifi accounts in under 5 minutes" href="http://www.keithrozario.com/2014/01/hack-unifi-in-5-minutes.html">'hacking' the Unifi modems</a> has a ridiculously simple work-around. Unfortunately, when I published the findings I was absolutely convinced the workaround didn't work--I was wrong :(</p>
<p style="text-align: justify;">Details about how I was mis-lead are unimportant for now (although I will explain it later on), for now I think the simplest way to address and to make yourself more secure (though not 100% secure) is to disable remote management of the router. Don't worry here's a step-by-step guide on how to do it.<!--more--></p>

<h2 style="text-align: justify;">Step 1: Logon to your router</h2>
<p style="text-align: justify;"><a href="/uploads/Router_Logon.png">![D-Link dir-615 Router Logon](/uploads/Router_Logon.png)</a></p>
<p style="text-align: justify;">To logon to your router, fire up your web-browser (Chrome, Firefox, Safari--even Internet Explorer will do).  In the address bar where you usually type www.google.com type <a title="Router Logon" href="http://192.168.0.1" target="_blank">http://192.168.0.1</a> or just click the link. Once there enter the username and password of the router. If you're uncertain try any one of the following combinations:</p>

<pre style="text-align: justify;"><strong>Username:</strong> Management
<strong>Password:</strong> TestingR2</pre>
<pre style="text-align: justify;"><strong>Username :</strong> operator
<strong>Password :</strong> h566UniFi</pre>
<pre style="text-align: justify;"><strong>Username</strong> : operator
<strong>Password :</strong> telekom</pre>
<pre style="text-align: justify;"><strong>Username :</strong> operator
<strong>Password :</strong> <em>&lt;your Unifi username in reverse order&gt;</em></pre>
<p style="text-align: justify;">Otherwise refer to this post on how to find your router password. Click <a title="Hack Unifi router" href="http://www.keithrozario.com/2013/08/hack-unifi-default-password.html" target="_blank">here</a>, and look for option 3.</p>

<h2 style="text-align: justify;">Step 2: Head on to the Maintenance Section</h2>
<p style="text-align: justify;"><a href="/uploads/Maintenance.png">![Maintenance](/uploads/Maintenance.png)</a></p>
<p style="text-align: justify;">Once logged on, click on the Maintenance tab of the router.</p>

<h2 style="text-align: justify;">Step 3: Uncheck the box that says Enable Remote Management</h2>
<p style="text-align: justify;"><a href="/uploads/Step_3_uncheck_the_box.png">![Step_3_uncheck_the_box](/uploads/Step_3_uncheck_the_box.png)</a></p>
<p style="text-align: justify;">Once you've entered the Maintenance tab, uncheck the "Enable Remote Management" check box. The image on top has the box check, you want to make it empty.</p>

<h2 style="text-align: justify;">Step 4: Save those damn settings</h2>
<p style="text-align: justify;"><a href="/uploads/Save_Settings.png">![Save_Settings](/uploads/Save_Settings.png)</a></p>
<p style="text-align: justify;">Finally make sure you save those settings, otherwise all your hard effort would have been wasted. Once you've saved your settings, the router will either inform you of the setting change or it'll take you back to the router login page (same as step 1)</p>

<h2 style="text-align: justify;">Step 5: Reboot the router for good-luck</h2>
<p style="text-align: justify;">Finally for extra good luck, reboot your router, and check if the settings are still the same. Some funky stuff sometimes occur between reboots. Rebooting is easy, just switch off the power to the router for 10-15 seconds, then re-start it again.</p>
<p style="text-align: justify;">That should do it. Easy wasn't it.</p>

<h2 style="text-align: justify;">How I was wrong</h2>
<p style="text-align: justify;">Aiyah--this was a bit of a boo boo lor, everyone makes mistakes mah :)</p>
<p style="text-align: justify;">Firstly, what you've done in the 5 steps above, is disable anyone from outside your home network from accessing the router. That means the only way you'll ever access your router config page is via your internal network and not from the internet. So your router IP won't even show up in the Shodan results and even if it did, your router wouldn't allow these external IPs from accessing it's page.</p>
<p style="text-align: justify;">Where I was wrong is that I thought this feature didn't work on the Unifi router, and to be fair there are plenty of Dlink routers that have this flaw. It didn't help that there were <a title="DLink disable remote access" href="http://superuser.com/questions/570966/disable-remote-access-to-router" target="_blank">support forums that explicitly addressed this</a>. Where I was wrong of course, is that when I tested this--I tested it from within my own network. From within my network, regardless of whether I used the internal or external IP, I could still access my router, I was under the impression that if I entered the external IP, it would only work if remote access was enabled--I was wrong. I should have tested this from an external network, and using my phone or even a web-proxy I would have easily realized that this fix works for my router (and possibly yours as well).</p>
<p style="text-align: justify;">So if you want to be sure that your router is no longer allowing GUI access over the internet, head on over to Texas Proxy, and then type your external IP to see if you can view your router login page, you should get a curl error, and that would confirm you're good to go.</p>
<p style="text-align: justify;">Now of course, I was wrong, and I'm sorry if I caused you to panic, or worse yet go out and splurge on a new router. I've been wrong before, and this probably isn't going to be the last time either--being wrong is part of the job, I try to avoid it, but sometimes it's unavoidable. The only thing I can truly offer, is my apologies for being wrong--and I really am sorry. To show just how sorry I am, take a look at the picture below <em>(can you really still be angry with me after seeing those sad eyes?)</em></p>
<p style="text-align: justify;"><a href="/uploads/11-.jpg">![Sad Puppy Dog Eyes](/uploads/11-.jpg)</a></p>

<h2 style="text-align: justify;"><span style="font-size: 1.5em;">Conclusion</span></h2>
<p style="text-align: justify;">Now, the final word though, is that while the fix will protect you, I'm not 100% sure why TM chose to NOT disable the remote login by default. From my quick check, most routers with the 7.17 firmware have this feature enabled and that's a really bad thing.</p>
<p style="text-align: justify;">Also, this isn't 100% full-proof, the exploit still exist, and if someone manage to compromise your laptop, desktop or even IP Camera, they may have a back-door to your router, but making this one check (or un-check) makes you FAR more secure than before.</p>