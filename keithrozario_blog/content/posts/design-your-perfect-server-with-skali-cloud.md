+++
title = "Design your perfect server with Skali Cloud"
slug = "design-your-perfect-server-with-skali-cloud"
date = "2012-04-06T12:18:38"
draft = false
tags = ['Amazon', 'Cloud', 'Maxis', 'Skali']
categories = ['Cloud Computing', 'Malaysia']
+++



![](/uploads/Design-your-perfect-Server.png "Design your perfect Server")

After doing some research on Malaysian Cloud offerings particularly the IaaS offerings, I noticed something rather interesting from Skali. Now I always remembered Skali as an early web startup some time back in the 90s trying to ride the internet wave but failing all along the way, this however has some promise.

Skali takes cloud scalability to a whole different level with their cloud offerings, unlike other IaaS providers who offer a fixed number of machine types Skali offers a fully scalable machine that you can add processing power, Memory and Disk independently. In essence near unlimited amounts of options in terms of machine type compared to just 3 from Maxis Cloud.

The pricing still seems high, but it can go toe-to-toe with Maxis although it would depend on the specific requirements. From just the high level you can sense that these IaaS providers are going to compete for Malaysian customers but they're competing with very niche offerings. Maxis ace up it's sleeve would be the unlimited data transfer, which Skali charges at a mind-blowing Rm2/GB. Skali on the other hand offers an entire range of machine types (possibly in the hundreds), while Maxis offers just 3.

The choice between Maxis or Skali would be a simple one that would come down to how much data transfer or scalability you need in your application. That being said, let's take a look at some other offerings from Skali Cloud.<!--more--> 

![](/uploads/idcpic-1-300x129.png "idcpic (1)")



The Skali data center is located at the UPM-MTDC University data park in Serdang, and on a separate note is it just me or do the pillars in the picture look slanted? The point is that the data center is housed in Malaysia, similar to Maxis housing their cloud infrastructure in Shah Alam, so if you absolutely, positively need a center in Malaysia, either option would work.

Skali differentiates itself from the competition by offering customized machine types, this is unlike Maxis or even Amazon that offer a fixed set of machine types. If you wanted additional machine types on Maxis or Amazon you'd need to purchase more machines, with Skali it's possible to just upscale the one machine you have. That's a good feature to have, and Skali advertise it front and center on their website.

Skali offers 3 tiers of Cloud Pricing, an hourly rate,  a monthly rate and a yearly rate. Of course the bigger time slot you book, the cheaper the overall price of the service is going to cost. This is unlike Maxis that offers only monthly price rates, but quite similar to Amazon who offer various tiers for the different time slots booked.
<h2>Pricing of Skali Cloud</h2>
Skali cloud pricing is straightforward, Rm0.08/core-GHZ-hour, RM0.10/GB-Memory-Hour and Rm0.40/GB-storage-Month. So based on the machine type you choose to design, you'd be charged accordingly. This allows you to scale exactly the size you want without having to buy more powerful machines you won't need. Skali also charges for everything else, including Rm5/month for a fixed static IP and RM2.00/GB of data transfer. Now I'm not sure about data transfer because the price is ridiculously high and it looks like Skali charge it for both inward and outward data transfer. Maxis offer this for free, and Amazon charge Rm0.60/GB of outward data transfer. That's a huge difference in cost, but Skali may be selling to customers who don't require that much data transfer.
<h2>What does highly scalable really mean?</h2>
Apart from buying a machine specific to your needs (which no other IaaS provider offers), Skali Cloud does have other pretty obvious advantages as well. The Skali Cloud Model is highly scalable particularly in terms of storage, so in theory you wouldn't need anything like S3 or EBS. In Amazon or Maxis you can only purchase a fixed set of machines with fixed storage capacities. Additional capacity can be purchased either by buying more machines or using a separate (and distinct) storage service such as Amazons S3 or EBS. In Skali, you could just scale up your machine storage capacity to fit your needs, bypassing the need for using a separate service or buying additional machines at additional cost. It's pricing of RM0.40/GB-storage-month make it reasonably cheap to do this, however the maximum I could see from the webtool was just 1.8TB of storage space per machine, that could be a limitation of the tool but it's something to keep in mind. It's also unclear how much it would cost to just store the data as a machine image as opposed to keeping the machine running. To really compare the pricing, Amazons S3 cost about Rm0.36/GB-storage-month, and that's a separate storage service not running on EC2. Overall though, there are good reasons why you would need such a highly scalable IaaS provider and Skali does have a niche market to cater to.
<h2>What about machine images?</h2>
Skali have a limited set of machine images, but all the standard windows servers are available at a starting price of Rm50/month. Linux and Unix distributions are available either directly from Skali or through 3rd-parties like elasticserver.com.
<h2>What about the Application programming interface (API)?</h2>
Unlike Maxis, Skali offers a good API with limited documentation. It's a step forward but it's unclear to me if the API allows you to scale up the machine type or if that has to be done manually?
<h2>Pricing Comparison</h2>
In terms of overall pricing however, it's a bit difficult to compare Maxis to Skali since they seem to be targetting different types of applications. However, using the golden RM900/month price point I think we can look at the offerings from a objective viewpoint. 

![](/uploads/Rm900skali.jpg "Rm900(skali)")

It's quite straightforward to compare Maxis and Skali because unlike AWS or Rackspace, I can very easily create a very specific Machine on Skali to match the Maxis Value plan. Then I raise the traffic GB till I reach the Rm900/month price point. What we end up with is a identical Machine to Maxis value, but offering just 210GB of Traffic as opposed to the unlimited traffic offered by Maxis. Of course this is under the assumption, that you require a Windows Machine (Rm50/month) and a fixed IP (Rm5/month). If you're using a Unix or Linux based platform then you can either save the Rm50 or choose to up your data transfer. On the high level though it's quite hard to see why you would want use Skali instead of Rackspace or the AWS offering that offer similar machines with much higher data bandwidth, this of course comes back to the discussion of do you really need a highly scalable IaaS provider?
<h2>Conclusion</h2>
While the post isn't conclusive and I haven't yet tried the Skali cloud I must say that I'm excited about their offerings. Apart from having a definitive differentiation factor in terms of having highly scalable machines, Skali also offers a possibility of hosting everything on a single machine for both computing and storage. It's data transfer though is a bit high. At Rm2/GB  (monthly subscription) or Rm4/GB (burst), it can easily burn a hole in your budget if you suddenly require the high data transfer, so it's something to be careful about. Overall though, Skali have a good set of machine images, a good price point, a good differentiation factor (that they make sure you know) and even an API complete with documentation to take advantage of it's high scalability. I must say, Skali do seem have their act together and it's quite obvious that this looks a lot more professional than Maxis Cloud. If you need lots of data transfer, look elsewhere, data transfer on Skali cost a lot. If you don't need lots of data transfer, but instead want highly scalable cloud offering. Skali could be the sweet spot you were craving. 

![](/uploads/logo1.png "logo")

