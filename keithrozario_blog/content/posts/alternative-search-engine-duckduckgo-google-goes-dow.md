+++
title = "What happens when Google goes down?"
slug = "alternative-search-engine-duckduckgo-google-goes-dow"
date = "2012-02-20T18:35:07"
draft = false
tags = ['duckduckgo', 'Google', 'ixquick', 'searchengine']
categories = ['Misc']
+++

![](/uploads/google-down-large-300x204.png "google-down-large")Yesterday, I was over at a friends house fixing up a PC that was ridiculously infected with malware. The only complaint they had however was that they couldn't access malaysiakini, a local news site that they subscribe too. True enough the page wasn't loading completely, and it was frighteningly slow even when it did. Now, this sort of symptom usually doesn't lead to much, maybe bad browser plugin or something like, but browsing from all 3 browsers on the machine (Chrome, Firefox and IE) yielded the same results.

So I decided to do what I always do and perform a Google search, and Google wasn't loading...gasp!!

Then I thought, I'd try <a title="Bing!" href="www.bing.com" target="_blank">bing</a> instead...and it wasn't working either.

Finally I did a simple <em><span style="color: #888888;">netstat -a</span></em> on the command prompt and I was horrified.<!--more-->

To confirm my suspicions, I did a simple ping for google.com and got the following:

![](/uploads/malware1.png "malware")

Now for those of you unaware a ping from google should point to <strong>74.125.227.47</strong>, somehow my computer wasn't resolving the right address to Google, and the reason why Malaysiakini wasn't resolving either was because Malaysiakini ran some google scripts on it's webpage that required me to download some stuff from Googles servers. Since I wasn't resolving Google correctly, I couldn't load the page till the script timed out and that took a looooong while.

This of course raises the question, if we're so reliant on Google for solving our problems, what do we do when Google is down...and Bing. If you take search engines out of the internet, the internet is basically useless!
<h2>Alternative Search Engines</h2>
So I was there stuck with an issue I couldn't resolve, because I couldn't search. However, there are other search engines out there, and according to the remarkable blog <a title="Search Engine lang" href="http://searchengineland.com/" target="_blank">searchengineland.com</a> these newer search engines offer better results than Google.
<h2>Duckduckgo</h2>
Duckduckgo's tagline is "Google tracks you. We don't". Thus, making it the defacto search engine from conspiracy theorist everywhere. It's unique name merely hides the fact that it's actually a pretty good search engine that prioritizes your privacy.

While the results from this search were pretty good, I found Google was better at solving my <strong>simda.f</strong> infection. I couldn't find anything information from duckduckgo that solved the problem, although the initial results were similar to Googles, Google had more data in the following pages that allowed me to find the results I needed.

That being said, if you're searching for something you don't people finding out you're searching for...use duckduckgo.

<a title="Duckduckgo" href="http://www.duckduckgo.com" target="_blank">www.duckduckgo.com</a>
<h2>Ixquick</h2>
Another search engine recommended by searchengineland was Ixquick, another search engine that prioritizes privacy, to the point where it proclaims itself "The worlds most private search engine"

Now Ixquick also claims it doesn't record your IP address, something Google is probably doing, search results were pretty good, but according to this post from gHacks ixquick doesn't do too well on complex searches.\

<a href="https://www.ixquick.com/">https://www.ixquick.com/</a>
<h2>What's become of Google</h2>
Using these search engines got me reminiscing about the time when yahoo, excite and altavista controlled the search engine world. Where are these guys now, and how did Google manage to completely obliterate these guys out of the water. I wouldn't hold my breath on any of these guys beating Google, but I was wrong before. There seems to be shift in the online world, and Google has become the IBM of the new millenium, the tech giant that everyone wants to beat, there also seems to be a movement towards privacy rather than search accuracy, and people may be willing to search a bit too longer to get the results they want as long as nobody knows what they're searching for.

So what happens when Google goes down? You use another search engine...but what happens if you don't know any? Just remember duckduckgo.com and you should be fine.
<h2>Conclusion</h2>
All that said I done, I just typed Googles IP address onto my address bar and searched using Google. Finally I managed to figure out a solution to my problems thanks to <a title="Redirect Virus Google" href="http://redirectvirusgoogle.blogspot.com" target="_blank">http://redirectvirusgoogle.blogspot.com</a>, and how did I find the website that helped solve my problems?

Why Google of course.