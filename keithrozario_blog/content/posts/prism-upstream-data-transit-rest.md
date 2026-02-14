+++
title = "Part 3: PRISM and Upstream"
slug = "prism-upstream-data-transit-rest"
date = "2013-06-28T08:00:11"
draft = false
tags = ['NSA', 'PRISM', 'Upstream']
categories = ['CyberLaw', 'Security &amp; Privacy']
+++

Initially I wrote about PRISM and how a lot of people felt it was a tool to<a title="What is PRISM?" href="http://www.keithrozario.com/2013/06/what-is-prism.html" target="_blank"> intercept communication in flight</a> to companies like Google and Facebook, however slightly more details have emerged to debunk that claim.

However, it's of paramount importance that we understand what people are saying. No one is denying that communications aren't being intercepted on their way to Google, Facebook or Apple, instead what they are denying is that the capability to perform that interception and storage is under purview of another program called Upstream, and that analyst like Edward Snowden at the NSA were encouraged to use <strong>both </strong>PRISM and UPSTREAM.

<a href="/uploads/PRISM-and-Upstream.jpg">![PRISM and Upstream](/uploads/PRISM-and-Upstream.jpg)</a> What the crudely drawn powerpoint on the left is trying to describe is the distinct-ness of the programs and how each program would complement (rather than replace) the other.

The release of this particular slide was done shortly after the initial news broke to<em>, in the interests of aiding the debate over how Prism works. </em>

The Guardian have intentionally redacted some of the program names from the slide, presumably in an effort to milk this story dry for all that it's worth, but probably also to keep the momentum of the debate just in case people move on. However,<a title="Guardian slide-41" href="http://www.guardian.co.uk/world/2013/jun/08/nsa-surveillance-prism-obama-live#block-51b36893e4b0cc6424372292" target="_blank"> in their own words</a> the slide:

<em>details different methods of data collection under the FISA Amendment Act of 2008 (which was renewed in December 2012). It clearly distinguishes Prism, which involves data collection from servers, as distinct from four different programs involving data collection from "fiber cables and infrastructure as data flows past".</em>

The of course points to separate approaches, one where information is accessed directly from the servers their stored in (data at rest), and one where information is collected while in transit (data in transit).

This distinction resonated with me, simply because I read about this a couple of months back when another wanted man name Kim Schmitz was making the news instead of one Edward Snowden.<!--more-->
<h2>The story of MEGA and Kim Dotcom</h2>
Kim Schmitz or more commonly known by his geeky nickname Kim Dotcom (I kid you not!), was an internet entrepreneur that started the file-sharing site MegaUpload. Megaupload achieved phenomenal success, rising to become the top-15 File sharing sites in the world, only to be shut down by the <a title="United States Department of Justice" href="https://en.wikipedia.org/wiki/United_States_Department_of_Justice">United States Department of Justice</a> for allegedly operating as an organization dedicated to <a title="Copyright infringement" href="https://en.wikipedia.org/wiki/Copyright_infringement">copyright infringement</a>.(*source<a title="MegaUpload" href="https://en.wikipedia.org/wiki/Megaupload" target="_blank"> wikipedia</a>)<b>
</b>

Kim Dotcom was <a title="Kim Dotcom house raid" href="https://www.youtube.com/watch?v=mmObwguVmEI" target="_blank">arrested in spectacular fashion</a>, and jailed for a short period of time before subsequently being released. On his release he plotted his revenge, creating a File Sharing site that would be free from anybody's prying eyes. In fact, the site he created was so secure, even the owners wouldn't be able to look at the data stored on it.

Unlike it's predecessors, Kim Dotcoms newest site would not just encrypt data in transit, but also data at rest. Every file uploaded would not just be encrypted on it's way from your machine to their servers--it would be encrypted ON the server itself. This would mean that even if Kim decided to handover all your user data to the world, no one would be able to know what files you had without first knowing the encryption key--something you should have kept a secret.

This new approach though is not without it's drawbacks, and many security researchers are beginning to question just how secure Dotcoms newest creation really is. However, the fundamental idea is that:

Encrypting data at rest would stop PRISM--presumably.

Encrypting data in transit would stop Upstream--presumably as well.

Encrypting both data in transit and at rest would give you the best data security and protect you from the prying eyes of criminals and governments--or would it?
<h2>When encryption really doesn't help anymore</h2>
Not if the NSA have their way.

In their <a title="Exaflop machine NSA Utah Data Center" href="http://nsa.gov1.info/utah-data-center/" target="_blank">Utah data center</a>, they aspire to build an Exaflop machine capable of 1 Quintillion instructions per second-- which dwarfs the current fastest supercomputer the <a title="Tianhe-2" href="https://en.wikipedia.org/wiki/Tianhe-2" target="_blank">Tian-He 2</a>, by about 30 times. Unlike other supercomputers that are basically just showpieces for an arms-race similar to the space-race of the 60's and 70's,  the NSA have a specific purpose for their new baby--they're going to take that enormous computing power and focus it like a laser on breaking encryption, specifically AES-256. In short, all that encryption that is protecting your data now is going to be literally crushed once the NSA bring the Utah data center online--now scheduled for 2018, but we all know how governments work, so I wouldn't hold my breath.

So what happens from now till then--well programs like Upstream and <a title="Tempora" href="http://siliconangle.com/blog/2013/06/24/project-tempora-how-the-british-gchq-helps-the-nsa-spy-on-us-citizens/" target="_blank">Tempora</a> are taking care of things. These programs aren't just snooping the data pipes, they're storing the data. So that when the time comes, 5 years from today--they'll be able to look back in time and crack all your 'secure' communications by today standards. Effectively, they'll be using the technology of tomorrow to crack the security of today--an analogy would be trying to crack the Enigma machine of WW2 with a super computer--it'll be relatively easy.

What can you do? Well for one thing--it may be time to switch to AES-512.
<h2>Conclusion</h2>
All in all, it gets to the point where the <a title="Can you out-tech the government?" href="http://www.keithrozario.com/2013/06/can-you-out-tech-the-government.html" target="_blank">ordinary citizen can't rein in their government through technology alone.</a> The oversight required to police these powerful programs must come from a political solution, rather than a technological one.

While we can't speak for the US nor hope of influence their decisions--we need to take a long hard look at the fundamental structure of our internet usage and figure out the best way forward. For now, unfortunately--I have no solution.