+++
title = "Death of Saas"
date = "2026-11-11T18:34:55+07:00"
draft = true
categories = []
description = ""
showFullContent = false
readingTime = false
hideComments = true
+++

Imagine you own a small gym, and you pay x dollars per member for a SaaS that helps maintain the memberships, invoices them, sets up personal training sessions etc. Typical CRM stuff.

Then one day you decide that "hey, I can build this thing myself using Claude and save a tonne of money", and so you buy some Anthropic subscriptions and then build your own gym app, over the weekend.

Maybe you always wanted 50 minute sessions for your personal trainers instead of an hour, and maybe you wanted to offer members the ability to pay every 7 months instead of 6. In the old SaaS you were limited by it's features, but in this world where you're building your own app, every feature is just a prompt (and tokens) away.

So even after spending a few thousand dollar on tokens, you get a full production (maybe!) grade app that fits your needs, and over the long run you'll save more money because you're not spending dollars per member to some SaaS company that operates for profit.

But....

Running software in production is ... HARD.

And with AI the problem just got harder.

Consider the [case](https://www.bbc.com/news/articles/cn0nww2qlp7o) of an AI agent that was tasked by it's human user to book a pilates class. Instead of booking like a normal person, the agent instead hacked into the gym system, kicked our existing reservations, and gave it's user the slots they desired.

Before AI, a gym in some Australian city, didn't have "get hacked by frontier model" on their top list of cyber threats -- but now every gym in the world is going to run into a similar problem. And it's not just gyms, if you've got some stuff facing the internet (which is nearly everyone), this is a real threat.

Operating a gym member portal just got harder, and a singular gym probably doesn't have the capacity or capability to address this. You need someone whose sole purpose is running software for the gyms, who can then run and maintain this software and keep up the infra ans security requirements.

Maybe that person will charge the gym x dollars per member to recoup its cost of operations.

In other words you need a SaaS.
