+++
title = "Omg I See the Light"
date = "2026-02-21T08:57:34+08:00"
draft = true
categories = ["agents"]
description = ""
showFullContent = false
readingTime = false
hideComments = true
+++

We just celebrated Chinese New Year here in Malaysia, which for means a roughly a week of eating and visiting relatives. Fortunately, I don't have much travelling as my wife an I come from the same town, and my in-laws and parents live less than 5 minutes drive from each other. So after landing from Singapore and making the short trip from Subang airport to Klang, the celebrations could commence.

I took advantage of the downtime to really get into the weeds of Coding assistants, and boy did I finally see the light. It's crazy!

I first used Gemini-Cli to help me code up a federation from GCP to AWS. As a GCP employee I get access to Google cloud resources including compute engine. But sometimes I need to federate into AWS to do some stuff there, and rather than copy over static keys (ugh!), I managed to get federation working. Gemini helped a bit with the federation, but where it really shined for me is modifying a Python script I wrote into a Go binary. Python is awesome, but getting a Python script (with dependencies) to run in a cronjob wasn't ... nice. Instead I used Gemini to give me a binary that could run without dependencies in isolation. I'll blog about the federation some time later.

Then mid-week, I decided to do some cleanup work on [Klayers](https://github.com/keithrozario/klayers), Klayers is my most popular project on Github (by far!), but it was showing it's age. Every year I need to do some tweaks to it to support newer Python Versions. Unfortunately, I've been slacking too much It's been nearly 2 years since my last update for Python 3.12.

But with Gemini I was able to get it to wrangle through this complex piece of code that used an outdated version of the Serverless Framework, Terraform and Github Actions all. I wrote some documentation in the repo to help me, but Gemini managed to not only figure it out, but re-write the documentation for better future implementations.

Finally, I also installed GasTown, and here's where things really got crazy. With less than 20 prompts over 2 days (off and on between house visits), I was able to spin up Sanction-Screener. Sanction Screener is a simple project that:

* Ingest an giant XML called the OFAC SDN List (a list of sanction entities)
* Loads that data in denormalized form into a Big Query Table
* Allows the querying of the data, and supports typos and names that 'phonetically similar'
* Exposes that data via an API, which is a FastAPI app hosted on Cloudrun
* Has a UI that allows users to upload documents
* Contains a separate API endpoint that runs a simple LLM call to extract names from documents like invoices and Bill of Ladings
* Deployed that UI in the same Cloudrun instance
* Deploys a GCP load balancer in front of that, and host everything behind a proper domain with a TLS certificate (sanctions.krozario.demo.altostrat.com)

It's CRAZY!! All of this is a amazing work -- and all for a couple bucks of tokens and me just prompting it during my free time.

CRAZY!!

I was VERY skeptical of the AI bullshit, and I think everyone still should be. But coding is perhaps the one place it's going to seriously take off. For many reasons:

* The L in LLM stands for Language, and coding is all about languages and text
* Coding allows for the creation of loops unlike most other work, i.e. we can ask the agent to do something, and then provide them test to verify if what they've done is correct. That way the agent can iterate as long as they like until the test pass. That iteration and looping may not exists elsewhere.
* If you're writing a trilogy of stories set in ancient times, you can't just re-write Lord of Rings. But if you're writing a piece of code to do 'X', it's perfectly reasonable to copy code that does 'X' from somewhere else, or if you're doing 'Y' which is just slightly different to 'X', you can copy all of 'X' and tweak accordingly.

Ironically it's the 'high-value' coding work that is most impacted by AI. Which is both scary and exciting. It's so wonderful to live in this precise moment, where I have just enough experience pre-LLM to be able to guide the bots to do the right thing -- and just enough runway left on my career to see how things will turn out, and hopefully ride the wave all the way.

What a blessing.
