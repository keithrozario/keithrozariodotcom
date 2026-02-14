+++
title = "How to determine your Unifi router MAC ID"
date = "2015-01-27T08:00:00"
draft = false
categories = ['Malaysia', 'Security &amp; Privacy']
+++

<h2 class="cufon"> Step 1: Logon to your router</h2>
<a title="D-Link dir-615 Router Logon" href="/uploads/Router_Logon.png" rel="fancybox-post-4212"><img class="aligncenter wp-image-4216" src="/uploads/Router_Logon.png" alt="D-Link dir-615 Router Logon" width="550" height="258" /></a>

To logon to your router, fire up your web-browser (Chrome, Firefox, Safari–even Internet Explorer will do).  In the address bar where you usually type www.google.com type <a title="Router Logon" href="http://192.168.0.1/" target="_blank">http://192.168.0.1</a> (sometimes it's <a title="Router Logon" href="http://192.168.1.1" target="_blank">http://192.168.1.1</a> ) or just click the link. Once there enter the username and password of the router. If you’re uncertain try any one of the following combinations:

<strong>Username:</strong> Management
<strong>Password:</strong> TestingR2

<strong>Username :</strong> operator
<strong>Password :</strong> h566UniFi

<strong>Username</strong> : operator
<strong>Password :</strong> telekom

<strong>Username :</strong> operator
<strong>Password :</strong> <em>&lt;your Unifi username in reverse order&gt;</em>

Otherwise refer to this post on how to find your router password. Click <a title="Hack Unifi router" href="http://www.keithrozario.com/2013/08/hack-unifi-default-password.html" target="_blank">here</a>, and look for option 3.
<h2 class="cufon"> Step 2: Click on the status button</h2>
<a href="/uploads/Status-button.png"><img class="wp-image-4726 aligncenter" src="/uploads/Status-button.png" alt="Status-button" width="551" height="272" /></a>

Hit the status button on the top right hand of the page (refer to the picture above). It'll take you to the status page which should display your MAC ID in the clear.
<h3>Step 3: Get the MAC ID</h3>
Your MAC ID for both the LAN and WAN should be presented in the clear on this page. Here you can cross-reference to check your MAC. Your MAC ID is something your router broadcast together with the SSID--although you (as a human) won't see it,  other computers and wi-fi enabled devices will see it. It's essential for communications between network devies.

<a href="/uploads/MAC-ID-Dlink-router.png"><img class="wp-image-4727 aligncenter" src="/uploads/MAC-ID-Dlink-router.png" alt="MAC-ID-Dlink-router" width="550" height="272" /></a>

&nbsp;
<h2>Step 4: Fix the hack so it doesn't happen again</h2>
If you've come to this page from the unifihack one, then here's <a title="How to prevent your Unifi account from being hacked" href="http://www.keithrozario.com/2014/01/prevent-unifi-hack-fix.html">the link to how you can fix your router</a> so that you're less exposed to this vulnerability. Performing the steps in the link not only make you more secure, they help with the overall security of UniFi subscribers in general, so it's a good idea to give it go.