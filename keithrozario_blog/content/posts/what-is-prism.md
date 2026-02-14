+++
title = "What is PRISM?"
date = "2013-06-17T08:00:08"
draft = false
categories = ['Copyright and Censorship', 'CyberLaw', "Keith's Favorite Post", 'Security &amp; Privacy']
+++

<a href="/uploads/images3.jpg"><img class="size-full wp-image-3685 alignleft" style="margin-right: 15px; margin-bottom: 10px;" alt="Prism controversy" src="/uploads/images3.jpg" width="275" height="183" /></a>There's a controversy brewing in the land of the free, one that will have implications for Americans, but also Malaysians and nearly every citizen of the world. We may look back at the moment Mr. Snowden leaked controversial (and ugly) slides about a program called 'PRISM' as the start of a pivotal moment in internet history, a moment where we either begun a massive campaign to prevent illegal and unethical government wiretaps or a moment where we let governments turn the internet into a police state.
<h2>So let's recap what happened.</h2>
First, the Guardian newspaper broke a story on how the US Government had 'direct' access to the servers of the tech giants of the Silicon valley including Google, Youtube, Yahoo, Apple and Facebook. In short, the report claimed US Government had direct access to the emails, personal details and chat sessions of everything stored on in massive datacenters of the social networks that the tech giants ran.

There isn't a person I know that doesn't have either an iPad, Facebook account or Gmail address. Even my dad who vehemently refused to have a Facebook account, eventually succumbed to the social pressure but that was much after I setup his company email with Google Apps. So to say that the US Government had access to private details of nearly every single person in the world is not a stretch.
<h2>So what is PRISM really?</h2>
The theory is that US government officials, specifically from the National Security Agency(NSA) have direct access to the servers of 9 Tech giants. Details are scarce and denials abound....what<strong> isn't</strong> debated is that the NSA has some sort of access to the server, even though the likes of Google and Facebook have repeatedly denied that they have created a backdoor.

So is it possible that the NSA has a backdoor to Google without Google knowing about it? Turns out it's not as far-fetched as it seems.

Steve Gibson, a security guru with his own show on TwitTv seems to think so. He's put together some high level analysis of the story, taking into account other similar stories and suggest that the NSA has a wire-tap on the entire world. A communications intercept targeting the likes of Google and Facebook, but one that the tech companies could be blissfully ignorant of. A wiretap strategically placed at the front door of Google, Facebook, Microsoft and Apple--that collects and stores every data packet passing into and out of their servers.

<em>But communications intercepts don't work--because the data is usually encrypted...isn't it?</em>

In most parts the communications that people like you and me use to connect to Google is encrypted, and we're secure in the knowledge that our data in transit is protected from prying eyes by a minimum 128-bit encryption--that's encryption that probably won't be broken for another 20 years.

But not all data flowing into and out of Google is encrypted, some of it flows in plaintext--ripe for any wiretap to pick up. Just like email.<!--more-->
<h2>...Yes even email</h2>
While your connection to Gmail is secured from prying eyes, the moment you hit the 'send' button, that email itself leaves Google servers un-encrypted. Email is a remnant of the internet past,from a time when encryption wasn't a necessity, and the protocols that email runs on hasn't change in long time. So while you're typing your email on a secure connection with Gmail--the email leaving Google servers to its destination at some other server--appears in plain sight for any wiretap to pick up on--and that's what Steve Gibson suggest the NSA were doing. Picking up on email in plain text flowing through public networks.

It's these sorts of data leakages, that the NSA were hoping to pick up and store in their Zetabyte level database. As John Oliver explained--a Zetabyte is what gave Michael Douglas throat cancer. <em>(it's a lame joke, but give it a minute and you'll get it)</em>.

Seriously though, a Zetabyte is 1 Billion Terabytes. Which means, that if the NSA were targeting a Billion people, it could have 1 Terabyte of information per person. That's more information per person, than I have on myself!!

This is in addition to the amount of metadata the NSA could be picking up on. That's probably the current scenario, the final end-state of PRISM is even scarier.
<h2>...Breaking all that encryption</h2>
The NSA clearly state on their webpage that their hope is to use the massive <a title="Utah data center to break AES-256" href="http://nsa.gov1.info/utah-data-center/" target="_blank">Utah Data Centre to break AES-256</a>. That's probably the most ubiquitous encryption protocol out there. That's considered far more secure today, than the encryption you use for your Maybank2u or CIMBClicks, or even Google (which uses just 128-bit). So it's not really a stretch to think that the NSA could be tapping encrypted data, and storing it for future decryption. Now that's a scary thought.

[box icon="chat"]In 2004, the NSA launched a plan to use the <a href="http://www.ornl.gov/info/ornlreview/v39_1_06/article14.shtml" target="_blank">Multiprogram Research Facility</a> in Oak Ridge, Tennessee to build a classified supercomputer designed specifically for cryptanalysis targeting the AES algorithm. Recently, our classified NSA Oak Ridge facility made a stunning breakthrough that is leading us on a path towards building the first exaflop machine (1 quintillion instructions per second) by 2018. This will give us the capability to break the AES encryption key within an actionable time period and allow us to read and process stored encrypted domestic data as well as foreign diplomatic and military communications.  </blockquote>

While this all sounds paranoid, the storage levels of the data center only make sense when you put it in conjunction with this. That the NSA is hoping to scan and save all the traffic routed to Google and Facebook for future use, because it were only hoping to use it today, they'd never need that sort of storage capacity.
<h2>...Should we be worried?</h2>
Yes. The biggest conversation in the US is purely around US Citizens, but 80% of the users of services from Google, Facebook and Apple--originate from outside the US. So it's not a stretch to say that the NSA is compiling a huge amount of data of every Malaysian Citizen on these services. Google by the way owns Blogspot, which is where a lot of our local bloggers choose to ply their trade.
<h2>...What can we do?</h2>
The reason I felt I needed to write this post is simply the amount of mis-information out there. So regardless of whether Steve Gibson's wiretap theory is correct or whether the NSA really have 'direct' access to the servers--the bottom line is that as long as you use these services, you could be spied on.

Nothing you do, on TOR or subscribing to a VPN or proxy is going to help here. The encryption and anonymity tools you use only serve to protect your connection, if Google opens a backdoor to the NSA--none of these tools would help.
<h2>Conclusion</h2>
The European Union is watching the story pretty closely, and are contemplating action, should the privacy rights of EU citizens be under threat. The EU has one of the toughest data privacy laws in the world, and having a foreign government snoop on their citizens private lives is not something they look kindly to.

Malaysia on the other hand has the PDPA, but it's unlikely the Malaysian government would ever do anything--considering that the government itself is accused of spying on it's own citizens.

#Slide-deck

Here's a quick slide deck I put together to explain Steve Gibsons theory on the NSA wiretap:

<center><iframe style="border: 1px solid #CCC; border-width: 1px 1px 0; margin-bottom: 5px;" src="http://www.slideshare.net/slideshow/embed_code/22979770" height="458" width="550" allowfullscreen="" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe></center>
<div style="margin-bottom: 20px;"></div>
And here's the best youtube video explaining the PRISM scandal in detail and humor from John Oliver (Jon Stewarts replacement on the Daily show)...forward to 1:1o to get to the PRISM part.

<center><iframe src="https://www.youtube.com/embed/tilfgWzhsns" height="315" width="420" allowfullscreen="" frameborder="0"></iframe></center>