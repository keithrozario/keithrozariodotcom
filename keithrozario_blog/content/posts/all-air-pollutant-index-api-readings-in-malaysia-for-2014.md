+++
title = "All Air Pollutant Index (API) readings in Malaysia for 2014"
slug = "all-air-pollutant-index-api-readings-in-malaysia-for-2014"
date = "2015-02-08T00:24:16"
draft = false
categories = ['Malaysia', 'Misc']
+++

<blockquote>I've stopped scrapping the API readings for Malaysia, as the MET department have stopped publishing historical readings on their website.

The data has been updated to include all API readings up to 01-Sept-2015, and then from 28-Sep-2015 to 03-Oct-2015. The 'gap' in the dataset is because the MET department changed their webpage and removed the legacy data before I could get my hands on them. I've written to them for it, hopefully we get a useful response. For now though, there's 24 months of data from Aug-2013 to Oct-2015 in the dataset. enjoy!

To get all the readings by region in a single delimited file, click this <span style="color: #0000ff;"><a style="color: #0000ff;" href="https://www.dropbox.com/s/6p65oyupycti32b/ReadingsByRegion%28SG%26MY%29.zip?dl=0">link</a></span>, I apologize for the messiness of the data and the files, I should tidy them up by the end of the month. Contact me directly for anything specific.

Keith</blockquote>
![Haze Malaysia](/uploads/8679939937_79ac83f81c_z.jpg)

Once again, your friendly neighbourhood techie has used this powers for the good of the country.

Last September, I scrapped <a title="MyProcurement: All government tenders in one Excel file" href="http://www.keithrozario.com/2014/09/myprocurement-all-government-tenders-in-one-excel-file.html">all the procurement data from the Malaysian's Government MyProcurement website</a>, this time I scrapped all the Air Pollutant Index (API) readings from the <a title="DOE website" href="http://apims.doe.gov.my" target="_blank">Department of Environment </a>(DOE) website.

First off, Kudos to the DOE for keeping such great tabs on the data--overall the DOE publishes one API reading for every hour or every day across 52 locations in Malaysians. Just to put the sheer volume of data into perspective, for just one year that's:

52 locations x 1 reading/hour x 24 hours/day x 365 days/year  =<strong> 455,520 readings.</strong><!--more-->

That's a lot of readings--and a scintillating amount of data, but it gets better. The DOE website has data going all the way back to Aug-2013, so I created a script in Python to grab all the data from Aug-2013, all the way to Mar-2015, more than a years worth of API readings, and more than 600,000 data points for you guys.

Grabbing that much data posed some challenges, both in programming the script, but also in my ability to share it with you. For those of you with older versions of Microsoft Excel, you're limited to just 65,536 rows per sheet, and even with the newer versions of Excel, loading 600,000 rows into a single sheet would freeze all but the most powerful of laptops.

For now though, let's move onto the top 10 things about the Air in Malaysia.
<h2>10 Things about the Air Pollutant Index in Malaysia</h2>
1. The <span style="text-decoration: underline;"><strong>highest API reading across 2014 was 358</strong></span>, recorded on the 14-March-2014 at 9am in Port Klang.

2. In fact, only two regions in Malaysia have ever recorded API readings above 300, and that's <span style="text-decoration: underline;"><strong>Port Klang and Banting</strong></span> (not good news for Klang folk!)

3. The worst month in 2014 (and indeed across the dataset) was March 2014, <span style="text-decoration: underline;"><strong>27 regions out of 52 had an average API reading that was above 50</strong></span> (the <a title="Air Pollutant Index" href="https://en.wikipedia.org/wiki/Air_Pollution_Index" target="_blank">healthy threshold</a>)

4. Bintulu, ILP Miri, Indera Mahkota, Kuantan, Jerantut, Kapit, Keningau, Kota Kinabalu, Kuching, Labuan, Langkawi, Limbang, Miri,Sarikei and Tawau <em><span style="color: #808080;">(running out of breath here...)</span></em> had consecutive 19 months where the Average API reading never exceeded 50--<span style="text-decoration: underline;"><strong>meaning they were pretty healthy for more than 1.5 years straight</strong></span>. The list is dominated by East Malaysian locations, but Langkawi and Jerantut stand out as Semenanjung's best place to live in for air quality.

5. That doesn't mean all of East Malaysia was good--<span style="text-decoration: underline;"><strong>Sibu had a really bad July in 2014</strong></span>, with a high of 270 (the highest recorded in an area outside of Port Klang or Banting), and a average API reading of 65.86. Otherwise it scored healthy averages for the remainder months.

6. But Averages can be tricky--looking deeper into the data, I found that <span style="text-decoration: underline;"><strong>Aug-2013 wasn't a good time for Bukit Ramba</strong></span>i, with 99.86% of all API readings in the region scoring above 50. In fact from Aug-2013 to Jan-2014, Bukit Rambai recorded readings above the healthy threshold of 50 more than 90% of the time. In Jan-2015, 90% of all API readings in the area were unhealthy. Something must be happening there, because in Aug-2014 only 9% of readings breached the 50 mark.

