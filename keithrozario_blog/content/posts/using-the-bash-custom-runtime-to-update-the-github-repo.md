+++
title = "Updating a GitHub repo from a Lambda Function using Bash!"
slug = "using-the-bash-custom-runtime-to-update-the-github-repo"
date = "2019-09-09T23:14:24"
draft = false
categories = ['Serverless']
+++

<!-- wp:image {"id":6791,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2019-09-09-at-11.10.52-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>At the end of 2018, AWS introduced <a href="https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html">custom runtimes for Lambda functions</a>, which provided customers a way to run applications written in languages not in the holy list of the<a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"> 'Official AWS Lambda Runtimes'</a> which include a plethora of languages. It has 3 versions of Python, 2 versions of Node, Ruby, Java, Go and .NET core (that's a lot of language support)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Security-wise, it's better to use an Official AWS Lambda runtime than it is to roll your own. After all, why take ownership for something AWS is already doing for you -- and for free! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But, as plentiful as the official runtime list is-- there're always edge-cases where you'd want to roll your own custom runtime to support applications written in languages AWS doesn't provide.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Maybe you absolutely have to use a Haskell component -- or you need to migrate a c++ implementation to lambda. In these cases, a custom runtime allows you to leverage the power of serverless functions even when their runtimes are not officially supported.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Bash Custom Runtime</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Which brings us to the topic of today's post, the <a href="https://github.com/gkrizek/bash-lambda-layer">bash custom runtime</a>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For Klayers, I needed a way to update a github repo with a new json file every week -- which can be done in python, but no python package came close to the familiarity of <code>git pull</code> , <code>git add</code> and <code>git commit</code>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So rather than try to monkey around a python-wrapper of git, I decided to use git directly -- from a shell script -- running in a lambda -- on the bash runtime.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So I pulled in the runtime a <a href="https://github.com/gkrizek/bash-lambda-layer">github repo I found</a>, and used it for write a lambda function. Simple right? Well not entirely -- running regular shell scripts is easy, but there are some quirks you'll have to learn when you run them in a lambda function...</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Not so fast there cowboy...</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Firstly, the familiar home directory in <code>~/</code> is off-limits in a lambda function -- and I mean <strong>off-limits.</strong> There is absolutely no-way <em>(that I know off)</em>, for you can add files into this directory. Wouldn't be a big isue, except this is where <code>git</code> looks for ssh keys and the <code>known_hosts</code> file.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Next, because lambda functions are ephemeral, you'll need a way to inject your SSH key into the function, so that it can communicate to GitHub your behalf.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, because you've chosen to use the bash runtime, you're limited to the <a href="https://aws.amazon.com/cli/">awscli </a>utility, which while fully functional doesn't come with the usual tools as boto3 for python. It's a lot easier to loop and parse json in python than it is in bash -- fortunately, <code>jq</code> makes that less painful, and <code>jq</code> is included in the custom runtime :).</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Enough talking let's build this</h2>
<!-- /wp:heading -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading {"level":3} -->
<h3>1: Loading the Environment</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>First we create the function -- for this I used the serverless framework, and the code snippet below:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/4e4eda7b3452f4f772f48505a9d39c83.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>I use the <code>provided</code> runtime, and then attach the publicly available bash custom runtime as a layer to the function -- that's really all there is to running a lambda function in bash. To eliminate a dependency on a public layer, you could download the runtime, and deploy it in your own AWS account.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I then pre-load environment variables for the function.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>GITHUB_REPO (the ssh location of the github repo)</li><li>KEK_PARAMETER (the parameter in SSM for the Key-Encrypting-Key)</li><li>S3_KEYS (the bucket with the SSH keys)</li><li>BUCKET_NAME (the bucket with the json file)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Environment variables are exactly that in lambda functions, and can be accessed directly by calling $GITHUB_REPO, $KEK_PARAMETER or whatever name you give it -- just like you would in bash.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>2: Loading the SSH key</h3>
<!-- /wp:heading -->

<!-- wp:image {"id":6796,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2019-09-09-at-11.21.48-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>In order to push anything to GitHub we're going to need an SSH key. That SSH key is a <strong>secret </strong>-- which requires us to store it away safely somewhere.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You could just load the SSH key as a environment variable -- but be cautious, the environment variable in lambda is a deploy-time dependency. Also, the environment variable is visible in the console (and anywhere else for that matter) to IAM role that has the <code>lambda:GetFunction</code> permission. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A recommended approach would be to store this in AWS Secrets Manager or Parameter Store. Secrets Manager is great if you're looking for a key-rotation of RDS instances etc, for this specific use-case though, Parameter store is cheaper and gives you the same required features.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But Parameter Store has a limit, for regular parameters, the maximum size is 4KB, which is OK -- but the public side of 4096-bit RSA key-pair will generally take ~3.3KB already, dangerously close to the limit. Hence I chose to store a Key-Encrypting-Key in parameter store instead -- and upload an encrypted version of the key to S3. This way, I can use this pattern for any arbitrary size data. It also makes sure that I have to mess-up two IAM permissions (one for the bucket, and one for the parameter) before anyone can view the key in plaintext. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You could use other <a href="https://www.ssh.com/ssh/keygen/">key-pairs like ECDSA</a>, which greatly reduce the key size -- but for now let's go with 4096-bit RSA. For this, I generate a random 4096-bit RSA key, which I then encrypt with a random 48 character AES-256-CBC key. The script to do this is below:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/da9e12e407392bc6ab61ab4161a680e9.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>I upload the AES key to Parameter store (manually), and the encrypted RSA key to an S3 bucket. I also need to add this SSH key as a deploy key to GitHub. GitHub only allows your deploy key to be used in one repo at a time, so you might prefer to use a user-level key instead.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Lambda function is explicitly granted access to both the bucket, and the specific parameter in the store. With both the <strong>Key-Encrypting-Key</strong> and the <strong>Encrypted Key</strong>, the function can easily decrypt and obtain the final SSH key to use for uploading into Github.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I use the <code>serverless-iam-roles-per-function</code> plugin in   
serverless that allows me to specify individual IAM roles for each   
lambda function. This way, only this one specific function has access to
   either the parameter in parameter store or the special S3 bucket  
created just to store the encrypted SSH Key.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I'm only human -- there's probably a better way to do this using KMS alone, or even just Parameter store -- don't @ me!</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>3: Running Git Commands</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Now to run the Git commands. The real secret sauce is setting the $GIT_SSH and $GIT_SSH_COMMAND variables to point to directories in the <code>/tmp</code> folder, everything else is pretty standard. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The code I run is the following:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/af361d7abb0d4c9cf12755a15e0bc26b.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>The entire script is under 70 lines of code (including comments and blank-lines). Also notice how I use jq to parse the response from the awscli requests.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>4: Deleting the SSH Keys</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Before I exit the lambda function I delete the /tmp/.ssh directory where I store the SSH key. This is more paranoia than anything, but everything in the <code>/tmp</code> folder exists across lambda execution contexts. Hence you're better off deleting this folder if it store anything of value like an SSH key.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>A note about OpenSSL on Lambda</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The bash custom runtime looks to be built on the Python3.6 runtime, which makes sense since awscli is written in python anyway -- <em>take that you Java lovers! </em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The official runtime environments came pre-packaged with a few binaries like <strong>curl</strong>, <strong>awk</strong>  and <strong>openssl</strong>. However, to limit the changes in the environment, AWS rarely update these binaries from the time of the runtimes publication. Hence, the version of OpenSSL available to the python3.6 runtime (and by extension) the bash runtime -- is <strong>OpenSSL 1.0.2k-fips</strong>, which is problematic because -- well it's kinda old.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>More importantly to my use-case, when encrypting a file with a password using OpenSSL version 1.0.x, the key is generated by running the password through a <a href="https://security.stackexchange.com/questions/29106/openssl-recover-key-and-iv-by-passphrase/29139#29139">single iteration of MD5 </a>-- which is bad. You can specify the use of sha256 instead, which is only slightly better because you cannot modify the iteration count. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can package a better version of OpenSSL (e.g. version 1.1.xxx) in a layer, but that's for a later date. For now, I just ensure that my password has sufficient entropy, i.e. 48 base-64 characters which is 288 bits of entropy. In the future, I'll change this to use a better version of OpenSSL.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Writing a Lambda function to update a GitHub repo took a lot more effort than I initially anticipated, but the results are kinda nice.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For now, this function kicks-off once a week, and updates the <a href="https://github.com/keithrozario/Klayers">Klayers repo</a> in the process. You can see the results below:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6790,"sizeSlug":"large"} -->


![](/uploads/Screenshot-2019-09-09-at-11.04.00-PM.png)


<!-- /wp:image -->