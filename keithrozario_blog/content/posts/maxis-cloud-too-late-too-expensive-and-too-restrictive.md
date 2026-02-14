+++
title = "Maxis Cloud : Too Late, Too expensive and Too Restrictive"
slug = "maxis-cloud-too-late-too-expensive-and-too-restrictive"
date = "2012-03-21T15:51:01"
draft = false
tags = ['Amazon', 'Cloud', 'Maxis', 'rackspace']
categories = ['Cloud Computing']
+++



![](/uploads/Welcome-To-The-Cloud-300x150.png "Welcome To The Cloud")

Maxis recently launched their new IaaS offering in the form called the Maxis Cloud. According to <a title="Lowyat.net Maxis Cloud" href="http://www.lowyat.net/v2/index.php?option=com_content&amp;task=view&amp;id=5075&amp;Itemid=2" target="_blank">Lowyat.net</a> the Maxis Cloud is said to be the " <em><strong>the most advanced</strong> on-demand, real-time, fully managed cloud service <strong>in Malaysia</strong>, Maxis Cloud allows businesses to scale their cloud computing infrastructure according to their needs at any time through its self-service portal</em>."

That's basically calling yourself Jaguh Kampung. Pardon the sarcasm, but the Maxis Cloud does seem a tad bit expensive for a such a late entry into the game. You'd expect new IaaS providers that show up this late in the cloud game throw everything including the kitchen sink to get new subscribers. That however, has been lacking and a marketing strategy that seems more intent on selling IaaS to non-believers as oppose to selling the Maxis Cloud itself isn't helping their case.

I'd loved to be rooting for Maxis, but most of it's offerings just don't add up, and there's a whole bunch of questions about it's <strong>bandwidth charges, support availability and API specifications</strong> that <strong>aren't clear</strong> enough to me to make any sort of comparison or even recommendation. Plus the fact that its self service portal had a 'technical issue' when I logged on didn't really bode well for my experience.

That being said, while analyzing I noticed that there is one thing Maxis could offer that could tilt the tables in its favor, Maxis is a communications company after all (unlike Amazon or Rackspace) and I think there just might be a chance it could offer something niche that would make it stand out. But first, let's take a look at some key concepts:<!--more-->
<h2>Infrastructure as a Service</h2>
First off, let's do a quick recap on what IaaS is, Infrastructure as a Service is a Cloud Offering that offers the IT infrastructure a real-time on demand commodity. So think of it as buying computing power on the fly, instead of buying physical hardware (which is essentially expensive Capex), you could buy virtual instances and pay per unit time of usage (Opex).

If you'd like to know more about Infrastructure as a Service, here's a post I wrote some time back explaining the <a title="IaaS vs. PaaS vs. SaaS: What do they mean?" href="http://www.keithrozario.com/2011/11/iaas-vs-paas-vs-saas.html">differences between IaaS, PaaS and SaaS</a>.

The important difference is that IaaS offers just the infrastructure, so that's computing power and network connectivity, you'd have to install your own applications to make use of the Infrastructure. This is opposed to SaaS which is a fully featured end user ready applications on the cloud.

In IaaS, you'd buy computing power and install your own email server and application (Microsoft Exchange).

In SaaS, you'd just subscribe to Google Apps and you'd have your own email ready to use.
<h2>Maxis Offering</h2>
So Maxis has decided it wants to become a IaaS provider, which is strange considering it's a telco company. I always had a feeling that telco companies would gain the most from cloud computing, but in an indirect way. A few months back I wrote about how I thought <a title="Cloud investment: Is Cisco the next big thing?" href="http://www.keithrozario.com/2011/12/investing-in-the-cloud.html">Cisco would be the biggest winner </a>when everything moves to the cloud, since cloud computing invariably puts a strain on networks which in turn require Cisco products to run.

That being said, Maxis is taking the head-on route in actually delivering a IaaS offering, putting it on a collision course with IaaS heavyweight Amazon and IaaS contender rackspace. Spending Rm7 million on it's data center in Shah Alam, Maxis hopes it's offering and Malaysian specific network would give it an edge , especially in the local market.

So what does Maxis Offer?
<h2>Machine Types and OS</h2>
For starters it offers just<strong> 3 machine types, Value, Power and Optimum</strong>, corresponding to 3 distinct machines from the 4GB of RAM and 30GB of HDD on the lowest end of the spectrum to 16GB or RAM and 160GB of HDD on the highest end of the spectrum.

