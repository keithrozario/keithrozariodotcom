+++
title = "Sub-domains on your site"
slug = "sub-domains-on-your-post"
date = "2011-05-10T07:38:39"
draft = false
tags = ['Blog Features', 'NearlyFreeSpeech']
categories = ['Blog']
+++

<a rel="attachment wp-att-665" href="http://www.keithrozario.com/2011/05/sub-domains-on-your-post.html/324448335_9d6bbb87a0_m" target="_blank">![](/uploads/324448335_9d6bbb87a0_m.jpg "Subdomain Graffiti")</a>Subdomains are a tricky thing. In laymans terms all it means is to have something else in place of the 'www' in your web address. So for example:

<span style="color: #993300;"><strong>http://www.keithrozario.com </strong></span>&lt;- This is my domain

<span style="color: #993300;"><strong>http://<span style="color: #3366ff;">resume</span>.keithrozario.com </strong></span>&lt;- this is my <strong>sub</strong>-domain, more specifically the <strong><span style="color: #3366ff;">resume </span></strong>sub-domain.

Creating a subdomain allows you to section out your website, while allowing your urls to look cleaner. Personally I'm a bit 'allergic' to the '/'. I much prefer a subdomain over a  '/'.

<span style="color: #993300;"><strong>http://resume.keithrozario.com</strong></span> <em>(good!)</em>
<span style="color: #993300;"><strong>http://www.keithrozario.com/Resume</strong></span> <em>(not good!)<!--more--></em>So how do we setup a sub-domain on our website?

It's really simple, but before I get to that there needs to be some explanation here. When you create a sub-domain, you are creating essentially a new site. A new site means you have to upload your stuff into a new ftp location, which means that data from one site has no access to the other locations (this is especially true host like nearlyfreespeech, but not true for host like dreamhost). That means my wordpress blog at <em>http://www.keithrozario.com</em>, can't access materials (images/html files) from my resume sub-domain <em>http://resume.keithrozario.com</em>. This has it's pros and cons:

<span style="color: #993300;"><strong>Pros:</strong></span> sub-domain is completely isolated from the domain, it's great and clean. You can delete it and the other sub-domains remain untouched.

<span style="color: #993300;"><strong>Cons:</strong></span> sub-domain can't share content between the 2 (at least not easily). This means that shared content like templates/designs need to replicated. This doesn't just waste space, but makes it difficult to upload changes as we need to do it twice.

As to why some other hosting websites allow you to have sub-domains linked to sub-directories (thereby eliminating the Con), here's why nearlyfreespeech has to say:
<blockquote>Please be aware, however, that we do <em>not</em> use the  subdomain-is-subdirectory hack (unfortunately) made popular by a certain  brand of web hosting control panel software. You can use our service to  create multiple independent sites and then assign or remove names from  one or more NearlyFreeSpeech.NET DNS domains at your discretion. There  is no connection between a site and a domain name or subdomain other  than what you create, and there is no correlation at all between  subdirectories of a site and subdomains of a domain.</blockquote>
So now that you understand (hopefully), let's get jiggy with it.
<blockquote>1) Logon to your NearlyFreeSpeech control panel

2) Go to the Sites Menu

3) Under the Actions menu, select <em>'Create new Site'</em>

4) Choose  a 'proper' shortname. Nothing generic please , something very specific, in my case it's keithrozariosresume

5) Then when it prompts for Use another name, select 'YES'. In the text box  labled "if so what is it" enter your subdomain. For e.g. <span style="color: #993300;"><em>resume.keithrozario.com</em></span>

6) Then hit the "Create Now" button</blockquote>
So then you'll get a new username for your sFTP upload. Connect there and then you can begin your new website. Here you can install new wordpress, or Joomla, or like I have done, posted my CSS based Resume on it. Feel free to have a look at <a title="Resume" href="http://resume.keithrozario.com" target="_blank">http://resume.keithrozario.com</a>

In dreamhost it's much easier, but that's for another post.

*Post Photo taken from <a href="http://www.flickr.com/photos/streetart/324448335/sizes/s/in/photostream/">http://www.flickr.com/photos/streetart/324448335/sizes/s/in/photostream/</a>