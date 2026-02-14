+++
title = "Evidence Act Technological Misconceptions: A response to Rocky and Fatimah"
slug = "evidence-act-114a-technological-misconceptions"
date = "2012-08-15T12:56:16"
draft = false
categories = ['Copyright and Censorship', 'CyberLaw', "Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

<center></center>The government has finally 'relented' and now wants to 'discuss' section 114A of the Evidence act 1950. Now it's great because it proves beyond a shadow of a doubt that:

1. The internet can be used for fantastic good.

2. The general Malaysian public can make a difference in the governance of the country.

My website also had the pop-up banner, and according to Google Analytics, all 300+ people who visited yesterday were at least enlightened by it.

However, there are some misconceptions about the act, or more specifically misconceptions about the technology behind the internet. The only reason, I'm writing this post is because yesterday morning <a title="Section 114a according to Fatimah Zuhri" href="http://www.rockybru.com.my/2012/08/section-114a-according-to-fatimah-zuhri.html" target="_blank">RockyBru posted up content by a blogger named Fatimah Zuhri</a>, defending the act. Why on earth would a blogger defend the act is beyond me, but it became clear that her understanding of key internet concepts were way off the mark.

From a technological perspective, she was advocating from a point of ignorance, and Rocky whose a popular (or unpopular) blogger/journo only served to spread these misconceptions. I hope to point out how it is very difficult to pinpoint the origin of an anonymous or malicious post, and how shifting that burden to the ordinary citizen is unjustified.

So let's start with the Post which you can read <a title="Amendment to the Evidence Act 1950" href="http://fatimahzuhri.blogspot.co.uk/2012/08/amendment-to-evidence-act-1950.html" target="_blank">here</a>, although for your sake I wouldn't suggest it. Partial contents of the post is quoted in here as well.<!--more-->
<h2>Overall summary</h2>
The gist of the article is that, if you're innocent you have nothing to worry about, because in every possible scenario there is a way to prove your innocence. This of course isn't what the law was designed to do, <a title="Nazri Aziz on 114a" href="http://www.thesundaily.my/news/384887" target="_blank">a quote from Nazri Aziz, taken from an article in the Sun reports</a>:

[box icon="chat"]

Nazri said that before the amendment, it was <strong>difficult to trace the source of an anonymous posting</strong> because even though there was an aggrieved party, no action could be taken as there was no evident publisher of the content.

</blockquote>

Pro-Government bloggers on the other side of this digital divide can't have it both ways, it's either the anonymous posting can <strong>easily be traced</strong> (thereby negating the very reason for the law), or the postings are <strong>difficult to trace</strong> (thereby shifting the burden of a difficult investigation from the police to the ordinary citizen).

So which is it?

If a perpetrator was even remotely tech-savvy, with a couple of Google Searches, they could completely anonymize their surfing making it very difficult for even law enforcement agencies to trace, let alone an ordinary citizens.

Fatimah then goes on to describes various scenarios where it would be <strong>'easy</strong>' to determine the source of any post, this part was actually quite sad.
<h2>Scenario 1: Getting an IP address from Google</h2>
[box icon="chat"]

There is an article titled "Azmin makan duit rakyat Selangor". The author wrote her name as Nazmi. Azmin brings Nazmi to court. Nazmi in her defense said "it was not me Min, sumpah! Bukan I Min! Percayalah...".

Since the article was written in blogger.com (owned by Google),<strong> the police can request the IP of the "mysterious writer" from Google.</strong> Every time you log in to your blogger or Goggle account, your IP will be stored in Google system. From the police investigation, they found that the IP does not belong to Nazmi's account.
Turn out the actual writer is: Faekah.

</blockquote>

This isn't so easy. Fortunately, Google is very transparent about government request, and have reported that up until 2011,<a title="Google User Data" href="http://www.google.com/transparencyreport/userdatarequests/" target="_blank"> the Malaysian Government has never requested for any user data, we have requested for takedowns but not user data</a>. What that means is that we're not sure if Google will happily comply with our request, the success rate of these government request range from 0% (in the case of Turkey and Russia) up to 93% in the case of the US Government.

So we're not sure how successful we would be, and to blindly assume it's a simple matter of asking Google for an IP address is just plain ridiculous.

Secondly, there are various ways to obtain a separate IP address from a separate entity. In my posting about how to activate your <a title="Kindle in Malaysia : Buying and Using a Kindle in Malaysia" href="http://www.keithrozario.com/2012/04/kindle-malaysia-buying-ebooks-amazon.html" target="_blank">Kindle in Malaysia</a>, I advocated using a service like Texasproxy or Hidemyass, proxy servers mask your IP address from Google by substituting it for their own IP address, and you could proxy over proxy providing extra layers of IP address obfuscation. For those who don't mind parting with a few dollars, a VPN service does the proxying in the background for all traffic, thereby making it difficult to trace.

Finally what if I just used TOR? <a title="Internet Privacy with TOR: Should the internet be anonymous" href="http://www.keithrozario.com/2012/06/internet-privacy-tor-anonymous-tracking.html" target="_blank">End of story, it's not traceable.</a>
<h2>Scenario 2: MAC addresses can identify you</h2>
[box icon="chat"]

There is photo of Izzah painted with the words "Izzah Penipu dan Gila Kuasa". The account was under the name Chua. Izzah brought Chua to court. Chua in his defense said : "Zah..bukan abang sayang...abang sayang Izzah..takkan la abang nak sabotage syg. Abg ni suka gigit...gigit telinga...sabotage ni tak main".

<strong>Every computer/phone/laptop/Xbox/etc has a MAC address. When you connect to the Internet your ISP can see this</strong>. The police check asked Chua whether he has any electronic devices and Chua replied "Only my phone sir" while looking at the officer's ear. Upon checking the MAC address of the phone, the MAC address did not match.

Turn out the actual writer is: Azmin

</blockquote>

First of all this is bullshit. Your ISP never sees the MAC of your phone or Ipod or Laptop, just the MAC address of the 'last hop' which in this case is your router or Wi-Fi access point. In fact, even that is not for sure. MAC addresses are used to manage local networks, such as the WiFi network in your home--it's not used at the ISP level.

Secondly, there is no central repositories of MAC addresses, what's to stop Chua from buying a separate iPod and ditch it once he's done the deed. No one knows who has which device with which MAC address, hence it's an ineffective investigative method.

Thirdly, even if this were possible, a tech-savvy perpetrator could spoof the MAC address of your machine for <a title="Change MAC windows" href="http://www.klcconsulting.net/smac/" target="_blank">Windows</a>, <a title="Change Mac macintosh" href="http://devices.natetrue.com/macshift/" target="_blank">Macintosh</a> and even <a title="Change Mac Android" href="http://android.stackexchange.com/questions/17657/how-to-change-permanent-mac-address-on-my-android-phone" target="_blank">Android</a>. <a title="MAC Spoofing" href="http://en.wikipedia.org/wiki/MAC_spoofing" target="_blank">There's a whole wikipedia article on Mac Spoofing</a>.

Finally, even if they did conclude that the MAC address didn't belong to Chua, how did they find out the actual writer?

In the words of Sheldon Cooper, this is <strong>HOKUM!</strong>

MAC addresses cannot identify a person, merely a piece of equipment. So it's absolutely impossible to use a MAC address to trace a person. If I identified a MAC address belong to a specific Samsung phone that was purchased from a specific Samsung shop in Mid-valley. Unless the Samsung shop keeps records of who bought their phone, there could be no trace of it. The same applies for much cheaper items like network cards and Wi-Fi dongles.
<h2>Scenario 3: Twitter complying with Government request from Malaysia</h2>
[box icon="chat"]

A tweet goes like this: "@anwaribrahim, you penipu kaum India! You promise macam2 sebelum GTX12 tapi skrg habuk pun tarak ada. @#$%@#%". The account was tweeted under the account psurendram. In anger, Anwar brought Surendran to court and in Surendran's defense he said: "Boss...sampai hati boss tuduh saya macam ini...lupakah janji2 kita dahulu? Sebangsa, Sejiwa, Sehidup, Semati? Cuma tak selubang sahaja...tu ka sebab boss marah?"

When a tweet is posted, all our tweets are stored in Twitter's many servers. Just like Facebook and Google, they also save for each tweet, info associated with that tweet e.g. time, date, location, IP, device name etc. <strong>The police can get these associated details of the tweet from Tweeter[sic]</strong>. Upon investigation, it was found that actually Surendran is innocent.

Turn out the culprit was someone who got jealous with Anwar's attention towards Surendran. He got so jealous that he took Surendran's phone while Surendran was busy entertaining Anwar and made that tweet. That person was Azizah!

</blockquote>

This is getting ridiculous. First of all it's TWITTER not TWEETer.

Secondly, If you take my phone and tweet something, there is NOTHING from twitters server to prove you didn't do it. As long as you took my phone, to twitter you look like me. That's it.<strong> Twitter doesn't know someone took my phone.</strong>

Once again, we see a trend that it's as easy as asking Twitter for info, and they'll gladly hand it over to me.<a title="Twitter Government Request" href="https://support.twitter.com/articles/20170002#" target="_blank"> Twitter also is very transparent about their Government request,</a> the only difference with Google is that Government request to twitter have a FAR FAR lower success rate , with most countries having a <strong>0% success rate</strong>.

So going to twitter is not an option. One would think a blogger would know this.

Plus how the hell did they find out it was Azizah, probably through good ol' fashion police work, that's the point. The burden of proof should be on the prosecution and police, not on the accused, because it's just impossible for the accuse to prove his innocence without the resources from law enforcement agencies to help him out.
<h2>Further misconceptions : You should PAY for Free Wi-Fi</h2>
It goes from being ridiculous to downright sad at this point. Fatimah goes on to explain herself in the comments section of the post.

A user by the handle of Julie Anne asked what happens when someone uses a Free Wi-Fi service to post a comment. Fatimah responded:

[box icon="chat"]

1. It is the duty of the owner of the cybercafes to put security measure. Please let me explain what I mean.

2. In western Europen countries, most of the area are wifi. The WIFI is free but the internet, you have to pay lor.

</blockquote>

Apart from the fact that she wants to revert to a paid Wi-Fi as opposed to Free Wi-Fi (which is stupid), she's also completely wrong about paying for Internet access. While in some cases like Changi Airport (I'm asked for my passport before I can access the Wi-Fi), it's completely ridiculous to ask Mamak shops to do the same. Given the <a title="Personal Data Protection Act 2010 Malaysia" href="http://www.keithrozario.com/2012/07/personal-data-protection-act-2010-malaysia.html">personal data protection act</a>, the Mamak stall needs to properly secure and maintain your personal data if it wants to capture it, something well beyond the scope of serving roti canai and nasi lemak.

