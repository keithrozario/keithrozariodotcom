+++
title = "Setting up a Dlink DDNS for your Unifi Router"
slug = "setting-up-dlink-ddns-unifi-router"
date = "2012-09-22T22:47:55"
draft = false
tags = ['dlink', 'Unifi']
categories = ['Malaysia']
+++

<p style="text-align: justify;">A Domain Name Server (DNS) is basically the address book of the world wide web. What it does in very simple terms is it converts a web address like www.keithrozario.com into an Internet Protocol address like 208.94.116.157<em> (this might look like garbage but it's actually 4 numbers separated by a dot, and it's these 4 numbers that uniquely define every machine on the internet).</em></p>
<p style="text-align: justify;">It's the Internet Protocol address that can actually get you to your destination. Think of it like the actual phone number of the person. It's nice to know someone's name, like Keith Rozario, but it means nothing in terms of contacting me if you don't have my Phone Number. So if you wanted to contact me with just my name, you'd have to look for something called a 'phone book'. In this case, the DNS is the phone book, that translates a name to a number, and the DNS is publicly available.So what is a Dynamic DNS? Well, that's where the allocation from name to IP is dynamically allocated. For instance, the IP address of my website has remained static for the 1.5 years it's been around. So the DNS allocation for my website is pretty much stable.<em> Although I did recently change the web-host, but that's another story.</em></p>
<p style="text-align: justify;">However the IP address of my home Unifi connection changes everytime I restart my router, which is about once a week or so. If I wanted to add some sort of permanence to my connection, without splurging for expensive static IP packages, I could opt for a Dynamic DNS (or DDNS).</p>
<p style="text-align: justify;">So let's say I have a IP camera at home, that's recording a video feed that I can view on my phone. If I connected my phone to the IP address directly, that wouldn't be a good idea. If the connection dropped while I was away, or my house had an intermittent power cut, that forced the router to re-start (and hence change it's IP), I would lose all connectivity to the IP camera, and my entire home network as well. This is because, I wouldn't know what my home network IP address would be anymore, and hence have no way to contact it. It's like changing my phone number, if you keep trying to call your old number you'd most probably get an error message, or wind up calling someone else.<!--more--></p>

<h2 style="text-align: justify;">How does the Dynamic DNS work?</h2>
<p style="text-align: justify;">Dynamic DNS solves that, in most implementations of Dynamic DNS, a piece of software is installed either on your router or local machine. This software intermittently updates the Dynamic DNS server of it's current IP address. Once the Dynamic DNS server knows of the new IP it can then update the DNS. Once the DNS is updated it will then automatically resolve itself to the correct IP address.</p>
<p style="text-align: justify;">Basically in one word, a Dynamic DNS makes sure it always resolves to the same machine, even though the IP address of the machine is changing.</p>
<p style="text-align: justify;">So in this case, I would point my camera app to something like http://keithscamera.dlinkddns.com (a Dynamic DNS service from DLink). And setup my router to periodically update the DNS server with it's IP address. This way, if the router restarts for whatever reason, it'll update the Dynamic DNS servers of it's new IP. So that keithscamera.dlinkddns.com always resolves to my home network.</p>

<h2 style="text-align: justify;">Setting up Dynamic DNS for your Unifi connection</h2>
<p style="text-align: justify;">The Dlink Dir-615 router you get with Unifi has an inbuilt DNS functionality. It even comes with Dynamic DNS service called Dlinkddns (duh!). It's a FREE service, and you can subscribe using the router that comes with your default Unifi installation.</p>
<p style="text-align: justify;">So here's a quick step-by-step guide to setting up a Free Dlink DDNS service on your unifi Router</p>

<h2 style="text-align: justify;">Step 1 : Logon to your router</h2>
<p style="text-align: justify;">Obviously the first step is logging onto your router, if you're unsure of your how to do this then you probably need to read the basics from <a title="How to change your Unifi password" href="http://www.keithrozario.com/2012/07/change-unifi-password-wifi-dlink.html">this post on how to change your unifi password</a>.</p>

<h2 style="text-align: justify;">Step 2:  Proceed to the Maintenance Menu</h2>
<p style="text-align: justify;">There's a special Menu on the DLink router that has access to the settings for the Dynamic DNS services, the router supports many services including dyndns, but for the purpose of this example we'll use the DlinkDDNS.</p>

<center><a href="/uploads/DlinkDDNS_Maintaneance.png">![Dlink_DDNS_Maintenance](/uploads/DlinkDDNS_Maintaneance.png "Dlink_DDNS_Maintenance")</a></center>
<h2 style="text-align: justify;">Step 2.1 : Proceed to the DDNS Menu</h2>
<p style="text-align: justify;">Then proceed to the DDNS setting page from the left menu bar:</p>

<center><a href="/uploads/Dlink_DDNS_Settings.png">![DLink DDNS Setting Page (DIR-615)](/uploads/Dlink_DDNS_Settings.png "Dlink_DDNS_Settings")</a></center>
<h2 style="text-align: justify;">Step 3 : Signup to DlinkDDNS by clicking on the link in the browser</h2>
<p style="text-align: justify;">Clicking on the link in the browser window will take you to the DlinkDDNS website. Here you can signup for the free service.</p>

