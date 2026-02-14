+++
title = "Cracking Passwords with the Cloud"
slug = "cracking-passwords-with-the-cloud-vertical-vs-horizontal"
date = "2012-08-20T19:56:34"
draft = false
tags = ['Accent', 'Amazon']
categories = ['Cloud Computing']
+++



![](/uploads/Cracking-with-the-cloud-300x225.jpg "Password Cracking with Cloud Computing")

I  remember my computer security professor telling me that encryption doesn't make it <strong>impossible to decrypt</strong>, but rather <strong>infeasible to decrypt</strong>. Nobody is going to buy a supercomputer to crack your final year thesis, simply because the data isn't worth nearly as much as the cost to crack it--thereby making it infeasible.

With cloud computing, however, end-users and regular joes like us, have access to very very powerful machines for a fraction of their actual cost (since we're only renting the machines). Couple that with the high scalability of the cloud , it means that what was previously infeasible, is now a very viable option. In fact what used to be only available to big corporations and governments, now has become available to anyone with a credit card and Amazon account.

I'm not talking about complex mathematical approaches to breaking encryption either, I'm talking about the standard brute force method. Brute Force basically involves trying every single possible password until you eventually find the password that works. In the past brute force wasn't considered a valid option since trying all those passwords which number in the hundreds of billions, would require a very powerful computer, and most people--not even criminals, had access to that sort of computing power. However, with the advent of cloud computing, powerful hardware is suddenly becoming more available to the general public for low-down prices. What use to cost tens of thousands of dollars per server now cost just 2.60 an hour to 'rent'.

What if we could use the power of the cloud to crack the average level encryption we have on our zip or excel files? Well it turns out, we can, and it's results are ridiculous!<!--more-->
<h2>Winzip encryption explained</h2>
Let's take Winzip as an example. Winzip has 3 options for encrypting a file:

1. The regular Zip encryption (96-bit)
2. AES 128 bit
3. AES 256 bit.

Unfortunately, the default option for encryption is Zip encryption (96-bit)--<strong>and that's not safe AT ALL</strong>. AES is still relatively safe, but ultimately the security the password provides depends on both the <strong>password itself</strong> (1234 is not a good password), the <strong>type of encryption you use</strong> AND the <strong>value of your data</strong>.

Further on, I'm going to show you how I used an Amazon EC2 instance to crack an 8 character password on Winzip in just 0.25 seconds.
<h2>Brute Force Explained</h2>
Let's say for example you had an 8 character password that consist of only lower case letters--I would have to try a maximum of 235 million passwords, and I'm talking about trying all combinations from 1 character long up to 8 characters in length.

If instead you decided to mix things around, and include upper case letters as well, that improves from 235 million to <strong>53 TRILLION</strong> possible combinations.

Finally if you include digits and special characters , that would result in almost <strong>7 quadrillion possible combinations.</strong> (a quadrillion = 1000 Billion).

Now these all may sound like a lot, but if you really wanted to crack these passwords, its actually straightforward. You just need more computing power, it's not a matter of trying to think outside the box, it's actually a straight forward solution--if you want to crack the password quicker, all you need are more powerful machines trying all those possible passwords.

The goal is to increase the rate of your attempts, measured in passwords/second. The more passwords/second you can process, the less time it'll take you to decrypt the file.
<h2>How does cloud computing fit in?</h2>
Most users don't have really powerful machines at home, High performance today, may mean mediocre performance next month, so a lot of people buy mainstream performance machines as a matter of practicality and cost--but what if you could go the Amazon cloud and rent a really powerful machine.

In fact,  I'll be spinning up the most powerful Amazon cluster instance there is--<strong>The Quadruple Extra Large Cluster GPU instance</strong>--almost sounds like something from McDonalds. You might wonder why I used a Cluster GPU instance instead of a cluster CPU instance, well in turns out your Graphics Processing Unit (which usually resides in your graphics card) is more attuned to parallel processing than your Computer Processing Unit (CPU). In fact using a GPU to crack passwords has provided results magnitudes of times better than using a plain CPU attack.

As of right now, a lot of companies out there have created software that utilizes your GPU to crack passwords rather than your traditional CPU. An example of such software is the Accent Zip Password Recovery Tool, it utilizes your GPU instead of your CPU cores to crack the passwords resulting in nearly 1000 times better performance.

So let's take a look at what the cloud offers.
<h2>Cracking a ZIP password using GPUs</h2>
First I spin up a Windows instance of the <strong>Quadruple Extra Large Cluster GPU</strong> instance<em> (I never tire of saying that).</em>

Then I install <a title="Accent Zip Password Recovery Tool" href="http://download.cnet.com/Accent-ZIP-Password-Recovery/3000-2092_4-75185227.html" target="_blank">Accent Zip Password Recovery Tool</a>.I choose a pretty simple Zip(96-Bit) encrypted file, and finally I hit Run.



![](/uploads/ZipLOck.png "ZipLOck")

And the results are in, I was cracking this file at a rate of<strong> 827 MILLION passwords per second</strong>, and since I used a trial version of the software only 1 of the 2 GPU devices on the cluster were used. Had I used the commercial version, my average speed would have reached the <strong>1.5 Billion mark</strong> -- easily.

What this means is the 235 million all lower case letter combination, would be cracked in about 0.25 seconds. So if you're wondering how secure an 8 letter password of lower case letters on a Zip algorithm is-- <strong>well it cost me just $2.60 US Dollars and 0.25 seconds of my time.</strong>

Similar test for AES-128bit and AES-256bits, yielded a much lower speed of 280,000 passwords per second. Again this was just 1 GPU the full version of the software would at least double this to 550,000.

In conclusion, with a cost of USD2.60/hour I can crack a Winzip passwords at 1.5Billion passwords/second or AES password at 550Thousands passwords/second.

Now you could buy a powerful machine for about Rm5000 to help you, but then again you'd be limited to just one machine.
<h2>A quick word about Accent Password Recovery</h2>
Unlike traditional password crackers, Accent utilizes GPUs rather than CPUs to accomplish it's goal. GPUs are far more attuned to the processing requirements of password cracking, to the tune to 100s (if not 1000's) times quicker.

