+++
title = "My Resume on the cloud"
slug = "my-resume-on-the-cloud"
date = "2011-11-21T00:20:09"
draft = false
categories = ['Social Media']
+++

<a title="Resume on the cloud" href="http://www.keithrozario.com/2011/11/my-resume-on-the-cloud.html/keiths-resume" rel="attachment wp-att-1404">![](/uploads/Keiths-Resume-300x153.jpg "Keith")</a>The 2nd most popular post of this blog is the one about <a title="Creative Resumes" href="http://www.keithrozario.com/2011/05/creative-resumes.html">creative resumes</a>, which brings in about 300+ hits/month all on it's own, almost all of it from Google. I guess a lot of people out there are trying to get an advantage in the job market by posting up creative resumes that help differentiate them from the rest of the applicants. Personally, I'm not too sure about the creative resumes, I believe they do help differentiate you, but whether it's a good differentiating is a separate story. A lot of resumes are boring, in both context and design, but having a really well designed resume with a boring context isn't going to get you far either...(at least that's what I think).

From my perspective, it's good to jot down a couple of key interesting points about yourself that you think might land you a job, and then form a consistent 'brand' around those key points. Then make sure what you say online, what's in the resume and what's in the cover letter all gel together to project those key points, making it a differentiating factor that will be your brand. However, that's a topic for a separate day. Today, I'd like to show you how I shared my resume online using Amazon Simple Storage Service (S3). <!--more-->

Previously, I blogged about how you can host <a title="Hosting a Web Page on Amazon S3" href="http://www.keithrozario.com/2011/10/hosting-web-page-amazon-s3.html">a static html website on your S3 account</a> to share wedding photos..etc etc, and it dawned on me, that a static website is a great way to host a resume website. Now there are a lot of really cool resume designs in html that you can find online, my favorite is the <a title="Azuka" href="http://www.csstemplatesfree.org/azuka.html" target="_blank">Azuka template</a>, created by <a title="http://www.chris-creed.com" href="http://www.chris-creed.com" target="_blank">Chris Creed</a>. The template is great on so many levels, but the greatest design advantage of the template is it's simplicity. The template to me, is perfect for newbies to play around with (like myself) and still project a very professional image, plus I'm really a minimalist at heart and judging by Chris website, so is he.

So the first thing I did was download the template and modify it to fit my needs, obviously I added my own photo and then created a space for a QR code at the bottom. Now there's really no practical reason to place a QR code on an online resume, but I'd thought it looked cool and it's my resume so I'll do what I want (<em>thank you very much!</em>).

The next thing I did was strip out everything on the resume except the summary and the contact information. To me, most hiring managers and recruiters aren't going to be reading the resume online, and the only thing I wanted to do was to provide a summary that was consistent with my brand and contact information. This was my online resume.

I also added download links to my 'actual' resume in pdf and word formats. The way I see it, if the recruiter is really interested, than they'll download the 'actual' resume and distribute that or use that for reference, the online resume is just meant as a 'placeholder' for my resumes online presence (separated from my own online presence on this blog). I'm still working out the chinks in this approach but to me a Business Analyst doesn't need an online portfolio or a full blown resume in html format, and what I have as the placeholder website for my resume is good enough.

Finally I created and drafted a resume in both pdf and word formats and omitted my phone number (simply because this resume would be freely available). I also needed to ensure that the resume didn't contain sensitive information that I didn't want to divulge to the public, so if you're thinking of placing more sensitive contact information or salary expectations, I recommend you omit those as well.

Then I added the two icons in a prominent position on the online resume and was pretty happy with the results. The link to the online resume is <a title="http://resume.keithrozario.com" href="http://resume.keithrozario.com" target="_blank">http://resume.keithrozario.com</a>

<a href="http://www.keithrozario.com/2011/11/my-resume-on-the-cloud.html/keiths-resume-2" rel="attachment wp-att-1405">![](/uploads/Keiths-Resume1.jpg "Keith")</a>

Now comes the tougher part....hosting it online on the cloud.

Since the resume is in HTML format, I simply created an Amazon S3 bucket called <strong>resume.keithrozario.com</strong> and then copied all the files into the S3 bucket.(don't worry a link to my files is <a title="Resume Download" href="https://s3-ap-southeast-1.amazonaws.com/resume.keithrozario.com/downloads/Resume.zip">here</a>)

Then I made the files public, and set the website setting of the bucket to enabled with the index document set to <strong>index.html</strong>

Finally, I created a CNAME entry pointing <strong>resume.keithrozario.com</strong> to the amazon S3 endpoint for the bucket. Remember, the bucket name has to the same as the CNAME entry for this to work. For instance, if I renamed my bucket to keithsresume, then this wouldn't work <em>(or at least I wouldn't know how to make it work)</em>.

So, if you plan to route all traffic from <strong>resume.example.com</strong> to your amazon S3 bucket, you need to name your S3 bucket <strong>resume.example.com.</strong>

It was pretty easy, and I'm really satisfied with the results.

An Alternative to CNAME entry, is that if you don't have a domain name (which you should), then instead of purchasing a standard .com domain for around 9.95/yr, try namecheap.com where they're offering .info domains for just 2.99/yr. That's pretty decent, and you can create a shortcut from the domain directly to the Amazon S3 endpoint. In case you don't know what the end point is, select the bucket in question, right-click on properties and then select website. So hosting your resume would be super-cheap and would look pretty good.

Currently I have both these setups in place so <a title="Resume" href="http://resume.keithrozario.com" target="_blank"><strong>http://resume.keithrozario.com</strong></a> &amp; <a title="Keith Rozario" href="http://keithrozario.info" target="_blank"><strong>http://keithrozario.info</strong></a> both take me to the same location , which is the index.html file of my S3 bucket.

You might also want to think about <a title="Analytics for your blog" href="http://www.keithrozario.com/2011/04/analytics-for-your-blog.html" target="_blank">installing google analytics</a> to see whose looking at your resume, and setup logging on the S3 bucket to see whose downloading it.

If you want a copy of the HTML template, <a title="Resume.zip" href="https://s3-ap-southeast-1.amazonaws.com/resume.keithrozario.com/downloads/Resume.zip" target="_blank">here it is</a>. Please pay tribute to <a title="Chris Creed" href="http://www.chris-creed.com/" target="_blank">Chris</a> , and it'll be great if you could pay tribute to me as well :)

Next step, ensuring my resume is consistent with the brand I want to project....and firstly is to figure out what exactly is my brand.

After that, get a better picture, the picture there is a crudely cut up from one of wedding pictures.