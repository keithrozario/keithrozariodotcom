+++
title = "Microsoft is eavesdropping on your skype conversations"
slug = "microsoft-eavesdropping-skype-messages"
date = "2013-05-22T07:00:59"
draft = false
tags = ['Skype']
categories = ['Copyright and Censorship', 'CyberLaw', 'Security &amp; Privacy']
+++



![Microsoft Eavesdropping on Skype messages](/uploads/2314400543_acd79bd7fb.jpg)

The guys over at H-online reported recently that they have some pretty good evidence that good ol' Microsoft is eavesdropping onto your Skype conversations, and the results are pretty damning.

The method for detecting those sneaky little eavesdroppers was pretty ingenious though. The researchers sent two urls in their skype messages to each other. The urls pointed to servers that the researchers owned. For all practical reasons these urls were made specifically for the purpose of the test and should not be receiving any traffic from anywhere--unless of course Microsoft was listening.

Then they sat at wait at their servers to see if they received any traffic, and lo' and behold barely a few hours later they received some rather funky traffic from an IP address registered to Microsoft in Redmond. <span style="color: #888888;">*busted!*</span>

The urls didn't just end with the .com, but had sensitive material appended to it (or at least that's what the researchers made it look like), and Microsoft used the url which meant they had to be eavesdropping on Skype messages and conversations. More importantly these urls were made to look like they held sensitive material, such as bank logins..etc etc, but Microsoft still used it, and worse even visited the sites to see what was on it.

Even more shocking is that Microsoft isn't even denying the charge--yet, but they point out that they do scan urls once in a while to flag spam, but H-online isn't buying it.<!--more-->

For more info, check out this brilliant post from them <a title="Microsoft eavesdropping on your Skype calls" href="http://www.h-online.com/security/news/item/Skype-with-care-Microsoft-is-reading-everything-you-write-1862870.html" target="_blank">here</a>.

Don't be surprised folks, if you can't even <a title="Jay Leno viral video online is a fake" href="http://www.thesmokinggun.com/buster/viral-video/actors-star-in-tonight-show-viral-video-6758492" target="_blank">trust Jay Leno these days</a>, what makes you think you can trust Microsoft. Reminds me of the time <a title="Nokia performs man-in-the-middle attacks" href="http://www.techdirt.com/blog/wireless/articles/20130111/03432221640/nokia-running-man-middle-attack-to-decrypt-all-your-encrypted-traffic-promises-not-to-peek.shtml" target="_blank">Nokia thought it was a good idea to look at the detailed web browsing habits of their customers</a>--guess what happened then. I'll give you a hint--the customers weren't too happy.

Now--here's a thought. How many foreign leaders do you think use Skype to phone home when their abroad?