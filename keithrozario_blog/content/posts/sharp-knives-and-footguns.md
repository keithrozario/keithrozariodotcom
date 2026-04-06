+++
title = "Sharp Knives and Footguns"
date = "2026-04-06T15:34:45+08:00"
draft = false
categories = []
description = ""
showFullContent = false
readingTime = false
hideComments = true
+++

When building a platform or tool for developers there are two extreme schools of thoughts:

* Provide Sharp Knives
* Safety By Design

When you provide Sharp knives you provide powerful (but dangerous) tools to your users, and trust them to do the right thing. The tools will make their job easier, but could also cause serious problems.

Safety by design is the other extreme end, the user is not given powerful tools, but simple and safe tools that they can't shoot themselves in the foot with. 

There is a middle ground -- provide sharp knives, but lock them in a drawer. 

When you use the Python Cryptography package, there is the general package modules you get from `import cryptography`, but there's **also** a separate part of the code that provides access to more 'dangerous' primitives that are aptly named hazmat (short for hazardous materials). So when you `import cryptography.hazmat.primitives...` you get access to the sharp knives, and the documentation clearly tells you to ["ONLY use it if you’re 100% absolutely sure that you know what you’re doing because this module is full of land mines, dragons, and dinosaurs with laser guns"](https://cryptography.io/en/latest/hazmat/primitives/). Safety by design for **most** of the code, but a sharp knives are available in the drawer marked hazmat.

But ... does this approach work with LLMs.

When you're writing your own code, and importing these things yourself, it's easy to be aware of you're importing hazardous stuff. But if you're coding in YOLO mode, you might not even be aware that your agent has accessed the deepest pits of the hazmats and is now gleefully implementing [Textbook RSA](https://arxiv.org/abs/1802.03367), which in cryptography is a **bad** thing.

Are agents going to pay attention to hazmats, or are they going to implement them as they would any other module or interface. After all they're there in the documentation and the interface is available.

You can't hide anything from an agent that's willing to read source code of anything it downloads. And the more YOLO the programmer is, the less likely it is that we'll notice those pesky laser shooting dinosaurs -- so why even bother labeling it hazmat? Why not just either put it all in one hierarchy, or remove them entirely -- choose the philosophy you want to follow (sharp knives vs. Safety by design), and just go all-in on it.

I found this fascinating. We've written these tools and frameworks for humans, and have a certain expectation of how they'd be used, balancing the sharp tools against safety. But all of that is irrelevant to an agent just trying to get the job done. Perhaps one solution is creating a package built for consumption by LLMs, an another for humans -- kinda how we have experimental/alpha versions of something? 

