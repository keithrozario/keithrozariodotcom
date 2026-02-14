+++
title = "The miners dilemma - Bitcoin sabotage can be profitable"
slug = "bitcoin-miners-dilema-sabotage-profitable"
date = "2016-02-27T12:07:32"
draft = false
tags = ['BitCoin']
categories = ["Keith's Favorite Post", 'Security &amp; Privacy']
+++



![black dice](/uploads/black-dice.jpg)

Imagine a small village of a 100 people.

One day,  a sorcerer shows up,  and grants all the villagers magical 1000-sided dice, which are purely random and can only be thrown at a fixed rate of 1 throw per second (no faster &amp; no slower).

Over the next year, at noon of every day, the sorcerer will announce a random number between 1 and 1000, and the first villager to throw that number on their magical dice will earn $100, just by raising than hands and announcing it to the wizard.

The villagers play along, and the since the dice are purely random, each villager can expect to win $100 every 100 days.

But if they pooled their dice together they could create interesting scenarios. For example, a group of 10 'pooled' villagers, could expect to win once every 10 days, and the winnings of $100 could be equally divided between them. To these villagers $10 every 10 days is a better deal than $100 every 100 days.

Eventually the village ends up with 2 pools of 50 villagers each. The pools expect to win once every other day, and the winnings would be $2 dollars per villager. So effectively, they're winning $2 every 2 days.

So far so good.
<h2>The Crooked Pool attacks</h2>
![crooks](/uploads/crooks.jpg)However, one of these pools (called the crooked pool), starts to act all dick-dastardly. They send 25 of their members to infiltrate the other 'honest' pool. These infiltrators will roll their dice, but never claim announce their winnings to the sorcerer, even if they roll the magical number. Essentially these <strong>infiltrators</strong> become dead-weight on the honest pool, rolling dice choosing to never win. The remaining 25 members in the crooked pool will continue rolling and trying to win.

At first this seems illogical, why would a pool intentionally give up half it's resources to sabotage another? How could discarding winnings actually benefit anyone? Does it even profit the crooks?

Yes it does:
<ul>
	<li>The crooked pool now has 25 villagers rolling dice;</li>
	<li>The honest pool has 75 villagers, but only <span style="text-decoration: underline;">50 of them are effectively trying to win</span></li>
	<li>Don't forget, the crooked pool has 25 members in the honest pool, and hence is entitled to 1/3rd of their winnings.</li>
	<li>Which means the original 50 villagers in the honest pool, only get 2/3rd of their winnings.</li>
	<li>With only 75 villagers effectively throwing the dice, the crooked pool now has both it's original 25 members and a 1/3rd share of the remaining 50.</li>
	<li>The maths is only a 'bit' complicated, but the result is the crooked pool <span style="text-decoration: underline;">increases its chances of winning from 50% to 56%</span>.</li>
</ul>
Amazing right?! Even though the 25 infiltrators are essentially wasting their throws, they can actually profit from the activity.

This isn't just a thought experiment either, this is a problem known in bitcoin as the <a href="http://hackingdistributed.com/2014/12/03/the-miners-dilemma/">miners delimma</a>, analogous to famous <a href="https://en.wikipedia.org/wiki/Prisoner%27s_dilemma">prisoner dilemma</a> thought in game theory. Bitcoin mining works almost exactly like this scenario, it is a purely random function similar to dice throwing, whose odds of success can only be increased if you ramp up the hashing power, or in this case, adding villagers to a pool.<!--more-->
<h2>The crooked pool vs. another village</h2>
But let's go back, and change some of the rules. Instead of announcing a new number once a day,  the magician now announces a new number as soon as the previous number is thrown. In this case, the crooked pool would still be <em>relatively better off than the honest pool</em>, <strong>but</strong> it would be <em>absolutely worse off</em>, since it's getting <span style="text-decoration: underline;">55% of 75 villagers</span> instead of <span style="text-decoration: underline;">50% of 100 villagers</span>. Over the course of a year, the crooked pool stood to gain more money acting honestly, than if sabotaged the other pool.

But bitcoin mining difficulty is re-calibrated over time to ensure that a new block (and coin) is mined once every 10 minutes, so this scenario isn't related. Another difference is that bitcoin's mining pool isn't equally divided between two pools either, it's divided among many different pools.

So imagine the original rules, but introduce another village of 100 people. So that there are 200 villagers trying to win everyday.

Once again the crooked pool using it's sabotage plan would be 'relatively' better off than it's honest counterpart in the same village, but would be absolutely worse off.

In the honest strategy, the crooked pool had 50 villagers from a total pool of 200, and stood a <span style="text-decoration: underline;">25% chance of winning</span>. In the crooked strategy, they have 56% of 75 villagers out of a pool of 175 (effective), resulting in a lower <span style="text-decoration: underline;">23% chance of winning</span>.
<h2>The Honest pool retaliates</h2>
Now things get really interesting, if the original pool realizes that they've been infiltrated, they may choose to retaliate, sending 25 villagers over the crooked pool to sabotage them.

Relatively, both pools in the same village are now equals, but they're diminished their absolute position, effectively winning half of what the other honest village is earning. Ittay Eyal, who wrote extensively about this (and other bitcoin phenomena) explains eloquently:
<blockquote>In the classical prisoner's dilemma two partners in crime have to decide whether to testify. If neither testifies, they both go to prison for a year. If one testifies, he is released and his partner is imprisoned for 5 years. If both testify, they are both imprisoned for 2 years. So testifying is a dominant strategy; a prisoner will be better off testifying whatever his partner does. However, if they follow the dominant strategy they end up in a tragedy of the commons where both are worse off than if neither testifies.

The situation in the pool's case is similar. If neither attacks, they both work fairly and their miners earn what they deserve. If one attacks, it improves its revenue, and the revenue of the other deteriorates. If both attack, at equilibrium, each earns less than if neither had attacked, but more than if only the other had attacked. Attacking is therefore a dominant strategy. <span style="text-decoration: underline;"><strong>A pool will improve its revenue by attacking, whether the other pool attacks or not.</strong></span></blockquote>
<h2>Conclusion</h2>
Although most of this work shows some weakness and flaw within bitcoin, I was thoroughly interested in a situation where intentionally doing useless work could benefit you under certain scenarios. Hopefully bitcoin and <a href="http://hackingdistributed.com/ittay/">Ittay Eyal</a> have more interesting scenarios to share.