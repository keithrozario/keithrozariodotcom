+++
title = "Sign you Git Commits to Github with A Yubikey"
slug = "sign-you-git-commits-to-github-with-a-yubikey"
date = "2021-10-08T21:34:22"
draft = false
categories = ['Misc']
+++

<!-- wp:image {"align":"center","id":7564,"sizeSlug":"full","linkDestination":"none"} -->


![](/uploads/Screenshot-2021-10-08-at-9.31.00-PM.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>I found a few tutorials online to do this, but they're old and don't 100% work. So here's some quick steps on how you might sign your git commits with GPG keys stored on your Yubikey.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Since I'm a mac user, these steps are specifically for macOS, for Windows check out Scott Hanselman's great post <a href="https://www.hanselman.com/blog/how-to-setup-signed-git-commits-with-a-yubikey-neo-and-gpg-and-keybase-on-windows" target="_blank" rel="noreferrer noopener" title="https://www.hanselman.com/blog/how-to-setup-signed-git-commits-with-a-yubikey-neo-and-gpg-and-keybase-on-windows">here</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Step 1: Generate your GPG keys</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>First install GPG and then generate the key using:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ brew install gpg
$ gpg --full-generate-key</code></pre>
<!-- /wp:code -->

<!-- wp:image {"align":"center","id":7561,"sizeSlug":"large","linkDestination":"none"} -->


![](/uploads/GPG-generate-key-538x500.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>I used a 4096 RSA key (minimum key length supported by Github). You could choose to use something like ECC, but generally I find RSA to be compatible with just about anything, at the expense of a little speed (not security). ECC is cool, but let's get the basics first and then we'll try different types of keys. I also chose to expire the key after 1 year, you could choose any time (or not set an expiry) but some expiry is better than no expiry.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once the key is generated, you can list it using:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ gpg --list-secret-keys --keyid-format=long</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p><em>[Note: when executing this step, you won't see the 'Card Serial No. line', in the screenshot below, we'll cover that later]</em></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7563,"sizeSlug":"large","linkDestination":"none"} -->


![](/uploads/GPG-List-Keys-820x182.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For now, note down the id of the key, it's the hex digits after the rsa4096/ on the first line. From here you can export the public key component for safe-keeping. We'll upload this public key to Github later on so keeping it handy is super important.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ gpg --armor --export 9600392115690F9 &gt;&gt; "pubkey.txt"</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2>Step 2: Configure git and test</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>OK, so now that we've generated our GPG key, and saved the public key into a file. Let's first see if we can sign git commits with it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For that we have to configure <code>git</code> to use our newly minted key, because I have code for personal and corporate use, and this is my personal Yubikey, I've set the git configurations locally to the specific directory I'm in. If you want to set it globally just replace <code>--local</code> with <code>--global</code>.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ git config --local user.signingkey 96003921156930F9
$ git config --local user.email "keithjosephrozario@gmail.com"</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>You can verify the configuration by running <code>cat .git/config</code>. Remember, if your email address here doesn't match what's in Github, Github will complain, or at best give you an 'unverified' tag.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once complete we can sign our commits using the -S flag, like so:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ git commit -S -am "commit with yubikey"</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Typically you'd have to enter the passphrase to finally commit.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's is where I had my first stumble, I kept getting:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>error: gpg failed to sign the data fatal:
failed to write commit object</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>It turns out my zsh wasn't properly configured for gpg_tty, setting this fixed everything up. Thanks to this fix <a href="https://github.com/keybase/keybase-issues/issues/2798" title="https://github.com/keybase/keybase-issues/issues/2798">here</a>. I managed to overcome this problem. If you have issues signing git commits, first try to sign a generic string with this command to see if it works:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>export GPG_TTY=$(tty)
echo "test" | gpg --clearsign</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2>Step 3: Transfer GPG key to Yubikey</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you managed to sign everything so far, you're almost there.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Don't try to push to origin yet, let's first transfer the key from disk to the Yubikey.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ gpg --edit-key &lt;key_id&gt;
toggle
key 1
keytocard
1
save</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":7562,"sizeSlug":"large","linkDestination":"none"} -->


![](/uploads/List-GPG-820x311.png)


<!-- /wp:image -->

<!-- wp:paragraph -->
<p>You will be prompted for an Admin PIN -- if you haven't changed this before, it'll be <code>12345678</code>. The user pin is <code>123456</code>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Of course, to protect your key further, it's important to set your Admin Key to something else, You can change this by:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ gpg --card-edit
gpg/card&gt; admin
Admin commands are allowed
gpg/card&gt; passwd</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Once the key is transfered, you'll see a 'Card Serial No. ' when you list the key.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7563,"sizeSlug":"large","linkDestination":"none"} -->


![](/uploads/GPG-List-Keys-820x182.png)


<!-- /wp:image -->

<!-- wp:heading -->
<h2>Step 4: Copy public key to Github</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>OK, so now the key is in our Yubikey. Last step is to set this up on Github. Follow these steps <a href="https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-new-gpg-key-to-your-github-account" title="https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-new-gpg-key-to-your-github-account">here</a>, if you've followed everything along so far, the "key" field should be populated with the full contents of the  <code>pubkey.txt</code> file in your current directory. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And that should work. Now you can sign your commits, and push to Github, and get a glorious Verified tag for your commits.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7564,"sizeSlug":"full","linkDestination":"none"} -->


![](/uploads/Screenshot-2021-10-08-at-9.31.00-PM.png)


<!-- /wp:image -->

<!-- wp:heading -->
<h2>Other notes</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In order to use this key on another computer, you'll need to load the public key there first. Fortunately, GitHub conveniently stores our public key at <strong>https://github.com/&lt;username&gt;.gpg</strong> for us. To make things easier run the following commands:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>$ gpg --card-edit
gpg/card&gt; admin
Admin commands are allowed
gpg/card&gt; url 
URL to retrieve public key: https://github.com/keithrozario.gpg
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The commands above set a url in our Yubikey so that other computers know where to download the public key from. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then on any new computer, simply plug in your Yubikey and:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>gpg --card-edit
gpg/card&gt; fetch
gpg/card&gt; quit

gpg --edit-key &lt;your_key_id&gt;
gpg&gt; trust
Your decision? 5
gpg&gt; quit</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>For some reason, gpg couldn't access github and download the key on my new macbook. So instead I downloaded the key from github, and hosted it on a local server using <code>python -m http.server</code> and then entered the localhost url to grab the key. This worked fine.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After you've imported the public key into the GPG configuration of your new computer, and also trust it, everything should work normally.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As to what the levels of trust mean -- honestly, that's something for me to check out <a href="https://www.gnupg.org/gph/en/manual/x334.html">later</a>. But check out further references, <a href="https://developer.okta.com/blog/2021/07/07/developers-guide-to-gpg#use-your-gpg-key-on-multiple-computers">here</a> and <a href="https://unix.stackexchange.com/questions/512434/why-does-gpg-fail-to-fetch-key-stubs-from-my-smart-card">here</a>.</p>
<!-- /wp:paragraph -->