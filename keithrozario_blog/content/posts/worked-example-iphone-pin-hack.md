+++
title = "Worked Example: iPhone PIN Hack"
slug = "worked-example-iphone-pin-hack"
date = "2015-04-10T22:00:24"
draft = false
categories = ['Security &amp; Privacy']
+++

Last month, a company called <a title="MDSec Bruteforcing iOS PIN unlock" href="http://blog.mdsec.co.uk/2015/03/bruteforcing-ios-screenlock.html" target="_blank">MDSec released a video </a>detailing how they manage to brute force hack an iPhone PIN lock. Pretty sweet piece of work, but I thought this would be a good example to understand how hacks work, and how hackers think.
<h2>What is a hacker</h2>
First off, we need to define what a hacker is, it's a convulated term, but my favorite definition is :
<blockquote>A hacker is someone who makes system work in an unintended way, because they know have a deep knowledge of the underlying mechanism of the system.
<p style="text-align: right;">-Keith Rozario (wannabe tech blogger)</p>
</blockquote>
I took great pains to avoid terms like technology and computers, because hacking isn't purely confined to these areas (unlike what other think). For example, Jazz musicians are hackers, they make music work in unintended ways, because they know how music works. You can't just string a couple of notes, and melodies together hoping to get a Jazz piece, you need to have a understanding of music before you can ad-lib your around notes and keys, and produce something that is pleasing to the ears. In music it's called improvisation,in tech we call it hacking.

Fusion cooking is another example, Asian Sambal wasn't meant to go with Chicken chops, but somehow chefs make it work (at least some of them do), but you can only do this if you understand things like flavor, taste, and texture work. Otherwise you end up with disgusting combinations like Nasi Jam Strawberry, or Black pepper goreng pisang.

Things in technology are designed to work in a specific way, like asking for username and passwords before granting access, but hackers get the technology to produce unintended results (like allowing access without the credentials)by passing certains steps and processes, because they know what those steps and processes are. For example the iPhone PIN hack I mentioned in the opening paragraph.

<!--more-->
<h2>Iphone Pin lock (happy path)</h2>
Take a look at the iPhone lock screen. The screen prompts users for a PIN that is usually 4-8 digits long, if the PIN is correct, then the phone unlocks, if the PIN is wrong, then it doesn't unlock.

In addition,  the iPhone that completely wipes the phones memory if an incorrect PIN was entered 10 times in a row. In other words, if you fail to remember your iPhone PIN after 10 failed attempts, the phone literally destroys itself ala Peter Grays Mission Impossible tapes.<em> (If you don't know what this tape will self-destruct in 5 seconds means, I must be getting really old)</em>

This is what (I think) the flow would look like:



![iPhone-Pin-hack (2)](/uploads/iPhone-Pin-hack-2.jpg)



It's quite a straightforward flow, at each PIN entry, the phone checks if the PIN is correct, if it isn't the phone remains locked, and a PIN counter is incremented by one. Once the PIN retry counter has reached 10, the phone will wipe out its contents.

The rationale of wiping out the contents is clear, if you allowed an unlimited amount of retries, than an attacker would just need patience to try every possible combination, but limiting the retries to just 10, gives a guessing attacker a 1/1000 chance of guessing the right PIN.
<h2>The Hack</h2>
But some rather smart guys over at MDSec, discovered that if you cut the power to the iPhone before the phone could increment the PIN retry counter,  but after it has confirmed if the PIN is wrong or right...then you'd be able to brute-force every combination while keeping the PIN retry counter perpetually set to zero.



![iPhone-Pin-hack-mechanism](/uploads/iPhone-Pin-hack-mechanism.jpg)



Essentially by cutting power to the phone before its able to increment the PIN retry counter, you'll  be able to brute force every possible combination without worrying about the phone wiping itself clean.

Pretty neat huh!

And this is what hacking is all about, trying to 'game' the system, and get it to do unintended things.

Apple however, have fixed this with iOS version 8.1.1, and while I don't have details of how the solved it, here's some ways you could go about it.
<h2>The fix (incomplete)</h2>
The first thing you would do, is just bring the process to increment the PIN retry counter BEFORE the PIN is validated. This would give the attacker little chance to bypass the PIN counter increment.

But as you can see in the diagram below, we still have a problem. An attacker could still cut the power once the iPhone confirmed that the PIN was correct or not, and the Phone wouldn't wipe itself.

Essentially this only addresses half the problem, because while we made it impossible for the attacker to bypass the PIN retry counter increment, it's still possible to bypass the Phone wipe, which is really the root cause of the problem. In this partially fixed scenario, the PIN retry counter would indeed increase after every PIN entry retry, but it wouldn't mean anything because the phone would never reach the point of the code where it would wipe the code. The counter could reach to infinity and it wouldn't make a difference.



![iPhone-Pin-hack-incomplete-fix](/uploads/iPhone-Pin-hack-incomplete-fix.jpg)


<h2>The final fix</h2>
The final fix is the full one, where the PIN entry counter is incremented BEFORE the PIN is checked.

AND the Phone Wipe is check is also done BEFORE the PIN is checked. By moving the PIN check to the very last step of the process, we eliminate these bypasses because in order to reach the PIN check, which the attacker must do in order to determine if the PIN was valid or not, the process must flow through each check first. If the attacker cut the power on any of the checks, the process would never reach the PIN validation stage, and it'll be pointless to continue.



![iPhone-Pin-hack-complete-fix](/uploads/iPhone-Pin-hack-complete-fix.jpg)


<h2>Conclusion</h2>
I thought this was a really cool worked example about security, and there a couple lessons we can take.

Firstly as a consumer, 4-digit PINs are a definite no-no. They're too easy to brute force, and offer little security. 6-digit PINs are just 2 extra digits to remember, but offer 100 times more protection. So in 2017, when Malaysia introduces PINs for our credit card remember to at least choose 6-digit numbers.

Secondly, look at the first example, it looked good enough, until you put yourself in the mind of a hacker. A hacker isn't satisfied with the way things are, they're only interested in the ways things could be. In order to build full-proof systems (or at least near full-proof systems) you'll need to attack the systems you build, and in most cases let others have a go. This is why companies pay through the noses for penetration testers to break their own systems, so at least they know what's going on. Some call this 'ethical hacking' , I prefer the more apt term 'security research'.

Thirdly, look at the flow that we started with and the flow that with ended with. The both accomplish the same thing, but one is more secure than the other. There are many ways to build things in IT, but there are much fewer ways to build them securely.

Finally, compare the differences between the two flows, looking at one very simple example, you can straight away see the amount of work it would take to rewrite code from the starting point to the end state. Fixing bugs and issues, sometimes require complete re-design to properly address the code, and that's why it may take some time to implement something which on a high level looks trivial. That being said, don't take excuses from your vendors when they refuse to fix stuff because it's too complicated.

Hopefully this was a good example of how issues are found and addressed using a real-world public released vulnerability, hope you enjoyed it.