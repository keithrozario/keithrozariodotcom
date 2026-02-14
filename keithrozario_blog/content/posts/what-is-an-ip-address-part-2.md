+++
title = "What is an IP address : Part 2"
slug = "what-is-an-ip-address-part-2"
date = "2013-09-22T21:39:55"
draft = false
categories = ['WhatisIT']
+++

<p style="text-align: center;">

![IP address on an envelope](/uploads/2652428181_1a9aa9d06e.jpg)

</p>
Information flows around the internet in chunks, with chunk of data very much like a letter in an envelope. Just like how there's a special place on the back on an envelope for you to write the address of the receiver, there's a special place in every 'chunk' for you to write the address of the receiving computer. These 'chunks' of data are called IP packets, and the addresses are called IP addresses.<!--more-->
<h2>But what is an IP address?</h2>
Well just like everything else in the digital world, and IP address is a long string of 1's and 0's, a string of <strong>B</strong>inary dig<strong>ITS</strong>--or<strong> BITS.</strong>

A bit is an interesting concept of Computer science. It's a  tiny piece of information that can either be a 1 or a 0, on the face it doesn't look like much, but one single bit can hold the information on whether a light is on or off, whether a gate is open or closed or whether an engine is running or not, all these possibilities held in just one tiny packet of data called a 'bit'.

Another way to think of a bit is a way to uniquely identify a single location out of two possible ones. So if I have two houses, I could call my first house, House-Zero and my second house, House-One. If I had 4 houses, I would need two bits of information to identify each single one, House-ZeroZero, House-ZeroOne, House-OneZero and House-OneOne. The more bits I have, the more houses I can buy, although with the current housing market that looks enormously unlikely.

Practically though, 1 bit is rarely enough, and so we commonly use multiples of them. 8 bits make a byte, and a byte is a useful size of information, because it has 256 possible combinations, meaning a single byte can uniquely identify a single character from the ASCII character set of numbers, letters and special characters. In other words if I had a byte of data, I could identify a single house from a collection of 256 of them.

The internet though is huge, and 1-bit or even 1-byte wouldn't be enough to uniquely identify every single computer among all the other computers on the internet. So the internet uses 32-bits for addressing, which just means that the IP address of every machine is 32 bits long, or a string of 32 1's and 0's.

In theory this can be used to identify a single computer from <strong>4,294,967,296</strong> others. That's about 4.3 Billion, or 66% of the population of the world.

But hang on a minute--aren't IP addresses usually denoted as 4 numbers separated by a dot '.', something like 123.456.789.0?

Yes, you're right. You see while computers deal with 1's and 0's,  humans prefer something a bit more nuanced, so we use the decimal notation. A decimal system is the system you're most familiar with, one with 10 digits rather than just 2. But even the decimal system has issues, because saying something like My IP Address is 425 Million 624 Thousand 7 Hundred and 3 is just a mouthful and difficult to remember or notate. In fact, about 75% of every IP address would require a number 10 digits long, and that's just too long for humans to handle.

So computer geeks the world over, decided to invent the octet system. Where the string of 32-bits, is divided into 4 'octets', with each octet a byte in length. Now things get easier, because each octet can range from just 0 to 255. That would mean that your IP address would sound something like 192 <strong>dot</strong> 168 <strong>dot</strong> 100<strong> dot</strong> 108 , sure this has a maximum of 12 digits rather than a straight on decimal notation of just 10, but it's a lot easier to work this way, and it maps more readily to single bytes on the computer.

Rest assured though, that no matter how you type the address on the screen, your computer is still reading it as 111010101010101010001011.........

Now you ask yourself why is an IP address 32-bits long, why not 33-bits, or 34-bits? Why couldn't they have made it 128-bits and be done with it? That's for the next instalment of What is IT?