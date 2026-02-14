+++
title = "Amazon KMS: Intro"
slug = "amazon-kms-intro"
date = "2020-01-06T23:41:19"
draft = false
categories = ['Security &amp; Privacy', 'Serverless']
+++

<!-- wp:paragraph -->
<p>Amazon KMS is one of the most integrated AWS services, but probably also the least understood. Most developers know about it, and what it can do, but never really fully realize the potential of the service. So here's a rundown of the innards of the KMS service.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>What is KMS?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>KMS (Key Management Service) is an AWS offering that allows us to <strong>create, manage </strong>and<strong> use cryptographic keys</strong>. Like everything else in AWS, it's highly available, provided via API, and charged on a per-use basis.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The service initially only supported symmetric keys, but now offers asymmetric keys in certain regions. With this, certain operations involving asymmetric keys cost more, but regardless of the key type, the charging model is on a per-use and per-key basis. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>i.e. more keys or more key operations and you'll pay more.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Keys stored in KMS are called Customer Master Keys(CMKs) and here's where the confusion starts.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>KMS and the Customer Master Key</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The term Customer MASTER key, suggest that each customer has one <code>Master</code> key and perhaps some <code>Slave</code> keys. But that's not true, a single customer can many CMKs, limited only by their budget.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Instead the term <code>Master</code> refers to the type of operations the key performs, which is to encrypt and decrypt other keys, a better term would be a Key-Encrypting-Key, but AWS are not in the habit of naming things well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>CMKs are never revealed in plaintext. You can never retrieve the key material from a CMK, there is no API call to do this, not even if you're the root user.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is a security feature, as you cannot lose (or accidentally reveal) something you never had. All you can do with CMKs is encrypt and decrypt other bits of data, but not all CMKs are created equal, here's the different type of CMKs available.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>There are 3 types of CMKs.</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>AWS Owned CMK</li><li>AWS Managed CMK</li><li>Customer Managed CMK</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Yes, <em>Customer Managed Customer Master Key</em> is a mouthful, but that's AWS for you! -- this still beats System Manager Session Manager though, so at least we're lucky.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But I digress, let's take a look at the AWS Owned CMK first.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>AWS Owned CMK</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The AWS Owned CMK is something you'll never see or be able to interact with, other than to point your data at it for encryption. This is owned and managed by AWS, and is shared across multiple customers in a region.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, the default encryption on DynamoDB is done using the AWS Owned CMK, which is provided for free and is done almost transparently to the user.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AWS Owned CMKs are pretty boring, the provide the base "encrypted at rest" requirement, but not much more than that. Let's move onto the AWS Managed CMK.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>AWS Managed CMKs.</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>AWS Managed CMKs are created by AWS, specifically for you to use on a specific service, like S3, DynamoDB, Lambda etc. You can use this to encrypt these resources, but because the key is unique to you, only principals in your account can access them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you encrypt an S3 Object using a CMK, then only principals with access to **both** the file and the CMK can read it. The additional protection means, that even lambda functions with full access to an S3 bucket will be denied access to S3 objects that are encrypted with CMKs they don't have access to. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It similarly applies for other data like EBS snapshots, DynamoDB tables and SSM Paramaters. But the AWS Managed CMK is limited in one crucial way -- it's key policies cannot be modified.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A key policy is the resource policy that defines who can/cannot access the key, and for AWS Managed CMKs the policy allows every principal within the same account access to them. Which means principals within your account are going to be able to access them -- unless you explicitly deny it in the IAM Role policy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's a statement in the key policy for a Amazon managed CMK, created specifically for S3:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>{
  "Sid": "Allow access through S3 for all principals in the account that are authorized to use S3",
  "Effect": "Allow",
  "Principal": {
    "AWS": "*"
  },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "s3.ap-southeast-1.amazonaws.com",
      "kms:CallerAccount": "&lt;AccountID>"
    }
  }
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>If you had an S3 bucket, shared between multiple accounts, by default any object you put into the bucket  (that you encrypt with an AWS Managed CMK) is going to only be accessible to principals in your account.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So while AWS Managed CMKs are great, they lack flexibility and granular control, for these features, we'd have to venture into the world of the Customer Managed CMKs.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Customer Managed CMK </h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The Customer Managed CMK is the most flexible key offered in KMS. Unlike their AWS Managed cousins, you can modify the key policies on these to:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Limit access even within your own account</li><li>Grant access to external users from other accounts</li><li>Allow users direct access to key operations like <code>GenerateDataKey</code>, <code>Encrypt</code> and <code>Decrypt</code>.</li><li>Use one key across multiple services</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>A Customer Managed CMK not only protects accidentally exposed buckets, but also provides protection against compromised resources -- as long as those resources aren't granted permissions for the specific CMK.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you had an S3 bucket, shared between lambda functions in one account, you can limit access to certain encrypted objects in the bucket by only allowing specific roles access to the CMK via the CMK policy. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But key policies differ from other resource policies in AWS by one critical difference -- they **must** grant access to the principal in order for the key to be accessed. In other resource policies, either the resource policy <strong>or</strong> the Principal policy could allow access -- but for CMKs, the key policy must <strong><span style="text-decoration: underline;">and</span></strong> the Priciapl policy but grant the access.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To add to the confusion, most Customer Managed CMKs have key policies that look like this:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>{
  "Version": "2012-10-17",
  "Id": "key-default-1",
  "Statement": &#91;
    {
      "Sid": "Enable IAM User Permissions",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::12345678:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    }
  ]
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The Principal in this case isn't the 'root' user of the account -- but rather it signifies that the key policy is <a href="https://youtu.be/X1eZjXQ55ec?t=1375">delegating access to IAM to grant access to this key.</a> In effect, this key policy states that any User/Role in the account can perform <code>kms:*</code> operations on the key. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So managing permissions to these keys can be a nightmare, mucking around with json doesn't cause anyone to jump for joy. A simpler way to grant access to CMKs is via Key Grants.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1>Key Grants</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Typically sharing resources within AWS require modify policy documents in IAM, but CMKs have a separate mechanism specifically designed to share them across principals called Key Grants.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Key grants give access to principals, allowing them to access specified permissions like <code>kms:DescribeKey</code> or <code>kms:Decrypt</code> on a permanent or temporary basis without having to modify either the key policy or the permission policy of the IAM Principal. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The example code below, will grant access a principal access to a Decrypt operation on a key, without the need for modifying policy documents.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>    response = kms_client.create_grant(
        KeyId=key_arn,
        GranteePrincipal='&lt;principal_arn>',
        Operations=['Decrypt'],
        Name='TestingGrants'
    )</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The IAM principal that receives the grant does not need to specify the KMS key in its permission policy for this to work. Hence it is possible for IAM principals to have access to CMKs in your account, but not be listed in the key policy. To see the full list of grants currently active on a CMK use the <code>listGrants</code> operation. You can also revoke/retire grants to principals, again using an identical syntax of code:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>response = kms_client.retire_grant(GrantToken=grant_token)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>So now we've got our keys, we know how to share them, but how do we rotate them?</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1>CMK Rotation</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>While regular password rotations are no longer recommended (<a href="https://pages.nist.gov/800-63-FAQ/#q-b05">true story</a>), encryption keys are different. For one, as we use our CMKs more, there will be more ciphertext out encrypted by it, which increases the likelihood of the key being compromised. It also increases the damage incurred from a compromised key as more data would have been encrypted under the same key. Hence key rotation is still considered best-practice.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's two ways to rotate a CMK in AWS, automatic rotation and manual rotation. Let's start with automatic rotation since it's easy. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Amazon Managed CMKs are automatically rotated once every 3 years, while Customer Managed CMKs can either be automatically rotated (once every year) or manually rotated at the users defined frequency.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But in order to understand automatic rotation better, we'll have to first unpack what a CMK is, because it's more than a key.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If your key is 256-bits of data, then a CMK is a container for that data, similar to howS3 objects are containers for files. The actually 256-bits is stored in something called the HSM Backing Key (HBK), and contained in a CMK together with Metadata about the key. Because the CMK is a AWS resource, it has properties like an ARN for unique identification, and resource policy (key policy) attached to it for access-management.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6900,"sizeSlug":"large"} -->


