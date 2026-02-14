+++
title = "Gov.My TLS audit: Version 2.0"
slug = "gov-my-tls-audit"
date = "2018-03-05T23:28:15"
draft = false
tags = ['jangankenahack', 'siteaudit']
categories = ["Keith's Favorite Post", 'Malaysia', 'Security &amp; Privacy']
+++



![](/uploads/scan_burgundy.jpeg)



Last week I launched a draft of the Gov.my Audit, and this week we have version 2.0

Here's what changed:
<ol>
 	<li><strong>Added More Sites</strong>. We now scan a total of 1324 government websites, up from just 1180.</li>
 	<li><strong>Added Shodan Results</strong>. Results includes both the open ports and time of the Shodan scan (scary shit!)</li>
 	<li><strong>Added Site Title</strong>. Results now include the HTML title to give a better description of the site (hopefully!).</li>
 	<li><strong>Added Form Fields</strong>. If the page on the root directory has an input form, the names of the fields will appear in the results. This allows for a quick glance at which sites have forms, and (roughly!) what the form ask for (search vs. IC Numbers).</li>
 	<li><strong>Added Domain in the CSV</strong>. The CSV is sorted by hostname, to allow for grouping by domain names (e.g. view all sites from <em>selangor.gov.my</em> or <em>perlis.gov.my)</em></li>
 	<li><strong>Added an API</strong>. Now you can query the API can get more info on the site, including the cert info and HTTP headers.</li>
 	<li><strong>Released the Serverless.yml</strong> files for you to build the API yourself as well :)</li>
</ol>
All in all, it's a pretty bad-ass project (if I do say so myself). So let's take all that one at a time.

<!--more-->
<h2>Added More Sites</h2>
I initiated a separate crawl last week, and obtained a larger number of government urls to scan. Currently there's 1633 unique hostnames that are scanned, but only 1324 are valid. Invalid hostnames, are either dead (DNS doesn't resolve) or the resolve to a Private IPs (typically 10. range).

Full list of hostnames are <a href="/uploads/hostnames.txt">here</a>. Feel free to add in the comments any <span style="text-decoration: underline;">.gov.my</span> or <span style="text-decoration: underline;">.mil.my</span> hostname I missed out, or better yet make a pull requests on the GitHub repo.
<h2>Added Shodan Results</h2>
The scan now stitches Shodan results for the IP, with the hostname records. It's currently limited to just the open ports and the Shodan Scan time. I may add banner information to the JSONs in the future. Stay Tuned.

Currently, Shodan doesn't index all the IPs in the range we scan, and I'm unable to trigger a scan without parting with some money ($19/mo).  If I can find some way to fund this, that's something to consider. For now, where the Shodan has the info it's stitched to the site record, otherwise the field is empty.

The results are quite amusing, among them a high prevalence of FTP servers, and one hostname having as many as 32 open ports !! I've never seen that many open ports on a server (not even one created to be insecure).



![](/uploads/Shodan_Results.jpg)


<h2>Added Site Title</h2>
The script now looks at the html content on the page and returns the site title. This is everything between the <strong>&lt;title&gt;&lt;/title&gt;, </strong>one of the great things about writing the script with Python is being able to leverage modules like Beautiful soup to parse the HTML. The code could be written in one line, but I chose to write it in 3, like this:
<blockquote>html_content = BeautifulSoup(response, 'html.parser')
site_title = html_content.title.string
site_title = site_title.strip()</blockquote>
<h2>Added Form Fields</h2>
I now added Form Fields into the output as well. This is every field within the <strong>&lt;input&gt;&lt;/input&gt; </strong>tags on the page (thanks Beautiful Soup). This allows for easy filtering of sites with forms (and without), and what those forms actually ask for.

