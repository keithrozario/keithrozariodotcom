+++
title = "Missing .SO files in Lambda functions"
date = "2021-08-09T11:14:28"
draft = false
categories = ['Misc']
+++

<!-- wp:image {"id":7512,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/uploads/Screen-Shot-2021-08-09-at-11.13.54-AM-820x237.png" alt="" class="wp-image-7512"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Most of the time, adding a python package to a Lambda function is a simple task. You <code>pip install</code> to a directory, and then copy that directory to the function either directly or through a lambda layer.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But sometimes, there's extra work required.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Packages like opencv install additional files on your system that aren't available in the same directory you pip installed into. When you <code>pip install opencv-python-headless</code>, additional .so files are downloaded to special directories in your environment to provide the openCV functionality.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So if you copied across the contents of your just your pip installed directory, you'll run into a  <span class="has-inline-color has-typology-acc-color">"libgthread-2.0.so.0: cannot open shared object file"</span> error.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Klayers had 3 open issues for opencv around missing .so files, and today I decided to fix them, and write about how you can do the same.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Step 1: Get a Lambda Environment</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In order to get the missing .so files, we'll need to replicate the environment in which lambda functions run. Remember, Lambda functions run in a Amazon Linux 2 firecracker container, and in order for us to get the specific .so file (that will work), we'll need replicate this environment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Fortunately, the folks over at <a href="https://github.com/lambci/lambci" target="_blank" rel="noreferrer noopener">lambci</a> have a solution. They publish docker containers that mimic the environment of a lambda function. By using their containers, we're able to <code>docker run</code> a lambda-equivalent environment on my macbook.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First we pull down the relevant container:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ docker pull lambci/lambda:build-python3.8</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Next log into that container, and pip install opencv-python-headless</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ docker run -ti lambci/lambda:build-python3.8 /bin/bash

bash-4.2# pip install opencv-python-headless</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Great, we've got it working. Now we need to copy out those .so files from our container to the local machine. At this point, we'll need to keep the container running until we've copied out the required files.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Step 2: Get the .sO file</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>First let's locate where the relevant .so files are. We know from the error message that we're looking for libgthread-2.0.so.0, but where is this file located?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Most of the time it'll be in <code>/usr/lib64</code>, and we can verify this, by listing out the directory and greeping for the specific name:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7502,"sizeSlug":"large","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="/uploads/Screen-Shot-2021-08-08-at-4.26.53-PM-820x78.png" alt="" class="wp-image-7502"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>So the file is here, but it also happens to be linked to another file <code>libgthread-2.0.so.0.5600.1</code>. I'm no Linux expert but I know enough that it'll take both these files to make our lambda function work. So if we copy out these files to our local machine, and we should be good right?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Well...not so. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You see libgthread might need other dependencies as well. In order to ensure we copy out all the required dependencies, we run the <code>ldd</code> command on the file to see if there's any other required files.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7504,"sizeSlug":"large","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="/uploads/Screen-Shot-2021-08-08-at-4.30.14-PM-445x500.png" alt="" class="wp-image-7504"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Once we identify the right files to copy out, we can copy them across by running the <code>docker copy</code> command.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The docker copy command allows us to copy files from a locally running container to our host machine, by following the simple syntax of:</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">$ docker cp &lt;container>:&lt;src-path> &lt;local-dest-path> </pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Note: in order to get the name of our running container, we need to run the docker ps command, in the example below, the name of our container is quirky_colden, docker containers usually have these odd 2-word names to allow for easy identification.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7506,"sizeSlug":"large","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="/uploads/Screen-Shot-2021-08-08-at-4.36.58-PM-820x76.png" alt="" class="wp-image-7506"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Now it's a simple matter of copying out the right files to our local machine, for example:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ docker cp quirky_colden:/usr/lib64/libpcre.so.1.2.0 .</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>And we should have a folder full of required files like so:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7507,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="/uploads/Screen-Shot-2021-08-08-at-4.40.10-PM.png" alt="" class="wp-image-7507"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Step 3: Package .so Files as a layer</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Once our files are ready, we need to get them ready as a layer. To do this, we place them all in a specific folder called <code>lib</code> and then zip the <code>lib</code> folder.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is important, as layers are extracted into the <code>/opt</code> directory of our lambda function. And since <code>/opt/lib</code> is a special directory where Amazon Linux will look for .so files, we need to ensure that the .so files are correctly stored in a <code>lib</code> directory -- no other directory name will work.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Note: the locations where Linux will look for .so files is specified by the <code>LD_LIBRARY_PATH</code> environment variable. In theory you could modify this variable, and place the files anywhere you want, but following convention saves us multiple steps of work.</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then we upload the zip file as a layer through the console (or CLI if you prefer).</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7508,"sizeSlug":"large","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="/uploads/Screen-Shot-2021-08-08-at-4.47.17-PM-562x500.png" alt="" class="wp-image-7508"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Finally we can test the functionality, by creating a function that references both layers.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>It is a bit manual of a process to copy across .so files, but fortunately with tools like lambci and docker, this is a bit easier than it would have been.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's also a one-time affair, as these .so files rarely change.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hopefully this post helps you, and if you want to use opencv in a python lambda, both the package and the .so files are available as publicly available layers from <a href="https://github.com/keithrozario/Klayers">Klayers</a>.</p>
<!-- /wp:paragraph -->