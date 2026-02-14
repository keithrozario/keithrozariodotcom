+++
title = "Maxis blocks Torrent traffic"
date = "2013-05-30T07:00:47"
draft = false
tags = ['Maxis', 'Torrent']
categories = ['Copyright and Censorship', 'CyberLaw', 'Malaysia']
+++

There's a really cool tool called <a title="Glasnost: Check if Maxis blocks torrents" href="http://broadband.mpi-sws.org/transparency/bttest.php" target="_blank">glasnost</a>, that can easily detect if your ISP is throttling certain traffic through its servers. It works amazingly well at detecting if your ISP is blocking that most sacred of all internet traffic--BitTorrent.

So running two test, one over my Unifi connection, and one more tethered over my Galaxy S3 on Maxis, and came to the conclusion that Maxis does indeed block torrents by default. However, just like how you have to call <a title="How to enable VPN connectivity on Maxis Mobile" href="http://www.keithrozario.com/2012/07/maxis-vpn-mobile-setting-3g.html" target="_blank">Maxis to enable VPN access via your phone</a>, you have to call them to <a title="Torrent traffic on Maxis" href="https://forum.maxis.com.my/forum_topic.asp?TOPIC_ID=6384&amp;whichpage=2" target="_blank">allow torrent traffic as well</a>...supposedly.

It's important to point out as well, that this is my Maxis Mobile connection and NOT Maxis Fibre, so there may be differences. To me it's surprising that Maxis is blocking bitTorrent traffic since it already has a datacap on my Mobile data (3GB/month).

Most feedback from the blogs and forums seems to suggest, Maxis isn't the most torrent friendly ISP. Which is sad.

Here's the glasnost result from Maxis:
<p style="text-align: center;"><a href="/uploads/Maxis_bit_torrent_block.png"><img class="aligncenter  wp-image-3467" alt="Maxis_bit_torrent_block" src="/uploads/Maxis_bit_torrent_block.png" width="715" height="195" /></a> <a href="/uploads/Glasnost_confirm_unifi_torrent_block.png">
</a></p>
And here's the result from Unifi, but of course I knew already that <a title="TM Unifi speeds actually quite GOOD!" href="http://www.keithrozario.com/2012/05/unifi-speed-test-broadband-torrents-youtube.html" target="_blank">Unifi didn't block torrent traffic</a>.
<p style="text-align: center;"><a href="/uploads/Glasnost_confirm_unifi_torrent_block.png"><img class="aligncenter" alt="Glasnost_confirm_unifi_torrent_block" src="/uploads/Glasnost_confirm_unifi_torrent_block.png" width="423" height="322" /></a></p>
You can run your own test <a title="BitTorrent Test" href="http://broadband.mpi-sws.org/transparency/bttest.php" target="_blank">here</a>, to determine if you ISP is blocking your torrent traffic. It's also able to detect if your ISP is blocking other popular peer-to-peer applications as well as youtube and email servers as well.