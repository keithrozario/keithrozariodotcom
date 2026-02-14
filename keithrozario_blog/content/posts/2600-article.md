+++
title = "2600 article"
slug = "2600-article"
date = "2016-08-01T08:00:39"
draft = false
categories = ['Misc']
+++

*A republication of my article on 2600, a hacker magazine*

Greetings from Malaysia.

This is my first time writing to 2600, although I've been a kindle subscriber for more than 2 years now.

For my first article, I hoped to write about a little hacking expedition I embarked on a couple of months back to help me improve my coding skills as well as help me learn more about local internet users.

Malaysia got onto the internet scene much later than most developed countries, our first ISP was only founded in 1992, and even then it was pretty much exclusively dial-up. Soon the local telecom company, Telekom Malaysia (TM) got into the ISP business and basically killed every other player because as the incumbent Government-owned telecommunications company, it alone had access to the phone lines of every Malaysian household.Until very recently, phone lines in Malaysia were owned by the Federal government through Telekom Malaysia, and it was only in the late 90's that a privatisation plan opened that up.

During the days of dial-up over PSTN, and even after ADSL connectivity (which still ran over PSTN lines), TM held a monopoly over all internet subscribers in the country, simply because it owned the phone lines. Other ISPs struggled to penetrate the market, because their offerings couldn't compete with the scale and unfair advantage of TM.

Fortunately, that all changed when TM was laying down fiber-optic cables. As part of a deal, TM secured a government subsidy to fund the fibre infrastructure but was forced to allow other ISPs to utilize the last-mile. In theory this would have increased competition and provided a more level playing field--which it did. But, TM was slow in opening up the last-mile, and manage to get a head-start of around 400,000 subscribers before any other ISP began to offer a Fiber to Home internet connection.

Why am I telling you this?

Because TM doesn't really prioritize security, and I discovered a near perfect storm of security lapses that may prove costly to TM at some point.

As a 'legacy' ISP in the country, TM was around when IP addresses were cheap, and IPv4 exhaustion was a prediction not a reality. Hence it managed to secure for itself nearly 2.5 Million IP addresses from IANA. This abundance of IP addresses meant that TM offers all its customers a public facing internet IP by default, something all other ISPs in Malaysia offer only on request of the subscriber. I won't go into the details of NAT-ing here, but you can Google it if you're interested.

Secondly, as part of a Fibre subscription, TM provide a Modem and WiFi router, which is nothing out of the ordinary, except that TM sourced all their routers from just 2 manufacturers, and each manufacturer provided only 1 router model. From a security stand-point having an entire population of a single device isn't a good thing, because a single exploit could take them all out at once, akin to the super-viruses we hear about that could make entire crops extinct because there's so little genetic biodiversity in industrial agriculture.

Thirdly, TM provide a TV box for free and paid channels streamed to your TV. Problem is, that the TV box requires a complex VLAN segmentation and setup on the router, meaning most routers won't support the TM Fiber offering. This forced most (or all) TM subscribers to continue using whatever router TM provided them in the first place, without the ability to swap the router for a more secure or feature rich one.

All in all, this meant that all of TM's 600,000 fibre subscribers (at the time of writing this) were connected directly to the internet via a Public IP, and most of them continued to use one of the two routers supplied by them.

So far, nothing too exceptional here, except for two last bits. All the routers were configured to allow access from the WAN interface (i.e. you could configure the router from the internet), and all the routers were setup with one of a 5 different username/password combination by default. The default passwords (as you may have guessed) were rarely changed, and most users were left completely vulnerable to attack on a device they never even considered would be a target.

In 2007, while the fiber offering was still very new, several hackers in the Malaysia alerted TM to the 'flaw' in their operating model, but TM maintained that the WAN interface was necessary for 'maintenance and support', although they did promise to change all passwords to a unique password per router.So here we are in 2015, and I wanted to see just how honest TM were in keeping that promise.

First I had to get the list of IP addresses that belong to TM, a quick Google search revealed that TM was AS4788. AS stands for Autonomous System, a sort of internal network within the internet and used primarily for BGP routing. BGP is the border gateway protocol, which defines how IP packets are routed between AS nodes, and the great thing about it is that all this information is public, meaning you can easily determine TM's IP addresses.

