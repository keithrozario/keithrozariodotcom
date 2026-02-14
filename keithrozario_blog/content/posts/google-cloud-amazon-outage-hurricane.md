+++
title = "When Lightning strikes the Cloud: Amazon Outage"
slug = "google-cloud-amazon-outage-hurricane"
date = "2012-07-12T04:00:43"
draft = false
tags = ['Amazon', 'Google', 'Heroku', 'Instagram', 'Netflix']
categories = ['Cloud Computing']
+++

<a href="/uploads/Lightning_Hits_The_Cloud.jpg">![](/uploads/Lightning_Hits_The_Cloud-300x246.jpg "Lightning_Hits_The_Cloud")</a>Google recently announced their Amazon EC2 killer, the <a title="Google Compute Engine" href="http://cloud.google.com/pricing/compute-engine.html" target="_blank">Google Compute Engine </a>or GCE. Google wasn't messing around and went straight for the Amazon jugular releasing 4 instance types all of which appear cheaper than their Amazon counterparts. That being said the price comparison was done solely on the basis on a on-demand Amazon instance types--Amazons most expensive prices, if you compare for the Reserved instances, then prices become more competitive.

It's exciting to finally see a Juggernaut big enough to take on Amazon in terms of price and scale. This is all around good news for everyone, especially since <a title="Cisco: Exposing the Cloud Value Chain" href="http://www.cisco.com/web/about/ac79/docs/sp/Cloud-Value-Chain-ExposedL.pdf" target="_blank">this report from Cisco</a> estimates that revenues from IaaS providers are not only high right now, but will continue to grow over the next 5 years. There's a lot of room at the IaaS space, and Google just wants to wet their beak here as well.

So it must have come as a pleasant surprise to Google when they heard<a title="Amazon Cloud Outage over storm" href="http://www.theregister.co.uk/2012/06/30/amazon_cloud_storm_outage/" target="_blank"> 'hurricane-like' thunderstorms ripped across the US east coast taking down power to 3.5 million--and the Amazon East Data center as well</a>. I was personally affected by this phenomena when <a title="Watch Netflix, Hulu and even Euro2012 online from Malaysia" href="http://www.keithrozario.com/2012/06/watch-netflix-hulu-bbc-spotify-malaysia.html" target="_blank">my access to Netflix </a>was abruptly halted, as you can imagine I <strong>wasn't</strong> a happy camper.<!--more-->

The <a title="Amazon Storm Outage" href="http://www.theregister.co.uk/2012/06/30/amazon_cloud_storm_outage/" target="_blank">Guardian UK</a> reported that:
<blockquote>According to the <a href="http://status.aws.amazon.com/" target="new">AWS Service Health Dashboard</a>, the Elastic Compute Cloud (EC2) compute cloud started having connectivity issues at 8:21 PM Pacific on Friday, <strong>June 29, and by 8:40 PM</strong>, Amazon said it had "a large number of instances in a single availability zone" had lost power due to the storms....By <strong>10:25 AM Pacific on June 30</strong>, Amazon said that the majority of the affected EC2 instances that did not have impaired EBS disk volumes were recovered, but it was still recovering EBS volumes for some customers; load balancing was restored and working normally.</blockquote>
That's more than 12 hours in downtime, The brilliant <a title="GigaOM: Amazon Outage" href="http://bostonglobe.com/business/other/2012/07/01/amazon-cloud-outage-disrupts-netflix-other-businesses/zagOmh7SEgtU9QQAS0eqfK/story.html" target="_blank">GigaOM rubbed a bit more salt </a>in Amazons wounds by saying:
<blockquote> but Joyent, an Amazon rival, also hosts cloud services from an <a href="http://joyeur.com/2012/02/24/joyent-cloud-going-east/">Ashburn, Virg. data center</a> and experienced no outage, something its marketing people were quick to point out.</blockquote>
Overall, not so good news for Amazon.
<h2>What a downtime means</h2>
The price of an outage, far exceeds the price you would pay for the service itself. I pay Rm150 a month for my broadband connection, the cost of having an internet downtime in my home is <strong>far higher</strong> than Rm150 a month, in fact it would be more than 10 times that amount.

The cost of these outages are usually quite significant even though they last just 12 hours. People aren't just complaining because there was an outage, there were real significant financial implications of the outage, and that's why companies are upset.
<h2>Why only Netflix, Instagram and Heroku</h2>
Amazon is conquering the world in terms of IaaS, so they don't just have Netflix, Instagram and Heroku, they have other services as well. These 'other' services include Spotify, Fox, Unilever and about 187 more government agencies, how come they didn't go the way of Netflix?

It could be that other services utilized data centers that were not affected, Amazon has 3 data center locations in the US and only one of them was affected.

Then of course the question becomes how come these services weren't spread out across all 3 data centers, to minimize the impact of the outage? Isn't that what cloud providers have promised all along, high scalable and flexible infrastructure, how come Netflix didn't have redundancy servers operating in the US west coast to cope with the Amazon outage? I'm not that good of an architect to comment, but I guess the sheer complexity of that approach would be quite prohibitive both in terms of execution effort and cost.

This outage has led to a soul-searching of sorts for not just Amazon but all other IaaS providers, smaller providers like Joyent, Softlayer and rackspace as well as the new big boy in town -- Google. Outages are beginning to be unacceptable.
<h2>What's the solution?</h2>
While outages may be unacceptable, they are in most cases unavoidable.

My first exposure to the 'cloud' was an Amazon presentation at my company, and I fell in love at first sight. The analogy that was given then, was the cloud would enable you to treat IT infrastructure like metered-electricity, pay for what you use and scale when you need it--instantly. The utility company would take care of the rest, in the real life electricity example the utility company would be Tenaga Nasional, in a cloud model that utility company would be Amazon.

Just like Tenaga though, Amazon will suffer their outages. No one can fully expect 100% uptime even for something like electricity or water. You can't expect one provider to give you 100% uptime.

While the cloud does help simplify your IT operations a bit, it doesn't free you up completely from thinking about backing up your infrastructure in case of an act of God. Getting your infrastructure from Amazon may be a good idea, but unless you couple that with redundancy operations and backups, you might find yourself on the wrong end of another outage.