<center><a href="/uploads/Dlink_DDNS_Signup.png">![Dlink DDNS Signup Page (DIR-615)](/uploads/Dlink_DDNS_Signup.png "Dlink_DDNS_Signup")</a></center>
<h2 style="text-align: justify;">Step 4 : Click Get Started</h2>
<p style="text-align: justify;">Pretty self-explanatory.</p>

<center><a href="/uploads/rsz_dlink_ddns_getting_started.jpg">![Dlink DDNS Getting Started](/uploads/rsz_dlink_ddns_getting_started.jpg "dlink_ddns_getting_started")</a></center>
<h2 style="text-align: justify;">Step 5 : Enter sign in Details</h2>
<p style="text-align: justify;">For the purpose of this example, I'll be using an account called keithtest1234. Remember your username and password here, as we'll be entering them into the router later.</p>

<center><a href="/uploads/Dlink_DDNS_Registration.png">![Dlink DDNS Registration Process](/uploads/Dlink_DDNS_Registration.png "Dlink_DDNS_Registration")</a></center>
<h2 style="text-align: justify;">Step 6 : Activate account</h2>
<p style="text-align: justify;">Once you're done. Dlink Will send you an email to the email account you entered in Step 4. Just click on the confirmation link for the activation URL and you should be done.</p>
<p style="text-align: justify;">Remember, sometimes these emails get incorrectly marked as Spam, if you don't receive anything in 30 minutes, check your spam box.</p>

<center><a href="/uploads/confirmation_email-2.png">![Dlink DDNS confirmation email](/uploads/confirmation_email-2.png "Confirmation Email Dlink DDNS")</a></center>
<h2 style="text-align: justify;">Step 7 : Create a Host on DlinkDDNS</h2>
<p style="text-align: justify;">Now logon onto your already activated account on <a title="Dlink DDNS" href="https://www.dlinkddns.com" target="_blank">DlinkDDNS</a>, and click on the Add Host button. This will be your DNS entry for your home network from now on.</p>
<p style="text-align: justify;">Be sure to use a unique name, however you may also want to be sure it's not an easy URL. This will be the URL of your home network, which may include access to stuff like your IP cameras and NAS devices. You will protect these with passwords, but it's also a good idea to obfuscate the url as well. So something like <em>keithrozarioshouseinklang.dlinkddns.com</em> may be a bit too much information, and would open yourself up to other attacks.</p>

<center><a href="/uploads/D-Link-Dynamic-DNS-Add-Host_2.png">![DLINK Dynamic DNS Add Host Instructions (New IP Address)](/uploads/D-Link-Dynamic-DNS-Add-Host_2.png "D Link Dynamic DNS   Add Host_2")</a></center>
<p style="text-align: justify;">Once you've added that you should see something like this</p>

<center><a href="/uploads/rsz_dlink_ddns_added_host-11.png">![](/uploads/rsz_dlink_ddns_added_host-11.png "rsz_dlink_ddns_added_host (1)")</a></center>
<h2 style="text-align: justify;">Step 8: Enter host details on Dlink router</h2>
<p style="text-align: justify;">Here is where you want to enter the details from step 7 onto the router. Head over to Maintaneance-&gt; Dynamic DNS, and enter the information below.</p>
<p style="text-align: justify;">Remember to use the username and password from step 5, together with the host information from step 7. Select DlinkDDNS from the drop down, and finally test the connection. If everything went well you'll see a "Test Successful" message when done.</p>

<center><a href="/uploads/step_6_confirmation-1.png">![Entering Correct Information onto DIR 615 router for Dlink DDNS](/uploads/step_6_confirmation-1.png "DDNS Account Testing Confirmation")</a></center>
<p style="text-align: justify;"></p>

<h2 style="text-align: justify;">Step 9: Save your settings</h2>
<p style="text-align: justify;">Thanks to commented Joseph Ting, who highlighted that I missed one step in this tutorial. Once you've successfully tested out your settings, make sure you save your settings, so that they take effect, otherwise you'll have to reset everything again (doh!).</p>
<p style="text-align: justify;"><a href="/uploads/D-LINK-SYSTEMS-INC-WIRELESS-ROUTER-HOME.png">![Save_Settings_DLINK_DDNS_UNIFI](/uploads/D-LINK-SYSTEMS-INC-WIRELESS-ROUTER-HOME.png)</a></p>

<h2 style="text-align: justify;">Conclusion</h2>
<p style="text-align: justify;">Just like all my other tutorials, I try to make them very specific so that it's easy for you. However, because it's so specific the instructions may not be exactly as required, particularly if you have a different router or the same router with a different firmware. Exercise common sense, and don't be afraid to ask questions in the comments. I always love comments and try to respond whenever possible--there are no stupid questions, just stupid answers--and you'll find no stupid answers here.</p>
<p style="text-align: justify;">The Dynamic DNS service from Dlink is free and works natively on your browser, so there really isn't any reason not to use it. However, be wary, that if you don't exercise proper security on your home network, you could be opening  a backdoor to malicious hackers to gain access to your network and anything connected to it.</p>
<p style="text-align: justify;">Use common sense, protect your network by changing the password of your unifi router and ensuring you obfuscate the port forwards on the router as well. Finally, you might want to disable the DDNS when you're at home, and re-enable only when needed, particularly if you have IP cameras in your home.</p>
<p style="text-align: justify;"></p>