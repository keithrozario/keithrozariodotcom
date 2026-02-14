+++
title = "Security on the Cloud: Does PCI compliance matter"
slug = "security-on-the-cloud-does-pci-compliance-matter"
date = "2011-11-28T09:33:19"
draft = false
tags = ['Amazon', 'Cloud', 'Security']
categories = ['Cloud Computing']
+++



![](/uploads/security_on_the_cloud-222x300.jpg "security_on_the_cloud")

The main concern companies have in migrating to the cloud is security. That in one sentence covers cloud computing greatest hurdle, as more and more companies are beginning to see the benefits (economically) of moving their infrastructure and data to the cloud, the major turn-off is control. In essence, the greatest advantage of cloud computing is also it's biggest detractor. Companies (especially non-IT companies) are really interested in letting someone else run their IT infrastructure, but their uncomfortable letting someone else run the IT infrastructure due to the security concerns.

In my work, I often deal with PCI-DSS (Payment Card Industry Data Security Standard), which is a benchmark of sorts on how secure your servers are. In the banking world, any application,system or vendor hoping to store, transmit or process credit card information needs to be PCI-DSS compliant. If you thought pronouncing the acronym was difficult, adhering to and complying to the standard is even more so. In fact, the direction now is to use certain 'tricks' to avoid having to be PCI-DSS compliant, including implementing point-2-point encryption (thereby disregarding the need for PCI-DSS compliance on all intermediary systems) or using tokenazation (to replace the card number with a token that can redeemed from a secure vault). The main direction is clear, compliance to security standards is mandatory and non-negotiable, but it's also expensive and time-consuming, and anything that can help reduce the effort and cost is really taking off (<a title="shift4" href="http://www.shift4.com/" target="_blank">just ask shift4</a>).<!--more-->

The major gist of it is this, security (especially information security) is now at the forefront of any IT discussion at even medium size companies (let along the Fortune 500). Just ask Sony how they felt when their servers got hacked. With hack groups like<em> anonymous</em> hacking into just about any server they deem fit, securing data, and especially if that data is your customers private data is of prime importance. The cost of failure far outweighs the cost of compliance, but the cost of compliance is still pretty high.

Which is why cloud computing isn't picking up at the speeds it should be. IT executives like to see their servers in their own data center, protected by multi-level security they can feel, touch and smell. They like to be able to touch the Hardware Security Module that is tamper proof and will wipe itself out in case of intrusion, these tangibles make people feel safer, and it will always be the case. Psychologically you'll feel safer behind a wooden box, than tempered glass even though the latter offers better protection. In order to feel secure, <span style="text-decoration: underline;">you need to see the security</span>, that's the way the world works.

However, the cloud operates on a different platform, in a data center even Amazon employees aren't sure where, and in data centers that have been certified to the highest security standards. Security is expensive, but because of it's scale and it's experience is dealing with loads of credit card information, taking that leap to trust Amazon isn't that hard.

Consider this, <a title="Amazon achieves PCI Compliance" href="http://aws.typepad.com/aws/2010/12/aws-achieves-pci-dss-20-validated-service-provider-status.html" target="_blank">Amazon recently Level 1 PCI compliance</a>. Which means,

<em>"Organizations can now run their applications on AWS PCI-compliant technology infrastructure to store, process and transmit credit card information in the cloud. "</em>

Thinks about it, if Amazons cloud is PCI compliant, it simply means that it's secure enough (from PCIs view) to store credit card information and card holder names, the same type of data Sony recently lost.For the general public, this is the the most confidential piece of data they want secured. Now obviously, <strong>just because the infrastructure is secure doesn't mean the processes ar</strong>e, and simply deploying your application on the cloud doesn't make it PCI-DSS compliant by default, all it means is that Amazons storage facilities (like S3) and computing (EC2), and even EBS, all have a very high level of security, for something they charge in cents/hour. Trust me, if you want to deploy a PCI compliant infrastructure in your IT landscape it will cost you more.

I'll end the post with a rather poignant quote from a<a title="Innovation Security" href="http://www.techdirt.com/blog/innovation/articles/20111031/00320016563/innovation-security-its-all-about-trust.shtml" target="_blank"> techdirt article(entitled Innovation in Security).</a>I glanced through today, and I think it introduces a new approach to security for organizations. Particularly to address the old way of thinking where if "I can't see it , it's not secure".
<blockquote>I've been thinking more and more about this now that "cloud" storage has become a bigger issue. There are some out there who think that cloud storage means that you have "less" security, since your data is "out there." And, in some cases, that might be true. But, consider this: if you store the data yourself, you're responsible for your own security, and you might not be nearly as good as whoever is on the security team at the cloud storage provider.</blockquote>
In essence we're seeing a reversal, instead of customers feeling edgy because they don't have control of their data, customers are beginning to have a greater sense of comfort because their data is being stored in an environment far more secure than they could ever build themselves....and at a reduced price. Now who wouldn't want that?

*as an additional note, post-thanksgiving Amazon processes about 30-40 THOUSANDS credit card transactions per SECOND. So if anyones pretty clear on how to protect cardholder data, it's Amazon.

<span style="color: #888888;">*picture courtesy of http://www.flickr.com/photos/cjmphotos/1141218766/sizes/m/in/photostream/</span>