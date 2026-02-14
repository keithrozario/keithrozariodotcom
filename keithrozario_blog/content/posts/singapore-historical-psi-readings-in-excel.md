+++
title = "Singapore Historical PSI Readings in Excel"
date = "2016-03-25T08:00:51"
draft = false
categories = ['Misc']
+++

<a href="/uploads/8679939937_79ac83f81c_z.jpg" rel="attachment wp-att-4752"><img class="alignleft wp-image-4752 size-medium" src="/uploads/8679939937_79ac83f81c_z-300x200.jpg" alt="Haze Malaysia" width="300" height="200" /></a>Every now an again, I brush off the dust from an old laptop I have in the corner, and boot-up a couple of forgotten python scripts.

One of those scripts would scrap the DOE Malaysia website for API readings in Malaysia, unfortunately, those damn fools at the DOE now only publish 7-day data, and completely wipe off anything older--for some unknown reason.

I even contacted my 'insider' over at MDEC to help out, since she's leading the open data initiative, but I've not had any response. So I've stopped work on the collating Malaysian API readings--for now. I suppose I could create a schedule job to scrape the website on a frequent basis, but that's not something I'm interested in at the moment.

But on a lighter note, I did modify the script to scrape data from the Singapore National Environmental Agency--and <a href="/uploads/Singapore-PSI-Readings.zip">here's the latest PSI readings</a> that go all the way back to April 2014, right up to yesterday (23-Mar-2016). This modification was part of my work last year to compare the PSI values that Singapore was reporting against the API values in Malaysia, (there was a wide discrepancy, check out my report <a href="https://www.keithrozario.com/2015/10/how-good-is-our-api-reading.html">here</a>)

As usual they come in lovely csv files <em>(separated by colons instead of commas, use the text to columns function in Excel to break them apart)</em>, and the full python script is fully available on my github page <a href="https://github.com/keithrozario/API_readings">here</a>.

All stuff produced on keithRozario.com is released under creative commons 4.0 (Attribution), which basically means who can use it for whatever you like--feel free, and don't worry about the government either, nobody holds 'copyright' to facts like PSI readings <em>(I don't know why people often ask me this)</em>, and the Singapore government does make this freely available, but not in a easy to crunch csv file.

So without further delay, here's the CSV files"

<a href="/uploads/Singapore-PSI-Readings.zip" rel="">Singapore-PSI-Readings</a> (click to download)

Enjoy.

P.S If this work has helped you in any way, would you mind leaving a comment below, helps me keep track of which of my crazy projects actually bring value to the wider community. Check out some climate change findings, based on my previous API reading work<a href="http://jason-doug-climate.blogspot.my/2015/03/will-i-choke-when-is-best-time-for.html"> here</a>.
<h2>TL;DR</h2>
For the truly un-initiated, here's the Google Sheets version of the Singapore readings. They had to be in individual sheets, because together they exceeded the cell-limit in Google Sheets. All in all, it's 17,000+ data points per region, so enjoy at your own risk :)

<a href="https://docs.google.com/spreadsheets/d/1qtVDpK6gxP_XLnOQqqPJ9XamQkWH-2V6qibjTxS95aw/edit?usp=sharing">Central</a> , <a href="https://docs.google.com/spreadsheets/d/1q8ahDPKazJANdoZU-zMJyNGYjav3T_bzrAgzm0_gYb8/edit?usp=sharing">West </a>, <a href="https://docs.google.com/spreadsheets/d/1zbzS1V50veGZkXvXoqo8HOw0otb5vhTdGQ1HgQJIWXc/edit?usp=sharing">East</a>,  <a href="https://docs.google.com/spreadsheets/d/1dh3SSjEGj-JhxxDnXIAbrRGGl6ymRbo7VQ2km9Qa1lM/edit?usp=sharing">South</a>, <a href="https://docs.google.com/spreadsheets/d/1kSTix4-hZr0oj7roBbJuRwZgljeAOP9maCWTQgSPBIQ/edit?usp=sharing">North</a>