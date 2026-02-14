+++
title = "Slow Loading Wordpress: How to fix it"
slug = "slow-loading-wordpress-how-to-fix-it"
date = "2011-06-21T14:57:51"
draft = false
tags = ['Firebug', 'wordpress']
categories = ['Blog']
+++



![http://www.flickr.com/photos/fatboyke/2668411239/sizes/m/in/photostream/](/uploads/2668411239_9c8d7b2342-150x99.jpg "http://www.flickr.com/photos/fatboyke/2668411239/sizes/m/in/photostream/")

I have a problem with my wordpress site, it was just too slow. It was taking me 20-30 seconds to load the page, initially I thought it was nearlyfreespeech, and was contemplating moving the blog to dreamhost (<em>both of whom happen to be amazing webhost by the way</em>).

The reason I thought it was a host problem because my browser kept displaying <em><span style="color: #888888;">'waiting for keithrozario.nfshost.com'</span></em> while the waiting, so I assumed that it was their servers response time. That however was too presumptuous on my part, and it took me a while to get to the bottom of things, but I finally figured it out.

I used a nifty little Firefox plugin called firebug. <!--more-->I've used firebug before (mainly for testing web pages as part of my day job). Firebug allowed me to measure the loading time of pages to meet non-functional requirements, for instance if there was a requirement for a page to load in 10 seconds or less and I wanted to test that requirement out. All I needed to do was run Firebug, and it would give me a whole report on how long  the page took the load and break that down to each element (text, graphics, javascript, css). So if one single image was taking too long to load and slowing everything down I could find the offending image and remove it.

So armed with firebug I booted up firefox and loaded my page. Lo and Behold, the answer was staring me right in the face:



![](/uploads/imghover.js-1024x342.jpg "imghover.js")



You see that line with the red font that says imghover.js, and how the timeline for that particular element stretches to 21.9s. That means that my page had a javascript (.js file) that took 21.9 seconds to load, obviously that's a problem.

The Status bar in firebug also gives you an indication of what's wrong. It list the<strong><span style="color: #888888;"><em> imghover.js</em></span></strong> file as <span style="color: #ff0000;">404 Not Found</span>, which just means that the browser was unable to get the <strong><em><span style="color: #888888;">imghover.js</span></em></strong> file.

What I suspect happened was that the file is not present on my system and the browser can't locate it, so it tries to get it until it finally gives up and times-out, a full 20 seconds later. This was the first step in troubleshooting, finding out which particular element is taking a long time to load, the next step is to fix the problem.

So then I looked at my page source, and from the page source search for the offending line that called the element (in this case imghover.js) and it wasn't too hard to find this:
<blockquote>&lt;script type="text/javascript" src=".../javascript/imghover.js"&gt; &lt;/script&gt;</blockquote>
Then from here I had 2 options:

1) Remove the offending line in my wordpress theme, or;
2) Find the imghover.js from the internet and copy that to the correct location so that wordpress can find it.

I chose option (2), simply because my page is loading without the script already, so removing it completely should have minimal (if any) impact. So I headed over to the wordpress dashboard, headed over to <strong>Appearance -&gt;Editor-&gt; Header.php</strong> , found the following line <span style="color: #808080;"><strong><em>"&lt;script type="text/javascript" src="&lt;?php bloginfo('template_url'); ?&gt;/javascript/imghover.js"&gt; &lt;/script&gt;" </em></strong></span> and deleted it.

A click on update, a clear of the cache, and voila problem solved.

Now when I loaded the page, there were no issues and firebug confirmed them. I'm now saving my viewers about 15 seconds of their time...Awesome.

I'm not saying you'd have the same issue, but firebug is an excellent place to start to determine the problem with your page loading time. Determine exactly which element is the slowing down the whole site, then either modify that element, or remove it from your page (like I've done). Each website is different and will have it's own set of problems, this is just a generic troubleshoot guide.

To download this awesome firefox plugin, head on over to their website @ <a title="GetFirebug" href="http://getfirebug.com/" target="_blank">http://getfirebug.com/</a>

To improve loading times for 'good' wordpress sites, or if firebug had found no issues try using a <a title="Enable Caching on your blog for better performance" href="http://www.keithrozario.com/2011/04/creating-a-cache-for-your-wordpress-blog.html" target="_blank">cache plugin</a> to speed things up.

*Sorry nearlfreespeech for doubting you guys....you guys are awesome.