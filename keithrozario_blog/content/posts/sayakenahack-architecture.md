+++
title = "Sayakenahack architecture"
date = "2017-11-23T07:23:19"
draft = false
categories = ['Misc']
+++

<a href="/uploads/image2017-11-22_10-36-1.png"><img class="alignnone size-full wp-image-6131" src="/uploads/image2017-11-22_10-36-1.png" alt="" width="1308" height="618" /></a>

I know the picture is a bit hard to read, but I wanted to make sure I had a detailed enough picture to understand the 'innards' of sayakenahack. Sometimes when you're building stuff on the fly, and bottom-up, it's good to take a step back, and have a top-down view.

I'll be expanding this post over time, wanted to get my thoughts down quickly on paper before I moved on.
<h2>Intro to serverless</h2>
Serverless is a new-ish buzzword. It's about building full-blown applications without servers (not even virtuals).

No EC2 instances -- at all!

Some folks thought that just because I was on AWS, I was calling it serverless. Not so, lots of people use AWS for EC2, which are virtual servers. This blog, is hosted on a virtual server, but sayakenahack ran without any servers (virtual or otherwise). Except that one spot instance at the bottom right of the picture, we'll get to that later.

That doesn't mean I ran it on Elven magic and sparkly fairy-dust though. At some point, there were servers involved. But I never managed or ran those servers, they were abstracted from me by AWS services such as API Gateway <em>(which is awesome by the way)</em> and Lambda.

The beauty of serverless is :
<ul>
 	<li>I don't have the headache of managing a full-blown OS stack (with requires more skills than I have)</li>
 	<li>It can scale till kingdom come Amazon has designed their serverless offerings to scale, and they do it beautifully.</li>
 	<li>It's cheaper. MUCH cheaper.</li>
</ul>
With API Gateway for example, I could focus purely on building the resources and methods, without worrying about Apache configurations.

With lambda I can write python code natively (almost magically), without building out an EC2 instance.

And with DynamoDB, I get a database that can do anywhere from 10 to 10,000 writes per seconds without worrying about clustering, mirroring , etc. And even at 37 mln rows, the DB still qualifies for the free-tier.

That's awesome (if I do say so myself).

Now of course there is a drawback. Without full granular control of Apache/Nginx, certain edge cases you need might not be possible, and DynamoDB is somewhat limited in it's capability (although I'm not sure if that's DynamoDBs fault, or because all NoSQL databases are like that).

But overall, for sayakenahack, serverless was the way to go. It might not work for you, but it worked beautifully for me.

Next up, we'll look at the Holy Trinity of Serverless (API Gateway, Lambda, DynamoDB).

--stay tuned.

&nbsp;