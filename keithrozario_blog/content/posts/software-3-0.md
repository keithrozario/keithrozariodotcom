+++
title = "Software 3.0"
date = "2025-08-11T09:31:48"
draft = false
categories = ['Misc']
+++

<!-- wp:paragraph -->
<p>If you have 3 apples, you take away 2, how many apples do you have?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1 of course!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But then again, <code><strong>you</strong></code> took away 2, so therefore <strong>you</strong> should have 2. The question is ambiguous depends on how you interpret the words 'have' and 'take-away'.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Compare that to something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>def apples_you_have (total_apples, apples_you_took_away):

    return total_apples - apples_you_took_away</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>It's super clear how many apples_you_have. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I'm just not sure how (or why) we would replace a precise language like Python or Go, with an imprecise language like English when building complex software. We're using the wrong tool (Human Language) to execute computer behavior. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When we write comments in code in English (or some other human language) those comments are meant for humans to read -- and they are meant to convey general ideas about the class, method of function, not specific implementation details. Those implementation details are best left to the actual code. </p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p>...English isn't always as precise as code, but it can still be used in precise ways and comments typically don't need the same degree of precision as code. Comments often contain qualitative information such as <em>why</em> something is being done, or the overall idea of something. English works better for these than code because it is a more expressive language.</p>
<!-- /wp:paragraph --><cite><a href="https://github.com/johnousterhout/aposd-vs-clean-code">https://github.com/johnousterhout/aposd-vs-clean-code</a></cite></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>And when we need high level ideas about the code we read the documentation or comments -- but when we want to understand the implementation details, like how many apples we have, then we read the actual code. English is not a replacement for code, or even code generation. You cannot avoid writing/reading code for implementing precise software.</p>
<!-- /wp:paragraph -->