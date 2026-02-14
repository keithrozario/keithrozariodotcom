+++
title = "Tweet This doesn't work with the 'new' twitter"
slug = "tweet-this-doesnt-work-with-the-new-twitter"
date = "2011-06-08T05:58:14"
draft = false
tags = ['twitter', 'wordpress']
categories = ['Blog']
+++



![](/uploads/twitterdead-150x100.jpg "twitterdead")

One of my favorite Wordpress plugins,  Tweet This by <a title="Visit Richard X. Thripp's website" rel="external" href="http://richardxthripp.thripp.com/">Richard X. Thripp</a> stop working ever since Twitter moved to the 'new' twitter. I just realized this yesterday. A quick search online revealed that everyone is experiencing the issue with the plugin and Richard is MIA. When you get a free plug-in don't complain if it breaks, I'm sure Richard is quite busy or probably has more pressing needs that write code for a free plugin that he's not getting any money out of. Most of the complainers haven't even donated. Plus the code is open source, and you can fix it yourself. Richard did a stand up job creating this super plugin and giving him a hard time because it's no longer with the 'new' twitter is just stupid.

One of the great things about open source software is the code is made public, and the general public usually has it's collection of super-geniuses as well. One of those super-geniuses is a guy named <a rel="external " href="http://thefinancialbrand.com/">Jeffry Pilcher</a> from the <a title="Financial Brand" href="http://financialbrand.com" target="_blank">financialbrand.com</a> who shared on the official website of the plugin how to sort this out quickly without getting angry at Mr. Thripp.

Here's what you do:

<!--more-->

From your wordpress dashboard, head over to plugins, then to the Editor.

Then Select TweetThis from the list, and then simply ctrl+F <em><span style="color: #888888;">"home/?status=</span></em>" and replace it with this<em><span style="color: #888888;"> "intent/tweet?text="</span></em>

If you're unable to modify the code through the editor, then you'll need to sFTP into the site, browse to <em><span style="color: #888888;">wordpress/content/plugins/tweet-this/tweet-this.php</span></em>, and modify the file there. Simple and easy way to get Tweet-This to work with the new Twitter.



![](/uploads/Tweet-This-Fix-300x280.jpg "Tweet-This Fix")



It's so simple.

Thanks Jeffry for solving the problem, Thanks Richard for the superb plugin.

*You'll need to clear your cache in order for this to work, if you're using hypercache or W3 total cache, go to the plugin options and clear it. Otherwise the tweet this icons on the older page wouldn't be fixed.