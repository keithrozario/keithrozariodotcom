+++
title = "How to bypass your office internet filters"
date = "2011-07-21T01:14:52"
draft = false
tags = ['Application']
categories = ['Blog']
+++

<a title="Glype " href="http://www.keithrozario.com/2011/07/how-to-bypass-%E2%80%A6office-filters.htm" target="_blank"><img class="alignleft size-full wp-image-1103" title="glype" src="/uploads/glype.jpg" alt="" width="254" height="95" /></a>Ever get tired of your office network administrator blocking youtube or facebook? Wished you could surf and get your daily dose of facebook and blogs from your office? Well there are many ways around this...most straightforward would be using a web-based proxy service like <a title="Hide My Ass" href="http://www.hidemyass.com" target="_blank">hidemyass .com</a> or <a title="Proxy4Free" href="http://www.proxy4free.com" target="_blank">proxy4free.com</a>. However, contrary to general opinion, your network administrators aren't lazy(or stupid!). If you know about these proxies they probably know about it as well, so they've probably have a whole loooong list of sites categorized as 'proxies' that are completely blocked from access. So how do you access those web-sites your administrators have deemed...unworthy?

The solution is  simple. Host your own proxy. This too can be blocked, but if you work in a fairly large company your own little private proxy is unlikely to generate enough traffic to warrant investigation and ultimately be blocked. So if I hosted my proxy on<strong> http://proxy.keithrozario.com</strong> its unlikely the traffic it generates would warrant anyone looking into it and eventually blocking it.So you have to strike a balance, surfing too much via proxy will arouse suspicion, too little and it defeats the purpose.

So how do you host your own proxy?<!--more-->

While there exist many scripts out there to run proxy servers, the simplest and quickest way to set things up would be to install an application called Glype. Glype is a PHP based proxy server that is completely free to download and easy to setup.

1)Simply download the Glype zip file <a title="Glype Download" href="http://www.glype.com/downloads.php" target="_blank">here</a>.
2)Unzip the file to somewhere on your local machine and upload the contents of the<strong> /upload</strong> folder anywhere to your website.
3)Then copy the <strong>admin.php</strong> file from the extras folder to the same folder.
4)Finally browse to the admin.php with your web-browser, set up a few options and you're done. (http://www.keithrozario.com/glype/admin.php)

I setup the whole thing in under 2 minutes (including download time). Awesome. The interface is extremely nice, and chances are you could get really really quick download speeds depending on your host. There exist certain problems however, the main one being it doesn't work too well with facebook, (I had to delete the facebook.php in the plugin menu for it to work), and even after I did this, the application didn't really work too well.

Some caveats though, that make this a less than ideal solution.

1) You need a webhost where you have unlimited bandwidth, otherwise you may find yourself spending a lot of money on traffic.
2) You need a PHP5 webhost with curl support (not too hard to find)
3) It doesn't work too well with a number of sites including facebook and youtube....and that's the point isn't it. (you could install separate Glype plug-ins but that's beyond the scope of this post)

Other than that, it does employ a couple of interesting points, you can browse anonymously (although not securely). Because the web-host routes data, you're susceptible to man in the middle attacks, and if your host is compromised so is your data, so don't use this to browse your internet banking accounts or sensitive email...you've been warned. Otherwise you could easily access sites that may have been blocked by over-zealous network administrators because they include words like proxy,games or sex (not that I would recommend it).