Finally, I think this sums her tech-savvy skills up. "<strong>The WIFI is free but the internet, you have to pay lo</strong>r"--Why would anyone use the Wi-Fi if there wasn't an internet connection?!!
<h2>The Final Straw : To be honest, even TOR can detect one</h2>
This is where I was completely flabbergasted, upon one user named beng pointing out I could spoof my IP address with TOR, Fatimah responded:

[box icon="chat"]

2. Tor? Of course la I know beng...coz I also use one mah. hehehe but be honest beng, even Tor also can be detect one.

</blockquote>

Really? Even TOR can detect? It's that easy???

Maybe, you'd like to work for the FBI, because<a title="TOR stymied child abusers" href="http://nakedsecurity.sophos.com/2012/06/14/fbi-tor-child-abuse-investigation/" target="_blank"> the FBI can't seem to detect Child Abusers who use TOR to post up child abuse images online</a>. In fact the FBI have released a report stating that :

[box icon="chat"]

Because everyone (all Internet traffic) connected to the TOR network is anonymous, there is not currently a way to trace the origin of the website. As such no other investigative leads exist.

</blockquote>

Well, maybe the FBI aren't as good as Fatimah Zuhri, or maybe Fatimah doesn't know what she's talking about. It's up to you to decide.
<h2>Conclusion</h2>
Normally I wouldn't bother with these kinds of post, but when it concerns matters of Government policy and when a prominent blogger with millions of hits post these inaccuracies on his blog, I think we need to step up and point out the errors so that people know the facts behind the policy.