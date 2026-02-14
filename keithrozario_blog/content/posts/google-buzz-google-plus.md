+++
title = "Goodbye Google Buzz, Hello Google+"
date = "2011-12-06T23:02:10"
draft = false
tags = ['Google']
categories = ['Blog', 'Social Media']
+++

<a title="Google Buzz" href="http://www.keithrozario.com/2011/12/google-buzz-google-plus.html/274852368_3bd1afcde7" rel="attachment wp-att-1521"><img class="alignleft size-medium wp-image-1521" title="274852368_3bd1afcde7" src="/uploads/274852368_3bd1afcde7-300x225.jpg" alt="" width="300" height="225" /></a>I've long been a great fan of all things Google, even when they weren't exactly producing top quality stuff (like Google Wave), I stuck by them through thick and thin. That being said, it's been more good than bad, sure they had a rough patch with Wave and Google Buzz, and yes Google+ isn't exactly the Facebook killer it was tauted to be. However, think of all the really cool stuff they're doing, consider the fact that I literally LIVE on Googles Cloud, all my email is on GMail, there isn't a single day that goes by that I don't get my daily dose of blogs via Google Reader and I do Google Searches at least 10 times a day. So overall Google is still pretty good in my book.

Be that as it may though, one of the hallmark of successful innovators is that they know when to call it quits. Google has already <a title="Google Kills off Buzz" href="http://crave.cnet.co.uk/software/google-kills-off-buzz-tells-you-how-to-save-your-posts-50005840/" target="_blank">shelved Google Buzz</a>, and spun off Google Wave as <a title="Apache Wave" href="http://incubator.apache.org/wave/">Apache Wave.</a> Which begs the question of what would replace Buzz.<!--more-->

The Answer is obviously Google+. Google+ is meant to compete head-on with Facebook, so in terms of functionality the 2 social networks are pretty similar.

Facebook has the 'Like' and Google has the +1

Facebook has the 'share' and Google has it's G+ share too.

Facebook however, also has 'Recommend' and 'Send' both of which (as far as I know) Google+ doesn't.

Another thing Facebook has that Google+ doesn't....600 million users!!

But if you like me, are routing for the boys over at the Googleplex and wish to place your +1 icons on your blog then you can refer to a <a title="How to add Google’s +1 to your wordpress blog" href="http://www.keithrozario.com/2011/06/how-to-add-googles-1-to-your-wordpress-blog.html" target="_blank">previous post I wrote some time back</a>. However, today I have a separate trick on how to Add multiple +1 icons to your blog (wordpress blog to be exact)

The trick is pretty simple, first logon to your dashboard and go to your Themes Editor:

1) First copy the following line of code into the header.php file of your theme:
<blockquote>&lt;script type="text/javascript" src="https://apis.google.com/js/plusone.js"&gt;&lt;/script&gt;</blockquote>
This ensures that javascript required for the icon is downloaded on every page.

2) Then copy the following line of code where you wish to see the icon in your index.php file. This file is the one that displays your index (or main) page. For instance it's the page that displays when I logon to <a title="Keith Rozario" href="http://www.keithrozario.com" target="_blank">www.keithrozario.com</a>
<blockquote>&lt;g:plusone href="&lt;?php the_permalink() ?&gt;" count="true"&gt;&lt;/g:plusone&gt;</blockquote>
3) Then copy the following line of code where you wish to see the icon in your single.php file. This file is the one that displays the single post. For instance it's the page that displays when I logon to <a title="http://www.keithrozario.com/2011/12/amazon-new-icons-for-aws.html" href="http://www.keithrozario.com/2011/12/amazon-new-icons-for-aws.html" target="_blank">http://www.keithrozario.com/2011/12/amazon-new-icons-for-aws.html</a>
<blockquote>&lt;g:plusone&gt;&lt;/g:plusone&gt;</blockquote>
That's really all there is to it.

As you may have noticed, I've taken out the buzz icons from my social media icons and added +1 icons instead. Let's hope Google+ won't go the same way as Buzz (or wave)

Now go forth and +1's.

<span style="color: #888888;">picture courtesy of:http://www.flickr.com/photos/latente/274852368/sizes/m/in/photostream/</span>