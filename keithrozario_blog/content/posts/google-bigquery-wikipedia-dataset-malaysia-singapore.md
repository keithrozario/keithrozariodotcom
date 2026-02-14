+++
title = "Google bigquery"
slug = "google-bigquery-wikipedia-dataset-malaysia-singapore"
date = "2012-07-17T07:00:16"
draft = false
tags = ['Google']
categories = ['Misc']
+++

![Google-bigquery-whatisit](/uploads/Google-bigquery-image.png "Google-bigquery-image")There are other more popular tools for big data, but today we'll focus on Google BigQuery for a very good reason. It's the only one I know how to use.

Google BigQuery is a full fledge big data tool developed by google and stored on the cloud. There's a lot more information you can glean from their presentation <a title="Google bigquery" href="http://www.youtube.com/watch?v=QI8623HlYd4&amp;" target="_blank">here</a>. The short story is that Google created this tool online where you can analyze your bigdata for a per use fee, similar to other cloud offerings. Google currently charges $0.035 per GB of data processed or $35 per TB of data. That seems like a small fee, but it adds up pretty quickly, so for the moment bigdata and bigquery aren't exactly end-user offerings.

I'm just going to quickly jump into a worked example of Google BigQuery before making some remarks. To use BigQuery, you're first going to have to create an API project in Google and then go to<a title="Google Bigquery" href="http://bigquery.cloud.google.com" target="_blank"> https://bigquery.cloud.google.com<!--more--></a>
<h2>The Wikipedia Public dataset on Google bigquery</h2>
Once you've created your project you have a few public datasets available to test out the application. My free account could only access these public datasets, but a paid account could upload your own dataset to Google for analysis on Google BigQuery.

The datasets include the full works of Shakespeare, the github timeline and Wikipedia revisions. For my example I'm just going to use the Wikipedia revisions, which is a dataset consisting of a single row of data for every Wikipedia revision/update, this includes the contributor_username who updated the article, and the article title itself. It also has language and contributor IP, etc, but for now we'll focus on these two attributes which is title and contributor_username.

It's also worth noting, that this is just the metadata of the revision and no details of the revision exist in this dataset.
<h2>Querying Wikipedia on BigQuery</h2>
So what's a good way to use BigQuery--well I wanted to find out for example the number of Wikipedia titles with the word Malaysia in them, all I had to do was run the following query on the Wikipedia dataset from Google:
<blockquote>SELECT title, count(title) as num_revisions
FROM [publicdata:samples.wikipedia]
WHERE
title CONTAINS 'Malaysia'
GROUP BY title</blockquote>
The results:

![](/uploads/Google-biquery-title-contains-Malaysia.png "Google-biquery-title-contains-Malaysia")The results were quite impressive 5423 rows returned from a total of 6.79GB processed--in 7.5seconds!

If I was getting a bit competitive and wanted to see the results from all Wikipedia entries containing Singapore for example, I rerun the query changing 'Malaysia' to 'Singapore'.

The results were equally impressive, 5920 rows returned from a total of 6.79GB processed--in 5.0seconds.

Now let's make things a  bit more interesting, let's look for the number of revisions across all titles containing the word Malaysia:
<blockquote>SELECT title, count(title) as num_revisions
FROM [publicdata:samples.wikipedia]
WHERE title CONTAINS 'Malaysia'
GROUP BY title
HAVING num_revisions &gt; 50
ORDER BY num_revisions DESC</blockquote>
![Number of revision per title Wikipedia](/uploads/BigQuery_contributor_num_revisions.png "BigQuery_contributor_num_revisions")Now things get interesting, from this query I can determined the most updated article containing the word 'Malaysia', all of this processing on 6.79GB of data in just 4.2 seconds. That's amazing.

At this juncture it's important to point out that the bigdata doesn't operate on the same principles as regular databases. Here things are sorted out in columns rather than rows, and all my examples prior to this select data from just the title column. So to see how things pan out when we look at 2 rows, I decided to look at who contributes the most to wikipedia by looking at the contributor_username.
<blockquote>SELECT contributor_username,title, count(contributor_username) as num_revisions
FROM [publicdata:samples.wikipedia]
WHERE title CONTAINS 'Malaysia'
GROUP BY contributor_username, title
HAVING num_revisions &gt; 50
ORDER BY num_revisions DESC</blockquote>
The results:

![Google-bigquery-most-contributions-wikipedia](/uploads/Google-BigQuery_contributorusername_title.png "Google BigQuery_contributorusername_title")This query, looks at all articles containing the word 'Malaysia', and it groups them by title and username. Basically it allows me to see which user is updating which articles the most. I've intentionally limited the returned data by looking at only those articles which have been updated more than 50 times by the user.

