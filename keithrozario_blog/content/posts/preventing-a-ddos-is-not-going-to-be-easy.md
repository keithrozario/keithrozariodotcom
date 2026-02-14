+++
title = "Preventing a DDOS is not going to be easy"
slug = "preventing-a-ddos-is-not-going-to-be-easy"
date = "2016-11-02T20:56:42"
draft = false
tags = ['DDOS', 'StarHub']
categories = ['CyberLaw', 'Security &amp; Privacy', 'Singapore']
+++

As a follow-up to my previous post on DDOS attacks [<a href="https://www.keithrozario.com/2016/10/how-the-starhub-ddos-possibly-happened.html">1</a>,<a href="https://www.keithrozario.com/2016/10/internet-of-shitty-things.html">2</a>], I've seen a lot of so-called 'solutions' to the problem, which really aren't solutions at all.

While it's still not explicitly clear that the StarHub DDOS was executed by Mirai, a recently released malware built specifically for DDOS, the timing and similarity of it to other Mirai attacks leave little room for doubt--at least to me.

If indeed, StarHub was a victim of a Mirai based attack, it would seem extremely odd that their CTO would reference <a href="http://www.theonlinecitizen.com/2016/10/27/starhub-recent-cyberattack-used-home-infected-computers/">phishing emails as a vector for infection</a>. So a few things don't quite line up here, including the advice from the CTO to change the default username and password, when <a href="https://krebsonsecurity.com/2016/10/who-makes-the-iot-things-under-attack/">Brian Krebs already reported that doesn't quite help</a>:
<blockquote>
<p class="m_-8085449076693160327gmail-p1"><span class="m_-8085449076693160327gmail-s1">Several readers have pointed out that while advising IoT users to change the password via the device’s Web interface is a nice security precaution, it may or may not address the fundamental threat. That’s because Mirai spreads via communications services called “telnet” and “SSH,” which are command-line, text-based interfaces that are typically accessed via a command prompt (e.g., in Microsoft Windows, a user could click Start, and in the search box type “cmd.exe” to launch a command prompt, and then type “telnet” &lt;IP address&gt; to reach a username and password prompt at the target host).</span></p>
<p class="m_-8085449076693160327gmail-p1"><span class="m_-8085449076693160327gmail-s1">The trouble is, even if one changes the password on the device’s Web interface, the same default credentials may still allow remote users to log in to the device using telnet and/or SSH.</span></p>
</blockquote>
<p class="m_-8085449076693160327gmail-p1">If you're more technically inclined, I strongly suggest listening the feature interview on<a href="http://risky.biz/RB433"> last week's risky business podcast</a>.</p>
<p class="m_-8085449076693160327gmail-p1">But the last piece of <a href="http://www.theonlinecitizen.com/2016/10/27/starhub-recent-cyberattack-used-home-infected-computers/">advice that the StarHub CTO gave</a>, that didn't make sense to me at all was this:</p>

<blockquote>
<p class="m_-8085449076693160327gmail-p1">"If you were to buy a webcam from Sim Lim Square, try to get a reputable one"</p>
</blockquote>
<p class="m_-8085449076693160327gmail-p1">Again, this may seem like good advice, but it doesn't conform to the evidence. Brian Krebs has <a href="/uploads/2016/10/iotbadpass-pdf.png">a list of devices that are hack-able</a>, and they include the likes of Panasonic, RealTek, Samsung and Xerox. All of which regular consumers would consider 'reputable'.</p>
<p class="m_-8085449076693160327gmail-p1">So StarHub claimed that you should change your passwords--but doesn't protect you from Mirai.</p>
<p class="m_-8085449076693160327gmail-p1">StarHub claim that you should buy equipment from 'reputable' suppliers, but even reputable suppliers produce hackable IOT devices, that can't be secured.</p>
<p class="m_-8085449076693160327gmail-p1">Finally StarHub are going to be sending technicians out in the field to help subscribers, and while this is laudable, it's not a sustainable solution. It only fixes a short-term problem, because as long consumers continue to buy hack-able IOT devices, the threat isn't going to go away.</p>
<p class="m_-8085449076693160327gmail-p1">And how often can StarHub afford to send technicians to make home visits before the cost start becoming un-bearable?</p>
<p class="m_-8085449076693160327gmail-p1">The way to view this issue is from a legal, economical and technical perspective--and in that order.<!--more--></p>

