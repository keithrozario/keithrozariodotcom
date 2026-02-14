+++
title = "Maxis Forum needs an upgrade"
slug = "maxis-forum-needs-an-upgrade"
date = "2014-12-28T16:36:33"
draft = false
tags = ['Maxis']
categories = ['Malaysia', 'Security &amp; Privacy']
+++

Yesterday I Googled something about maxis that took me to a forum.maxis.com.my link. Unfortunately, Firefox wasn't happy with Maxis, because I got the following screen:

<a href="/uploads/Maxis-forum.png">![SSL V3 on maxis forum](/uploads/Maxis-forum.png)</a>

Firefox is the first of the mainstream browsers to end support of SSLv3, ever since <a title="Poodle Security Vulnerability" href="https://en.wikipedia.org/wiki/POODLE" target="_blank">Poodle</a> was published. For those of you who aren't keeping tabs of security issues--Poodle was a big vulnerability discovered in the 2nd half of 2014, that affected the SSLv3 protocol.

The only fix for Poodle was to completely stop using SSLv3 altogether, not a bad idea, since the protocol itself is nearly 18 years old. In other words, the people born at the same time of the protocol, are already driving cars by now--on the other hand people born at the same time as the very first iphone have only just finished kindergarten, and Apple have long since stopped supporting version one of the iPhone. So would anyone support this grandfather protocol?

Just to drive home the point of how old SSLv3 is--the protocol is 3 years older than Maxis pre-paid offering, Hotlink--which was only launched in 1999.

Fortunately, most modern day browsers already support newer versions of SSL, namely TLS version 1.0, 1.1 and 1.2 (1.3 is still draft)--which means of course most people aren't fully susceptible to the issue. Even then computer geeks were switching SSLv3 off on their servers just to be sure (there are downgrade attacks, which can force a connection to use SSLv3 even though both server and client can support TLS)

But here's the kicker--some websites continue to support SSLv3, leaving people vulnerable as long as they're  using a SSLv3 capable browser--which is the main reason Firefox has <a title="Poodle on firefox" href="https://blog.mozilla.org/security/2014/10/14/the-poodle-attack-and-the-end-of-ssl-3-0/" target="_blank">disabled SSLv3 in it's latest installment</a>, and<a title="Google stop support of SSLv3" href="http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-exploiting-ssl-30.html" target="_blank"> Google will follow very soon on Chrome</a>. So regardless of whether the server support SSLv3, clients using the latest version of Firefox will be secure (at least from Poodle)

Now with the Maxis forum though--things are far worse. Not only does forum.maxis.com.my continue to support SSLv3--it apparently is the ONLY version of https supported by the forum page. In other words, the only security the Maxis forum offers, is based of an 18-year old protocol that's already been owned. This from a company that apparently put their CTO's <a title="Watch Youtube Maxis CTO" href="https://www.youtube.com/watch?v=os3kxErz6Jk#t=130" target="_blank">life on the line to promise zero youtube buffering</a>.

I mean, it's great that Maxis is promising zero youtube buffering and all---but if you can't even get the security basics on your forum page done right--then I question your ability to secure just about anything.

Fortunately, the Maxis login page to view account information isn't susceptible to the attack (but most users would re-use their passwords for both the forum and login),so that's not exactly great news.

Honestly Maxis, you have to do better.