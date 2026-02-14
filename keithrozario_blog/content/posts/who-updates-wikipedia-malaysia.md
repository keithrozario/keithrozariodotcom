+++
title = "Wikipedia from a Malaysian perspective"
slug = "who-updates-wikipedia-malaysia"
date = "2012-07-18T04:00:34"
draft = false
categories = ['Big Data', 'Crowdsourcing', "Keith's Favorite Post"]
+++

<a href="/uploads/wikipedia_crowdsourcing.png">![](/uploads/wikipedia_crowdsourcing.png "wikipedia_crowdsourcing")</a>Wikipedia is quite possibly the greatest repository of information mankind has ever seen. It's built around an amazing concept of allowing anyone the ability to create, document and moderate information in real-time, and so far the concept has proven successful--some may even argue that it's too successful.

For the past two days, I've been writing about <a title="Google bigquery" href="http://www.keithrozario.com/2012/07/google-bigquery-wikipedia-dataset-malaysia-singapore.html">Bigquery</a> and <a title="What is big data" href="http://www.keithrozario.com/2012/07/what-is-big-data.html">Big Data</a> in general, and for the most part I've been using the freely available wikipedia dataset in Bigquery to perform some queries and analysis. The results were so interesting, that they warrant a post on their own--and this is that post!

For instance, I was curious who Aiman Abmajid was. For those who aren't following the blog, Aiman is the undisputed King of Wikipedia in Malaysia. Aiman has single-handedly helped update Malaysian articles on Wikipedia a mind-blowing 13 THOUSAND times--and that's just the English articles. Almost 6 times more than his closest Malaysian rival.

I was intrigued as to who he was and why was he updating so many Wikipedia entries (some more than 900 times per article), and more I dug the more intriguing it got.

A quick Google search, brought me his Wikipedia which led me to the following:<!--more-->
<blockquote> <strong>Assalamualaikum</strong>, <strong>Salam Sejahtera</strong>, <strong>Salam <a title="1Malaysia" href="http://ms.wikipedia.org/wiki/1Malaysia">1Malaysia</a></strong>, dan <strong>Selamat Datang</strong> ke Wikipedia saya. Nama saya <strong>Aiman bin Ab Majid</strong>, (<strong>أيمان بن ابمجيد</strong>). Saya adalah anak kedua dari keluarga Abdul Majid bin Aziz. Saya dilahirkan pada <a title="2 Jun" href="http://ms.wikipedia.org/wiki/2_Jun">2 Jun</a> <a title="1985" href="http://ms.wikipedia.org/wiki/1985">1985</a> di <a title="Petaling Jaya" href="http://ms.wikipedia.org/wiki/Petaling_Jaya">Petaling Jaya</a>, <a title="Selangor" href="http://ms.wikipedia.org/wiki/Selangor">Selangor</a>, <a title="Malaysia" href="http://ms.wikipedia.org/wiki/Malaysia">Malaysia</a>. Saya ialah <a title="Orang Kurang Upaya (tidak wujud)" href="http://ms.wikipedia.org/w/index.php?title=Orang_Kurang_Upaya&amp;action=edit&amp;redlink=1">Orang Kurang Upaya</a> (OKU) dari jenis masalah pembelajaran dan <a title="Autisme" href="http://ms.wikipedia.org/wiki/Autisme">autisme</a>. Sejak kecil lagi saya tidak petah bercakap tapi kini sudah ada sedikit lancar memandangkan saya sudah besar dan berfikiran seperti orang dewasa. Saya boleh membaca, menulis dan banyak tertumpu kepada pembelajaran dari tadika sampailah ke kolej. Saya pernah mendapat pendidikan awal di beberapa sekolah pendidikan khas bermasalah pembelajaran (Autistik) di <a title="Shah Alam" href="http://ms.wikipedia.org/wiki/Shah_Alam">Shah Alam</a>, <a title="Johor Bahru" href="http://ms.wikipedia.org/wiki/Johor_Bahru">Johor Bahru</a> dan <a title="Subang Jaya" href="http://ms.wikipedia.org/wiki/Subang_Jaya">Subang Jaya</a>.</blockquote>
Now for those who can't read Malay, Aiman is a man (as can be inferenced from the 'bin' in his name), born on the 2-Jun 1985 (making him just 27 years old) in Petaling Jaya Malaysia.