All machine types run on Windows 2008 R2 64bit, and have a 'claimed' bandwidth of 100Mbps. (why that matters when most offices don't run anywhere near that is beyond me).

So let's recap, just 3 machine types on 1 single OS. Compare that to <a title="Amazon instance types" href="http://aws.amazon.com/ec2/instance-types/" target="_blank">Amazon</a> which has at least 10 machine types (12 if you include cluster computes) and <a title="rackspace instance types" href="http://www.rackspace.com/cloud/cloud_hosting_products/servers/pricing/" target="_blank">rackspace</a> which has 8 machine types. Both Amazon and rackspace also offer both Linux and Windows offering (with Linux offering costing lower).
<h2>Price</h2>
The Value Pack from Maxis offers you a 1CPU machine with 4GB of RAM and 30GB of HDD at Rm900/month. Now although the press release and wording in some of the statements seem to suggest otherwise, the actual black and white pricing on the Maxis website <strong>suggest it's going to be a monthly billing.</strong> That's pretty lame.

The highest end machine from Maxis operates with 2 CPUs, 16GB of RAM and 160GB of HDD for a whopping Rm1900/month. That's a lot of moolah.

In terms of comparison to Amazon and rackspace, I thought I'd leave that for later in the article.
<h2>Support and Bandwidth</h2>
I've been scouring online and can't find much more details about the Maxis Cloud in terms of it's support and Bandwidth. I'd be very interested to know if it's a 24x7x365 support and what kind of SLAs we're looking at, it'll also be interesting to see what charges (if any) Maxis would be charging you for outward data flow.

Now Maxis is a telco company, and it could possibly be that for all 'local' customers you could see unlimited outward bandwidth. That could be a game changer, particularly since Amazon and rackspace charge USD0.19 and USD0.18 per GB of outward data traffic respectively. That's a lot of cash in data traffic and something we'll see in the head to head comparisons later on.

That being said, it's a rather silly marketing tactic to keep that secret, considering that's the differentiation that Maxis needs to compete with Amazon and rackspace.
<h2>Performance</h2>
Maxis is pretty new at this, and I won't be surprise if their performance isn't as great as they claim it to be. That being said, the portal did mention some 'technical' issue barely a week from their launch.

It's also good to keep in mind that Amazon has had its problems as well, and too be fair we can't criticize Maxis here till everything pans out.
<h2>Maxis Cloud API</h2>
Is there even an API? I can't seem to locate any information on any API for the Maxis Cloud. Once again a lack of information is hurting Maxis adoption rates.
<h2>Comparison : Maxis Cloud vs. AWS vs. rackspace</h2>
So let's do a little comparison, If we compare the Maxis Value Cloud offering against something similar from Amazon (the small instance), and rackspace (the 1GB RAM 40GB Disk instance) it really doesn't look good for Maxis from a price perspective:



![](/uploads/Low-End-Comparison.jpg "Low End Comparison")



Not only is the Maxis instance the one with the lowest HDD space, it also is the most expensive by a long mile. I know what you're thinking though, Maxis has 4GB of RAM while the rest have just 2GB. That's true, but at this low end of the computing spectrum I'm not sure what you need 4GB of RAM for, especially when you have just 30GB of storage space. So to make things fair, I looked up the 4GB instances for Amazon and rackspace as well:



![](/uploads/Low-End-4GB.jpg "Low End 4GB")



Now things get really out of hand, once we streamline the RAM, we see that the HDD space starts to fluctuate. Maxis offering is still the most expensive, but not by much. This time however,  it's got 5 times LESS storage than rackspace and about 14 times less than Amazon.

Of course, you have to take into account that both Amazon and rackspace charge for outgoing traffic per GB, while it's unclear (at least to me) if Maxis would give this for free.

If we take a look at the Medium range offerings we get:



![](/uploads/Mid-Range.jpg "Mid Range")



And then looking into the highest range offering:



![](/uploads/High-End.jpg "High End")



I realize that this isn't the best way to compare the cloud providers, a more relevant question would be<strong> what can RM900/month buy me for the 3 providers.</strong> That question at least sets a standard to compare as oppose to CPU and RAM and HDD space.
<h2>What Can I get from Amazon and Rackspace for Rm900/Month?</h2>
So what does RM900/month buy you with Amazon:



![](/uploads/900monthAmazon.jpg "900monthAmazon")



Of course this comes with Silver Package support, if you're willing to forgo support you can save yourself a cool USD100 (or 33% of the package cost) or bump yourself up for a LOT more bandwidth or even a more powerful machine.

Next up rackspace at Rm900/month gets you:



![](/uploads/900monthrackspace.jpg "900monthrackspace")



rackspace offers their trademark 'fanatical' support for all packages, and when you take that into account their prices don't differ significantly from Amazons.

Of course what you really want to see is all these Rm900/month packages lined up against each other, and I don't dissapoint:



![](/uploads/Rm900Comparison.jpg "Rm900Comparison")



From just the high level you can see that Maxis storage is way too low in comparison to both rackspace and Amazon, that could be on purpose to set Maxis apart, but giving me so much RAM on just one CPU with just 30GB of HDD isn't something I'm particularly fond of. Even if it was unlimited bandwidth, how much could I possibly use on an instance with just 30GB?

If you're hoping for me to recommend something, I can't. It depends on what you need the cloud infrastructure for, that being said Maxis offering the Value pack as "Ideal for hosting email servers" is <strong>bloody ridiculous</strong> if you ask me. Who in their right mind host an email server Rm900/month on a machine with just 30GB of storage?

You can get 25GB per user on Gmail, for just USD25/year. That doesn't require OS level support, cloud support and probably has a much higher uptime then anything a company can host on it's own. For email servers people should think SaaS rather than IaaS. <strong>The guys over at Maxis need to rework their marketing of the Maxis Cloud.</strong>

Next let's look at something similar to pit against the high end Maxis offering at the RM1900/month range:



![](/uploads/1900comparison.jpg "1900comparison")



Here is where I think if Maxis has a unlimited bandwidth it could compete. If you're wondering why I haven't upgraded the support for AWS the reason is that AWS Gold cost too much at a budget of just RM1900/month. Rackspace however can offer Managed Service Level which would give it's Medium offering the best support in its class.

It's also important to note, that rackspace fanatical support is comparable to Amazon Silver (or even Gold), and it comes free. Amazon support on the hand increases as you increase your usage. For more info on comparison between Amazon and rackspace <a title="Rackspace vs. Amazon" href="http://www.rackspace.com/cloud/cloud_hosting_products/servers/compare/" target="_blank">check this out</a>.

However, if you look at it, even on the AWS Large instance with 2TB of bandwidth, that's just 2.5 times the storage space which may not be enough. If Maxis plays its cards right and offers unlimited bandwidth, some might be tempted to subscribe and I wouldn't blame them.
<h2>Maxis Marketing</h2>
I think I also need to mention a few words about Maxis marketing strategy here. I'm not a marketer, but I work in IT and I know what IT guys look for. Unfortunately, I couldn't find it in Maxis messages.

If you head on over to their website, you see a whole bunch of stuff talking about the benefits of IaaS. I know IaaS, I want to know what sets the Maxis IaaS apart from Amazon and rackspace. Judging from the offering, the lack of clarity in the details (support and bandwidth are big questions left unanswered) and just the overall feeling of the campaign makes everything feel a bit <strong>'amateur-ish'</strong>.

If I was a new IaaS provider, I'd make sure you know what sets me apart from Amazon and rackspace.

If I was a new IaaS provider, I'd worry less about IaaS and more about your specific needs as a customer.

If I was a new IaaS provider, I'd make sure you knew exactly what I offered in terms of <strong>support and bandwidth. </strong>

If Maxis offered <strong>free bandwidth</strong>, that's the game changer,<strong> that should be upfront and center. </strong>If it doesn't offer free bandwidth, then it needs to stipulate the fees related to it. it's that simple and Maxis fumbled this up.

I'd make sure you knew how my console looked like, what you could do, how you could do it. <strong>My API specification, and if I didn't have one, when I plan to release one</strong>.<em> (if Maxis doesn't have an API, it can just kiss it's Maxis Cloud goodbye). </em>

I'd make sure you knew my <strong>technical roadmap</strong> and how that could fit your organizations future landscape. Amazon goes one up and has developer resources and forums to assist.

I'd make sure I answered every damn question you had in a serious looking website. (What about PCI compliance?)

Maxis really flunked this out, I don't know any of this. Either the information is in some obscure place or they expect me to call their customer service to find out. C'mon guys, you're a communications company.
<h2>Conclusion</h2>
So in conclusion, while it's definitely early days for any of this to be recommended, I'd say hold on a bit before switching to Maxis. If you absolutely need an IaaS provider, head on over to Amazon or rackspace.

I really can't recommend Maxis based on the information I have. In fact, anything short of unlimited bandwidth at this point would force me to say , forget Maxis completely.
<h2>What happens when I tried to contact Maxis?</h2>
I logged onto the Maxis portal today and tried to fill up a form inquiring on the support and bandwidth charges, the form also mentioned I could get one month free of Maxis Cloud....but when I filled it up:



![](/uploads/Runtime-Error-1024x383.png "Runtime Error")



Now that really doesn't bode well for Maxis.