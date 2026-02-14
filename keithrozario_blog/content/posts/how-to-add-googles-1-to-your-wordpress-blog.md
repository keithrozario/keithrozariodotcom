+++
title = "How to add Google's +1 to your wordpress blog"
date = "2011-06-06T01:45:33"
draft = false
tags = ['Blog', 'Blog Features', 'Google', 'wordpress']
categories = ['Blog']
+++

<a rel="attachment wp-att-861" href="http://www.keithrozario.com/2011/06/how-to-add-googles-1-to-your-wordpress-blog.html/google1button"><img class="alignleft size-thumbnail wp-image-861" title="Google+1button" src="/uploads/Google+1button-150x108.jpg" alt="" width="172" height="123" /></a>Google has just hit back at Facebook with the new +1 button. Similar to facebook's like, it's a one-click button to symbolize you 'like' the site. However, that's where the similarity ends:

&nbsp;

&nbsp;

&nbsp;

<!--more-->1) Facebook Like will post the content to your wall with a link to the site, +1 will not add the content or link to your google buzz feed. It ends up in your google profile...you probably didn't know you had one. But you need to make your +1 feed active in order for people to see it.

2) Facebook Like doesn't appears on Google Search. +1 Does. If your friends +1 a site, then you can see that information while you're doing a search in real-time. Excellent integration if you ask me, but I can't see it. I specifically searched for a site I +1-ed <em><span style="color: #c0c0c0;">(is that a word?)</span></em> and I couldn't see any social info, maybe it's not fully available yet.

2) Facebook Like allows you to share the link with friends, +1 will not.

3) +1 will <span style="color: #c0c0c0;"><em>'</em><em>in the future'</em></span> actually contribute to search results, generally I think the more +1's you get, the more prominent your site becomes on google. Facebook likes, do not have this, facebook like only last as long as your wall isn't over-crowded.

4) Likes and +1's require you to be logged on to your facebook and google accounts respectively. Google Apps for organization are NOT applicable....at least the free ones.

5) Most office network administrators have blocked Facebook, which sometimes plays havoc on your Like buttons.....no office I know has blocked Google. So Google is going to have free reins with the office crowd :).

In the face of all this, the +1 is probably not as appealing as a Facebook like or recommend. However.....if you're still game to join the Google frenzy (as I am), here's a quick way to add the +1 button on your post.
<ol>
	<li>Log on to your wordpress dashboard.</li>
	<li>Go to Appearance-&gt;Editor</li>
	<li>Select Single Post <em>(single.php)</em> from the side-menu</li>
	<li>Add the following code to where you want your +1 icon to be:</li>
<blockquote>&lt;!--Google +1--&gt;
&lt;br&gt;
&lt;script type="text/javascript" src="http://apis.google.com/js/plusone.js"&gt;&lt;/script&gt;
&lt;g:plusone size="medium"&gt;&lt;/g:plusone&gt;
&lt;!--Google +1--&gt;</blockquote>
	<li>Save the updated</li>
	<li>Be sure to clear any cache you have with your Hypercache or W3 plugins. The cache prevents the button from being displayed</li>
	<li>+1 away :)</li>
</ol>
There you have it, and here's your +1's will look on your google profile, click on the picture to enlarge:

<a rel="attachment wp-att-862" href="http://www.keithrozario.com/2011/06/how-to-add-googles-1-to-your-wordpress-blog.html/google_profiles"><img class="size-medium wp-image-862 aligncenter" title="Google_profiles" src="/uploads/Google_profiles-300x173.jpg" alt="" width="300" height="173" /></a>