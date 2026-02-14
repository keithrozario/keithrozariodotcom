+++
title = "Run serverless on GitHub actions"
slug = "run-serverless-on-github-actions"
date = "2020-02-27T20:26:31"
draft = false
categories = ['Security &amp; Privacy', 'Serverless']
+++

<!-- wp:paragraph -->
<p>GitHub actions is the new kid on the workflow block.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It allows users to orchestrate workflows using familiar git commands like push &amp; pull requests, and un-familiar GitHub events like gollum, issue creation and milestone closures.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this post, we'll use GitHub actions to orchestrate a build pipeline that will deploy lambda functions using the <a href="https://serverless.com/">Serverless framework</a>. There's a lot of tutorials that cover the basics of doing this, but we'll dive deeper and cover off framework plugins and deploying to different environments using feature branches.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A working example of all this can be found in this GitHub repo <a href="https://github.com/keithrozario/github_actions_serverless">here</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>GitHub Actions basics</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let's start with the basics -- in order to create a build pipeline in GitHub, you'll first need to define the workflow via yaml files in the <code>.github/workflows</code> directory of your repository.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Each workflow file consists <strong>triggers</strong>, <strong>jobs</strong> and <strong>steps</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Triggers define when to execute jobs.</li><li>Jobs define what steps to execute (with flow logic)</li><li>Steps are the granular commands of each job.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>For a simple serverless deploy project, we can use the following workflow file:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/297194ec935436b432e613fa6020a047.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>If you put this yaml file into <code>.github/workflows/main.yml</code>, then a push to master will trigger it -- which in turn will deploy your <code>serverless.yml</code> configuration using <code>serverless deploy</code>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So far, so good, but there are already <a href="https://vishwas.tech/blog/2019/12/15/serverless-deployment-using-serverless-framework-github-actions.html">good post </a>online for basic deployments like this, so let's shift our gears by including framework plugins.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Using plugins</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Plugins are a mixed-bag with any framework. On one hand, they add amazing functionality by leveraging the community -- but on the other hand, they introduce lots (and lots) of security, stability and trust issues. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Serverless plugins aren't that bad though ( at least compared to something like wordpress) -- so far I've had only good experiences with them -- although I still limit them wherever possible. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But that still means I use them, and need a pipeline that supports them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So how do we include serverless plugins? Simple.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Include a <code>package-lock.json</code> file in our deployment, and the previous workflow file would work just fine In my example, I installed two serverless plugins:</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">$ npm install --save-dev serverless-iam-roles-per-function
$ npm install --save-dev serverless-step-functions</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>As long as the corresponding <code>package-lock.json</code> file is located in the working directory of serverless.yml file, the framework will deploy with the plugin installed. You can view the package-lock.json file <a href="https://github.com/keithrozario/github_actions_serverless/blob/master/package-lock.json">here.</a></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6955,"sizeSlug":"large"} -->
![](/uploads/Screenshot-2020-02-27-at-7.14.37-AM.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>With that simple step out of the way, let's now switch our attention towards setting up our pipeline for deploying to different environments.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Stages and Environment</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This is where things get a bit clumsy, GitHub actions work off Git version control, and the triggers are limited to Git actions -- as far as I can tell you can't simply trigger a job by pressing a button. Everything has to be done via GitHub and the triggers already specified.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can circumvent this issue by creating a dummy deploy, using something like this:</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">$ git commit --allow-empty -m "trigger GitHub actions"</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>But you'd be trying to hack around Git rather than embracing it. Instead, I think we should approach this problem by trying to embrace the wonderful harmony of Git and serverless all at once.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With serverless, each additional environment of lambda functions cost nothing. Even additional SQS queues, DynamoDB tables and S3 buckets would add pennies on your AWS bills. Furthermore, the serverless framework actually helps us create these separate environments via the stages.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Each stage in the framework is an independent (namespace separated) environment, containing a copy of all deployed resources. <em>Under the hood, the framework uses Cloudformation to deploy, and includes the stage name in the resources in the stack to ensure uniqueness.</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here we can see how the harmony might work -- if we ensure that branches in git corresponds to stages in framework, we can generate unique environments for each branch, and have that propagate all the way from feature branch to master. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The main caveat, is that we should limit our tinkering with our environments outside of this pipeline (and that's true of any pipeline), if you deploy using the pipeline, but modify configuration manually, the system breaks down quickly! Use the console/CLI as read-only mechanisms, everything else should go via the pipeline.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Feature Branches and Serverless</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Imagine we had a standard feature-branch strategy as below:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6947,"sizeSlug":"large"} -->
![](/uploads/feature_branch_flow.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>In order to ensure that each branch in the repository corresponds to a different environment, all we need to do is modify the Github actions workflow to specify the stage on each deploy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Typically, we'd deploy a stage via serverless framework using the following:</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">$ serverless deploy --stage dev</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>But an easier way for us is to set the <code>$STAGE</code> environment variable. If we set the workflow to set <code>$STAGE</code> to the name of the current branch, then the framework will deploy all branches into their own stages.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Doing this took some digging around in docs. But each time a Github action is invoked a <code>$GITHUB_REF</code> environment variable is populated, which contains the name of the current working branch. To get the branch name out of this variable -- and then setting the <code>$STAGE</code> environment variable we have to do something like the below:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/e079be6bc68456bd9c6da50a567e5c4c.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>When combined with the previous example, we can trigger a build on every commit to every branch in the repository -- which in turn will deploy environments per branch into our AWS account, like below:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6951,"sizeSlug":"large"} -->
![](/uploads/feature_branch_flow2.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>But at some point, presumably after the 10,000th Jira story is closed, we'd want to clean up those environments .... so let's move onto deletion and environment cleanup.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Cleanup</h2>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>What Git giveth, Git can taketh away!</p><cite>- Keith</cite></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Logically, if a new branch creates a new environment, then a deleted branch should remove the environment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For this we can use <code>serverless remove</code>, but we'll need two <em><span style="text-decoration: underline;">minor</span></em> tweaks.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First we need to setup a trigger for delete (instead of push), so that the job gets triggered on a deletion of a branch. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Second, for some strange reason, the <code><a href="https://help.github.com/en/actions/reference/events-that-trigger-workflows">$GITHUB_REF</a></code> variable during branch deletion refers to the <strong>default</strong> branch of the repository (instead of the <strong>deleted</strong> branch). Hence, we need to dig deeper into the innards of GitHub actions to extract the name of the deleted branch during a deletion trigger.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Every github action populates a json file into the running container with the full event data that triggered that action, this file is known as the <a href="https://www.edwardthomson.com/blog/github_actions_12_information_about_your_workflow.html">github context</a>. Because the file is json, we can use <a href="https://stedolan.github.io/jq/">jq</a> to extract specific fields of that event including getting the name of the deleted branch:</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/6f0031111f71d1569ffb0c1e515a236c.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>This way, once a branch is deleted, a job is triggered that deletes the environment tied to that branch, using <code>serverless remove</code>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence, as long as our repository is pruned of these branches every once in a while, we'll reduce clutter in our AWS account as well. Now we have an account with environments for each branch, and maybe even a develop and master branch -- what about pushing this to production?</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Branches vs. Repos</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Here's a question....</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Can we run GitHub actions for production and development environments from a single repo -- yes!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Should we do that? -- NO!!!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Typically, for security (and other!) reasons your development and production environments will live in different AWS accounts -- which means they'll get a different set of AWS Secrets. These secrets are stored in Github for our pipelines to consume.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As far as I could tell, there's no way to limit secrets to specific branches or users. Hence, any user could modify the workflow files in their branch, and trigger a deploy to production utilizing the AWS keys in the repo. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After all the current executing workflow is the one defined in your current branch. So if you had your production key named <code>AWS_SECRET_KEY_PRODUCTION</code> there's nothing to stop me as a developer working on feature branch to use that key to deploy into prod.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So instead, we should keep the production keys in a separate (forked?) repo, and only deploy to production from there. Obviously this repo should be tightly controlled, and presumably will only accept pull requests from the release or QA branch of a developer repo -- I'm not sure I have an elegant solution here.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Typically, you wouldn't have 2 separate code-repos, but you would have two separate build pipelines, and since in Github Actions the repo and pipeline are the same thing -- this might make sense.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6952,"sizeSlug":"large"} -->
![](/uploads/Different_repo.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Also, I'm still torn about how hotfixes might work in the solution above. It'll be a pretty slow process to modify the Release branch, and then perform 2 pull requests, but perhaps that's OK. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Github actions is really cool, but it's a workflow tool that <strong>may</strong> work well as a build pipeline. It misses the mark in some places, and felt a bit un-finished to me -- at least for this use-case.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But it does have magnificent promise, after all your code is already there -- and you're already using it for issues/pull requests. You owe it to yourself to at least try it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The best thing about GitHub actions though, is that it is SaaS offering -- no more mucking around with Jenkins configs, and no maintaining servers with provisioned capacity or storage issues. It fits in well with our serverless paradigm and works better than most other build pipelines, and I can easily see a bigger community forming around this than for something like Travis or CircleCI (don't @ me).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sometime later, I hope to include tests as part of the build pipeline, and some Terraform scripts for our deployment as well.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>TL:DR</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>One thing that frustrated me about the GitHub actions was the fact that it built a ephemeral container **everytime** we made a deploy -- and for some reason that container wasn't cache-able. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Which meant every build took at least ~45seconds just to get that container ready. In addition to that -- serverless framework uses cloudformation, which means the bulk of it's time is spent waiting on Cloudformation to deploy (another ~40seconds to deploy). Even for fairly simply deployments it can take 3-5 minutes end to end.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can actually shorten this tremendously, by skipping the serverless action, and installing the framework yourself into the container. This way, you can cache the npm modules, and cut down the build time by 1-2 minutes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Or you could just run unit test, and even deploy locally from your machine, and only push to the build pipeline once everything is ready -- although this is prone to error, as a missed stage name will over-write an already existing stage.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Even longer stop reading</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The example <a href="https://github.com/keithrozario/github_actions_serverless">repo here</a> has all the code, and with one small change. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Instead of using the serverless github actions in the recommended way:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>serverless/github-action@master</code> </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I use:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>serverless/github-action@e17abe72d4969e86cb53576ade34e95c40362f0e</code> </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>to avoid a security issue highlighted <a href="https://julienrenaux.fr/2019/12/20/github-actions-security-risk/">here</a>.</p>
<!-- /wp:paragraph -->