The results were interesting, but I'll share those in a separate article I intend to write about Malaysia's King of Wikipedia and how Malaysian Airlines (MAS) looks to be updating their own wikipedia page...tsk tsk tsk.

In terms of performance, the query looked up 9.28GB of data in 6.1seconds. The addition of one column (contributor_username) added nearly 3GB of data to the query, but no significant amount of time. Also remember, Google charges by the GB not time.

Finally, I decided to look across the region for the most updated articles. So I ran a query to check on all revisions for articles with 'Malaysia', 'Singapore', 'Philippines','Brunei' and 'Thailand' in the title:
<blockquote>SELECT title, count(title) as num_revisions
FROM [publicdata:samples.wikipedia]
WHERE
title CONTAINS 'Singapore' OR title CONTAINS 'Malaysia' OR
title CONTAINS 'Thailand' OR title CONTAINS 'Indonesia' OR
title CONTAINS 'Brunei' OR title CONTAINS 'Philippines'
GROUP BY title
HAVING num_revisions &gt; 250;</blockquote>
The Results:

![Google-Bigquery-wikipedia-Malaysia-Singapore-Philippines-Brunei-Indonesia](/uploads/Google-BigQuerymultiple-countries.png "Google BigQuery(multiple countries)")The results, 6.79GB processed, in 5.8 seconds.

So overall I think, regardless of whatever data you query from the wikipedia public data set, whether you add CONTAINS statement and an 'OR' on that, or query two columns instead of one, or even add a HAVING clause and a overtly complicated WHILE clause, you're unlikely to break the 10s/query barrier with this baby.

This big data is awesome. You can crunch huge amounts of data in a short span of time.
<h2>What if I don't want to query Wikipedia</h2>
Of course you may not want to query Wikipedia. You can upload your own dataset to the Google cloud for processing. That data set needs be denormalized, something most DBAs frown upon. However, with big data the focus is less on getting 'one version of the truth' and more on 'optimizing for performance', so it's here we see a stark difference between regulars DB and big data approach.
<h2>Google bigquery Prices</h2>
Google charges per GB for cloud storage (just like anything else0, however, the BigQuery charges are pretty expensive at $0.035/GB processed. That's nearly RM0.10 per GB processed.

Which means for a paying account, I would have had to pay nearly <strong>RM3 to execute the 4 queries above</strong>, that's a lot of money for just 4 queries (even though I manage to get really good meaningful data).

Pricewise bigdata is still out of reach for personal use, but as cloud computing cost reduce I expect to see the price of BigQuery reduce as well. A lot of big corporations are working on utilizing big data to meet the ever growing demands of our complex markets.

Overall I really enjoyed Google bigquery, and I recommend you try it out for yourself. You can find the Wikipedia King of your country, or even state or town--who knows? All I know is that it'll take you seconds to get the data if you wrote the query correctly.
<h2>Final thoughts</h2>
I really enjoy analyzing data, it's probably the reason I'm so good at Excel <em>(self-praise is no praise!!).</em>

So I really enjoyed playing around with BigQuery, it's interesting to see how this will compare to Hadoop and things like SAP HANA, both of these tools by the way are available on AWS.

I used the free version--which has limits, so I ended up having to create multiple projects to write this article, but overall I enjoyed doing it. For the most part, having a paid account, would have allowed me to really delve into the data more, but until some ad revenue for the blog starts to flow in or I get some sponsored post there will be financial limits to how far I play around with Google bigquery or Amazon AWS.

You can export the BigQuery results in a csv, if your results are less than 16,000 rows (or so Google claims), but with my Free account all I could export was somewhere in the region of 500 rows, anything more and I had to create a paid account, and have that transported via Google Cloud Storage. So remember to limit the rows with a WHILE or HAVING statement if you wish to export to CSV.
<h2>What did I find?</h2>
Since wikipedia is a crowdsourcing, I intend to write an article on the undisputed King of Wikipedia from Malaysia, this is a guy who updated 60+ articles a total of 13,179 times. That's amazing.

Also, I noticed a wikipedia user named yamahaboy81 who updated the Malaysian Airlines article a total of 401 times, and other MAS entries--and only MAS entries.

Similar search on Singapore revealed Singapore Airlines to be a top article for editing as well. The Singapore Airlines article was edited 612 times by a user Huaiwei, but this user also updated articles on Changi Airport, Singapore Bus Routes, etc. Yamahaboy only edited articles directly associated with Malaysian Airlines.

Of course I saved the best for last.

One article in particular was update more than 5,000 times!! This article was from my last query, and contained the word Philippines and that article was--<strong>List of fraternities and sororities in the Philippines.</strong>

Boy, the must take this pretty seriously over there.

What can you find out from Google bigquery, create an interesting query and run it, or leave a comment here, and if it's interesting enough, I'll run it myself.