7. Looking specifically at Port Klang and Banting in March and July, there seemed to be no correlation between time and API readings--meaning that the API readings didn't rise in the morning or lessen at night. I anticipated some level of change to account for the additional cars on the road, but it appears they have no effect on the API readings--suggesting to me that <span style="text-decoration: underline;"><strong>there's little we can do to reduce the API readings once the haze sets in</strong></span>. Our cars don't emit nearly enough to mess with the forest fires.

8. Where's the place with the cleanest air? Well hard to say, using a simple metric of the percentage of readings below 50 across the entire dataset, Limbang scores 98.7%, while a host of other East Malaysian regions together with Langkawi and Jerantut score well over 90%. Meaning that 90% of the time, the air in these areas are at healthy levels.

9. Dirtiest? No prizes for guessing--<span style="text-decoration: underline;"><strong>Port Klang and Banting</strong></span>. In Mar-2014 the Average readings in these areas were 97.4 and 91.6 respectively, almost twice the healthy limit. While across the entire dataset, Port Klang records readings above the unhealthy limit of 100 4.5% of the time, with Banting following closely at 2.5%. The cleanest areas in Malaysia have never recorded readings above 100 in the past 18 months :)

10. The Dirtiest month across Malaysia was <span style="text-decoration: underline;"><strong>Mar-2014</strong> </span>(Average of 51.7), while the cleanest was <span style="text-decoration: underline;"><strong>Dec-2013</strong></span> with an average of just 33. Although I must warn you that Malaysia is a pretty big country--if you include the space between Semenanjung and East Malaysia, the geographic spread of our country is massive, and an average for such a large area doesn't make much sense.

Now let's get a bit technical
<h2>Challenges with the dataset</h2>
Overall the data was pretty good, but there were still some gaps. More than 23,000 data points were empty...quite a lot but just 3.5% of the entire dataset, so overall DOE manage to record 96.5% of the time. Pretty good I must say.

But the gaps did present problems, and in my dataset I had set them to 0. The 'proper' way to resolve this was to give the missing data points the average of the previous and next data point, but I wanted to present this rather than perfect this. That will take time, so I'm sharing it here--maybe in the next instalment I will code this into the script.

The other challenge I had was how to share across 650,000 data points. I decided to share the entire data set as an SQL file that can be downloaded from the Project's Github page (link below). Also on the GitHub page are csv files that list all API readings per region in case you want to play around. Unfortunately, the CSVs had to be ":" separated rather than comma-separated because some of the region names already had commas.

So you can't validate the entire dataset unless you're willing to setup a an actual Database yourself, and I appreciate most Malaysians aren't that savvy, but this is the best I could do. If you have a better way to share the data,then let me know--or you can do it yourself, as everything in the project is open-source (using Python and MySQL)
<h2>The Data in Excel</h2>
The code I used, the database and the Excel spreadsheets are available at the following <a title="Air Pollutant Index Malaysia GitHub" href="https://github.com/keithrozario/API_readings" target="_blank">link</a>.

As always, everything published on the blog is released under Creative Commons 4.0--so do with it what you please, but consider attributing it to me by linking back to this specific post or to www.keithrozario.com.

For more information on the Air Pollutant Index refer to <a title="Air Pollutant Index" href="https://en.wikipedia.org/wiki/Air_Pollution_Index" target="_blank">wikipedia</a>.

Two guys, Jason Benedict and Doug Beare, who are part of the CGIAR Research Program on Climate Change, Agriculture and Food Security (CCAFS) - <a href="http://ccafs.cgiar.org/">http://ccafs.cgiar.org</a>, took this data set and created a really cool analysis of air quality in Penang and tried to determine the best time for outdoor activities on the Island. Check out their work <a title="Jason and Doug Blogspot outdoor activities pollution" href="http://jason-doug-climate.blogspot.com/2015/03/will-i-choke-when-is-best-time-for.html">here</a>.

Stay cool!

<em><span style="color: #808080;">Picture courtesy of <a style="color: #808080;" title="Firdaus Latif" href="https://www.flickr.com/photos/firdausjongket/" target="_blank">Firdaus Latif</a> : Link <a style="color: #808080;" title="Haze Picture on Flickr" href="https://www.flickr.com/photos/firdausjongket/8679939937/in/photolist-ee1XJR-B9x2d-MsPtt-4QMHA-e3MA6X-3UHTQ-3UHTP-pXRDE-5dpH4d-25SGUk-6sgK8C-5dpGBh-c496X-5dknFX-5dpNwA-5dktov-5dkuPR-5dkv4Z-5dpNZ3-5dpHGb-5dpPQE-5dkmS4-5dko54-5dkvfe-5dku54-5dkuE6-5dpPoC-5dkuv6-5dpHSq-5dpNCQ-5dpNNU-5dpHvu-5dkngz-5dpGFq-5dknkK-ajmk1p-arGMKL-25SGUH-8BTMWU-3VLcZ-3VL5H-YoJXR-pZcDj-3VLd5-3VLd4-3WVCD-3WVCC-3VL5K-3VL5G-3VL5J" target="_blank">here</a>.</span></em>