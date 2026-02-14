+++
title = "MyProcurement: All government tenders in one Excel file"
slug = "myprocurement-all-government-tenders-in-one-excel-file"
date = "2014-09-16T22:54:40"
draft = false
categories = ['Big Data', 'CyberLaw', 'Malaysia']
+++

![MyProcurement](/uploads/MyPROCUREMENT-Pusat-Maklumat-Perolehan-Kerajaan.png)
<blockquote><span style="color: #99ccff;">I've updated this post on 31-Mar-2015, to incorporate the latest changes, and to provide more up to data info on the procurement database. Left everything else in tact.</span></blockquote>
Happy birthday Malaysia!! Just how awesome is our country, that we celebrate an Independence Day AND a Malaysia Day, not to mention 2 New years day, (or 3 if you count Awal Muharram).

So on that note, I decided to use my IT skills for the good of the country.

To be honest, my IT skills have never been up to par, my day job is more managing/planning/documenting than actual execution of 'real' IT work. But it was good for me to dust of the ol' programming fingers and learn Python to grab some publicly available information and make it more accessible to the less IT centric members of society.

Since I had limited time, and sub-par skills, I decided to set my sights low, and aim to extract all the data from the Malaysian <a title="Myprocurement" href="http://myprocurement.treasury.gov.my/" target="_blank">MyProcurement</a> portal, which houses all the results of government tenders (and even direct negotiations) in one single website for easy access. The issue I had with the portal though, was that it only displayed 10 records at a time--from it's 10,000+ record archive, so there was no way to develop insights into the data from the portal directly, you had to extract it out, but the portal provider did not provide a raw data dump to do this.

So I wrote a simple Python script to extract all the data, and prettified the data in Excel offline. The result is a rather mixed one.

I was happy that I could at least see which Ministeries or Government departments gave out the most contracts, and what the values of those contracts were. All in all, the excel spreadsheet has more than 10,000 tenders with a cumulative value of RM35 billion worth of contracts going back to 2009. The data allowed me to figure out which Ministry gave out the most contracts, the contracts with the highest and lowest value (including one for Rm0.00, and one for just Rm96.00). All in all it was quite informative.

![Results_by_ministry](/uploads/Results_by_ministry.png)

<!--more-->

What I wasn't too happy about was the data quality in the dataset. Firstly, there were 419 tenders where the winning party wasn't documented--in other words a total of Rm2 Billion was given out through this system but the winning parties who received that huge amount of cash was blank. Also the names of the winners were not documented consistently, for example look at the screenshot below:

![Advance Altimas](/uploads/Advance-Altimas.png)

This company "ADVANCE ALTIMAS SDN.BHD." won 5 different contracts, but the name of the company seems to change with each contract. Sometimes there is a dot at the end of the SDN and BHD, sometimes there isn't, and one time there is a huge typo that changes ALTIMAS to AGITMASS. Even the ROC registration number or the Ministries own registration number (under MOF/PKK) is inconsistent acrosss the 5 entries, and this is not specific to this company either. The entire dataset is filled with these inconsistencies.

This made it difficult to see which companies were getting most of the contracts and which companies were one hit wonders. That being said, before you start to criticize, anyone who has worked with government or even large corporations know that this is all too common, and nothing specific to our Govenrment. Maintaining and cleaning up data is something a lot of bureaucracies find hard to do.

But if you're in the mood for some data analysis (and who isn't)--<a title="MyProcurement Data" href="https://www.keithrozario.com/wp-content/special-uploads/MyProcurementData(31-Mar-2015).xlsx" target="_blank">here's the excel spreadsheet</a> of the data and here's the <a title="Git Repository MyProcurement" href="https://github.com/keithrozario/MyProcurementDataScrapper" target="_blank">git repository</a> with the code.

I've blogged about the <a title="Auditor-General report 2011 : When can Malaysians expect Transparency in IT spend" href="http://www.keithrozario.com/2012/10/auditor-general-report-2011-malaysian-government-it-spend-transparency.html" target="_blank">Auditor-Generals report previously</a>, specifically with regards to IT spend, and how the US government has an IT dashboard. Hopefully, this will help improve transparency in our government expenditure.