The script only visits one page, the root directory of the hostname. If the form were on a separate page, say <strong>/login.asp</strong>, the script will miss it.
<h2>Added Domain in the CSV</h2>
The CSV now has a the domain (not sub-domain) of the site. This allows for easy filtering/pivoting of hostnames from a particular domain like <em>selangor.gov.my</em> or <em>melaka.gov.my.</em>
<h2>Added an API</h2>


![](/uploads/everybody_gets_an_API.jpg)



The biggest change is that I added an API to the project. Currently only one end-point is exposed, which allows you to query by hostname (or more specifically Fully Qualified Domain Name). I was struggling to figure out what the 'proper' term for something like <span style="text-decoration: underline;">www.keithrozario.com</span> was, and my gut-feeling is that calling it an FQDN is more explicit and less ambiguous than hostname.

So the API end point is:
<blockquote>https://api.sayakenahack.com/siteDetails?FQDN=</blockquote>
A sample query is <a href="https://siteaudit.sayakenahack.com/api/siteDetails?FQDN=www.hasil.gov.my">here</a> and <a href="https://siteaudit.sayakenahack.com/api/siteDetails?FQDN=spr.gov.my">here</a>. The API is very much in Dev at the moment, and I'm looking for anyone willing to help me build it out (hint hint!). Contact me via email if you want to help!

Also you'd notice the API is hosted on a familiar domain, I'm not made of money you know -- so I have to reuse domains! If I had $12.00 to buy the domain, I'd buy the Shodan scan instead.
<h2>Full Results</h2>
Finally the full results are located in the output/ folder of the <a href="https://github.com/keithrozario/Gov-TLS-Audit">git repo</a>. The coders among you will also notice that the repo has been substantially cleaned up, and now contains an extra folder called <em>lambda/</em> which includes all the lambda functions and API Gateway configurations. I used the <a href="https://serverless.com/">serverless framework</a> to deploy this which means, you can deploy this thing yourself with just a single <strong>sls deploy</strong> command.

If all this git stuff is scary to you (I know the feeling!), here's the full results in a more <a href="/uploads/output.zip">human readable format (hint: use the csv file)</a>
<h2>Next Steps</h2>
The plan is to run these scans every week on Sunday, and continuously upload them to the back-end database (running on the ever impressive DynamoDB). Also, I need to create some sort of page that will query the API via a nice GUI. That will take time :)

Finally Next week, I want to write a post about the architecture of siteaudit (I initially wanted to call it jangankenahack, but thought against it).

Nothing's perfect, and there's always going to be something to improve/refactor/tear-apart. It's sometimes scary putting code onto a public repo (lest someone criticize you online), but I find that I hold myself to a higher standard when I know others can view this. It's a good way to improve myself, and a perfect way to get some good honest feedback!

So let the insults roll in -- I can take it!
<h2>What can the government do?</h2>
To be fair, the government is probably trying it's best, and IT is hard to get right. But if they were to ask me, the first step is killing all sites that are 'zombies', and slapping TLS onto sites that aren't. Some of these sites are clearly corpses that have been forgotten, the certs on some sites were issued when <del>Mahathir was Prime Minister</del> Arsenal was winning the Premier League, obviously these aren't being used anymore.

For the sites that are still active, we should just slap TLS onto all of them (with no exceptions).

The easiest way to do this is to add CloudFlare, or if they're paranoid over having a foreign CDN, they can just use Let's Encrypt to generate the certs. Let's Encrypt installation will actually 'correctly' configure the webserver (Apache/NGINX etc) to redirect users from http to https. There are even Windows PowerShell scripts that integrate with it -- though you might want to run this on a Dev Domain before doing this on the production site.

Come July this year, Google will start flagging 954 of the 1324 sites as "Not Secure", something we definitely don't want on Government sites.

And it's not that we think Google are Masters of the Internet that decide what's Secure, It's because if a site hasn't configure TLS properly, it probably more serious configurations issues underneath that would make it susceptible to breaches and hacks!

Security is a process not a end-state, and we should start getting on that process, lest we want breaches of government data to more common.