+++
title = "The Drudgery of Servers"
slug = "the-drudgery-of-servers"
date = "2020-08-08T12:13:56"
draft = false
categories = ['Misc']
+++

<!-- wp:paragraph -->
<p>As much as I love Serverless architectures, I find myself 'locked-in' to a server-ed WordPress blog. It's a mixture of too much legacy content to migrate, lack of easy migration tools, and just the fact that WordPress for all it's faults --- just works!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So rather than spend countless hours trying to migrate content, I decided to keep paying the $5/mo to DigitalOcean so that they can continue hosting a VM which PHP on it for my blog.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>PHP isn't that bad -- it still runs a large chunk of the internet. But ultimately as with any server-full application, there's a bunch of stuff to patch. I imagined my LAMP stack WordPress to look like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7290,"sizeSlug":"large"} -->


![](/uploads/Wordpress-Stack.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>But over the last week, as I attempted to migrate my site, I found that Wordpress actually looks more like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7291,"sizeSlug":"large"} -->


![](/uploads/Wordpress-Stack-full.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>And because it's been nearly 5 years since I last SSH-ed into the server, everything on it was out-of-date. The version of PHP, Apache, LetsEncrypt Agent, even the Digital Ocean Agent. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So while I kept my Wordpress and Plugins up-to-date via the web GUI, the underlying components of the server were slowly (but very surely) fading into obsolescence! And it turns out trying to update them in place was a fool's errand. The first issue I had was LetsEncrypt, who dutifully sent me an email that were deprecating my agent version:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7293} -->


![](/uploads/Screen-Shot-2020-06-26-at-9.09.45-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Updating that was easy enough, but soon I started getting warnings about my PHP version, and as I dug around, I found all the other tid-bits of obsolete software. Pretty soon it was obvious, that a full migration to an up to date server would be easier than trying to update this in place.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So I resolved to basically spin up an empty VM, and begun installing all the components by hand (like a caveman!). It was really shocking to learn all the pieces of software that are installed on a regular server that needs updating.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The same is true in your organization as well. You may be running a simple SpringBoot application, but you've probably got a bunch of monitoring, security, and scheduling software all running on that server. All those agents need patching and updating like everything else.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Contrast this to serverless, like Lambda. If you have Java code running in the function, you don't care about updating any agents, or renewing TLS certificates, or even IAM credentials. All of that menial work is taken care of the platform.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But wait -- I hear a chorus of objections shouting "we've automated our agent updates!!"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Yea, but you still own the thing that automates those updates. Layers of abstraction are nice, unless you're having to maintain those layers yourselves. Why invest in automating agent updates, when you can get rid of agents altogether. Why invest in a hardcore security solution that will generate and rotate passwords, when you can get onto a platform that rotates them all for you (just like Lambda).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's crazy the amount of work I'd save if my WordPress site wasn't running on a Linux server I owned, and while I have a lot of content that just can't move anywhere for now, there's very little reason for your greenfield projects to still focus on making those same mistakes.</p>
<!-- /wp:paragraph -->