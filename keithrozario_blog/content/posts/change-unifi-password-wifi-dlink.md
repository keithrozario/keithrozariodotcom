+++
title = "How to change your Unifi password"
slug = "change-unifi-password-wifi-dlink"
date = "2012-07-14T23:00:56"
draft = false
categories = ['Malaysia', 'Misc']
+++

Now It's quite clear from a previous post I did how about easy it was to <a title="Is your Wi-Fi safe?" href="http://www.keithrozario.com/2012/07/dlink-dir-615-wi-fi-password-unifi-hack.html" target="_blank">hack a Unifi Dlink DIR-615 Wi-Fi router</a>, that the least you should do is change your standard router password to something that's more than the regular 8 digit Pin Unifi gives you by default.

Let's take a look at how to change your unifi password, or how to find it in case you've forgotten.
<h2>Step 1: Login to your router</h2>
![](/uploads/rsz_1step_1_login_dlink_dir615-300x148.png "rsz_1step_1_login_dlink_dir615")
First you'll need to login to your router. For this open up Internet Explorer or Firefox or Chrome to access the internet. Then instead of typing something like http://www.google.com in the address bar to visit google, type <a title="DLink Dir615 Router" href="http://192.168.0.1" target="_blank">http://192.168.0.1 </a>in the address bar to visit your routers web server. Your router actually has a webpage that allows you configure you, but this web page is only visible from within your home network so don't worry.

You can just click the <a title="Unifi Router Logon" href="http://192.168.0.1" target="_blank">link here</a> to take your there as well.

Once you see the page look something like the picture above, enter admin for the username. For the password, use the default password Unifi has given you, <strong>when in doubt, look at the bottom of your router</strong> (that's the orange color device with the 2 antennas) and look for an 8 digit PIN. That's your default password. It's printed there in big bold letters--you can't miss it.

Now don't be confused, this is merely the password to access the router, not your Wi-Fi password, for now their the same password, but they could be different. That's what we're going to do.

If the password at the bottom of your router doesn't work, try the following. Depending on your router firmware, one of them is bound to work:
<p style="color: #3f4549;"><blockquote>Username: Management
Password: TestingR2</p>
<p style="color: #3f4549;">Username : operator
Password : h566UniFi</p>
<p style="color: #3f4549;">Username : operator
Password : telekom</blockquote></p>
<!--more-->
<h2>Step 2: Access the Wireless setup configuration on your router</h2>
![](/uploads/rsz_step_2_wireless_setup.png "step_2_wireless_setup")Once you've logged onto your router, visit the Wireless Setup menu (click the Wireless Setup button on the right menu)
<h2>Step 3: Manual Wireless Configuration</h2>
![](/uploads/rsz_step_3_manual_wireless_connection_setup_dlink-dir615.png "rsz_step_3_manual_wireless_connection_setup_dlink-dir615")Once there, look for the Manual Wireless Connnection Setup and click that. This will take you to a manual configuration page for your Wi-Fi settings.
<h2>Step 4: Change the Password</h2>
![](/uploads/rsz_step4_network_key_dlink_dir615.png "rsz_step4_network_key_dlink_dir615") 

Now browse to the bottom of the page and look for where the WPA/WPA2 Network Key is, you want to change your Password here to something other than the default 8 digits given by Unifi. Incidentally, this is also a way to determine the current password for wifi networks. It'll only work for the standard Dlink dir-615 router, but the general principle is still the same for other routers, you just to search around a bit more once in the administrator panel.
<h2>Password tips</h2>
I suggest at least a <strong>12 alphanumeric password</strong>, which includes numbers and letters. If you're afraid you'll forget you can paste the password at the bottom of your router for safe keeping, a easy to crack password will just get you in trouble. If visitors want to use your wi-fi you can look at the bottom of your router for information.

Next click on the Save Settings button, and reboot for safe measure. Remember all devices that were configured with the old password now need to refreshed.

That's it--pretty simple isn't it.

For added security I'd advise you to change your router admin password and disable Wi-Fi protected setup option on the router.

<strong>[if this post was helpful to you, please leave a comment in the comments section below, it helps me keep track of which articles have helped the most people]</strong>
<h2>Try it on someone else router :)</h2>
I noticed a lot of cafe's provide free Wi-Fi with an 8-digit password, and just based on that I can guess that the 8-digit password was provided by Unifi. If you're ever in a cafe where the Wi-Fi password is 8 digits long, then try logging onto 192.168.0.1 on your router and enter that same 8-digit password as the router password. Most of the time it doesn't work, but once in a while you get a poor soul that forgot to change their router password before broadcasting their Wi-Fi password.
<h2>What else you need to do</h2>
Just changing your Wi-Fi password is not enough, as I demonstrated when I logged onto some unsuspecting unifi subscribers without even accessing their WiFi. Be sure to disable remote access to your Router to ensure that no one can access your router from the internet as well. Follow the instructions<a title="How to prevent your Unifi account from being hacked" href="http://www.keithrozario.com/2014/01/prevent-unifi-hack-fix.html"> here</a>.