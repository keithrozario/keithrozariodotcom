+++
title = "What is big data"
slug = "what-is-big-data"
date = "2012-07-16T07:00:13"
draft = false
tags = ['Apache', 'Google', 'Hadoop', 'SAP']
categories = ['Big Data', 'Misc']
+++

![big-data-getting-bigger](/uploads/big-data.jpg "big-data")It's obvious that people have gotten bigger these past few decades, what's less obvious is how data has grown bigger in the past few years. In fact, 90% of the digital data we have today, was created in the last 2 years. Put another way, in 2010 we had just 10% of the digital data we have today.

In 2011, an estimated 1.2 TRILLION Gigabytes of data was created. That's roughly 200GB for every man women and child in the world--In just one year. That's every person in the world watching almost 300 feature length films every day, and this is the average.

The reason is simple, we now keep digital records of our transactions (e-banking and credit cards), our running patterns, our spending habits and even our wedding photos--and that's just commercial end user applications.

What about corporations who track thousands of data points per second for their manufacturing plants and supermarkets tracking the purchases of customers. We're creating and gobbling far more data than before, and the trend doesn't look to be stopping. Every day, we create 2.5 quintillion bytes of data — <strong>so much that 90% of the data in the world today has been created in the last two years alone.<!--more--></strong>
<h2>What's so big about Big Data?</h2>
The problem with this is that the big data sets is that they're different from 'regular' data in 3 ways.

<strong>Volume:</strong> Today, we process far more data than before, the older database architectures take too long to process.

<strong>Velocity:</strong> Millions or Billions of people tweeting involves a not just a lot of data, but in high velocity. Decisions need to be made quick so big data has to work quick as well.  <a href="http://www.dailymotion.com/video/xdaoae_ibm-commercial-the-road-intelligent_tech">A commercial from IBM</a> says it all--you wouldn't cross a highway if all you had was a 5 minute old photo.

<strong>Variety:</strong>Tweets aren't just formalized and structured data. You need to be able to identify keywords and look through the different types of data. Tweets also involve photos or just gibberish, links as well as language variances.

As time goes on we not only have MORE data, but the data coming in is coming at high velocity and even variety. Consider a big data challenge from the IBM big data page:
<blockquote>Turn 12 terabytes of Tweets created each day into improved product sentiment analysis</blockquote>
12 Terabytes of tweets is a really big challenge, not only do most big corporations have nothing close to this size, most database are very regular and uniform. Tweets on the other hand, span from 1-160 characters, could include shorten links or pictures, include tweet-slang and shorten forms of words <em>(like 'you' to 'u')</em>, and usually come sporadically throughout the day. This has all the components of todays big data challenge, from Volume, Velocity and Variety.

Your standard database would be unable to cope with this. Searching through 12 Terrabytes of tweets for meaningful data would be quite difficult, particularly if you wish do in real-time or near real-time.

The general rule of thumb is this--if you can solve it in Microsoft Excel, it's not big data!
<h2>What does this mean?</h2>
Big data is the next 'big' thing!! (pardon the pun).

Cloud computing has stopped becoming a buzzword and is now on top of the list of priorities for CIOs and companies alike. However, with cloud computing and the near infinite processing power they provide, comes the ability to crunch big data, but just adding processing power isn't going to improve your ability to handle the data.

What's needed is a re-think. A re-think towards the way we look at data.
<h2>Bigdata Tools</h2>
Big data applications like SAP HANA have taken the first step, they've taken the data from their usual database and jammed into high-performance memory in their SAP HANA boxes. Literally putting everything in-memory <em>(that's another buzzword)</em>. That means that SAP HANA no longer queries an external database for data, but rather it's own store of data which is fantastically fast. I saw a demonstration of this the other day, and I was blown away by the speed!!

SAP HANA comes in separate piece of hardware, it won't run on your current machines, but Amazon is already offering a SAP HANA cloud instances if you're interested, plus I'm not sure how many people would like their core ERP analytics tool on the cloud anyway, but SAP is becoming very developer friendly and the developers look to be responding.

Hadoop is another bigdata application that allows you to work on petabytes of data. The name is derived from the creators sons toy elephant, which is why it sounds so 'big', and Hadoop is big. Hadoop is released by Apache, which means just like the Apache webserver it's free and open source.

You can try it out for youself on Amazon as well. Amazon also provide 54 public sets from Genome sequences to the characters of the Marvel Universe for you crunch through.

Finally there's bigquery, a google offering, which offers real-time crunching of humongous data. Googles definition of big data is 100 million rows and up, so there aren't many datasets that reach that volume. Bigquery allows you to upload your own dataset to the Googlecloud and then use the bigquery to analyze it through regular SQL statements. More importantly, Google provide an API that allows you to utilize bigquery queries from just about any platform imaginable, these are REST APIs after all.

Google bigquery is charged on a per GB processed basis, on top of storage of whatever dataset you uploaded. Currently Google charges $0.035 per GB processes.
<h2>The downside of big data: Disappearing Privacy</h2>
So the world of bigdata is evolving, and with it comes a whole new world of possibilities and legal ramifications to work out. If every single transaction, tweet, facebook post, foursquare check in and blog comment of yours was crunched to identify you individually, you'd be very concerned about your privacy. An <a title="Big data and Privacy" href="http://money.cnn.com/news/newsfeeds/gigaom/articles/2012_07_11_big_data_and_the_changing_economics_of_privacy.html" target="_blank">article from CNN </a>clearly illustrates the point:
<blockquote>This shift illustrates a fundamental change in the economics of privacy: it has become cheap and easy to pry into the lives of others at the same time that protecting our own lives has become time-consuming and expensive</blockquote>
So we have here two opposing forces, as bigdata makes it easier to crunch the huge datasets in public domains, it means more and more businesses will be looking to source this data from public domains. It also means there will be less and less avenues for people to voice out without fear for their private data being shared across.

Big data does bring with it privacy concerns, but since corporations aren't going to stop doing what they do, it'll be up to governments to look into the privacy concerns of it's citizens. Here in Malaysia the newly enacted Data Protection Act looks a step in the right direction.

<span style="color: #888888;">picture of big fat men taken from: <a href="http://www.flickr.com/photos/selago/980565532/sizes/m/in/photostream/"><span style="color: #888888;">http://www.flickr.com/photos/selago/980565532/sizes/m/in/photostream/</span></a></span>