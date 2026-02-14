+++
title = "DAP lodges report with MCMC over blocked sites"
slug = "dap-blocked-sites-tm-bluecoat-packetshaper-arbor-network"
date = "2013-05-23T07:00:31"
draft = false
tags = ['Arbor', 'Bluecoat', 'Maxis', 'TM', 'Unifi']
categories = ['Copyright and Censorship', 'CyberLaw', 'Malaysia']
+++

<p style="text-align: center;">![Blue Coat packetshaper](/uploads/blue_coat_packetshaper.png)</p>
Two days ago, the Democratic Action Party (DAP) lodge a report to the MCMC on an 'internet blockade' targeting DAP related political websites that was allegedly being carried out by Telekom Malaysia (TM). As you may know TM is the largest ISP in Malaysia, and if TM suddenly blocks a website--a large chunk of the Malaysian public are automatically denied access to it.

The DAP IT manager (<span style="color: #888888;"><em>didn't know the DAP had an IT team now did ya?</em></span>), in his press statement said that :
<blockquote>In investigating the DPI filtering equipment location, I have found 1032 suspicious network equipment using same IP address family as the the Arbor Network Peakflow SP with TM branding. Since the login page of this network equipment bears TM logo, undoubtedly MCMC should haul up TM and conduct IT forensic investigation on all 1032 equipments without delay. I am fully prepared to assist MCMC in its investigations.

In light of this new evidence, MCMC must re-examine its 2nd May statement. MCMC should be politically impartial and hold the standard of government regulatory body that it should be. It must put the interest of all Malaysians first.</blockquote>
Now this isn't really news, to be fair the Arbor Network Peakflow SP solution is meant primarily as a DDoS protection security suite with a slight tinge of DPI functionality added on the side. TM in their defence haven't really denied they own the Arbor Network solution--there's even a joint <a title="TMNET purchases Arbor Network Peakflow SP" href="http://www.arbornetworks.com/news-and-events/press-releases/2004-press-releases/883-arbor-networks-and-commverge-solutions-team-up-to-protect-tm-nets-ip-network-from-zero-day-worms" target="_blank">press release from 2004 to announce their purchase of it</a>.

Unless TM operates like the government, in which they announce the purchase of something in 2004, but only start to using it in 2013--I'm guessing they were using Arbor for other purposes before they decided to unleash its DPI functionality.

But there could be a twist.<!--more-->
<h2>Bluecoat Packetshaper in Malaysia</h2>
We all know the Labour Day report from Citizenlabs suggesting that government agents were intentionally spying on Malaysian Citizens using Finspy (or at least we 'should' all know about that report). There is however, a lesser known <a title="Malaysia Blue Coat Global center" href="https://citizenlab.org/2013/01/planet-blue-coat-mapping-global-censorship-and-surveillance-tools/" target="_blank">report</a>, that was released early this year that detailed Bluecoat Packetshaper servers in Malaysia. Unlike Arbor, which promotes itself as a DDoS protection solution, Bluecoat Packetshaper openly advertises itself as a censorship tool, an excerpt from their website says:

<blockquote>
<h2>It’s your network. Own it.</h2>
Does your network know the difference between important web traffic like online meetings, and lower-priority traffic like games or streaming media? Your security solution might block entire categories of content, such as gambling or pornography, but how do you control everything else?
</blockquote>

Bluecoat is currently being used by ISPs in countries like Syria, Burma, Egypt and Saudi Arabia for various reasons, but are these the sorts of countries we want to be associated with? Rubbing shoulders with the worst of the worst--of course to be fair they're also deployed in Singapore and South Korea, so what is Bluecoat really used for?

There's a whole bunch of easily obtainable documentation online, where Bluecoat openly boast about their ability to <a title="Bluecoat dynamically filter URL" href="/uploads/editor_files/BlueCoat_WebFilter_wp_v1c.pdf" target="_blank">dynamically filter url's </a>, which is exactly what we see in Malaysia for these DAP sites. One user on the <a title="Unable to block HTTPS" href="/uploads/bluecoat_SGOS5.5.png" target="_blank">here</a>.

Of course Bluecoat has legitimate uses on private networks--like preventing government employees from downloading porn <em>(hint: they <a title="Government Network used to download porn : Privacy is dead" href="http://www.keithrozario.com/2013/04/malaysian-government-network-download-porn-privacy-dead.html" target="_blank">are</a>), </em>but in the public sphere, like your regular Unifi and Maxis subscriber it has no place since filtering content is tantamount to censorship--and that's something we should never do to the internet.

More importantly it allows for targeted URL specific blocks, and so far the vast majority of the blocked content is politically related--signalling a government or political intervention. However, does it really matter if TM uses Bluecoat or Arbor Network as their censorship tool? I think it does.
<h2>Bluecoat vs. Arbor : Does it matter</h2>
I've saved the best for last....

The reason why I think it's important to really identify if its Bluecoat or Arbor is because Bluecoat has been ramping up their technological capability. Bluecoat recently acquired Netronome SSL, which specializes in monitoring SSL traffic. Apparently they've made a big jump to the point where they now 'boldly' proclaim this on their website:

<blockquote>

Now you can have visibility into <strong>all the encrypted SSL traffic on your network</strong>—at extremely high performance—so you can inspect it, identify potentially nefarious activities, and feed the intelligence to an ecosystem of security application vendors—all through Blue Coat.

That’s where Netronome’s SSL appliances can help. They deliver SSL decryption in networks ranging from 100 Mbps to 10 Gbps full duplex, giving you visibility into SSL traffic while it’s running across your network.

</blockquote>

I don't believe this is possible, but you never know. I personally feel this is more salesmanship than true engineering, SSL (and its successor TLS) is the encryption mechanism used not just to protect your Facebook login and Email accounts--it protects your bank logins and VPN (usually). In fact, most of the time TLS encryption is considered to be the most secure form of internet communication online, without it nearly nothing you do online would be safe from prying eyes.<a href="/uploads/bluecoat_SGOS5.5.png">
</a>

So when the DAP IT manager recommends you use “https everywhere”, well that may work --for now. There is a huge latent demand for these surveillance and censor software suites like Bluecoat, and as long as the governments and ISPs of the world feel they have a right to intercept the private communications of their users and citizens, companies will continue creating these capabilities--and governments will continue buying them.
<h2>Conclusion</h2>
While which solution TM uses is irrelevant to the topic of this discussion, I want to go back to the original premise of internet censorship in Malaysia. We saw back in 2008, when the government first formally censored the internet that if we grant politicians the power to censor--they will censor for political gain. The very first site censored formally by Malaysia was, MalaysiaToday--a political website that published a huge array of anti-government articles.

We continue to see censorship along the political front, targeting blogs and sites of popular (and not so popular) opposition politicians, to the point where political parties feel they need to hire IT Managers <em><span style="color: #888888;">(seriously, I can't get over this)</span></em>

It's important to remember, that the government has made a promise to not censor the internet--and that promise should include regulating ISPs so that they too do not censor the internet. It remains to be seen how this will be played out--but rest assured that the ISPs already have the technological capability to censor and even inspect your personal internet traffic--the only thing stopping them now is the law and lack of political will.