<h2 class="m_-8085449076693160327gmail-p1">Legal</h2>
But if you fail to secure your brand new toaster, and it becomes part of a DDOS, that doesn't hurt you at all--aside from some slightly burnt toast. In Singapore, where homes regularly have Gigabit speed connections, a single IOT device running may consume just 5% of total bandwidth--meaning the owner of the home could be blissfully unaware that they're part of a DDOS. In short, the victim doesn't even know they're a victim.

Just like how the police can't act against a wife-beater if the wife refuses to press charges--no government agency is going to be empowered to fix the problem without the user's consent. But user consent doesn't scale, just try getting user consent for 100,000 devices--that's not going to be a solution.

It's not suprising that hacker-vigilante groups are already hacking these devices to 'clean' them up--because these hackers groups are less encumbered by legal redtape. The only true solution here is that if a government got involved and hacked these devices for good.

Think of these IOT devices as warzone in Iraq and Syria, the ownership of which consistently flip-flops between various nasty villians. But we all know, that if the US (or even Russia) really wanted to, they could lay stake on the land, and permanently gain control. The only actor that can permanently gain control of these IOT devices and prevent similar scale DDOS attacks in the future are state-sponsored.

So there has to be a legal fix to this issue, at least to address the short-term issue.
<h2>Economics</h2>
<p class="m_-8085449076693160327gmail-p1">The true problem with the IOT-DDOS problem is economic incentives. If you fail to properly secure the front-door of your house, a break-in would cost you directly. Hence you have an incentive to properly secure it.</p>
<p class="m_-8085449076693160327gmail-p1">But fail to secure your Webcam or Toasters, and the consequences of a hack could be so miniscule that you'd hardly notice. The true victim though, the one running the service being hit by thousands of hacked devices, is not you.</p>
<p class="m_-8085449076693160327gmail-p1">Hence, consumers buying these IOT devices, wouldn't bother spending even an extra penny on something as boring as security, then that money could be spent on other more 'useful' features.</p>
<p class="m_-8085449076693160327gmail-p1">And if consumers don't care--neither will suppliers, which explains why we're in this shit-hole.</p>

<h2 class="m_-8085449076693160327gmail-p1">Technical</h2>
<p class="m_-8085449076693160327gmail-p1">This is the one area where we have useful solutions. Your iPhone is remote-updateable, it is a 'thing' on the internet and regularly gets patched to close up security holes.</p>
<p class="m_-8085449076693160327gmail-p1">Even when the FBI had a phone in their physical possession, <a href="https://www.keithrozario.com/2016/03/fbi-vs-apple-everything-you-need-to-know-part-2.html">they couldn't hack into it</a>--let alone a remote hack over the internet (which by the way, could <a href="https://www.wired.com/2016/09/top-shelf-iphone-hack-now-goes-1-5-million/">earn you $1.5 million</a>). So there are technical solutions to avert the IOT disaster.</p>
<p class="m_-8085449076693160327gmail-p1">Even on items cheaper than a phone, the ring video doorbell, an IOT device that replaces your doorbell--has the ability to <a href="http://blog.ring.com/index.php/2016/01/13/100-of-active-ring-video-doorbells-keep-your-wi-fi-password-secure/">push firmware updates over the internet</a>, ensuring software security flaws are patched consistently, In early 2016, Ring used this function to patch a newly discovered security vulnerability--demonstrated that IOT doesn't necessarily mean shitty security.</p>
<p class="m_-8085449076693160327gmail-p1">We have a solution--but the economics don't allow it, and unless a legal solution</p>

<h2 class="m_-8085449076693160327gmail-p1">Conclusion</h2>
<p class="m_-8085449076693160327gmail-p1">The Internet of Things is a whole new can of worms, and we need new solutions to address the complexity and scale of the issue. Unless governments are prepared to regulate the stuff we put online, the economics of the problem suggest it will persist.</p>
<p class="m_-8085449076693160327gmail-p1">But then again, I was never a fan of government intervention--so why recommend it now?</p>
<p class="m_-8085449076693160327gmail-p1">Because there are no alternatives.</p>