+++
title = "Now On Hugo"
date = "2026-02-15T10:21:10+08:00"
author = "keithRozario"
authorTwitter = "keithrozario" #do not include @
description = "keithRozario.com is now on Hugo"
showFullContent = false
readingTime = false
hideComments = false
+++


This blog is finally on Hugo hosted on Github Pages. I've been meaning to do this for years, but never had the time, patience and skill to execute the change. To be honest, I still don't have the time, patience and skill to do it -- but fortunately for me I have a coding assistant.
i
## Why move away from Wordpress

I loved Wordpress when it first started, but everyone loves things when they start. Over time, the PHP upgrades, the maintaining of Apache scripts and configurations, and the bloated feeling of the extra UI really started to degrade the experience of writing in Wordpress. The UI went from simple Microsoft-word like to some monstrosity of AI infused crap.

Not to mention, when I moved my hosting from Digital Ocean to AWS Lightsail, the stability of Lightsail was just bad. The blog would go down from time and time, and even restarts wouldn't fix it. The only thing that fixed it for a while was restoring a snapshot to a new VM and pointing my domain to the new IP. I worked at AWS for 4 years, so I don't think they save the 'bad' VMs for Lightsail, but it was a crappy stability that might have been my fault.

But that's the point -- even if it wasn't Lightsails fault, I don't have the time or inclination to troubleshoot and fix this crap anymore.

## Why Hugo

I moved away from Wordpress because I didn't like the overhead of managing a server, so Hugo seemed like the perfect choice. I also wanted to ensure the blog would have a little overhead as possible, and be maintainable for the longest period of time.
 
Hugo 'builds' your site. You write in markdown, and it converts to static HTML, both those formats are mainstays of the internet, nothing proprietary. The architecture ensures that I can run an ancient version of Hugo as long as I like, because it's only involved in the build process -- after that I get static HTML, and as long as the internet supports static HTML I'll be alright. So in theory, 20 years from now, I can keep everything the same, as long as I can get Hugo and the outdated Go install to run it -- I will be able to continue writing this blog.

No more wordpress upgrades or plugin updates that suck time.

## What's the trade-off

But not all is rosy.

I had a few Wordpress plugins that were helpful for SEO, security, and comment moderation. I now no longer have any SEO stuff here (hopefully Google can index this site without my SEO skills), and security plugin is no longer needed as I don't host servers and this is basically a protected Git repo. The biggest drawback is that I removed the ability to accept comments.

That was a BIG drawback.

Unfortunately, readers can comment at any time, so you need something up and running to accept those comments, like Servers. There are paid services available that can do this, but they generally would cost more than the hosting charges of my previous blog. There are Hugo plugins that use Github as a backend to store comments -- but not many of my readers have Github accounts. Finally you can use Disqus, which has a free version but ad-supported. 

So far, no good options.

Ultimately, the decision was I can choose an extremely cheap low-maintenance blog, or a slightly expensive maintained service, or something ad-supported. I chose a cheap low-maintenance blog, because that's the reason I switched to Hugo anyway. 

When I first started this blog it was to get an audience, but the blog has morphed more into a place for me to write down my thoughts more than anything else. I may introduce comments in the future, but for now they're disabled for all posts.

It was still important that I kept all comments, fortunately I could migrate those across. If you left a comment before, I'm so grateful for your input and thank you for your time, it was very much appreciated.




