+++
title = "Multi-Accounts for AWS with Google &#39;+&#39; emails."
slug = "multi-accounts-for-aws-with-google-emails"
date = "2019-12-15T12:51:01"
draft = false
categories = ['Misc']
+++

<!-- wp:image {"id":6861,"sizeSlug":"large"} -->
![](/uploads/Screenshot-2019-12-17-at-9.29.38-PM.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Last week, I launched a new pipeline for Klayers to build Python3.8 Lambda layers in addition to Python3.7. For this, I needed a separate pipeline because not only is it a new runtime, but under the hood this Lambda uses a new Operating System (Amazon Linux 2 vs. Amazon Linux 1)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So I took the opportunity to make things right from an account hierarchy perspective. Klayers for Python3.7 lived in it's own separate account from all my other hobby projects on AWS -- but I kept all stages in it (default, dev and production). [note:<em>Default</em> is an odd-name, but it ties to the Terraform nomenclature]. This afforded some flexibility, but the account felt bloated from the weight of the different deployments -- even though they existed in different regions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It made no sense to have default and dev on the same account as production -- especially since accounts were free. Having entirely separate accounts for prod &amp; non-prod incurred no cost, and came with the benefit of additional free-tiers and tidier accounts with fewer resources in them -- but the benefits don't stop there.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>Multi-accounts allowed me additional security controls through Service Control Policies (SCP) via AWS Organizations. Which keeps a nice tight lid on everything. For example, all accounts in Klayers have an SCP that prevents any EC2, EKS, ECR, Fargate and Route53 activities. This helps to limit the effect of any compromise on those accounts -- no bitcoin mining here if I lose the key!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That being said, once you put the accounts in organizations, they share the free tier across the account -- so balance it out!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So whey don't people do this more often?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>One major drawback of creating this multiple accounts is managing them -- if you kill an AWS account -- you'll permanently kill the email associated with it as well. To avoid this, I use a lesser known feature on Gmail (and Google Apps) to create an infinite number of email accounts tied to a single 'real account'.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Unlimited Gmail Accounts</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>You can a '+' anywhere between your username and @ sign to get a new email address that requires zero additional effort on Gmail to setup. For example</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>johndoe+aws1@gmail.com</li><li>johndoe+aws2@gmail.com</li><li>johndoe+awsDev@gmail.com</li><li>johndoe+awsProd@gmail.com</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>All send their emails to the same email address (johndoe@gmail.com)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This way, I only need to create AWS accounts, and not have to create additional email accounts to support them. This make sense in 'real' organizations where there a multiple folks with actual different email addresses -- but could work for individual projects like Klayers, using this '+' email addresses to simulate those different people.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There is still manual effort in setting up the accounts (generally 5-10 minutes), and then creating the API keys necessary to deploy -- but this is a one-time thing. I also have to replicate some manual work, like enabling a<strong>p-east-1</strong> and <strong>me-south-1</strong> on the accounts, as these regions are activated by default -- but again a one time thing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Overall the mixture of AWS Organizations capability, and Gmails '+' addresses allow even one-person projects like Klayers to benefit for a better hierarchy of accounts, resulting in far tidier and simpler account management.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Last note, both Terraform and Serverless Framework support multiple accounts on a single machine. Simply configure your <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html">~/.aws/credentials file for multiple profiles</a>, and then point both them using the <strong>provider-&gt;profile</strong> variable to the correct AWS profile as setup in the credentials file.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Final bit, is that sometimes we have to resort to quick n' dirty solutions which require us to copy paste stuff using the AWS Console -- I'll be honest, using the console for anything other than view only feels wrong to me, but sometimes we gotta do it. When we have multiple accounts on AWS, trying to copy and paste stuff across them is a pain -- but a useful feature baked into Firefox comes in handy. Using firefox containers, we're able to have a single Browser instance open, that access multiple aws accounts, each with their own tab nicely color-coded for you.</p>
<!-- /wp:paragraph -->