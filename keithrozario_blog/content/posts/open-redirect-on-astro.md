+++
title = "Look ma, Open Redirect on Astro"
date = "2018-06-07T23:03:17"
draft = false
categories = ['Malaysia', 'Security &amp; Privacy']
+++

If you've come here from a link on twitter -- you'd see that the address bar still says <span style="text-decoration: underline;">login.astro.com.my</span>, but the site is rendering this page from my blog. If not, click <a href="https://login.astro.com.my/ssowebnx/logout.aspx?pid=stadiumastroweb&amp;returnUrl=https%3A%2F%2Fkeithrozario.com%2F2018%2F06%2Fopen-redirect-on-astro.html%2F%27%3Bvar%20a%20%3D%20document.createElement(%27iframe%27)%3Ba.src%3Dreturnurl%3Ba.width%3D%27100%25%27%3Ba.height%3D%27100%25%27%3Ba.style.border%3D0%3Bdocument.body.appendChild(a)%3Bdocument.body.style%3D%22margin%3A0%22%3B%0Awhile(false)%2F%2F">this link</a> to see what I mean. You'll get something like this:

<a href="/uploads/astro_open_redirect_1.jpg"><img class="wp-image-6402 aligncenter" src="/uploads/astro_open_redirect_1.jpg" alt="" width="500" height="337" /></a>Somehow I've managed to serve content from my site on an astro domain. Rest assured, I haven't 'hacked' astro servers and uploaded my page, but I've performed an equally sinister attack called <em>open redirect</em>.

While browsing online for some more info on the <a href="https://www.keithrozario.com/2018/06/the-astro-data-breach.html">astro breach</a>, I found <a href="https://kaizen1996.wordpress.com/2016/11/26/6-astro-another-open-redirection-bug/">this blogpost</a> from Amirul Amir, detailing the open redirect vulnerability on astro's website. The post is dated Nov 2016, yet the vulnerability still works -- and even though Amirul laments that he informed Astro, they seem to have taken no action in more than a year.

You might be wondering what good is an open redirect vulnerability?

Well, an attacker might send you a phishing email, pretending to be astro asking for you update to update your info on their site, and they've even included a conveniently placed a link for you to click. The link looks <strong>legitimate</strong> (it has <em>login.astro.com.my</em> in it), so you click it to a find a legitimate looking site, with valid certificates to boot -- so you enter your username and password.

But the site isn't legitimate, it's an attackers page (that looks exactly like Astro's) rendered over the original website, leveraging the vulnerability <em>(and some added javascript)</em> -- and now you've just given your username and password away.

The frustrating thing with open redirect, is that all the techniques we educate people to use for detecting phishing sites, don't work in this case -- because this is the 'real' site, that's been compromised by open redirect.It has the correct domain, it even has the right certificates, the only way you'd know is if actually look into the embedded javascript, but 99% of folks never do that.

So for a company like Astro to be sitting on this vulnerability for more than a year is not acceptable.

Just more bad news for their already shitty response to the original data breach.

Shout out to Amirul who blogs over at <a href="https://kaizen1996.wordpress.com/">kaizen1996.wordpress.com,</a>although it looks like he stopped blogging in 2016, pity because he had good content.