Once I had the list of IP addresses I quickly created a python script to loop through each individual IP, and determine the http-header of the end device on that IP (if there was one in the first place). I queried only port 8080, to save time. Since TM had only 2 router models, it was pretty trivial to validate the http-header and see if the IP was hosting a vulnerable TM router. A more professional approach would be to use zmap, or Shodan, but creating your own scripts to do this has it's advantages in learning.

IP scanning was easy, and determining if indeed a particular router was on port 808o of a specific IP address wasn't a tall hurdle to cross. The much harder portion was to actually test the hypothesis that most of the routers still used the default usernames and passwords. This meant I had to actually post data via http into the page from my python script. This isn't usually a difficult task, but the routers themselves operated a large amount of javascript, and that just threw my python scripts into a tail-spin.

Try as I might, I couldn't get it working using just python. Eventually I gave up trying to navigate the routers homepage, but then I found Selenium.

Selenium is a tool that allows you to "create robust, browser-based regression automation suites and tests", in otherwords Selenium allows you to control a browser like FireFox or Chrome from a python script. This was the holy grail, because the web-browser would take care of all the Javascript nastiness for me, and now I could go deeper into the router configuration settings and poke around to determine other things, like do people even bother to change their WiFi SSID and password?

But Selenium has a performance drawback, a single python script querying a webpage, takes a couple MB of RAM, but a entire instance of Firefox kept open could consume a a few hundred megabytes, which severely limited my ability to scale the scanning. Even after discovering the tool, I tried to go back to just native python, but that Javascript stuff just threw me off.

Eventually, I wrote a whole script in Python, that would scan an IP range, determine if a router was present at the end of the IP (on port 8080), and then pass that to another script that would use Selenium to interact with a Firefox browser to visit the routers webpage, try the handful of default username/passwords and determine if any of them worked. And they DID!!

Of course, while I was in, I poked around to determine things like WiFi SSIDs, etc, but mostly for fun, and I made it a point not to change any setting on the router.

But there's no way I could scale all of this on my home PC, or even my laptop. So, I decided to host this on the cloud, and chose to use Amazon--specifically a Windows instance on Amazon.

Initially, I decided to host this in Singapore--made sense since I was visiting Malaysians IPs, but then I realized that the Oregon data center of Amazon had much cheaper rates than the Singapore one--so I changed my decision and hosted in Oregon instead. IN some cases this was a 20% reduction in cost, and the expense of 'slightly' more latency, but my application wasn't latency sensitive, as much as I was price-sensitive :)

Then in true, cheap-skate fashion, I decided to toy with Amazon spot instances--this a special deal from Amazon, where they would lease you un-utilized machines to the highest bidder, and you can get this for nearly 50% the price of the 'on-demand' Amazon instance. The only down-side is that Amazon reserves the right to terminate your instance at anytime--but from my experience of using this, and from the blogs I read, the chances of that happening were pretty slim.

I've run nearly 10 of these so far, and every time I spin up a spot-instance, it's never been auto-terminated. Pretty decent deal--the only real down-side is that a spot-instance usually takes about 3-5 minutes to launch, due to the bid processing. But other than that it's as good as a on-demand instance :)

With a very powerful Amazon instance, that had a large amount of RAM, I could spin up a large number of instances of Firefox to do my bidding. Using a simple Database to ensure all the instances weren't visiting the same IP addresses, I was able to automate the whole process of 'visiting' TM routers with ease.

Eventually, a single large Amazon instance (procured through a spot-instance method), was able to hack through 10,000 routers in less than 12 hours for under $10.00. Quite a good return of investment if you're looking to create your own little bot-net army.

TM have especially dropped the ball here, they now have at least 10,000 vulnerable routers floating on their network, waiting to be owned by the next Lizard Squad characters. I could have easily configured my script to turn-off the WAN interface on the router, to limit people's exposure, but I thought against making changes on a host system without the owners explicit permission.

Hopefully if you're from Malaysia and a TM subscriber, now you know, and you're that yourself.

Selamat Tinggal from Malaysia.