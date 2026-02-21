+++
title = "Reverse Centaurs and HITL"
date = "2026-02-21T10:05:26+08:00"
draft = true
categories = []
description = ""
showFullContent = false
readingTime = false
hideComments = true
+++

> A “centaur” is a human being who is assisted by a machine (a human head on a strong and tireless body). A reverse centaur is a machine that uses a human being as its assistant (a frail and vulnerable person being puppeteered by an uncaring, relentless machine).
>Like an Amazon delivery driver, who sits in a cabin surrounded by AI cameras, that monitor the driver’s eyes and take points off if the driver looks in a proscribed direction ...
>The driver is in that van because the van can’t drive itself and can’t get a parcel from the curb to your porch. The driver is a peripheral for a van, and the van drives the driver....
>Obviously, it’s nice to be a centaur, and it’s horrible to be a reverse centaur.
> -- Cory Doctorow

When you're developing with coding assistants, it's important you avoid being the reverse centaur of the agent. 

Last week, while developing a Dataflow job on GCP, for some reason the agent was unable to verify the completion of a specific job it had started. So instead, it kept asking me to verify. I was copying error messages from the console and pasting them diligently into the terminal to keep the agent happy. This process was unsurprisingly slow ... and painful!

When the human is in the verification loop, it requires every loop to be verified at human speed; this is slow. Worse yet, it wasn't a good use of my time. I was the reverse centaur, the agent couldn't verify something from within the terminal, and I was the human body for it to verify via the Console.

Instead I should have spent maybe 5-10 minutes pointing the agent to the right place to verify the logs and errors of the dataflow job, and let it iterate till success. Then (and only then), I should have verified the output and method the agent had used.

This is probably similar to work -- if an intern was performing the task, I would never accept a scenario where every single iteration of a loop needed my verification. Instead, give the intern the right tools to verify the outcome of their work, and review only after a successful run.

Reverse centaurs might be everywhere in the agentic era, we need to consciously avoid them.
