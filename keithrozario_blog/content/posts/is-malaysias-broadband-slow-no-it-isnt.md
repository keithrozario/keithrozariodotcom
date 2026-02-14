+++
title = "Is Malaysia's Broadband slow--no it isn't. "
slug = "is-malaysias-broadband-slow-no-it-isnt"
date = "2014-09-14T23:31:20"
draft = false
categories = ['CyberLaw', 'Malaysia']
+++

![Broadband_speed_klang_malaysia](/uploads/Broadband_speed_klang_malaysia.png)Recently KiniBiz did a piece on Malaysian broadband speeds, and once again the<a title="Local broadband speeds slower than Cambodia: Why it doesn’t matter" href="http://www.keithrozario.com/2014/05/malaysia-broadband-slow-cambodia-ookla.html"> hoopla about how Malaysian broadband speeds are slow</a> arose. Kinibiz quoted an article from Asean DNA which stated that the average broadband speed in Malaysia was <em>just</em> 5.5 Mbps, while Thailand, Vietnam and Singapore had speeds that were double that (or more!)

The report however was inaccurate, and I think there's a need to address the hoopla, because this happens often. There was a report couple months back that said Cambodia had faster speeds than Malaysia, and I <a title="Local broadband speeds slower than Cambodia: Why it doesn’t matter" href="http://www.keithrozario.com/2014/05/malaysia-broadband-slow-cambodia-ookla.html">wrote a post addressing that</a>. This time I think, we have to really go into the data and find out what exactly is going on.

So let's start at the source of this data.

The data was built from billions of download test conducted by users throughout the world on <a title="Speedtest" href="http://www.speedtest.net" target="_blank">speedtest.net</a> <em>(a website that allows users to test the speed of their internet connection)</em>. This dataset is HUGE!, one of the biggest I've seen and definitely the biggest I've had the pleasure to play around with. Just one file in the set had more than 33 Million rows and weighed in at more than 3.5GB.It took me some time and lots of googling just to figure out how to deal with a csv file this large. Fortunately, there's LogParser, but we'll skip that tutorial for now and focus on the juicy details of data.

The number reported by Asean DNA is wrong. The average internet speed in Malaysia isn't 5.5Mbps, it's more like 7.5Mbps.

5.5 Mbps was obtained by averaging the speed across the regions of Malaysia (Kl, Alor Setar, Klang..etc) rather than by averaging the speed across all the test conducted by Malaysian users. In short, Asean DNA placed equal emphasis on Kuala Terengganu and Kuala Lumpur, although Kuala Lumpur had 50 times more test conducted. It would be like calculating GDP per state, rather than GDP per capita. The real per capita download speed in Malaysia is 7.5Mbps, rather than 5.5Mbps (if you limit yourself to just data from 2014).

Here's the breakdown. You can download the file from netindex.com or just use an<a title="extract Malaysian speed test data" href="https://drive.google.com/file/d/0Bxr9pDWP2zrdeEhOZjNsaVNoT0k/edit?usp=sharing" target="_blank"> extract</a> I created with just the Malaysian data--it took some time to do this so leave a Thank you in the comments if you downloaded the data.

![Average-speed-internet-Malaysia](/uploads/Average-speed-internet-Malaysia.png)

<!--more-->
<h2>What's the big fuss of 7.5Mbps</h2>
But what's the big fuss, if the same methodology applied for Thailand they'd have an average of 22Mbps. Our position in the rankings wouldn't change--I hear you say.

But is our <span style="text-decoration: underline;">relative position</span> important, or is the <span style="text-decoration: underline;">absolute bandwidth</span> number all that matters?

Consider if the average speed of cars in Malaysia was 200Km/h, but the average speeds of cars in Thailand was 350Km/h--would we care? 200Km/h is fast enough to do anything, and why do we bother if the Thais like fast cars?

In essence 7.5Mbps is fast enough to do just about anything. With few notable exceptions, even with 5 Mbps you could <a title="Can you view Netflix in HD on Unifi" href="http://www.keithrozario.com/2013/08/view-netflix-hd-unifi-5mbps.html" target="_blank">watch Netflix</a>, Stream Spotify, Watch Youtube, Play Dota, surf unlimited websites and more--why would you need 10Mbps? The only real service I can think of, where you need more than 5Mbps is 4K streaming, which Netflix claims would require a minimum of 15Mbps--but how many Malaysians actually have 4K streaming--how many users in Thailand are using it on their 22Mbps connections? Not many .

It is the absolute value of the Bandwidth that matters--in truth if broadband penetration was 80% and the average Malaysian got 5.5Mbps, I would personally shine the shoes of <a title="Meet your new Ministers of Communication and Multimedia" href="http://www.keithrozario.com/2013/05/meet-your-new-ministers-of-communication-and-multimedia.html" target="_blank">Shaberry Cheek </a>himself.

But look at the data above--notice that Kuching is missing and so are towns like Miri. The average speed of users in Ipoh is just 3.2Mbps, while KL has a whooping 10Mbps, smaller towns have to make do with ADSL instead of Fibre-optics, so obviously their speeds are going to be lower.

Malaysians have enough bandwidth, what we need is broadband penetration, and while the Kinibiz article is right in that reducing price will increase penetration--it was wrong to focus on speed as the primary concern.
<h2>Why Broadband Penetration is important</h2>
Broadband penetration is somewhat mediocre in Malaysia, it's not poor, but it's not stunning either. Our penetration rates hover around the 50-60%, while Thailand's internet penetration is just over 25%, something the Kinibiz article conveniently forgot to mention. At lower penetration rates, it's easier to get high average speeds.

