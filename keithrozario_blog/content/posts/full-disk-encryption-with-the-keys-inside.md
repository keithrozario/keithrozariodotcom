+++
title = "Full Disk Encryption with the keys inside"
slug = "full-disk-encryption-with-the-keys-inside"
date = "2016-04-09T12:52:55"
draft = false
tags = ['EMV', 'Iphone']
categories = ['Security &amp; Privacy']
+++

Nobody really knows how the FBI is hacking into iPhones.

Well nobody, except <a href="http://www.cellebrite.com/Pages/ios-forensics-physical-extraction-decoding-and-analysis-from-ios-devices">Cellebrite</a> and the FBI themselves.

We can safely assume that the underlying crypto wasn't hacked--that would be truly catastrophic for everyone's security, and way above the pay grade of a company like Cellebrite.

So we have to conclude that somehow the FBI has managed to trick the iPhone into giving up it's encryption keys, or bypassed the Passcode protections on the phone. Apparently the hack <a href="http://recode.net/2016/04/07/fbi-director-comey-iphone-hack-limits/">doesn't work on iPhone 5S and higher devices</a>,  and obviously this can't be a software bypass (because all iOS devices literally run the software), so it has to be a hardware limitation, one that probably affects the key storage.<!--more-->

The only difference between the iPhone 5C--<em>which can be broken</em>, and iPhone 5S -- <em>which can't be broken</em>, is the secure enclave, which leads me to believe this is some sort of key extraction that can be performed when keys are stored outside the secure enclave--although I'm no expert here.

When a company like Whatsapp decides to implement end-2-end encryption, they release a <a href="/uploads/wpid-wp-1442992521638.jpeg">they're "absolutely un-hackable</a>", but provide no proof for such ludicrious claims, nor detail the method in which their keys are generated and stored. Claims like these should never be trusted.

Encryption is hard, not because encrypting is hard--but because it's hard to securely store the keys. It's made even harder when you have to store the key and data on the same device, but fortunately, there are some examples of securely doing so.
<h2>Using Asymetric keys</h2>
The key storage problem can be circumvented if you use asymetric encryption, where the encryption key is different from the decryption key. Well written ransomware, like crypto-locker, receive pre-generated encryption keys from central servers that they use to encrypt files, leaving the asymetric decryption key 'securely' on the server. This way, even though there is a key on the victims computer, that key is completely useless when it comes to decrypting the ransomed files.

But asymetric encryption is painfully slow, and implementing it on something like a windows PC and iPhone will incur to big a performance penalty to be 'consumer' friendly.
<h2>Using user-generated passwords</h2>
When you use bitlocker or <a href="https://www.keithrozario.com/2014/05/truecrypt-has-ended.html">truecrypt</a>, the encryption key is derived from a secure password you provide the computer when you logon or mount the drive. The moment the computer is turned-off, the memory is flushed and the key is forgotten. So without your knowledge of the secure password, the encrypted data remains safe, since it doesn't co-habitat the key that encrypts it.

Usually what programs like these do, is turn a user generated password into a key by running it through a some 'key strengthening' algorithms, such as PBKDF2. These take generally low-entropy user passwords and pass them through relatively time-consuming functions to generate the necessary high-entropy output to be used for a encryption key.

Iphones do something very similar with your passcodes.
<h2>iPhones approach</h2>
But with the iPhone, the key is derived from a something a lot less secure than a random password--it's derived from a simple 4 or 6 digit code <em>(for most people at least)</em>. This is trivial to brute-force on most computers, and hence makes the device inherently insecure.

What Apple do to secure this is to 'complement' the passcode <em>(which has very little entropy)</em> with a unique device key <em>(which has very high entropy)</em>. These two keys are then used to encrypt a further set of keys, which finally encrypt the data on the disk , the primary purpose though is that the security of the phone is reliant on both the <span style="text-decoration: underline;">user entered passcode</span> <strong>and</strong> <span style="text-decoration: underline;">the unique device key</span>.

The problem of course is that the unique device key, which provides the most entropy is on the device itself, and with a little computer forensic techniques, or some clever hack, might be reveal itself and thus break the entire system.

This is very similar to the Truecrypt and Bitlocker approach disk-encryption, with the fundamental difference being that on a laptop or computer you have a keyboard--and a keyboard lends itself better to long/complex passwords. Laptops are also more likely to be used for long-stretches at a time without turning off--smartphones on the other hand are far more likely to be turned off and on, requiring a password entry each time.

Hence a long alphanumeric password is acceptable for laptop use, but not iPhone use.



![Apple-Encryption-Keys](/uploads/Apple-Encryption-Keys.png)


<h2>The problem with physical access</h2>
For a long time in computer security, we've always lived under the assumption that if the attacker has gained physical access to the computer in question, <span style="text-decoration: underline;">all bets are off</span>. Apple is working hard to ensure that this assumption will no longer hold true for the next iteration of iOS, and are putting that assumption to a serious test.

But there is already a computer that broke that assumption nearly a decade ago--you quite possibly have it in your pocket right now. It's your credit card.

Last year, I wrote a piece about how <a href="https://www.keithrozario.com/2015/10/chip-and-pin-an-intro-for-malaysians.html">Chip and PIN will be coming to Malaysia</a> at the end of 2016, and credit cards are great examples of crypto-engines that hold secure keys and never give them up.

When you insert (or as the British say 'dip' ) you card into a card terminal, the card authenticates itself to the terminal by providing it two chained certificates, one that belongs to the issuing bank, and another that is card specific. The terminal uses a root certificate provided by the card scheme (Visa, Mastercard, JCB..etc) to verify these card-provided certificates. Finally the terminal challenges the card to prove that it has the private key corresponding to the card specific certificate.



![Card-Bank-Key](/uploads/Card-Bank-Key.png)



It's all very complex, but it's worked so far, because no one (at least officially) has figured out how to obtain the secret key from the card--but many have figured out easier ways to circumvent the protection.

Credit cards also have fail-safes (just like iPhones), where the chip will completely block all Pin attempts after a certain number of re-tries. Brute-forcing a card to determine the PIN isn't a feasible option.

The point though is that the hardware chip on the card never reveals it's encryption keys to anyone, it can only encrypt an input as directed--or validated an already encrypted key (nothing more and nothing less).

Think of encryption as a massive forty foot tall fence that is only one foot wide. It's much easier to work around then it is to breakthrough, and when you have the keys to the kingdom on a device you physically have in your hand, things get easier--although if Apple has it's way, easier would still be pretty darn hard.

As challenging as it is to secure a device with the keys inside--it's even more challenging to secure devices with implicit (or explicit) back-doors. Hopefully we solve this issue before we are forced politically to solve the other.