+++
title = "Spreadsheets"
date = "2020-10-30T07:02:00"
draft = false
categories = ['Misc']
+++

<!-- wp:paragraph -->
<p>Spreadsheets are the bedrock of the modern enterprise, they're ubiquitous, from small family business' to large multi-nationals, and you'd be surprised by the number of critical activities that run off them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Pound-for-pound, Microsoft excel is the most valuable piece of software on the planet. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But are really that good?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The answer depends on what you mean by 'good'?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you need something flexible and editable by a user, which is universal enough to ensure everyone in the organization can view the data -- then yes, spreadsheets are good. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But if you need something that powers a critical business process, where scalability, stability and accuracy are critical  -- then no, spreadsheets are evil!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But why would a spreadsheet not be accurate? </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well ... buried deep within Excel's code are a bunch of auto-corrects which often corrupt data. An auto-correct is a programs attempt to correct a human-error, and generally speaking it works, but occasionally it takes perfectly good data and makes it bad.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When you type in 'MARCH1' into an cell on your spreadsheet, Excel automatically thinks you're entering a date, and converts that entry into '1-Mar.' Normally, this would be desirable, but if you're a geneticist, 'MARCH1' could be short for "<a href="https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26077">Membrane Associated Ring-CH-Type Finger 1</a>" -- which isn't a date.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The problem is so perverse, that <em>HUGO Gene Nomenclature Committee,</em> decided to rename these genes, rather than fixing Excel:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>This week, the HGNC published new <a href="https://go.redirectingat.com?id=66960X1514734&amp;xs=1&amp;url=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41588-020-0669-3&amp;referrer=theverge.com&amp;sref=https%3A%2F%2Fwww.theverge.com%2F2020%2F8%2F6%2F21355674%2Fhuman-genes-rename-microsoft-excel-misreading-dates" rel="noreferrer noopener" target="_blank">guidelines</a> for gene naming, including for “symbols that affect data handling and retrieval.” From now on, they say, human genes and the proteins they expressed will be named with one eye on Excel’s auto-formatting. That means the symbol MARCH1 has now become MARCHF1, while SEPT1 has become SEPTIN1, and so on. A record of old symbols and names will be stored by HGNC to avoid confusion in the future.</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>If the worlds brightest scientist have been defeated by Excel, what chance does Bob from accounting have?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But the reason for this post though, is the offense I took from a claim that NHS in the UK was 'incompetent' because it used spreadsheets to track contact tracing. The mis-step resulted in a failure to inform nearly 50,000 people to self-isolate, which might be partially responsible for the recent rise in cases.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For sure, it was a terrible mistake. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But <strong>incompetence</strong> is a strong word, it means <em>"inability to do something successfully"</em>, and generally refers to a innate inability as opposed to something environmental. You fire people for incompetence, recognizing that an average individual under the same conditions would have performed adequately.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But people resort to spreadsheets, not out of choice -- but financial necessity. Most organizations equip their desktops and laptops with a Microsoft Office (which includes Excel), and hence distributing <code>.xls</code> or <code>.xlsx</code> files is a cheap way for any project to distribute data -- they don't have to worry about the hosting anything, or installing anything on people's laptops.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The NHS was strangled out of cash, and yes, they could have spend a couple hundred thousand dollars to have a system that did all this tabulation in a accurate, stable and scalable way. But someone probably decided that buying extra ICU beds was a better use of that money. Can you blame them? </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Excel spreadsheet (up until then) was working perfectly, it had a few drawbacks, but spending money on something that isn't broken, is a luxury few Governments can afford.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Nobody anticipated a COVID like epidemic, and hence nobody was preparing IT systems to handle this load of daily patient data -- I'm guessing the UK isn't reporting 17,000 daily cases of any other illness. The software had no a reason to exceed its limits, so the current limits were deemed adequate (and reasonably so).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence, the reason the software missed out these 50,000 people, is the same reason we don't have enough ICU beds. We just weren't prepared for this scale.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Yes, they should have used a proper database, with a proper software running. At the very least, they should have reported an error when the spreadsheet was filled over. But those things cost money -- and depending on who you ask, the NHS has experienced a <a href="https://nhsfunding.info/staffing/unison-survey-shows-nhs-staff-are-overworked-and-underpaid/" target="_blank" rel="noreferrer noopener">decade of under-funding</a>, with three quarters of NHS workers saying there isn’t enough staff in their ward, and 49% reporting they couldn't take breaks because of their workload.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Do you really think they had couple hundred thousand lying around to implement the software?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The NHS used spreadsheets not because they were <strong>incompetent</strong>, but because they were <strong>underfunded.</strong> Incompetence is a devastating insult to folks who are already trying their best with the limited resources they have. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Addendum</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For those asking why a simple error message wasn't present when the spreadsheet overfilled -- the answer is also economic. Delivering a working IT solution is usually cheap and easy, but making that system <strong><span style="text-decoration: underline;">good</span></strong> requires a multitudes of complexities, from scalability, disaster recoverability, archival, performance, running cost...and the list goes on.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Merely testing your system to figure out the breaking points requires time and effort -- all of which eventually translates to cost. The 'error' wouldn't have been discovered, unless someone predicted a epidemic with more than 10,000 patients a day -- something no one was expecting a decade ago (or even 18 months ago).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sure it could have been done -- but who was going to spend money to test for a situation that no one had seen before, or even realistically expected? -- especially when budgets were tight?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>No one!</p>
<!-- /wp:paragraph -->