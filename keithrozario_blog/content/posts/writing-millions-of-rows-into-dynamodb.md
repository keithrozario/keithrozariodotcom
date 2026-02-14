+++
title = "Writing Millions of rows into DynamoDB"
date = "2017-12-09T23:03:56"
draft = false
categories = ['Misc']
+++

While designing sayakenahack, the biggest problem I faced was trying to write millions of rows efficiently into DynamoDB. I slowly worked my way up from 100 rows/second to around the 1500 rows/second range, and here's how I got there.
<h2>Work with Batch Write Item</h2>
First mistake I did was a data modelling error. Sayakenahack was supposed to take a single field (IC Number) and return the results of all phone numbers in the breach. So I initially modeled the phone numbers as an array within an item (what you'd called a row in regular DB speak).

Strictly speaking this is fine, DynamoDB has an update command that allows you to update/insert an existing item. Problem is that you can't batch an update command, each update command can only update/insert one item at a time.

Running a script that updated one row in DynamoDB (at a time) was painfully slow. Around 100 items/second on my machine, even if I copied that script to an EC2 instance in the same datacenter as the DynamoDB, I got no more than 150 items/second.

At that rate, a 10 million row file would take nearly 18 hours to insert. That wasn't very efficient.

So I destroyed the old paradigm, and re-built.

Instead of phone numbers being arrays within an item, phone numbers were the item itself. I kept IC Number as the partition key (which <strong>isn't</strong> what Amazon recommend), which allowed me to query for an IC Number and get an array of items.

This allowed me to use DynamoDB's <a href="http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#DynamoDB.Client.batch_write_item">batch_write_item</a> functionality, which does up to 25 request at once (up to a maximum of 16MB). Since my items weren't anywhere 16MB,  I would theoretically get a 25 fold increase in speed.

In practice though, I got 'just' a 10 fold increase, allowing me to write 1000 items/second, instead of 100. This meant I could push through a 10 million row file in under 3 hours.

First rule of thumb when trying to write lots of rows into DynamoDB -- make sure the data is modeled so that you can batch insert, anything else is painfully slow.<!--more-->
<h2>Turn off auto-scaling</h2>
Unlike server-ed Databases, where your throughput is limited by the hardware you have, DynamoDBs throughput is limited only by how much you're willing to spend.

Amazon effectively charge you a throughput fee, in the form of Capacity Units. Each unit cost per hour, and provide throughput for your database. More units equals more throughput.

In Auto-Scaling, you can set minimum and maximum values for the both Read and Write Capacity units, and Amazon will automatically scale based on the consumed capacity. So a spike in traffic results in an automatic increase of units, while a drop in traffic, will scale down your database to save cost.

Auto-scaling sounds nice, but it doesn't respond in real-time. There is lag between the demand increase, and the provision of supply. Secondly, Amazon allow for only 4 'scale-downs' a day or once every 2 hours, i.e. you can't scale your database downward too often, this applies for auto-scaling as well, and the algorithm just wasn't very effective for a migration.

When you're migrating data into a non-production DynamoDB, you go from 0% capacity, to 100%, and then back 0% again. This is not what typically happens for production systems, hence the algorithm that manages auto-scaling, doesn't cope with this very well.

Hence I recommend turning off auto-scaling, it's much better to have the granular manual control.

The script I wrote, would basically scale up before insertion, and scale down after insertion. I would monitor the cloudwatch logs to see my consumed capacity, and tweak everything manually from there.

Since Amazon allow unlimited scale-ups and limited scale-downs -- it's advisable to start a small-ish provision (200 Write units for example) and work your way up.
<h2>Latency matters</h2>
Even with Batch write item, latency matters.

With my laptop in Singapore, writing to the AWS Singapore region, I sensed that latency was causing issues. Just FYI, Singapore has world-class infrastructure, my home has a 1Gbps connection, and the country is just 60km across (end to end), which meant that I couldn't have been more than 30km from the actual data center hosting my DynamoDB.

Even then, when I spun up an EC2 instance in the same region, and ran the script from there, I got a 50% increase in throughput, from 1000 items/second to roughly 1500 items/second, peaking at around 1800 items / second.

It wasn't hard cloning my scripts (they were on gitHub), but I made sure I encrypted the file, before sFTP-ing to the EC2 instance. Once transferred, I could sit back and relax. If you buy spot-instances, they can cost as little as just 3-4 cents per hour -- well worth the money.
<h2>To multi-thread or not to multi-thread</h2>
From here the obvious next option was multi-thread the whole thing. If one thread can do 1500, then 20 threads can do 30,000. I was keeping <a href="https://www.troyhunt.com/working-with-154-million-records-on/">Troy Hunt's 22,500 row/second</a> record as my benchmark.

But hold on a gosh-darn second there!

Troy uses Azure Table Storage which is very different to DynamoDB.

Table Storage charges per operation, while DynamoDB charges per Capacity Unit, and those are billed per hour. Plus, there's a soft-limit of 10,000 Units per table, which you'd need to write to Amazon to have increased.

In other words, Azure charges per operation with seemingly no limit on the throughput, while Amazon charges entirely on the throughput. You need to optimize your throughput, to balance out cost vs. performance, if you're hoping to make DynamoDB work for you.

At 1,000 rows per second, it takes 3 hours to insert 10 million rows, and cost $2.22.

At 10,000 rows per second, it takes 17 minutes to insert 10 million rows, but cost $7.44.

You basically pay more to spend less time, or my way of thinking, why spend money, when time is cheaper. The keened eyed would point out that I'm using EC2 instances to push this, so each extra hour cost me something -- but spot instances (even of high end servers) can run to just $0.03 per hour.

And honestly speaking, I haven't really mastered this multi-threading stuff, so I decided to give it a skip, and just stick to best effort of 1,500 rows per second. 3 hours to process 10 million is fine by me, just leave it overnight, and look at the logs in the morning.
<h2>Conclusion</h2>
If you want to write millions of rows into DynamoDB at once, here's my advice:
<ul>
 	<li>Model the data right, so you can batch write everything</li>
 	<li>Turn of auto-scaling, and manually manage the throughput</li>
 	<li>Run the insertion from an EC2 instance in the same region</li>
 	<li>Consider multi-threading, but also consider the cost associated with it</li>
</ul>
Sorry I don't have the cloudwatch graphs, learnt today they only last 2 weeks, and it's been more than 2 weeks since I pushed this data into the DynamoDB.

Lastly, consider this, a full-blown DynamoDB in SG, cost $7.44 per hour. That's a noSQL database capable of doing 10,000 writes per second -- with all the backup/restore, mirroring, clustering, taken care for you. Serverless is ridiculously cheap, and getting cheaper, the only thing holding most people back is feature set, but I expect that over the next 3-5 years DynamoDB will be 70% of features existing noSQL databases have today, and that's what 99% of folks ever need.