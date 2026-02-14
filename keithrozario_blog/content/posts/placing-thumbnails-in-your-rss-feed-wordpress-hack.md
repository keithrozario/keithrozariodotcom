+++
title = "Placing thumbnails in your RSS feed: Wordpress Hack"
slug = "placing-thumbnails-in-your-rss-feed-wordpress-hack"
date = "2011-07-19T21:02:54"
draft = false
categories = ['Misc']
+++

![](/uploads/1318759358_1b323f8a7b_m-150x112.jpg "1318759358_1b323f8a7b_m")My wordpress RSS feed has always been a bit dull without the accompanying pictures I scour flickr for. However, today there is promise as I stumbled across a post by the wordpress geniuses at catswhocode, there was a wordpress hack to include pictures in your RSS feed, and all it requires is to post the following code into your themes functions.php file.

<!--more-->
<blockquote>function cwc_rss_post_thumbnail($content) {
global $post;
if(has_post_thumbnail($post-&gt;ID)) {
$content = '

' . get_the_post_thumbnail($post-&gt;ID) .
'

' . get_the_content();
}

return $content;
}
add_filter('the_excerpt_rss', 'cwc_rss_post_thumbnail');
add_filter('the_content_feed', 'cwc_rss_post_thumbnail');</blockquote>
I'm just trying this out to see if it works, for a list of other hacks and great wordpress content, head on over to <a title="Cats who Code" href="http://www.catswhocode.com/blog/8-new-and-amazing-wordpress-hacks" target="_blank">catswhocode</a>, source code via <a title="Snipplr" href="http://snipplr.com/view.php?codeview&amp;id=56180" target="_blank">http://snipplr.com/view.php?codeview&amp;id=56180</a>

 

*Latest update: the hack didn't work, and I had to delete it because it kept giving me errors. Will investigate further and update when I can.