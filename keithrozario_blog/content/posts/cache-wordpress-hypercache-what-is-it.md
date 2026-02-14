+++
title = "What is a Wordpress Cache and how do I use it?"
date = "2011-04-27T10:49:20"
draft = false
tags = ['Blog Features', 'Cache', 'HyperCache', 'W3 Total Cache']
categories = ['Blog']
+++

<a href="/uploads/satollo-small.jpg"><img class="alignleft size-thumbnail wp-image-162" title="HyperCache creator" src="/uploads/satollo-small-140x150.jpg" alt="" width="140" height="150" /></a>Wordpress is the best blogging platform out there. It's the best blogging platform ever. It's great, but there is one downside. It's SLOOOOW. How Slow, depending on what you post up. People are a lot more forgiving on a PC, but if you're surfing on EDGE through your mobile phone, or browsing on a slow connection, it's very very slow. Painfully slow.

There is a great solution though<!--more-->It's called caching.
<h2>What is Cache?</h2>
The reason why Wordpress is slow, is because when a visitor visits your page, they trigger calls to your wordpress for various objects to be displayed, whether it's your page or your post contents etc, those calls then access your database (yes, wordpress has a database) and then generates the HTML code for the page. The HTML code is what finally gets displayed in your web browser.

Now, depending on how fast your hosting is, all these database queries and post data take time to be <strong>retrieved, formatted and then displayed. </strong> Those are the 3 main steps, retrieve the data, format it and display. Caching removes the first 2 steps, leaving you with blazing fast page loads.

How does it work? Well simple, the very first person to visit your post, (usually this is you testing your post) triggers wordpress to retrieve the data, format and display it. So far it's business as usual, but now comes the twist. Caching will now take this formated site and all it's data and store it somewhere on your blog. Usually in a cache folder located in your wordpress directory. So the next person to visit your site (still you testing your blog), will be redirected to the cache-d version rather than the original one.The next person will no longer cause a database query or wordpress formated it will instead access the html version of your pre-formated site from the folder.

If you're interested to know, it does this by automatically saving the file and then redirecting the user via the .htaccess file. Fantastic speeds, and it even saves the system performance.
<h2>Cache for Wordpress</h2>
So far the best recommended caching plugin for wordpress was <a title="W3 Total Cache" href="http://wordpress.org/extend/plugins/w3-total-cache/">W3 total Cache</a>, but I couldn't get that to work with my web host (nearlyfreespeech.net), so instead I got <a href="http://wordpress.org/extend/plugins/hyper-cache/">HyperCache</a> which was equally as good. The installation was a breeze and a couple of settings that I changed, namely the age of the file which I increased from 1 day to 5 days. This is important so listen up.

Once a person visits your site the plugin creates a cache version of the post in your cache directory. However, after X minutes it then deletes that cache version so when someone new visits the site the page is generated again. This happens so that if there's any new content the old content is replaced, otherwise you'll have no way to display updates. Now obviously a new post update will trigger this deletion but it's always good to put this in place. For high volume blogs a one day refresh period is OK, for low volume blogs like this the more days the better.

If you're looking for more info, these writeup is the best I've seen so far:

<a href="http://www.tutorial9.net/tutorials/web-tutorials/wordpress-caching-whats-the-best-caching-plugin/">http://www.tutorial9.net/tutorials/web-tutorials/wordpress-caching-whats-the-best-caching-plugin/</a>

And if you're wondering who the guy in the picture is--well that's the creator of Hypercache. I couldn't get W3Cache to be installed correctly because nearlyfreespeech runs their php in safe mode, and that can't be removed unless you change a few more settings. Not wanting to go through that trouble I deactivated the plugin and installed <a href="http://wordpress.org/extend/plugins/hyper-cache/">hypercache</a> instead.

You can download Hypercache for your blog <a title="Hyper Cache" href="http://wordpress.org/extend/plugins/hyper-cache/" target="_blank">here</a>--I recommend it.