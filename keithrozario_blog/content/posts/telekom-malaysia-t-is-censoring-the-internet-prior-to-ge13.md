+++
title = "Telekom Malaysia is censoring the internet prior to GE13"
slug = "telekom-malaysia-t-is-censoring-the-internet-prior-to-ge13"
date = "2013-05-02T10:17:35"
draft = false
tags = ['Unifi']
categories = ['Copyright and Censorship', 'CyberLaw', "Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++

<p style="text-align: center;"><iframe src="http://www.youtube.com/embed/rsqp3hMgM98" height="315" width="560" allowfullscreen="" frameborder="0"></iframe></p>
I'm not a usual fearmonger, or a person who panics easily--yet you friendly local tech evangelist has a warning for Malaysian users out there. Unifi is censoring the internet in the run up to the hotly contested GE1--and that's what the data suggest.
You heard that right folks, some of you suspected all along, and I apologize for not believing you earlier. I was initially skeptical that Unifi and Telekom Malaysia would go to such extents to censor our right to information, and I'm deeply upset that this is happening in my own country.

Usually most Internet Service Providers (ISP) don't censor the internet, not because they don't want to--it's simply because censoring the vast amount of online traffic is a monumental technical challenge. In the past we've seen Malaysia ISPs do this, for instance when they blocked Malaysia-Today in the run-up to the 2008 General elections, but censoring one entire website is a fairly straightforward thing to do--<a title="Bypass Unifi blocking and censoring using a DNS switch or VPN connection" href="http://www.keithrozario.com/2012/03/bypass-unifi-blocking-and-censoring-using-a-dns-switch-or-vpn-connection.html" target="_blank">an bypassing that censorship is equally straightforward</a>.

However, what Telekom Malaysia have done in this case, is not just censor one website--but rather <strong>parts</strong> of a website. Telekom Malaysia has gone leaps and bounds ahead in terms of  censoring capabilities--now they're able to censor 'parts' of a website including specific videos on youtube, and pages on Facebook.

Any government that blocks Facebook completely, isn't going to get re-elected in Malaysia, the enormous public backlash we can expect would be enough to unseat even the great Barisan Nasional. Can you imagine how upset my aunty would be when she can't play Candy crush???

It was in this premise that caused me to be skeptical that a government would be able to censor the internet, blocking only certain pages of Facebook (like the DAP Malaysia Facebook page) is far more technically challenging, than blocking and entire website like Malaysia Today.

Unfortunately, I can almost 100% confirm at this point that Telekom Malaysia now have this capability. A capability once only used by countries like China and Iran, have now reached our borders--and it is being used.
<h2>What is Deep Packet Inspection</h2>
Just to briefly explain what's happening here.

1. The internet is this vast network running on something called the Internet Protocol or IP. This is what we mean by IP Address, it is literally your address on the internet.

2. The way the protocol works is routing data in packets. Essentially a packet is a small amount of data.

3. An analogy would be that if you used IP to send a long letter to your mother, instead of writing a 100 word letter and then sealing it in one envelope and sending it your mother. Your computer breaks that 100 word letter into 10 packets  of 10 words each(for example) and sends those along in 10 different envelopes. So your mother would receive your message in increments.

4. This is why webpages don't load instantly. Instead they take time, because your browser just displays your web page for packets you've already received and what you get is an incremental load.

5. It's also why on slower internet connections you'd see a image load in stages, rather than instantly see the entire image.

6. Just like envelopes sent via mail, packets also contain addressing information, so that the Postman knows where your letter needs to go to.

7. In all cases, the postman looks at the OUTSIDE of the envelope and sends your letter to the address you've written on it--without OPENING the letter.

8. So if the Postman wants to block you from sending letters to your mother, he'd just discard all the envelopes going from your home to your Mothers home. He can do this easily without opening your letter.

9. That's how TM can easily block MalaysiaToday. They can just cut-off all traffic to the MalaysiaToday IP address (although this is a bad analogy).

10. However, if the PostMan wanted to block only certain letters to your mother--let's say all letters you sent to your mother to vote Pakatan Rakyat, but allow letters that had nothing to do with the election--he'd have to OPEN the letter and find out what information you're sending.

11. Similarly if Telekom wanted to block only certain parts of Facebook from you, they'd have to OPEN your data packets, to see which Facebook pages you were visiting.

12. This is the technically challenging part. Opening up the Data Packets routed through Telekom is an enormous amount of work, and obviously slows down the entire process. The internet was built on speed and trust, and not for censorship at the packet level. How many postmen would you need if you wanted them to open each and every envelope sent??!

13. This process is called Deep Packet Inspection (DPI) and it is such an engineering challenge that very few countries even bother trying. The only country with the true audacity to do this is China (and possibly Iran).

14. Yet, from my analysis and my data--I can conclude that Telekom Malaysia at least have this capability. I could be wrong--but it's unlikely.
<h2>What data do I have?</h2>
I made fun of Malaysiakini previously, when they claimed they were being blocked by Malaysian ISPs. The reason was that Malaysiakini had no data--but they did do something strange. They claimed that the encrypted website http<span style="color: #ff0000;"><strong>S</strong></span>://www.malaysiakini.com was fine, while the normal website had http://www.malaysiakini.com was being blocked. <strong>(<a title="How SSL works: A presentation on Slideshare" href="http://www.keithrozario.com/2012/08/how-ssl-works-powerpoint-slideshar.html">the S at the end of http means the website is encrypted</a>)</strong>

You see if all you're doing is blocking all traffic to the portal (for instance blocking all traffic to MalaysiaToday), it would make no difference if the data was encrypted.

However....

If you're doing deep packet inspection--then encryption would basically bypass that censorship. The analogy here is that if you write to your mother in  Cyrillic Russian and the Postman can't read it. He can't determine if this indeed was a letter asking your mother to vote pakatan or whether it's just you asking for some money from mummy dearest. So in the end the postman has to make a decision to either throw the letter away or forward it onto your mother--but he doesn't know.

In the same way, encrypting the line, means Telekom Malaysia doesn't know which video on youtube you're watching or which page on facebook you want to see, they still know you're connected to Facebook or Youtube, but they don't know if you're watching a Pakatan ceramah or Psy-Gentlemen--it's all encrypted to them.

And I proved this by trying to visit the DAP Facebook page on my Unifi connection, first without encryption--and it failed. And then with encryption--and it worked. (check out the video above--the DAP Facebook page on https loads instantly, but the DAP Facebook page without encryption is blocked!!)<a title="DAP Facebook Page Blocked" href="http://screencast.com/t/dfbATO3jtX" target="_blank">
</a>

This is no accident, I tried it plenty times--and it gave me the same result.

Is this accidental? Could be, but highly unlikely. Deep Packet Inspection is a technically sophisticated process, and a sophisticated process is usually purposeful and intentional. It's VERY unlikely to be some sort of accident, and there is no other way for me to explain why an encrypted version of facebook page worked, but not the unencrypted version, although networking isn't my strong suit and I'm open to opinions.
<h2><strong>Conclusion</strong></h2>
Beware ladies and Gentlemen, I'm convinced that Telekom Malaysia at least are beginning to censor the internet, Malaysiakini seems convinced as well. I can't be 100% sure from my data (since it's just from my connection), but I'd be looking forward to an explanation from Telekom.

Till then--happy voting from your local neighbourhood Tech Evangelist.

More information <a title="Youtube Deep Packet Inspection" href="https://forum.lowyat.net/topic/2794929" target="_blank">here</a> and <a title="Website blocked by Malaysian ISP" href="https://plus.google.com/101396658148522528050/posts/ak6opfbDxwa" target="_blank">here</a>. Sorry gotta go to work now folks, keep in touch.