+++
title = "How to enable VPN connectivity on Maxis Mobile"
slug = "maxis-vpn-mobile-setting-3g"
date = "2012-07-11T14:37:58"
draft = false
categories = ['Malaysia', 'Misc']
+++

[caption id="attachment_2505" align="aligncenter" width="271"]

![](/uploads/rsz_maxis-vpn-setting.png "rsz_maxis-vpn-setting")

 Maxis VPN Setting[/caption]

Just a quick post for a Wednesday, as most of you know I just recently purchased my Samsung Galaxy S3 courtesy of the Maxis One Club. With that S3, I also purchased a RM68/month mobile data plan for 3G.

Now for those of you with an Android phone that tethering on the Phone is super easy. Tethering is when I use my phone as a wireless router for my laptop (or any other device). So I'm connecting my laptop to the internet via my phone and the Maxis network.

Now for those of you already using your Maxis phones for tethering, you'd notice one thing pretty soon--it doesn't allow for VPN connectivity. A lot people need VPN connectivity to their office Networks to access work emails or sharepoint folders, without VPN none of these would be accessible.

However, as I discovered, I couldn't access my office VPN while tethering on Maxis. I thought it was an Android issue or something to do with my phone and kept it in view till I really needed to solve it. Today a friend of mine told me it's a Maxis network setting I needed to change, and all I had to do was call Maxis.

A quick Google search actually showed me the way. Maxis Forum has extensive discussion on the topic, <a title="Maxis is not allowing PPTP and OpenVPN connections" href="https://forum.maxis.com.my/forum_topic.asp?TOPIC_ID=400" target="_blank">here</a> and <a title="PPTP VPN Issue" href="https://forum.maxis.com.my/forum_topic.asp?TOPIC_ID=1633&amp;whichpage=1" target="_blank">here</a>.

Maxis also attempt to explain the VPN blocking here:
<blockquote>Hi Joy,

We wish to share with you that we have privatised our IPs in an effort to provide better and secure services to our users. Due to this, the impact is that you will not be able to perform VPN.

To ensure all our users enjoy a quality browsing experience, we do not assure constant connectivity if you use 'peer to peer' or file sharing programs. This is in accordance with our Fair Usage Policy. To learn more, you may refer to<a href="http://www.maxis.com.my/personal/broadband/Fair_Usage.pdf" target="_blank">http://www.maxis.com.my/personal/broadband/Fair_Usage.pdf</a>

We hope the above clarifies,do let us know should you have any further concerns.

Thank you.</blockquote>
I'm not sure what 'privatised' our IPs mean, or why they do it. I'm not even sure why Maxis has a Fair Usage policy on a capped bandwidth offering, where they charge me per MB once I exceed it. Isn't charging me for my traffic considered 'fair' already?

Fortunately, the work around is simple. If you have issues connecting to your office VPN via Maxis, all you have to do is place a call to the Maxis Customer Care line, let them know you need to access VPN via your mobile data, and they'll set it up in a jiffy. I spoke to a friendly guy named Danny, and he sorted out my issue in a under a minute.

Another note, is that you need to change your Data Network APN. On my Samsung Galaxy it was a breeze:

<strong>Settings - &gt; More Settings -&gt;Mobile Networks -&gt;Access Point Names -&gt; Maxis 3G Internet -&gt; APN</strong>

Then follow the instructions from Maxis on what to change this to (usually it's just adding a letter to the end of the APN).

This only applies to the Mobile data though, so similar issues could be faced if you have an iPhone or another android device--or even Windows 7(gasp!!).

It doesn't apply to the Maxis Home users. I'm not sure if it impacts Digi and Celcom subscribers. Yes however, doesn't suffer the same restriction.