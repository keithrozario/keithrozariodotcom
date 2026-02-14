+++
title = "The Monty Hall Problem in Excel"
date = "2014-06-07T17:06:05"
draft = false
tags = ['MontyHallExcel']
categories = ['Misc', 'Science']
+++

<img class="aligncenter wp-image-4396" src="/uploads/Monty_Hall_Problem_Excel-1024x489.png" alt="Monty Hall Problem Excel" width="550" height="263" />

I remember this problem from watching an episode of numbers. You're a contestant on a game show--and you're given 3 doors to choose from.

Behind one door is a shiny new sports car--behind the other 2 are goats. Your goal is to get the sportscar, by choosing a door. But after you choose a door the host reveals one of doors with the goats. Leaving you with you just two doors, instead of your initial 3.

The choice is now yours again--do you switch doors or do you keep your initial choice--or do you think it doesn't matter.

Think about it.

The answer is that's is always better to switch, in fact your two times more likely to win the car if you switch than if you don't. There's  a quick video at the bottom of the post, outlining the problem, but here's an <a title="Monty hall problem Excel" href="http://www.keithrozario.com/wp-content/special-uploads/Monty_hall_problem_Excel.xlsm" target="_blank">excel spreadsheet </a>simulation I coded with some macros to help you visualize the problem.

All you have to do is enter in how many games you want to play (the default is 1000), and what kind of switching you want:
<ul>
	<li>YES - Switches the choice everytime</li>
	<li>NO - keeps the initial choice door everytime<a href="/uploads/Monty_Hall_Problem_Excel.png">
</a></li>
	<li>RANDOM - randomly selects a door from the remaining 2 doors</li>
</ul>
Then you can see how many games you would have lost or won based on your strategy, and it's clear that switching is twice more successful than keeping. To download the spreadsheet click <a title="Monty Hall Problem Excel Macro VBA" href="http://www.keithrozario.com/Monty_hall_problem_Excel.xlsm" target="_blank">here</a>.

One way to think of it, is that your initial choice has a 1/3 chance of winning the car. Meaning you had a 2/3 chance of losing. So your initial choice was most likely wrong, and switching after the a goat is revealed flips your chances of winning from 1/3 to 2/3.

<center><iframe src="//www.youtube.com/embed/4Lb-6rxZxx0" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe></center>