![](/uploads/CMK-Component-View.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>With automatic rotation, AWS creates a new backing key while keeping the old one(s). Your applications can continue to reference the same ARN and all encryption and decryption activities will continue to work even on objects encrypted with the old backing key. The only thing to note, is that you'll be charged per backing key, and not per CMK (which can hold multiple keys).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For Customer Managed CMKs, we have the added benefit of manual rotation, which isn't really a rotation but creating a new CMK, and pointing all new operations to the new CMK while keeping the old one. But when you create a new CMK -- you get a new ARN, in order for manual rotation to work we'll need to work with key aliases.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Key Alias and Manual CMK rotation</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Think of a key alias as bit.ly links for CMKs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A key alias is a pointer to a CMK. Any reference to the key alias via AWS SDKs (like boto3), resolves to the CMK that the key alias points to at that moment in time. Key alias can be updated, ensuring that any program referring to the key alias can be pointed to any key in an account without the need for code changes on the application.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence in order to rotate CMKs:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Create a new CMK</li><li>Update the key alias to point to the new CMK.</li><li>But….. we need to keep the old CMK. </li><li>If you're wondering why ... read on!</li></ul>
<!-- /wp:list -->

<!-- wp:image {"id":6901,"sizeSlug":"large"} -->


![](/uploads/rotated.003.jpeg)


<!-- /wp:image -->

<!-- wp:heading -->
<h2>Rotation doesn't re-encrypt.</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Key rotation, either manual or automatic does not re-encrypt anything that was encrypted using the 'older' CMK. It merely creates a completely new CMK (manual) or a new version of the CMK (automatic rotation). So if you delete the old key, all data encrypted with the old CMK will be lost to you forever.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you have a policy to rotate keys once a year, then after 7 years, you'd have 7 keys guarding your data, the compromise of 1 key would only compromise 1 years worth of data. If you re-encrypted the data every time the key was rotated -- you'd have only one key guarding all your data.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Add to that, the cost of re-encrypting increases every year as you'd have more and more data to re-encrypt with the new key.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But how would you know which CMK was used to encrypt which data after 7 years?! For that we have to dive into how Encryption with KMS actually works.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Object Metadata</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>As mentioned the CMK is not used to Encrypt data directly, rather it's used as a <strong>Key-Encrypting-Key</strong>. You can also ask KMS to do all the heavy-lifting for you, by generating a key, and providing both the plaintext key and encrypted key to you.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The encrypted key comes in the form of a <code>CipherTextBlob</code>, which is not just the Ciphertext, but includes additional meta-data about the CMK that was used to encrypt it. When you ask KMS to decrypt the resulting <code>CipherTextBlob</code>, it will:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Check meta-data</li><li>Select the right key</li><li>Decrypt the data</li><li>Send back plaintext to you</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>In short, for symmetric keys, KMS can decrypt a <code>CipherTextBlob</code> without the need for the caller to specify the CMK, as that data is already present in the blob.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Similarly, every S3 object encrypted with a CMK, contains the key id as part of its metadata. You can check an objects <code>ssekms_key_id</code> to determine which CMK was used to encrypt it. S3 does this on your behalf when you try to access an encrypted object. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence, you don't have to specify the CMK when trying to access encrypted objects in S3, as the service already knows which CMK to use.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But how does this work in practice?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First we request a key from KMS specifying a CMK, and KMS will provide both the plaintext key and encrypted key (encrypted using the CMK). </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With the plaintext key, an application can now proceed to encrypt data, erasing the plaintext key once the encryption operation is done. Then it  store the encrypted key next to the encrypted data in a single structure called an envelope.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Decryption involves decrypting the encrypted key, using the resulting plaintext key to decrypt the data. I know it's pretty complicated, so here's a picture.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6889,"sizeSlug":"large"} -->


