+++
title = "Klayers Part 1: Building Lambda Layers with Lambda Functions"
slug = "klayers-part-1-building-lambda-layers-with-lambda-functions"
date = "2019-08-18T22:17:30"
draft = false
categories = ['Serverless']
+++

<!-- wp:paragraph -->
<p>This is a continuation in the Klayers series, where I deep dive into the architecture of Klayers. At its core, Klayers is a collection of AWS Lambda Layers for Python3, with the idea that python packages in layers is more efficient than packaging them with application code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Visit the GitHub repo <a href="https://github.com/keithrozario/Klayers">here</a>, where you'd find 50+ lambda layers for public consumption across most AWS regions (including HK and Oman). This post is how I automated the building of layers inside lambda functions -- but specifically on layers composed of Python Packages (e.g. requests, beautifulsoup4, etc)</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Python Packages for Dummies</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":6771,"sizeSlug":"large"} -->
![](/uploads/pypi.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>As a primer, let's take a look at python packages in general. Python utilizes the Python Package Index (or PyPI), this is similar to Maven for Java or NPM for Node. It's simply a package manager that helps with the installation of python packages for your application.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In order to help with this, there is a program called <code><a href="https://pypi.org/project/pip/">pip</a></code> that helps with the installation of python packages. While <code><a href="https://pypi.org/project/pip/">pip</a></code> isn't limited to packages from PyPI, you can use it to install packages from other sources as well -- it and PyPI are the dynamic duo of Python packages.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The problem is that while Python is a interpreted language, there are some components of it that are OS specific. When you pip install into Windows, you get a different package installation than when you pip install into Ubuntu or OSX. <code>pip</code> detects your OS and installs specific files for your specific purpose -- sometimes those files need to be compiled for your OS as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which means, if you wanted to put a Python Package into a Lambda Layer, it would need the AWS Linux version of that Python Package <em>(Ubuntu might be close enough, CentOS is even better)</em>, because Lambda functions run on AWS Linux. And because not many folks run Linux as their core distribution, the general recommendation for creating these lambda layers  has always been to use Docker.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's very easy to use a docker container based on <a href="https://hub.docker.com/r/lambci/lambda/">lambci/lambda:build-python3.7</a>, to build python packages for lambda. In fact I even have a script that does that <a href="https://github.com/keithrozario/Klayers/blob/master/scripts/deploy_with_docker/package.sh">here</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But to me, this seemed <strong>sub-optimal</strong>. After all, we preach the 'serverless first' mantra, yet when it comes to building lambda layers -- we default to a docker container on a serverful laptop .... there must be a serverless way.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>The Serverless Way</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>And indeed there is serverless way. We used Docker to grant us a environment that mimics the actual lambda function -- but you know what else has an environment that looks exactly like a lambda function?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>An actual Lambda Function.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Why couldn't we pip install inside a lambda -- and then use that as our python package? </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Turns out there is no reason we can't. A simple code snippet below is all you need to install a package in your lambda function.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/7237de9c325fa55a6bdfe280b0c661f9.js"></script>
<!-- /wp:html -->

<!-- wp:heading -->
<h2> Caveats</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>There are a couple of caveats though, firstly a lambda function has only one write-able directory (<code>/tmp</code>) and that has a limit of 512MB. So you have to ensure that the building of the package is sent to the <code>/tmp</code> directory. This isn't a problem for our use-case as the limit on the lamba layer is generally smaller than this.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Secondly, we use the Python3.7 lambda runtime, as that already has pip installed -- but there's a catch. And this deserves a short explanation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>The AWS lambda runtime</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>When AWS create a new runtime (e.g. Python3.7), they generally release that runtime with the latest bells and whistles <span style="text-decoration: underline;">at that time</span>. Hence, your boto3 version will be pretty recent, and so will versions of bundled applications like openssl, curl, etc.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But, as time goes on, AWS will **NOT** upgrade them. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The rationale is to avoid an upgrade of the underlying boto3 or openssl that might break your functions. It'll be a nightmare, if a your production API started failing because you relied on a version of OpenSSL that AWS decided to one day switch on you!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AWS will upgrade and patch the OS level, so you don't have to worry about Meltdown or Spectre -- but you still need to be absolutely sure what underlying application on the OS you're using.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example boto3, the version of boto3 on the Python3.7 runtime is <code>1.9.42</code> while the current latest version of boto3 is <code>1.9.210</code>, that's more than 150 versions behind! Even if you weren't interested in the stability aspect of using a specific version of boto3 -- you must be interested in all those additional features that version 1.9.42 didn't support. Boto3 inside a lambda function, doesn't support publishing lambda layers -- they didn't exist when the runtime was published.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence, the version of pip in the runtime is also a bit behind. So I ended up having to package a newer version of pip into a lambda layer to run -- so that I could <code>pip freeze</code> with a <code>--path</code> option (this was introduced fairly recently) and get the full <code>requirements.txt</code> of the installed package.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Pythonpath</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Lastly, the current PYTHONPATH in the AWS Lambda is set to <code>/var/runtime</code>, in order for my to use my version of pip, I had to set it <code>opt/python</code>, so that it references the pip in the lambda layer ahead of the pip already installed in the lambda. This use-case of building lambda layers in lambda functions is pretty unique -- I doubt you'll ever encounter a time where you need to do this.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Limitations</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Finally, let's talk limitations.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For the purpose of building one python package -- the 900 seconds execution time, or 3GB memory limit of lambda was never a factor worth considering. The packages typically get built in 10-60 seconds (depending on the size).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>However, some packages require gcc or some other underlying dependency, that lambda currently does not have. I could not build these packages -- it's on my to-do list, but it'll take a while to reach it.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Using lambdas to build lambda layers is freaking awesome! It means I can execute as many times as I like -- and still stay comfortably within the free-tire of AWS. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I schedule the lambdas (which exists inside step functions) on Monday every week -- I could easily have scheduled them everyday, but managing that many layer versions was just too cumbersome.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's a pretty novel trick, to build lambda layers with lambda -- now the problem is too much scale. Klayers attempts to build 50+ lambda layers weekly, and if any package was upgraded in the last week, a new layer version is published, ready for public consumption.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can get more details in the github repo <a href="https://github.com/keithrozario/Klayers">here</a>.</p>
<!-- /wp:paragraph -->