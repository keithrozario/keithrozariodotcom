+++
title = "Using Google Web Fonts on Wordpress"
slug = "using-google-web-fonts-safe"
date = "2011-04-27T14:51:26"
draft = false
tags = ['Blog Features', 'Fonts', 'Google']
categories = ['Blog']
+++

<link href='http://fonts.googleapis.com/css?family=Tangerine|Special+Elite|Syncopate' rel='stylesheet' type='text/css'>![](/uploads/font_directory_logo_beta1.gif "Google Web Fonts") 

Ever got up in the morning and wished you could blog in <span style="font-family: 'Tangerine'; font-size: 28px; color: #2abada;">Tangerine</span>, or felt like only <span style="font-family: 'Special Elite',serif; font-size: 18px; color: #2abada;">Special Elite </span>could fully express your creative juices. How about: <span style="color: #2abada; font-family: Syncopate, serif; font-size: 28px; text-align: center;">syncopate!!</span>

<center></center>All those words in <span style="color: #2abada;">color</span> are in fonts that are deemed not websafe, yet you can probably view it nicely on your browsers...the trick is using Googles new web gizmo, the Google WebFonts API.<!--more-->

Font designs are actually stored in your computer in files. When you load a webpage with a font like Arial, what the webpage does is it passes information over to your computer saying <em>"Print this is Arial size 10 -&gt; Keith Rozario". </em>What your computer then does is it references the Font design stored in a file called Arial.ttf, and then displays the words <em>Keith Rozario</em> in the font design specified in the file.

The problem is of course, some computers may not have the Arial font, in which case your computer may default the font to something like Times New Roman, or even not display the font at all, thereby having the whole page blank. To prevent such catatrosphic failure of a blog, web designers reverted to using a very limited set of fonts deemed web-safe, these were fonts that were found on virtually every computer out there. That posed a serious limit on the creatives among us, as there are literally millions of fonts on the web, but only a handful were deemed web-safe.

Fortunately, Google figured out a very quick and near painless solution. Google figured that these font files were actually pretty small, in most cases barely 2 to 3KB large. Most pictures on blog post are nearly 10 to 100 times larger, coming in at 30KB to 300KB in size. So if you can download a picture to view on the web, why couldn't you download a .ttf font file for the web, thereby making everything web-safe.

With just a bit of programming to utilize fonts usually reserved for web-designers to incorporate into their designs via photoshop. The selection is still limited, but far more comprehensive then the web safe fonts (after all who wants to view everything in Garamond or Times new Roman). On my last count there were 501 fonts on the Google API compared to just 5-10 web safe fonts.

Google calls their new creation the Google Web Fonts API.
<h2>Using Google Web Fonts</h2>
So head on over to <a title="Google Web Fonts" href="http://www.google.com/webfonts/" target="_blank">Google web fonts</a>, pick a font you like. Then google will present you 2 lines of code. The first is the most important:

<code>&lt;link href='http://fonts.googleapis.com/css?family=Syncopate' rel='stylesheet' type='text/css'&gt;</code>

You have to paste this either in the post itself (like this example), or preferably in the various .php files of your wordpress theme. Remember, this needs to be pasted in a loaded page, and if you're pasting it in the post itself, you need to switch the post editor into HTML mode and keep it there. For some reason switching into visual mode messes it all up.

Finally then you can use the font as normal. It's  advisable to change the css values in your style.css sheets, however if you're a bit lazy like me you can change it at the post level (provided you're in the html view) by using the following command:

<code> &lt;span style="font-family: 'Tangerine'; font-size: 28px; color: Red";&gt;</code>

That way you can incorporate your new font, and the web browsers display them without a hitch. You can even customize the first line of code, to only download the letters you need from the font, theyby making the file smaller and faster to load.
<h2>Example</h2>
So for example, in this post I used 3 fonts from the API, <span style="font-family: 'Tangerine'; font-size: 28px; color: #2abada;">Tangerine</span>,<span style="font-family: 'Special Elite',serif; font-size: 18px; color: #2abada;">Special Elite </span>and <span style="color: #2abada; font-family: Syncopate, serif; font-size: 18px; text-align: center;">syncopate!!</span>

To display them correctly, all I need to do is:

1. Choose my font from the Google Web Font API page

2. Review my font on the API page

3. Use my font, by getting the bit of code from the API page, it'll look like this

![](/uploads/Google-Web-Fonts-300x56.png "Google Web Fonts")4. Copy that bit of code and paste it in your wordpress blog post. In my example, I switched the view from Visual to HTML, and just pasted it at the top of the post.
<blockquote>&lt;link href='<a href="http://fonts.googleapis.com/css?family=Tangerine|Special+Elite|Syncopate" target="_blank">http://fonts.googleapis.com/css?family=Tangerine|Special+Elite|Syncopate</a>' rel='stylesheet' type='text/css'&gt;</blockquote>
<span style="color: #888888;"><em>*be careful as I noticed, Wordpress automatically deletes this the moment you switch from HTML back to Visual, I would keep this step to last, just before I press the POST button on the page</em></span>

5. The code downloaded the 3 fonts from the Google Web Font API onto your computer.

6. Then whenever I want to display in a particular font all I had to do was this:
<blockquote> &lt;span style="font-family: 'Tangerine'; font-size: 28px; color: #2abada;"&gt;<strong>Tangerine</strong>&lt;/span&gt;</blockquote>
7. This puts the word Tangerine in a HTML <span> that I could then display as Tangerine. </span>

Neat huh?