![](/uploads/KeyGeneration_KMS.001.png)


<!-- /wp:image -->

<!-- wp:heading -->
<h2>CMK with Imported Key Material</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In case you don't trust AWS to generate CMKs for you, or you have a strict requirement to be able to delete keys instantaneously -- then you're going to have to use imported key material.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The option is a Customer Managed CMK with Imported Key Material -- which is basically loading your own HSM Backing Key (HBK), into an existing CMK, remember CMKs are just containers for keys.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can generate the 256-bit symmetric key on your own, and import it into a empty CMK. Because keys are considered super duper sensitive (that's a technical term), AWS doesn't allow you to just send the binary blob to them, instead you'll have to:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Request Upload parameters from AWS, to obtain a wrapping key and a import token.</li><li>Use the wrapping key to encrypt your symmetric key.</li><li>Send a request to import the key, providing the import token and encrypted symmetric key.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>It's a bit hard to comprehend, but here's a quick python code to execute the steps above</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>import boto3
import json
from botocore.exceptions import ClientError
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

imported_key_arn = &lt;imported_key_arn>
symmetric_key = &lt;binary symmetric key>

kms_client = boto3.client('kms')

print("Getting Import Token and RSA Wrapping key from AWS")
response = kms_client.get_parameters_for_import(
    KeyId=imported_key_arn,
    WrappingAlgorithm='RSAES_OAEP_SHA_1',
    WrappingKeySpec='RSA_2048'
)

import_token = response['ImportToken']
public_key = RSA.import_key(response['PublicKey'])
rsa_key = PKCS1_OAEP.new(public_key)  # defaults to SHA1 Hash
encrypted_key = rsa_key.encrypt(symmetric_key)

print(f"Importing key material into {imported_key_arn}")
response = kms_client.import_key_material(
    KeyId=imported_key_arn,
    ImportToken=import_token,
    EncryptedKeyMaterial=encrypted_key,
    ExpirationModel='KEY_MATERIAL_DOES_NOT_EXPIRE'
)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>These imported keys have two special properties:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>You have the key material for them</li><li>You can delete them instantly</li><li>You can re-import key material into AWS</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Which means if you've got a large bucket of data encrypted with a CMK, you can delete the key material, rendering the entire bucket useless -- with immediate effect. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can re-import the key material back into the CMK, should your mind suddenly change, but there's a catch, you can only re-import the same key material back into the CMK -- you can't use this method to swap the HBKs in the CMK.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>More importantly, creating two CMKs with the same key material won't help you either Anything encrypted with CMK, can only be decrypted with the exact same CMK (remember the meta-data paragraph we covered earlier). AWS will not decrypt anything encrypted under a different CMK, even if the the CMK contains the Backing Key.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally let's talk about all we audit all of this.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Encryption Context</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>All calls to KMS are logged in Cloudtrail, but as you can imagine a CMK might be used for create many other keys, and trying to keep track of those can be hard. A key generated by a CMK is called a data key, and is not an AWS resource, hence has no ARN and cannot be tagged.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When you generate a data key in KMS, you can specify key-value pairs along with that generation process. Similarly when you request decryption of that key, the key-value pair must be provided along with the request. This is called the encryption context. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>KMS will refuse to decrypt a key, if the encryption context provided is not identical to the one during generation. But beware, this is not a password, the encryption context will appear in plaintext in Cloudtrail logs -- because that's the point. With the encryption context, you can now quickly query the log data for when a specific key was used for decryption.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's a snippet of a CloudTrail event with encryption context:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>{<br>
  "eventVersion": "1.05",<br>
  "eventTime": "2020-01-11T09:04:15Z",<br>
  "eventSource": "kms.amazonaws.com",<br>
  "eventName": "Decrypt",<br>
  "awsRegion": "ap-southeast-1",<br>
  "userAgent": "Boto3/1.10.34 Python/3.7.5 Linux/4.14.138-99.102.amzn2.x86_64 exec-env/AWS_Lambda_python3.7 Botocore/1.13.34",<br>
  "requestParameters": {<br>
    "encryptionAlgorithm": "SYMMETRIC_DEFAULT",<br>
    "encryptionContext": {<br>
      "purpose": "for fun",<br>
      "env": "test"<br>
    }<br>
  },<br>
  "eventType": "AwsApiCall",<br>
  "recipientAccountId": "820756113164"<br>
}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And with that we've come to the end of this post.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>KMS is a kick-ass AWS offering, and hopefully this post helped you understand if better. Let me know if you have any feedback, I'm happy to hear them. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>p.s. I'm prepping for my security specialty certification, and hence the long post. Wish me luck!</p>
<!-- /wp:paragraph -->