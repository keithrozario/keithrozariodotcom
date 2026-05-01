+++
title = "400 Dollars on Claude"
date = "2026-04-29T16:28:06+08:00"
draft = true
categories = []
description = ""
showFullContent = false
readingTime = false
hideComments = true
+++


Last week I managed to put the final commit on a Github repo that demonstrated something fairly esoteric in Google Cloud. The entire thing took roughly 10-12 hours, and cost just under $400 in tokens. Fortunately I work for a cloud provider and the token cost was borne by my employer -- but I can imagine how scary this would be for someone paying for this out of pocket. $400 is a large portion of most peoples monthly salary, and would actually cost more than 12 billable hours for a lot of junior developers.

Why did it cost so much?

I did go a bit overboard (as usual) with the optimizations. Somewhere around hour 1 or 2, the git repo would have demonstrated what I needed it to demonstrate, but I proceeded to spend the next 10 hours or so 'optimizing'. This included among others:

  * Moving a simple Init script to a Container image pull instead
  * Modifying the architecture to remove Cloud Nat requirements
  * Replacing an Ubuntu image with a Container Optimized image for 'security'
  * Automating the Agent deployment from Terraform instead of a separate deploy script
  * Iterating through 3-4 different things that proved to be dead ends

In the process, I developed a deeper understanding of the demo, and more importantly automated the deployment to a single `tf deploy` instead of a multi step process for the user. All that optimization cost a lot more time and tokens than the initial demo -- sometimes maybe good is good enough.

But the agents (and token cost) also allowed me continue testing the script to ensure it was bullet-proof -- so perhaps not all optimizations are superfluous. 

In the past, these optimizations were a purely a timing constraint on my behalf, today it's a timing and cost constraint. Neglecting cost, I can also tell you that I wouldn't have manually attempted any of these optimization manually -- the tokens allowed me to venture into places I otherwise wouldn't have attempted, which makes it hard for me to put a price on it.

The most interesting thing of the exercise was the cost -- at $400 this wasn't cheap. In the past, we'd argue that a $30/mo or even $200/mo subscription for a developer was only an incremental cost that could be absorbed and justified by the improved productivity. But as coding assistants start to shed their fixed price monthly fees -- they can start to cost thousands or even tens of thousands per month, equaling or even exceeding the price of the developers using them. The economic and financial decisions around something that cost are not be to taken lightly.

It's just a fact, that either organization:

* Start to limit developer access to these assistants, thereby taking a productivity hit
* Provide unlimited access to these assistants, and start looking for ways to to make up the cost, either
  * Developers start to show their cost-savings or revenue generating ability
  * Companies just hire less developers

I suspect in the short run, developers will be get 'throttled' access to these things. Monthly subscriptions that either stop working after a certain number of tokens are consumed, or provide 'distilled' and less effective models instead of the frontier ones, in both cases developers will require to start learning to work without them, and play a more active role than they would previously.

In the longer run, I think the bottom line is that less developers get hired. If every developer requires an additional $1000/mo in tokens, then developers in countries where starting salaries $1000/mo then there's only so much money to hire them. Even for larger orgs that pay their developers handsomely, say $10,000/mo, a 10% increase in employee cost has to be realized somewhere. 

And the kicker is that a lot of folks using these tools aren't developers, we'll be seeing lots of Business Analyst and Product Manager start using these tools, removing the developer bottleneck.

All of which point to fewer opportunities for developers and arguably lower demand  -- which eventually leads to lower salaries.

Maybe DHH was right -- we've already reached peak developer!