He's an Orang Kurang Upaya (OKU) --which is the official term for disabled people in Malaysia--due to his autisme, and he gives a brief story as to how he overcame the odds from being unable to speak to actually speaking a bit from kindergarten till College. It's an amazing story to read, that someone with Autisme in Malaysia is actually contributing to our countries repository of information--this could only happen with technology.

I usually would be skeptical of such stories, but Wikipedia users aren't exactly glamour hungry, there really is no reason to lie on a Wikipedia profile. You can read more about <a title="Aiman Abmajid Wikipedia User Page" href="http://ms.wikipedia.org/wiki/Pengguna:Aiman_abmajid" target="_blank">Aiman on his Wikipedia User Page</a>.

Although it's not mentioned here, his Wikipedia user page also goes on to elaborate that he's an expert in Malaysian Expressways, which explain why the <em>Malaysian Expressway System</em> Wikipedia page was updated a total of 912 times by Aiman. This is a page you'd expect many updates, since Malaysia adds a highway nearly every day as far as I can tell, and the person keeping Malaysian up to date on our expressways--is Aiman bin Ab Majid.

I'm really blown away by the results, and it's only while writing this article and looking through the data that I noticed I might be looking at only the English articles, and Aiman had already updated English articles a total of 13,179 times. His closest rival in this case was wikipedia user <strong>Earth</strong>, who updated English articles a total of 2,477 times (about 5 times less than Aiman).

It's really really nice to see, someone from Malaysia actually updating information about our country, particularly our Nations expressways. I think crowdsourcing in Malaysia has definite potential.
<h2>Methodology for calculation</h2>
1. I used Google Bigquery on the publicly available Wikipedia dataset

2. Unfortunately, the data set didn't have contributors country of origin, therefore I had to settle for the next best thing, which was to filter all Wikipedia articles by only those that had Malaysia in the title.

3. This meant, that Malaysian users updating articles about other countries were not counted in the equation.

4. It also meant, Malaysian users updating articles that didn't contain the word Malaysia in the title, were also not counted in the equation.

5.The 13,179 revisions by Aiman were on ALL articles revised by him, but because I couldn't export the data for a more granular analysis, based on what I could see this covers only ENGLISH articles.

6.While the methodology is very restrictive and has some flaws (we do the best with the data we have), the fact that Aiman blows everyone else out of the water could be a good thing. The difference between Aiman and the rest of the pack is just so wide, that even if we improved the data quality and availability, it's unlikely he could be overtaken by anyone.

7.A similar search for Singapore, yielded Wikipedia User Huaiwei as the Singaporean Wikipedia King (or Queen) with a total of 9,477 revisions.

8.Just like Aiman, Huaiwei writes a lot about public transport in terms of Singapore airlines, bus routes etc.

9.In terms of article titles, the article titled Malaysia, is the most updated article on the list (quite obviously).

10. What's not so obvious is why Malaysian Airlines is 2nd most updated article on the list.

That I will cover in my next post, but as a preview to that--the data suggest MAS was updating their own Wikipedia page, a solid no-no when it comes to Wikipedia ethics.
<h2>Conclusion</h2>
Some might say, doesn't he have  things to do other than update Wikipedia.

This really <em>"Makes my blood go upstairs".</em>

Contributing to Wikipedia is an indirect (and sometimes direct) contribution to society at large. What else could be more important. His 13,000 + revisions have helped keep articles up to date and added value not just to Wikipedia but to the internet in general. The value of updating wikipedia--even a slight amendment--dwarfs any value of watching any program on TV. Yet, we seem to have no problem with people to openly admit to watching hours upon hours of korean dramas or reality TV--but spend hours updating Wikipedia, and suddenly people ask you about having better things to do.

I'm proud of Aiman (whoever and where ever he is), and I'm proud to have a fellow Malaysia take Wikipedia so seriously. You should be too.

*I've tried contacting Aiman, but he hasn't replied to any of my emails, I've decided to leave it at that. If you know Aiman , you might want to give him that pat on the back he so greatly deserves.