A good friend of mine from Sabah complains that his father's house in KK doesn't even have unifi access yet--what more the rest of Sabah (a state that's bigger than Penang, Perak and Selangor combined!). It's much harder to connect over large distances over sparse populations, and that difficulty translates to higher cost--just ask the Australians.

So the government has to step in--in the same way it steped in during the initial HSBB initiative. For a subsidy of about RM1.5 Billion (can't really remember), the government forced TM to open the last-mile to other ISPs. That's why Maxis Broadband can ride on the same fibre to your home as Unifi does--that was brilliant, and we have to give credit where credit is due.

Unfortunately, much water has flowed under the bridge since then--and there isn't much the government has done since.
<h2>A couple of last notes</h2>
Two things I wanted to clarify on the Kinibiz report before I moved onto the response from Pemandu.

The first part of the report stated that<em> "However this includes the Streamyx service which is based on copper cabling and not fibre. If this is excluded, then broadband penetration can be lot lower"</em>. This makes it seem as though Copper was inferior to fibre, and it is, but not to such a large extent as to disregard it. Streamyx provides connection speeds of up to 8Mbps and is well and truly a broadband connection.

Kinibiz also stated in the 2nd part of their report<em> "a basic 5Mbps UniFi package with a 60GB cap costs US$47 or RM149"</em>. Surely the reporter for Kinibiz should have done her homework and found out that the 60GB Fair Usage Policy was a recommendation by TM, and still hasn't been enforced. In fact, I blogged last year how <a title="Maxis and TM Fair Usage Policies : Are they fair?" href="http://www.keithrozario.com/2013/06/fair-usage-policy-tm-maxis.html">the average user in Asia-Pacific downloads less than 10GB per month</a>--so the topic of a Fair Usage policy is moot at those low numbers.
<h2>Pemandu's and MCMC's response</h2>
![SKMM](/uploads/SKMM.jpg)First a stupid question from Kinibiz which asked the MCMC chairman Mohamed Sharil why the target is <strong>only</strong> 50Mbps by 2018 when <strong>Singapore is already able to offer 1Gp</strong>s to home users.

Take a deep breath and listen to my sigh....haiiiiih!!

Let's be honest--how many Malaysian even have the infrastructure in their own home to support 1Gbps? I only recently procured a Gigabit router, and that only applies to it's wired connections. Most routers support a maximum of 300Mbps on it's WiFi network, and that's the theoretical maximum--in practice you'd get between 50-60% of that. So basically most Malaysian households have routers that can only go as fast as 150-200Mbps. Which brings us this new phenomena, the 'last-mile' people often speak of when they talk about broadband, isn't the fibre TM pulls into your home anymore--the last mile is the router you have supporting your home network, and even if TM pipes in 1Gbps to your home, if you're running some crappy network, it'll count for nothing.

The real-life speed of a Wireless-N network is around the 40-50Mbps range per device, and even discounting everything else (which is a LOT of other things), you'd need to hook up 20 wireless devices to your router before you hit 1Gbps. So Kinibiz really doesn't understand this if they start off with that question.

Fortunately, the MCMC chairman responds with a somewhat right response by saying "Not everyone feels the need for 100Mbps". That's like saying not everyone needs a Ferrari. Here's a quick breakdown, If you used 100Mbps at full speed for just 8 hours a MONTH--and you'd have downloaded enough data to fill up 3 of the largest capacity iPhones--every month.And that neglects the fact that most networks don't provide 100Mbps, and you're unlikely to get 100Mbps end-2-end for an internet connection.

Pemandu did well to point out that they're trying to move a lot of the foreign internet content to Malaysia, primarily Youtube. That's the real silver bullet here, if you can keep the traffic in Malaysia flowing in Malaysia, the cost will inevitably drop because all of that data is being routed through local players only. Of course for some unknown reason Pemandu then went on to say "We want to see more Zaloras versus Amazons, as a lot more traffic is kept locally, if that works then it becomes a positive multiplier." Well, firstly, from my quick searches, even Zalora is not hosted in Malaysia, and secondly, websites account for such a small amount of traffic so as to be inconsequential for this discussion. True you may spend a whole bunch of time on Facebook--but it doesn't take much bandwidth to load a Facebook page, watch 20 minutes of Youtube on High-Def and that probably consumes more than your monthly Facebook bandwidth.
<h2>Conclusion</h2>
So if I had to summarize this hastily written post, it'll be this.

Malaysians have enough broadband speed, what we need is penetration and moving more content locally, which will hopefully reduce prices, thereby increasing penetration is a positive feedback loop of sorts.

Finally Kinibiz need to buck up, for a website that charges people to view their content they should have at least done their homework before hand.

Click here for <a title="Why Broadband is slower and costlier in Malaysia" href="http://blog.limkitsiang.com/2014/09/11/why-broadband-is-slower-and-costlier-in-malaysia/" target="_blank">part 1</a> &amp; <a title="Lessons from South Korea" href="http://blog.limkitsiang.com/2014/09/13/lessons-from-south-korea/" target="_blank">part 2</a> of the <a title="Pemandu and MCMC answer criticism" href="http://blog.limkitsiang.com/2014/09/14/mcmc-pemandu-answer-broadband-criticisms/" target="_blank">Kinibiz</a> report, and here for the response from Pemandu (all sourced from Lim Kit Siangs blog).