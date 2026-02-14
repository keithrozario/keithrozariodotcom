+++
title = "Interactive Shell on a Lambda Function"
slug = "interactive-shell-on-a-lambda-function"
date = "2019-08-25T21:54:26"
draft = false
categories = ['Security &amp; Privacy', 'Serverless']
+++

<!-- wp:image {"sizeSlug":"large"} -->


![](/uploads/revshell_on_lambda.gif)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>One of a great things about Lambda functions is that you can't SSH into it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This sounds like a drawback, but actually it's a great security benefit -- you can't hack what you can't access. Although it's rare to see SSH used as an entry path for attackers these days, it's not uncommon to see organizations lose SSH keys every once in a while. So cutting down SSH access does limit the attack surface of the lambda -- plus the fact, that the lambda doesn't exist on a 24/7 server helps reduce that even further.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Your support engineers might still want to log onto a **server**,  but in todays serverless paradigm, this is unnecessary. After all, logs no longer exists in <code>/var/logs</code> they're on cloudwatch, and there is no need to change passwords or purge files because the lambdas recycle themselves after a while anyway. Leave those lambda functions alone will ya!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As a developer, you might want to see what is **in** the lambda function itself -- like what binaries are available (and their versions), or what libraries and environment variables are set. For this, it's far more effective to just log onto a<a href="https://hub.docker.com/r/lambci/lambda/"> lambci docker container</a> -- Amazon work very closely with lambci to ensure their container matches what's available in a Lambda environment. Just run any of the following</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><code>docker run -ti lambci/lambda:build-python3.7 bash</code></li><li><code>docker run -ti lambci/lambda:build-python3.6 bash</code></li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Lambci provide a corresponding docker container for all AWS runtimes, they even provide a <code>build</code> image for each runtime, that comes prepackaged with tools like <code>bash</code>, <code>gcc-c++</code>, <code>git</code> and <code>zip</code>. This is the best way to explore a lambda function in interactive mode, and build lambda layers on.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But sometimes you'll find yourself wanting to explore the actual lambda function you ran, like checking if the binary in the lambda layer was packaged correctly, or just seeing if a file was correctly downloaded into <code>/tmp</code>-- local deploy has it's limits, and that's what this post is for.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Why no shell</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Obviously the first problem is that a Lambda function exposes no ports. Nada! Zilch! Secondly, even if you could bind to a port -- Lambdas run in an AWS VPC that is NAT-ed. Hence you're stuck behind a NAT, even after exposing the port.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And this dear friends, is where hackers would tell you to use a Reverse Shell!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>What the hell is a reverse shell??!!</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Glad you asked -- a normal Shell is when you log onto a server, and execute Shell commands on it. A reverse shell is when the server logs onto <strong>you</strong> and, you execute commands on it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The 'reverse' part refers to who initiates the connection. The typical usage is when you've compromise a server through some traditional exploit and obtained remote code execution -- but that server is behind a NAT that prevents ingress connections. However, NATs don't stop outgoing connections from a server -- do they? So if we could somehow get the lambda function to initiate the shell, we're good as gold!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And that's where areverse shell comes in.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After compromising a server, you spin up a listener to receive the incoming connections -- and then instruct your compromised server to initiate a reverse shell to that listener. Granting you an interactive shell on the exploited machine.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6776,"sizeSlug":"large"} -->


![](/uploads/reverse_shell.png)


<!-- /wp:image -->

<!-- wp:heading -->
<h2>Using Hacker techniques for Devs</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>So let's take this hacker technique and get ourselves an interactive shell on a Lambda Function. After all, it's **our** lambda function, hence we've already code code execution capability! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So what do we do?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First we package a wildly out-dated, but very useful version of netcat. This version actually gives us simple commands to initiate a reverse shell to any listening ip and port. Fortunately, there's a publicly available layer with netcat already published on <a href="https://github.com/keithrozario/Klayers">Klayers</a> (a github repo I made, that's full of cool layers).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Next we spin up a lambda using this layer, and the <a href="https://github.com/gkrizek/bash-lambda-layer">bash runtime</a> for our lambda function -- to give us access to real bash commands. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then we create a bash script, that simply initiates a reverse shell to a ip and port provided in our <code>EVENT</code> object, and load that into the functions execution code (in this bash runtime, the event object is simply <code>$1</code>).</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/edc67f48c07c7cfd1ad6840a86708847.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>And finally, we'd spin up an EC2 instance (or any other server) to run our listener on. Eventually, the whole setup looks something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6777,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2019-08-25-at-9.35.57-PM.png)


<!-- /wp:image -->

<!-- wp:heading -->
<h2>Results</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The GitHub repo with all this code is <a href="https://github.com/keithrozario/Lambshell">here</a>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally the results look something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large"} -->


![](/uploads/revshell_on_lambda.gif)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If you like this content, please consider starring this <a href="https://github.com/keithrozario/Lambshell">github repo</a>, or the <a href="https://github.com/keithrozario/Klayers">Klayers github repo</a> -- or both!</p>
<!-- /wp:paragraph -->