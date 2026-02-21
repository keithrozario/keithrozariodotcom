+++
title = "Reverse Centaurs and HITL"
date = "2026-02-21T10:05:26+08:00"
draft = false
categories = ["agentic"]
description = ""
showFullContent = false
readingTime = false
hideComments = true
+++

> A “centaur” is a human being who is assisted by a machine (a human head on a strong and tireless body). A reverse centaur is a machine that uses a human being as its assistant (a frail and vulnerable person being puppeteered by an uncaring, relentless machine).
>Like an Amazon delivery driver, who sits in a cabin surrounded by AI cameras, that monitor the driver’s eyes and take points off if the driver looks in a proscribed direction ...
>The driver is in that van because the van can’t drive itself and can’t get a parcel from the curb to your porch. The driver is a peripheral for a van, and the van drives the driver....
> -- Cory Doctorow

When you're developing with coding assistants, it's important you avoid being the reverse centaur of the agent. 

Last week, while developing a Dataflow job on GCP, for some reason the agent was unable to verify the completion of jobs it had started. So instead, it kept asking me to verify via the console.

I was copying error messages from the console and pasting them diligently into the terminal to keep the agent happy and iterating, but the dataflow jobs were slow to build, and we struggled through a few loops of careless errors like permissions and versions. This process was unsurprisingly slow ... and painful!

When the human is in the verification loop, it requires every loop to be verified at human speed; this is slow. Worse yet, it wasn't a good use of the human's time. I was the reverse centaur, the agent couldn't verify something from within the terminal, and I was the human body for it to verify via the Console.

Instead I should have spent maybe 5-10 minutes pointing the agent to the right place to verify the logs and errors of the dataflow job, and let it iterate till success. Then (and only then), should I have stepped in verify -- in Centaur mode!

This is probably similar to work -- if an intern was performing the task, I would never accept a scenario where every single iteration of a loop needed my verification. Instead, I would give the intern the right tools to verify the outcome of their work, and review only after a successful run.

Reverse centaurs might be everywhere in the agentic era, especially when we use "Human in the loop" as an check on the robots. We should be careful that humans use the AI, and not the other way around.
