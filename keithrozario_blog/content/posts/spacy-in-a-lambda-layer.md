+++
title = "Spacy in a Lambda"
date = "2019-04-22T00:29:34"
draft = false
categories = ['AI', 'Singapore']
+++

<!-- wp:image {"id":6728} -->
<figure class="wp-block-image"><img src="/uploads/social_default-1d3b50b1eba4c2b06244425ff0c49570.jpg" alt="" class="wp-image-6728"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>I've been really digging into <a href="https://www.keithrozario.com/2019/02/keith-at-aws-meetup.html">Lambda Layers</a> lately, and once you begin using layers you'll wonder how you got by without them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Layers allow you to package just about anything into lambda, but in a modular way. So elements of your code that don't change much, can be packaged into layers, while keeping your actual lambda deployment for just the code that's changing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> It's akin to docker cache, where you keep the un-changing elements higher up in your docker file, separate from the code that always changes. The difference though, is that docker cache speeds up builds, while layers speeds up lambda deployments.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But layers aren't magic, and they're still limited by the AWS size limit, hence your entire function (including all it's layers) need to be no larger than 250MB (unzipped). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which is tough for something like <a href="https://spacy.io/">spaCy </a>-- because its default installation size on a AWS Linux is ~400MB (or 492MB based on my quick installation on <a href="https://github.com/lambci/lambci">lambci</a> for python3.7). So, in order to get spaCy working on a lambda, certain tweaks are going to be necessary.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Some have tried working around this problem by installing spaCy onto the lambda container on <a href="https://stackoverflow.com/questions/47879258/spacy-model-wont-load-in-aws-lambda">cold-start</a> -- i.e. pull the data into lambda only when you have access to the 512MB in <code>/tmp</code>. Cool solution, but it almost completely fills out <code>/tmp</code>, and makes a cold-start even slower.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A more optimal solution would be to reduce the size of the spaCy installation and have it fit into a layer! Fortunately I found a <a href="https://github.com/explosion/spaCy/issues/2851">GitHub issue</a> after some googling that enables us to do exactly this.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It involves removing unnecessary language files, which spaCy lazy load in, If you're only interested in one language, you can simply remove the unnnecessary language files in the <code>site-packages/spacy/lang</code> directory. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After manually removing all non-English (en) language files, I managed to reduce the size of the spaCy package to 110MB, which fits very nicely into a lambda layer, in the end my lang directory only had the following files:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6733} -->
<figure class="wp-block-image"><img src="/uploads/Screenshot-2019-04-22-at-9.54.23-PM.png" alt="" class="wp-image-6733"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>As a bonus, I also included the English <a href="https://github.com/explosion/spacy-models/releases/tag/en_core_web_sm-2.1.0">en_core_web_sm-2.1.0</a> model, to make the lambda layer fully usable on its own . </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally I published it as a publicly available layer, for anyone to consume. One of the amazing things about layers, is that once a layer is made, it can be shared across AWS for anyone to consume.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>How to use the layer</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The simplest way to get spaCy working on your lambda function is to just import the publicly available layer I created. To do this, create a python3.7 function in an aws region of your choice.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6727} -->
<figure class="wp-block-image"><img src="/uploads/Screenshot-2019-04-21-at-11.57.32-PM.png" alt="" class="wp-image-6727"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Then select layers, and add the spaCy layer as an arn (details of the arn for all regions can be found <a href="https://github.com/keithrozario/Klayers">here</a>) -- for spaCy the layer arn takes the form below, replace <em>&lt;region&gt;</em> with your actual aws region (e.g. us-east-2)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>arn:aws:lambda:&lt;</code><em><code>region</code></em><code>&gt;:113088814899:layer:Klayers-python37-spacy:1</code> </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6726} -->
<figure class="wp-block-image"><img src="/uploads/Screenshot-2019-04-21-at-11.58.59-PM.png" alt="" class="wp-image-6726"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Finally copy the code below as an example usage (just to make sure things work):</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/dcc85b21a5192f409a4c28dd16381668.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Before you test, raise the lambda execution time to 10 seconds, and allocate 512MB of memory (128MB wasn't enough for spaCy). From there you can run a dummy test, and get the following results:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6725} -->
<figure class="wp-block-image"><img src="/uploads/Screenshot-2019-04-22-at-12.10.42-AM.png" alt="" class="wp-image-6725"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If all goes well, you'll have a spaCy fully working within a lambda function, with very little effort. To accommodate more languages, you'll have to manually package the lambda layer by simply removing the un-needed language files from the site-packages directory.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Remember you can't simply package layers from any box, it has to be pip-ed installed onto an AWS Linux installation. I recommend using the lambci docker images to do this.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Lambda layers are an awesome way to store python packages, and since everyone uses python packages in lambda, it makes sense to share them via layers rather than having everyone packaging them repeatedly.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's a bunch more layers for python in my repo <a href="https://github.com/keithrozario/Klayers">here</a>. If you've used the layers or find the project helpful, all I ask is that you consider starring the repo :)</p>
<!-- /wp:paragraph -->