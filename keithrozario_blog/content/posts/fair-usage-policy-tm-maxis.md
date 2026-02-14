+++
title = "Maxis and TM Fair Usage Policies : Are they fair?"
slug = "fair-usage-policy-tm-maxis"
date = "2013-06-24T08:00:31"
draft = false
tags = ['Fair Usage', 'Maxis', 'Unifi']
categories = ['Copyright and Censorship', 'Malaysia']
+++

<p style="text-align: center;">![Fixed Access in asia](/uploads/Fixed_access_Asia.png)</p>
Every six months, the great people over at Sandvine release their Global Internet Phenomenon report, which seeks to make sense of global internet traffic across the different regions of the world, and every six months I learn a lot from just gleaning through it. For instance most of the traffic in the US continues to point to just one website--Netflix, which also explains the drop in bitTorrent traffic in the US<span style="color: #c0c0c0;"><em> (why bother downloading anything when you can stream)</em></span>. However, in Malaysia, where it's difficult <a title="Watch Netflix, Hulu and even Euro2012 online from Malaysia" href="http://www.keithrozario.com/2012/06/watch-netflix-hulu-bbc-spotify-malaysia.html">(but not impossible) to get a Netflix account</a>, most of the traffic for both upstream and downstream still uses the bitTorrent protocol--which mostly means there's still a lot of illegal downloading going on in these here parts--but you can't blame us, because the alternative isn't legal downloading, it's buying a DVD--if you can find the DVD you want in the first place.
You can view the report in it's entirety <a title="Sandvine Global Internet Phenomenon report" href="http://www.sandvine.com/downloads/documents/Phenomena_1H_2013/Sandvine_Global_Internet_Phenomena_Report_1H_2013.pdf" target="_blank">here</a>, but I just wanted to point out one cool fact.
<h2><strong>The average monthly traffic in Asia-Pacific has dropped.</strong></h2>
Just 12 months ago the average monthly consumption was 32.2GB, now it's at 22.oGB. That's a significant drop in traffic, that which really boggles the mind. This is the growth region of the world--why is our average monthly consumption of the 'internet' decreasing. Put another way, why are Asians using less internet?

I suspect the average monthly consumption has dropped because of the growth in Asia Pacific, it's quite counter-intuitive, but as Asia Pacific adds more users to the internet, the newer users in the more rural parts of the region aren't downloading as much as their urban cousins. Therefore, while the overall traffic flow has increased, the <strong>average</strong> monthly consumption per account has reduced. It's all conjecture at this point--but that's what I think based on just this one data point. It makes sense to me, as a lot of people aren't torrent-crazy-downloaders, which just means that they aren't consuming anywhere near the full amount.

The Median monthly consumption is just 8.8GB, while the Mean monthly consumption was 22.0GB, and that tells me that the data is skewed--highly skewed. The statistician inside me is just crying to get out and shout--SKEWED!!

Skewed is just another way of saying that the distribution of internet consumption is un-evenly distributed across--or in more laymens terms--a few internet users are using the vast majority of the bandwidth.<!--more-->
<h2>Fair Usage Policy for TM and Maxis</h2>
While half of all users in the region use under 8.8GB a month, there exist a small population of 'power' users that consume a significant portion of the traffic, which may explain why ISPs are looking to throttle traffic. HOWEVER, before you defend your ISP, just remember that Unifi fair usage threshold (though not yet implemented) is 60GB while Maxis has a threshold of 40GB. Basically the fair usage threshold is the point at which your ISP thinks you've consumed more than your fair share, and begins to slow down your speed.

Now, it stands to reason--that since a large portion of users in the Asia-Pacific don't use anywhere near the Fair Usage Policy threshold, and these users would never hit the limits imposed by the ISP. So why then imposed a fair usage policy? After all, even when you average out the bandwidth of all your users, you don't expect anywhere near your fair usage thresholds.

The average profile of an Asia Pac user shouldn't much different from the average profile of a Malaysian user. After all, Malaysian isn't super-urban like Singapore and Hong Kong, and we're not as rural as Indonesia or Philippines. Which makes TMs decision to not throttle torrent traffic on Unifi or implement a Fair usage policy look very pragmatic indeed.

So we have a case of two major ISPs here. TM who have a Fair Usage policy on their contract, but for very good reasons don't enforce it, it's always been TMs position to test out an unfettered and unthrottled internet--introducing the Fair Usage policy only when needed--and so far they've not needed it.

Maxis on the other hand imposed it straight out of the box, and 'claim' they need it--but all the data from both Sandvine and TM suggest they don't need a fair usage policy-- provided they've allocated enough infrastructure to support 40GB per user per month. So why bother?
<h2>BitTorrent vs. Netflix</h2>
On that same note, the percentage of torrent traffic in the Asia-Pacific has also decreased year-on-year. Last year 33% of all internet traffic along fixed lines was bitTorrent traffic, now it's just 29%. Most of that shift can be directly attributed to Real-Time Entertainment which saw an increase from 42% to 46%.

The interesting thing about this is that most Real-Time Entertainment protocols use legal content--the same can't be said for bitTorrent. As I blogged last year that the best way to reduce pirated content in any region is to <a title="Reuding Pirated content Malaysia" href="http://www.keithrozario.com/2012/06/reducing-pirated-content-movies-music-malaysia.html" target="_blank">increase the availability of legal content</a>, and we're seeing some of that in Malaysia--and hopefully we begin to see more in the form of hyppTV and a Netflix here.
<h2>Conclusion</h2>
It seems that most of the global research suggest that there isn't a need to throttle internet speeds of anyone in Malaysia--not even specific protocols like bitTorrent. If the ISPs really had allocated the 'fair amount' of bandwidth per user per month, it's unlikely they'd need to go through the hassle of logging peoples traffic usage just to throttle them later.

So then why do they do it? Your guess is as good as mine.