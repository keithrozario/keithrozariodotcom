+++
title = "Creating a email for your domain using Google Apps"
slug = "email-on-google-using-google-apps"
date = "2011-04-20T12:19:05"
draft = false
tags = ['Blog Features', 'Google', 'Mail', 'NearlyFreeSpeech']
categories = ['Blog']
+++



![](/uploads/google_apps-150x150.jpg "Google_apps")

 So with the latest that the Malaysian government hopes to spend upwards of USD15 million to give every single Malaysian above 18 years of age an email address, I just noticed I have no email address @keithrozario.com

Unfortunately, Nearlyfreespeech.net (my web host) does not provide a email like other webhost do. If you've got your website hosted on goDaddy, Dreamhost or bluehost, you'll have in built email functionality. If you're with Nearlyfreespeech, you're on your own (which is why they're cheap).

That being said, Google also offers free email service for your own domain and it's much better than whatever offered by GoDaddy or Dramhost. So no matter where you host your domain, I advise you use Google Apps to host your email. Here's a quick and dirty tutorial on how to setup your Email on Google apps, and have Google host your domains email for FREE!!<!--more-->
<h2>What is Google Apps?</h2>
If you've used Gmail or Google Docs to share word documents and spreadsheets, or if you've used the new Google Drive, you've used Google Apps. The only difference is that Google offers these Apps for free for the public with some restrictions. Some organizations would like to leverage on these Apps for their day-to-day work, and these organizations pay a small fee for extra functionality which usually includes increased space, added flexibility and support.

So if I wanted an @keithrozario.com email for example. I'd need to host the email server somewhere and point my domain to this server. However, hosting any server cost money. Google on the other hand allows you to do this for free, provided you never need to create more than 50 email accounts. Any more and you'd have to start paying.
<h2>Setup email on Google Apps</h2>
If you're left out in the lurch by your hosting company and wish to have an email on your domain a couple simple steps would get you up and running. First head on over to the <a href="http://www.google.com/apps/intl/en/group/index.html">Googleapps</a> webpage . Hit the get started button and register your website.

From the Google Apps dashboard you can start creating the emails account you desire. However, you'd now need to setup a domain entries.

First, you need to 'prove' to Google that you actually own the blog, and this can be done a variety of ways including, installing the google analytics on your blog or a straightforward registration on the domain.

On Nearlyfreespeech.net I went to the domain options and added a TXT domain entry to my domain , and once that was sorted out I could tie the email to my domain.

Then I needed to add about 5 different MXs to my domain and the thing worked. Lastly I added a CNAME entry to point http://mail.keithrozario.com to my login for mail. This makes it easier for me to logon then having to go to <strong>www.google.com/a</strong> all the time.

So to recap the entries:

1) Add a TXT to the domain to link Google with the domain (you can send mail) -&gt; This is a text entry to prove ownership to google.
2) Add the <a href="http://www.google.com/support/a/bin/answer.py?answer=54719">6 MX entries</a> to your domain (you can now receive email) -&gt; this is a mail exchange entry to forward email to your domain to google.
3) Add a CNAME entry (now you can access the mail via http://mail.yourname.com) -&gt; just a subdomain re-direct.

At the end they look like this:



![](/uploads/DNS-Information-keithrozario.com-NearlyFreeSpeech.NET-Member-Interface-1024x188.png "DNS Information   keithrozario.com   NearlyFreeSpeech.NET Member Interface")

It's also important to note, that between steps (1) and (2), I could send email out but couldn't receive any. And I didn't get any error messages till I did step (2). If you were wondering why you could send email but not receive them at your domain on google apps, that's probably the reason, you haven't configured your CNAME entries.What this means is that your emails were in a state of Limbo, because your domain had no MX entries, email sent to your domain didn't know which servers to route to. Once you set the MX entries, emails lookup your domain, grab the MX entries and send the emails to anyone of the Google.com servers.

The last thing to remember is that these DNS entries take about 1 hour to take effect, so don't worry if you don't see immediate effects. You'll need to wait as much as 1 day in some cases.
<h2>How does email on Google Apps look like?</h2>
The first thing you notice is that Google Apps (at least the mail part), looks exactly like gmail. So now I have gmail functionality and gmail availability but with a @keithrozario.com email rather than a @gmail.com email. Sounds cool, and the best part of it is that it's FREE!!. Wonderful.

Other cool features are you get 25GB of space. The only downside though is that the free version comes with a limit of just 50 accounts, perfect for a blog like myself, not so perfect if you're a small size company hoping to outsource your email servers. The premium versions come with unlimited accounts @ USD50 per account per year. It's still cheaper than hosting the email yourself though I think.

Lastly, I just got word that Malaysians will be getting 25GB of free email space on the new <a href="http://www.myemail.my/what-is-myemail.aspx">myemail</a> space. Of course I can get that for free at GMail or Amazon S3 or Windows Skydrive. Another question that's on my mind is that will I want an email that is linked to the government..the answer, HELL NO!

And how does a company on the brink of bankruptcy think they can claw their way back into profit by giving every Malaysian 25Gb of free storage? What's even stranger is that the share prices skyrocketed today. More info at the myemail website, I have to say though, it's a pretty nice design.