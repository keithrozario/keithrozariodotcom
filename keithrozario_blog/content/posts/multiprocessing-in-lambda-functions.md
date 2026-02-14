+++
title = "Multiprocessing in Lambda Functions"
date = "2019-10-13T18:28:52"
draft = false
categories = ['Serverless']
+++

<!-- wp:image {"id":6810,"width":480,"height":270,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="/uploads/PyCon_2.001.jpeg" alt="" class="wp-image-6810" width="480" height="270"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Lambda functions are awesome, but they only provide a single dimension to allocate resources - <code>memorySize</code>. The simplicity is refreshing, as lambda functions are complex enough -- but AWS really shouldn't have called it <code>memorySize</code> if it controls CPU as well. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then again this is the company that gave us <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html">Systems Manager Session Manager</a>, so the naming could have been worse (much worse!). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Anyway....I digress.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The <code>memorySize</code> of your lambda function, allocates <strong>both</strong> memory and CPU in proportion. i.e. twice as much memory gives you twice as much CPU.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The smallest lambda can start with minimum of 128MB of memory, which you can increment in steps of 64MB, all the way to 3008MB (just shy of 3GB).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So far, nothing special.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But, at <strong>1792MB</strong>, something wonderful happens -- you get one full vCPU. This is Gospel truth in lambda-land, because <a href="https://docs.aws.amazon.com/lambda/latest/dg/resource-model.html">AWS documentation</a> says so. In short, a 1792MB lambda function gets 1 vCPU, and a 128MB lambda function gets ~7% of that. (since 128MB is roughly 7% of 1792MB).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Using maths, we realize that at 3008MB, our lambda function is allocated 167% of vCPU. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But what does that 167% vCPU mean?!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I can rationalize anything up to 100%, after all getting 50% vCPU simply means you get the CPU for 50% of the time, and that makes sense up to 100%, but after that things get a bit wonky. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After all, why does having 120% vCPU mean -- do you get 1 full core plus 20% of another? Or do you get 60% of two cores?</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>It's a complex topic, that our friends in the server-ed world have struggled with for a long time, EC2 has the T2 instances with burst performance working on exactly the same concept of percent points of a vCPU. In effect, AWS can actually allocate vCPU time dynamically to your lambda function across both the cores depending on your consumption pattern.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1vCPU can either be 100% of one vCPU, or 50% of 2vCPUs -- or any combination across the cores that add up to a full 100%. It purely depends on your usage pattern.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AWS think about this from an economics and financial standpoint -- i.e. they <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html">allocate vCPU credits to you</a> -- which you can use across both cores at every lambda size any way you like!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That's right, because even at 128MB, lambda functions are deployed with <a href="https://gist.github.com/keithrozario/aaeef41f227f7b5c03eecf2da8fb854f">two CPUs</a> -- regardless of <code>memorySize</code>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But what does this mean to us?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you increase the <code>memorySize</code> of your function, you'll get a CPU performance boost -- but <strong>only</strong> until 1792MB. After that, there's no point allocating more <code>memorySize</code>, <span style="text-decoration: underline;">unless the function has multi-core capability.</span> </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because if you're consuming compute on just one-core, the maximum theoretical limit is 100% vCPU, allocating more is wasteful, which is what happens after 1792MB.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The following diagram shows a simple compute-intensive function of calculating 1,000,000 iterations of PBKDF2 on 4 different strings. The results are exactly as we expect (well sort-off). At <code>memorySize</code> of 1792MB, multi-threading the lambda has no performance gain over single-thread, but after 1792MB, the effects can be seen.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>More importantly, a single-threaded lambda function won't perform any better for compute jobs once you hit 1792MB. Finally, even at 3008MB, we do not see a 67% improvement in performance -- in this scenario at least it's just ~40%.</p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"ids":[6807]} -->
<figure class="wp-block-gallery columns-1 is-cropped"><ul class="blocks-gallery-grid"><li class="blocks-gallery-item"><figure><img src="/uploads/PyCon_img.001.jpeg" alt="" data-id="6807" data-link="https://www.keithrozario.com/?attachment_id=6807" class="wp-image-6807"/></figure></li></ul></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>But lambdas very rarely perform purely compute operations, they usually have a mixture of compute and network (rest calls with boto3 for example), so what would a highly intensive network load look like? Well something like this...</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6809,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/uploads/PyCon_img.002-1.jpeg" alt="" class="wp-image-6809"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>This job wrote 100 items to a dynamoDB table, one item at a time (it's very bad practice, but a good test case for this example). At the lower end of the spectrum ~512MB, the single threaded lambda does better than multi-threaded. We'd expect this, since with just ~33% vCPU, the over-head of multi-threaded actually slows down performance rather than improves it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But even at 1024MB, we see a significant increase in lambda performance -- what gives? Network jobs are high latency, and having multi-procs does help significantly even if you don't have 100% vCPU -- remember you still have 2 cores.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>At 3008MB, you now have roughly 80% of two cores, and can actually multi-proc even better. But remember, the best solution for writing 100 items into DynamoDB is batch-writing :).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Anyway, all this is complicated -- but the lesson is that you can't simply up your <code>memorySize</code> to get a performance boost, and that you can get a performance boost by multi-threading functions even before the magic number of 1792.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To properly size your funtions -- you can use <a href="https://lumigo.io/blog/introducing-the-lumigo-cli/">lumigo-cli</a>, which works with <a href="https://www.npmjs.com/package/lumigo-cli#lumigo-cli-powertune-lambda">powertune</a> to spin up a step functions and runs your lambda across multiple <code>memorySize</code> to report which is faster/cheaper.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Remember, Lambdas are charged per GB-s, and sometimes allocating twice the memory will not only save you twice the time, but cost you nothing extra. So when sizing lambda functions, remember that more can sometimes mean less.</p>
<!-- /wp:paragraph -->