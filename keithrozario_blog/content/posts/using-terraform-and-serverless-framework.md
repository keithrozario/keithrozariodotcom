+++
title = "Using Terraform and Serverless Framework"
slug = "using-terraform-and-serverless-framework"
date = "2019-03-03T19:10:54"
draft = false
categories = ['Cloud Computing', 'Serverless']
+++

<!-- wp:image {"id":6691} -->


![](/uploads/800px-Guaricano-Bambini.jpeg)<figcaption>Image from <a href="https://en.wikipedia.org/wiki/Holding_hands#/media/File:Guaricano-Bambini.JPG">wikicommons</a>.</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The Serverless framework (SF) is a fantastic tool for testing and deploying lambda functions, but it's reliance on cloudformation makes it clumsy for infrastructure like DynamoDB, S3 or SQS queues.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, if your <code>serverless.yml</code> file had 5 lambdas, you'd be able to <code>sls deploy</code> all day long. But add just one S3 bucket, and you'd  first have to <code>sls remove</code> before you could deploy again. This different behavior in the framework, once you introduce 'infra' is clumsy. Sometimes I use <code>deploy</code> to add functions without wanting to remove existing resources.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Terraform though, keeps the state of your infrastructure, and can apply <strong>only</strong> the changes. It also has powerful commands like <code>taint</code>, that can re-deploy a single piece of infrastructure, for instance to wipe clean a DynamoDB. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this post, I'll show how I got Terraform and Serverless to work together in deploying an application, using both frameworks strengths to complement each other.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>**From here on, I'll refer to tool Serverless Framework as SF to avoid confusing it with the actual term serverless </em></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Terraform and Serverless sitting on a tree</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>First some principles:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Use SF for Lambda &amp; API Gateway</li><li>Use Terraform for everything else.</li><li>Use a tfvars file for Terraform variable</li><li>Use JSON for the tfvars file</li><li>Terraform deploys <span style="text-decoration: underline;">first</span> followed by SF</li><li>Terraform will not depend on any output from SF</li><li>SF may depend on output from terraform</li><li>Use SSM Parameter Store to capture Terraform outputs</li><li>Import inputs into Serverless from SSM Parameter Store</li><li>Use <code>workspaces</code> in Terraform to manage different environments.</li><li>Use <code>stages</code> in Serverless to manage different environments.</li><li><code>stage</code>.name == <code>workspace</code>.name</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>In the end the deployment will look like this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6696} -->
<figure class="wp-block-image">![](/uploads/TerraformAndServerless1.png)


<!-- /wp:image -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Using SSM Parameter store</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>AWS System Manager(SSM) parameter store is the hands-down the best way to store deployment variables. It's a Key-Value store on AWS, that offers high scalability, data encryption at rest, and all for the very low price of free.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The real magic though is that SF can natively import ssm parameters into its deployment scripts (with no added plugins), which allow for an elegant way of getting deployment variables (like arns, bucket names and SQS urls) from Terraform into SF.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To export a variable out of Terraform onto Parameter store, use the following syntax. <em>note: Each parameter is a resource that needs to be deployed</em></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/ead7715fa64ae8cd38584e1e66be603f.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>and then use the following to import that configuration into serverless.yml as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/6b32c14fbb943a72d9a8f58b74a57c0f.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>I chose to do all my imports in the custom section of the <code>serverless.yml</code> file, as it gives me a single place to look for them. At this point you're probably wondering why I chose convoluted names for the parameters -- why not just <code>temp_table</code> instead of <code>/${var.app_name}/${terraform.workspace}/dynamodb_temp_table</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The short answer is that storing all parameters in a flat hierarchy doesn't give us the flexibility we need to manage parameters across different environments (like dev, test, and prod) and applications. Chances are, your single AWS account is being used for multiple applications, and multiple environments in those application -- hence breaking down the parameters in following form made sense:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><code><strong>/ &lt;app_name&gt; / &lt;environment_name&gt; / &lt;variable_name&gt;</strong></code> </p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>But to do this properly, we need to figure out how each framework manages environments.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Stages and Workspaces<br></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Because we pay zero for idle in serverless (at least in theory), we can effectively spin up a development environment per developer at no extra charge (theoretically!). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But to do this our tooling needs a way to separate out environments. Your single AWS account can't have identically named DynamoDB tables or Lambda functions in a single region, worse still S3 Buckets must be uniquely named throughout AWS! </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>SF uses <code>stages</code> to separate environments. It will append the stage name to the name of the Lambda function to prevent duplicates. This naming extends to even the Cloudwatch Log Groups and IAM roles.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Terraform uses <code>workspaces</code>, but doesn't automagically create different named resources for you. For this you'd either need to append the workspace name (ala SF) or use a tfvars file. Here's an example of a tfvars file (in json format).</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/5baa5d8906a7e57c96efcb2845c0ba60.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Here I have an <code>app_name</code> variable which is the same across all workspace. But then <code>s3bucket_domains</code> and <code>dynamodb_temp</code> variables are 'maps' that have different values for my two workspaces, <span style="text-decoration: underline;">default</span> and <span style="text-decoration: underline;">dev</span>.  I can reference them in my Terraform script by simply looking it up, for example:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/69585e5b986b0d8c9b994f385e3b783e.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Depending on my workspace (<span style="text-decoration: underline;">default</span> or <span style="text-decoration: underline;">dev</span>), different variables are used and created. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence we see that <code>workspace</code> in Terraform is the same as <code>stage</code> in SF. If we ensure that both of them have the same values, both frameworks can align their deployments.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As long as Terraform outputs to parameter store in the form of:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><code><strong>/${var.app_name}/${terraform.workspace}/&lt;variable_name&gt;</strong></code></p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>and serverless imports variables in the form of:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><code><strong>/${self:service.name}/${self:provider.stage}/&lt;variable_name&gt;</strong></code></p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>They'll be referencing the same value for the same environment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For those watching closely you'd have noticed that Terraform actually has no concept of application name, hence I just created a variable named <code>app_name</code> that is constant throughout the application and referenced that. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>But wait ... what about AWS Region<br></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For multi-regions deployment using the parameter store has a limit. How would serverless know which region's parameter store to query?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To resolve this, we made an exception. For this <strong>one</strong> variable, i.e. the region we deploy in, we have to use a variable available locally.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For that we reference the input variable file into Terraform, i.e. the <code>.tfvars</code> file. A lesser known feature of this file, is that it can be written in json, which as luck would have it, SF can read natively as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence by storing the aws region in our <code>tfvars.json</code> file like this:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/df874086d56e91fd24041e1213bd2006.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>And referencing it from our <code>serverless.yml</code> like this:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/2d521666cc980bf26c5f891b67ff692f.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>We can make sure serverless will continue to query the right region's parameter store for all other parameters.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Terraform is fantastic for laying down Infra, it doesn't package your code, or allow you to invoke/test lambda functions. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Serverless is awesome for deploying lambda functions, it takes care of IAM roles, Cloudwatch Logs and can easily connect to event triggers throughout your AWS infrastructure, but it lacks the desired features to deploy infrastructure.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Both these tools have a purpose, and neither one is sufficient (at least to me), but together they're pretty unstoppable. <em>(that being said, maybe packaging in Jenkins might be a better options)</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>No go forth and serverless.</p>
<!-- /wp:paragraph -->

<!-- wp:jetpack/gif {"giphyUrl":"https://giphy.com/embed/26BRCoPeetq9cAdhK","searchText":"success","paddingTop":"50%"} /-->