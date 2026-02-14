+++
title = "Adding a facebook Like Button to your post"
slug = "adding-a-facebook-like-button-to-your-post"
date = "2011-05-08T09:18:19"
draft = false
tags = ['Blog Features', 'Facebook']
categories = ['Blog']
+++

Adding fa![Facebook Like](/uploads/facebook_like_by_socialmouths_2-150x137.png "facebook_like_by_socialmouths_2")cebook like buttons are tricky things. It used to be I'd need to install a new plugin to have these facebook like buttons. For instance I use to use DiggDigg, which is a pretty good plugin for wordpress. However, for the initiated a code version that I could stick anywhere in my post seemed a lot more flexible to me.

So how does it work. Simple.<!--more-->

Just cut and copy over the code below into your single.php page and you're good to go:
<blockquote>&lt;code&gt;&lt;iframe src="http://www.facebook.com/plugins/like.php?href=&lt;?php  echo urlencode(get_permalink($post-&gt;ID));  ?&gt;&amp;amp;layout=standard&amp;amp;show_faces=false&amp;amp;width=450&amp;amp;action=like&amp;amp;colorscheme=light"  scrolling="no" frameborder="0" allowTransparency="true"  style="border:none; overflow:hidden; width:450px;  height:60px;"&gt;&lt;/iframe&gt;&lt;/code&gt;</blockquote>
It's that simple. For more info, head on over to the post I copied this info <a title="Adding a facebook like button" href="http://www.wpbeginner.com/wp-tutorials/how-to-add-facebook-like-button-in-wordpress/">from</a>. It's from a great website called WPBeginner that will actually setup your blog for free (some fine print though).

So now you've got your facebook like button, and it can be either at the top of your post, the bottom of the post, at the middle, or even in the archives.

<em>Cool.</em>

I noticed a lot of people like to have the scrolling like buttons at the side of the post, I think these things just complicate the website design, but that's just me. Seeing something scrolling while I'm reading a post is just irratating to me.

For the even more initiated, you can read more about the facebook like button <a title="Facebook like button developer help" href="http://developers.facebook.com/docs/reference/plugins/like/">here</a> at the Facebook Developers page.

*Added 12-May-2011

After a couple rounds of informal testing, I've discovered that this post is incomplete. Due to the fact that the thumbnail image on the post would always be messed up. In order to fix a wrong image being displayed in your facebook like, your best bet is to install the <a title="Facebook Like thumbnail" href="http://wordpress.org/extend/plugins/facebook-like-thumbnail/">facebook-like-thumbnail plugin</a><em><a title="Facebook Like thumbnail" href="http://wordpress.org/extend/plugins/facebook-like-thumbnail/"> </a>(do they have plugins for everything on Wordpress??)</em>