+++
title = "Domain Registration (www vs. bare domain)"
date = "2011-04-24T15:31:39"
draft = false
tags = ['NearlyFreeSpeech', 'wordpress']
categories = ['Blog']
+++

<a href="/uploads/logo.gif"><img class="alignleft size-full wp-image-144" title="logo" src="/uploads/logo.gif" alt="" width="278" height="80" /></a> As you probably know by now, I host my blog on NearlyFreeSpeech.net, they are easily the best host out there, why?

They AREEEE CHEEEEAP!! <!--more-->I mean <strong>dirt</strong> earth cheap, they make Dreamhost and Bluehost look like Louis Vuitton. How do they do it? They don't support you, Nearlyfreespeech doesn't have wannabe handholding software like cPanel, they don't support you and if you've got a question you have to pay to ask them. That's right...PAY to ASK them. They sell support points, that you buy and then redeem in the form a support question.

On the flip side.

They cost next to nothing and they're servers haven't failed me since. My first 3 weeks with them...AMAZING. Total cost? less than 50 cents (I didn't count the 9.98 for the domain registration though).

If you're hosting your first web host, I recommend them. You'll learn everything. They're FAQ may not be remarkably comprehensive (it's still good) but with a google searches here and there, you will find what you're looking for.

Now onto the question at hand, I just noticed today that while <em>http://www.keithrozario.com</em> was working perfectly well--but <em>http://keithrozario.com</em> wasn't. So if you typed in my website address and missed the www (like a lot of people do), you're likely to come to a really lousy looking start page, not the kind of first impression you'd want to make.

So I went the the FAQ and found this:
<blockquote><a name="BareDomain" href="https://members.nearlyfreespeech.net/support/faq?q=BareDomain#BareDomain"></a>I have NearlyFreeSpeech.NET DNS and <em>www.example.com</em> works but <em>example.com</em> does not. Why?
By default, this is the correct behavior. Using URLs of the form <em>http://example.com/</em> creates a number of problems, and we strongly recommend that you avoid it.</blockquote>
Nearlyfreespeech doesn't like you using it, and they give good reasons why you shouldn't, but that doesn't discount the fact that you'll want to get it done. So what's  poor old blogger to do. Further checks on the FAQ reveal the following:
<blockquote>
<ul>
	<li>You can add the <em>example.com</em> alias to your site and enable <a href="https://members.nearlyfreespeech.net/support/faq?q=CanonicalType#CanonicalType">hard canonical type</a> setting.</li>
	<li>If you have NearlyFreeSpeech.NET DNS and are using your domain with a site hosted here, you can enable this option by selecting the "Add Bare Domain Forward" action on the DNS information panel for your domain in our member UI. (This option will only appear if you are using the <em>www.example.org</em> name as an alias <strong>and</strong> you are <strong>not</strong> using the <em>example.org</em> name. If you are using it, you'll need to delete its alias from your site first.)</li>
	<li>You can create a second site that <a href="https://members.nearlyfreespeech.net/support/faq?q=ForwardSite#ForwardSite">automatically redirects</a> people to the preferred name.</li>
</ul>
</blockquote>
Not bad, so nearlyfreespeech actually offer a couple of solutions. The first solution was simple:
<ol>
	<li>Go to the Nearlyfreespeech UI -&gt;Site-&gt;Select the site in question-&gt;Add a new alias e.g. <em>keithrozario.com</em></li>
	<li>Once <em>keithrozario.com</em> appears under the Site Name and Aliases table in the site menu, click the "Set Canonical Name" <em>(on the menu on the right)</em></li>
	<li>Select HARD Canonical settings and select <em>www.keithrozario.com</em></li>
</ol>
The settings take a while to take effect, I'm guessing anywhere from 20 minutes to 1 hour. So relax if it doesn't happen straightaway (this is typical of DNS changes).

There's a problem. Once this is set I couldn't login to wordpress anymore. So I had to go to square one.
<ol>
	<li>Go to the Nearlyfreespeech UI -&gt;Site-&gt;Select the site in question-&gt; Once there delete the <em>keithrozario.com </em>alias (if you've set this already)</li>
	<li>Click on the "View DNS" button next to <em>www.keithrozario.com .</em></li>
	<li>Click on the "Add bare domain forward" button. This button won't be visible if you didn't delete the bare domain alias. e.g. <em>keithrozario.com (without the 'www').</em></li>
	<li>Once that's done. Back to the Site menu and select "Add new alias"<em> (on the menu on the right)</em></li>
	<li>Enter <em>keithrozario.com </em>as the alias. And you're good to go.</li>
</ol>
Now it works with both wordpress login and regular login.

And now the www domain and the bare domain both point the same awesome looking wordpress page!! :)