Accent offers a free trial to test out their tool, but it's very limited functionality meant I couldn't fully crack a file. In their defence most of Accent's customers are probably one time only users who download the tool to crack a zip file they encrypted with a password so secure--even they couldn't access it anymore.

The tool is remarkably simple, and appears effective, with mind-blowing speeds on the Amazon GPU cluster, however it will cost around $40.00 for the full version, and so far from my Nuffnang adverts I've only made $0.75 cents :), so I can't really afford to buy the full version just yet. But if you have a zip file you need cracking, I'd definitely recommend this.
<h2>Scaling the Cracking</h2>
Cloud Computing isn't about buying just 1 machine, it's also about scaling up, buying lots and lots of machines for short burst on demand.

Cloud Computing introduces the concept of a Machine-Hour. Every computational process could be quantified by machine hours. And if you want something done in less hours, just buy more machines.
So let's say we can we have a file protected by a 8 Character password comprising of upper and lower case letters, and for simplicity sake, let's say it'll take an Amazon Extra Large Quadruple Cluster 56 Hours to crack the password. You've been given a strict mandate to crack the file in one hour. All I need to to at this point is spin up extra machines on Amazon, since every computational process can be quantified by machine hours, <strong>the more machines I have, the less hours I need</strong>.

For example, I could spin up 56 Amazon machines two for each letter of the alphabet (upper and lower case), and then have them work on passwords starting with the letter their assigned to. So one machine would try all passwords starting with 'A' , and another trying all passwords starting with 'a' and then so and so forth for 'b','B','c','C'....all the way to 'z' and 'Z'.

56 machines in total, requiring just one full hour of cracking per machine.

Before cloud computing, the only way to do this was to actually BUY 56 different machines--that's expensive. With cloud computing it could cost just USD2.60/machine-hour. That's cheaper than buying even one machine. The best part is, since Amazon charges per machine-hour it'll cost the exact same amount but in far less time. Of course, I've neglected the setup time taken to split the load among the 56 machines, but for simplicity sake let's say it was negligible.

This is of course a case of Vertical vs. Horizontal, buying more machines from Amazon is a straightforward way to crack a password in a short amount of time, provided you have pockets deep enough to pay Amazon at the end of the month.



![](/uploads/Vertical-vs.-Horizontal-1024x576.jpg "Vertical vs. Horizontal")


<h2>How about Scaling against the harder to crack passwords</h2>
For a real world example, let's take the 53 Trillion combinations for upper and lower case passwords. Now if you protected the password with a AES-256bit password, doing a bit of math leads us to a total cost of <strong> 26,700 machine-hours.</strong>

Sounds like a lot? Well it is, but remember that with cloud computing and a smart enough programmer you could spin up 1000 machines on Amazon and it'll take just 26.7 hours to crack the password. That doesn't sound like a lot anymore.

Technically you could spin up 10,000 machines and it'll cost you 2.67 hours ...so on and so forth--ad infinitum. Up to a point where it'll take just minutes to crack the password provided you could afford the machines and had the know-how.

Scaling up with the cloud basically means, cracking is no longer a matter of time--but just cost.
<h2>What about the dollar cost?</h2>
At 2.60/hour on the Xtra Large GPU cluster-- 26,700 hours would cost about $70,000 USD.

That's a lot of money, but some files floating on the internet protect data far more valuable than $70,000 USD, and of course this extends to not just Winzip, but encrypted emails and messages as well. In fact since AES is used both in Winzip and for some Email encryption, the numbers here may be reflective of how hard it would be to decrypt secured emails.

If your data was valued at $2 million dollars for example, what is the $70,000 cracking cost?

Taking it to the extreme, even the 7 quadrillion password combinations could be cracked in 3.5 Million machine-hours. That translates to just over $9 Million US Dollars. In a time where state-sponsored cyber-attacks are a real occurrence--What is $9 million dollars to a government anyway?
<h2>Conclusion</h2>
This was a real world test with real world implications.

If I get my hands on valuable encrypted data, there really is nothing stopping me spending money to spin up thousands of instances on Amazon trying to decrypt the data. In fact with cloud computing, anyone with a credit card has access to huge computational power and that opens up a the possibility of criminals cracking what used to be 'secured' data.

The cloud also provides this at low-cost, thereby reducing the barrier to entry for criminals to crack your code, so a lot of the older password mechanism like the Zip Password protect, aren't relevant anymore (unless you go to extremely complicated and long passwords, but those have their disadvantages as well).

Isn't it any wonder then, that more and more cases of hacking seem to be occurring?

Is your data secure? Have you thought about criminals using the cloud to crack it?

Will this change your organizations password policy?
<h2>Protecting WinZip Files:</h2>
Here's some quick rules I learnt about protecting WinZip files from cracking WinZip files:

1. Always use a minimum of 8 character password

2. Always use AES-256bit (never use the default WinZip encryption)

3. Mixing up upper case, lower case, symbols and digits help, but I learnt from practice that having overtly complicated passwords are both inconvenient and insecure. You're more likely to write down a complicated password than you are to write down a password composing of just words. Writing down passwords open up a new avenue for attackers to use. So try using just characters and digits, but have it around the 10-12 character mark.

4. If you're trying to protect high-value data, you really want to rely on something else rather than WinZip protection.