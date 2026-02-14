+++
title = "You own your software supply chain"
slug = "you-own-your-software-supply-chain"
date = "2019-08-05T20:58:41"
draft = false
categories = ['Security &amp; Privacy']
+++

<!-- wp:paragraph -->
<p>Just this week, my team was on the cusp of demo-ing a product they've been working on for the last 2 months, only for a build process to fail, just hours before the demo to some very high ranking people.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Troubleshooting the build took a while, but eventually we found the root cause, a missing package version! This probably wouldn't have been a big deal, had we not stumbled across it at midnight the day before an important demo -- but nevertheless failing builds are never a good thing!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Python, my favorite language, comes with fantastic built-in libraries that handle large number of use-cases -- but it still isn't **all** use-cases. In almost all real-world projects, you'd find yourself downloading an external package to extend the functionality of your code, without you (or your team) having to code all that by hand.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Want to access a PDF doc, there's a library for that! Need to see the contents of an xlsx file, library for that as well. Require a jpeg image to be inverted, there's something for everyone in Python -- but in order to fully benefit from these libraries require external packages to be downloaded and imported into your code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To keep track of these packages, most projects use a <code>requirements.txt</code> file to maintain the list of packages and their versions. This ensures that as new package versions roll out, you'd still install the older version you tested against. At build (or deploy) time, you would generally download this package version from the package index (PyPI) and use it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In my specific case, the package <a href="https://github.com/pymupdf/PyMuPDF">PyMuPDF</a> rolled out a newer version, but <strong>deleted</strong> the older one from the package index. This meant that my build process, which referenced the older version started failing -- because the index no longer carried the older version.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Luckily the fix was ~10 minutes of effort, and we managed to squeeze our demo back on track, but this raised and interesting question-- how do you take advantage of great open-source software while mitigating the effect of these kinds of issues?</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>All of it is open source</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Firstly, open source software is everywhere. I've seen vendors pitch multi-million dollar software suites that have dozens of open-source packages, and while **some** of those packages might be maintained, I've never seen one where **all** of them were. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In some cases, vendors pitching multi-million dollar pieces of software were reliant on packages that hadn't been updated since 2014 -- and in one case that package was written by a single lone individual who probably no longer supported the package anymore.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's highly unlikely that any piece of software you're currently running was built without some open-source in its supply chain, it's only a matter of how far you're willing to dig.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Not all open source is hobbyist</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>PyMuPDF made a rookie-error, and to be fair, most open source software is maintained pretty well. So well in fact, that people hardly prepare for these outcomes anymore.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After all, if Python packages regularly failed installations, this wouldn't be a blog post -- the problem with open source is (ironically) the fact that it works so damn often.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If 99% of packages installed all the time, you're less likely to plan for the outcome of one of them failing, or if one of them goes rogue! </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Open Source gone rogue!</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>And go rogue they do!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In November last year, the big story was an npm package <a href="https://thenewstack.io/attackers-up-their-game-with-latest-npm-package-compromise/">being 'infiltrated' and modified to target bitcoin accounts</a>. The infiltration in this case, was simply an attacker sending the rightful owner of the package and email, volunteering to take over the repo and maintain it. The owner, not using the package anymore, gladly agreed.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Some blamed the owner, claiming they had a 'responsibility' as they owned the repo -- but in reality, that argument could equally apply to the creators of software that used the package as well. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which brings me to my final thought. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I would never download an executable, written by a random Jane over the weekend and run in on my laptop -- let alone put it on servers in production. But I gladly pull down code from PyPI, NPM and Maven -- and then include that on workloads in production?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Aren't these both code executing in production? And while an executable is slightly more dodgy (can't see the code) -- I'll be honest and say, with very rare exceptions I've never looked at the source code of the packages I've downloaded. Have you?!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I guess the outcome we're looking for is that if you deliver some software to an end-user, you are responsible for that piece of software -- regardless of how many upstream packages you download, or how many package managers you rely on -- the buck stops with you. If the package fails, or goes rogue that's on you!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Given that -- at some point, developers are going to be a bit more careful about the number of external packages they pull in. They're also more likely to clean up their <code>pom.xml</code> or <code>requirements.txt</code> files to reflect packages they actually use. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can always take a hard look at the packages before you use them -- like evaluating the number of maintainers, the number of updates they push regularly and how many downloads there are. You cannot however, completely eliminate the risk that a piece of software you downloaded for free off the internet is going to be bug infested or go rogue at some point in the future -- unless of course you start contributing to that code base, and gain some control of the repo.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I guess it's why the biggest open source projects these days are all funded in part by large companies (Tensorflow from Google, React Native from Facebook etc). If your organization uses a certain open source software a lot, maybe it's time you start contributing back to it -- not out of some benevolent intention -- but really to cover your own risk of it going rogue.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Footnote</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p> I raised an <a href="https://github.com/pymupdf/PyMuPDF/issues/333">issue with PyMuPDF on their github page</a>, the owner and maintainer were very receptive to feedback, and graciously promised not to delete older versions in the future. If you use Python in production, you definitely want to build your virtual environments as part of the build process rather than deployment, this decouples your deployment from the package index and makes the installation far smoother at the cost of larger artifacts -- but that cost is well worth the price.</p>
<!-- /wp:paragraph -->