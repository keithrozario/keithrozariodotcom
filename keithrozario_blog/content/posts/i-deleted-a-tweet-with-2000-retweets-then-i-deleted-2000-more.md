+++
title = "First I deleted my most popular tweet -- then I deleted 2000 more."
slug = "i-deleted-a-tweet-with-2000-retweets-then-i-deleted-2000-more"
date = "2018-04-22T19:39:38"
draft = false
categories = ['Misc']
+++

<a href="/uploads/undi-tweet-edit.jpg">![](/uploads/undi-tweet-edit.jpg)</a>Two weeks ago, I <a href="/uploads/undi-tweet.jpg">rage-tweeted</a> something regarding Malaysian politics that got a lot more viral than I liked (I've censored out the profanity for various reasons, most notably, there are teenagers who read this blog). It was a pointless collection of 200 characters, that somehow resonated with people enough to be shared across social media. Obviously, since it was me, the tweet was filled with a small collection of profanities, and laced with just the right amount of emotive content :)

But then things started getting bad.

Soon after I tweeted, I received messages from folks I hadn't met in decades, showing me screenshots of their whatsapp group that had my tweet -- my wife's chinese speaking colleagues were showing it to her at work -- I checked, and nearly 2,000 people retweeted it, which isn't typical for me, and frankly speaking pretty scary.

As much as I'd like to have my content shared, the tweet in question is nothing but couple of crude words pieced together in a 'rage-tweet'. And I understand that it emotionally resonates with folks who are angry, but if this the level of discourse we're having on  Malaysian social media, we should be alarmed. Completely pointless rants being viralled is not how we ubah, it is the absolute opposite of how we ubah!

Research on the virality of articles from the New York Times showed that 'angry' content was more viral than any other, beating out awe, surprise and even practical value. The angrier the content, the more likely it would be shared. A rage-tweet is more likely to go viral than something like fuel-saving tips, even though the latter clearly is more valuable to readers.

At this point, I'd rant about how the media has a responsibility to look beyond clicks and ads, and to think about the impact of their content on society, but since <strong>I </strong>owned the tweet, I simply deleted it. Of course, I can't stop the screen-shots being shared across whatsapp, but we do what we can.
<h2>Deleting your tweets</h2>
That got me thinking, twitter is a cesspool of angry farts screaming at each other, and that has some value.

But while, what I tweet today, may be relevant and acceptable today, it may not be 2-3 years from now. Kinda like how <a href="https://www.independent.co.uk/voices/apu-the-simpsons-pc-political-correct-stereotype-marge-a8297876.html">Apu from the Simpsons was acceptable and non-offensive in the 90's.</a>

I'm ashamed to say it, but I once thought that Michael Learns to Rock was a great rock band, in context, thats acceptable for a 12 year old 2 decades ago, before even Napster or Limewire. Of course, as a adult in 2018, I'm thoroughly aware that AC/DC are the greatest rock band ever, and Michael Learns to Rock, well they're not exactly Denmark's best export.

And that's the problem, <span style="text-decoration: underline;">twitter removes context</span>  -- it's very easy to take a 140 character tweet from 5 years ago out of context. Nobody cares about context on a platform that limits users to 140 characters (or 280 characters since end 2017). Maybe you quoted an article from TheMalaysianInsider, which, guess what, no longer exist. Context is rather fluid on twitter, and it changes rapidly over weeks, let alone the years from your first tweet.

For example,  this tweet from Bersatu's Wan Saiful:
<blockquote class="twitter-tweet" data-lang="en">
<p dir="ltr" lang="en">No the internet shouldn't be censored. He doesn't know how to shut up. His views are old and racist. But freedom of speech is for everyone.</p>
— Wan Saiful Wan Jan (@wansaiful) <a href="https://twitter.com/wansaiful/status/399686611488612352?ref_src=twsrc%5Etfw">November 10, 2013</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Gee, I wonder who he was talking about, a simple internet search will give you the answer, but that's not the point.

Wan Saiful changed his opinion,  and he's <a href="http://www.malaysia-today.net/2018/03/01/wan-saiful-ready-to-face-critics-for-making-u-turn-and-joining-ppbm/">explained why</a>, people should be allowed to change their mind.Freedom to change your opinion not just perfectly fine, it's a per-requisite for progress.If we allow our tweet history to be a ball-and-chain that ties us to our old idealogy, how could we ever progress? Everybody changes their mind -- and that's OK.

The point is twitter should not be a historical archive -- it should be current. A great place to have an informed discussion of current affairs, but not a place to keep old, out-dated and out of context material floating around.

Hence, I decided to delete all my tweets that were older than 90 days old, and here's how.<!--more-->
<h2>How to delete your tweets</h2>
There are some services online that help you do this, but I chose to code this myself (obviously!). Based mostly on code found <a href="https://pushpullfork.com/i-deleted-tweets/">here</a> and <a href="http://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy">here, </a> my little script will archive the older tweets into a jsonl file, before deleting. The code is <a href="https://gist.github.com/keithrozario/2cf05656335e604e1ec1896c8ff4cd44">here</a>, and it's relatively easy to run.

Overall, I deleted 2533 older tweets, and hope to 'operationalize' the deletion to more frequent intervals.
<h2>Conclusion</h2>
I feel a whole lot more refreshed, I feel more in control of my tweets, and generally I think this was a good move. It's always nice to do some spring cleaning.

But as a surprise for you who've read all the way to the end, here's a <a href="/uploads/Tweetpy.zip">link</a> with the collective tweets of 40+ politicians/observers from twitter. Unfortunately, I don't have the 'Premium' twitter API, and hence the tweets are not exhaustive -- merely 3000+ tweets per user. But still a pretty good number, and where I found the Wan Saiful tweet above -- who knows what you'll find. I must warn you though, scrolling through 3000 tweets from Ahmad Maslan might cause irreversible harm :).

*AFAIK the 'normal' twitter API only allows for the latest 3000+ tweets (or there abouts) and prolific tweeters will only have the latest tweets available. This is just how the API works, and nothing I could do. In the interest of full-transparency, code for generating these extracts is <a href="https://gist.github.com/keithrozario/bc1ee53f921a8e167827669a518c3d60">here</a> -- enjoy.