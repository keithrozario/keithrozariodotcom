+++
title = "Learning VIM over a Weekend"
slug = "learning-vim-over-a-weekend"
date = "2021-06-06T18:18:59"
draft = false
categories = ['Misc']
+++

<!-- wp:image {"align":"center","id":7472,"sizeSlug":"large","linkDestination":"none"} -->
![](/uploads/Screenshot-2021-06-05-at-3.55.28-PM.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>This weekend, I decided to learn me some Vim.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>According to it's website, "Vim is a highly configurable text editor built to make creating and changing any kind of text very efficient" -- to be honest, I only used vim when forced to from the command line, I wasn't sure why anyone would choose to do 'serious' editing in Vim. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Vim is notoriously hard -- so hard, <a href="https://qz.com/990214/a-million-people-have-visited-this-web-page-explaining-how-to-close-vim-a-notoriously-difficult-text-editing-program/">that millions of developers get stuck just trying the exit the damn program</a>. If you have an interface so difficult to understand that people can't intuitively do something mundane like exit -- you know you're dealing with something very user-<strong>un</strong>friendly. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But.....</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I also knew that Vim was powerful, and millions of other folks who invested the time to learn the damn thing swear by it. Vim's real power comes from the keyboard shortcuts -- which allow you to quickly move/edit different lines of text in a file without ever touching the mouse. Some of this is Geek-Snobbery, a elitist feeling of pride when you manage to execute something without ever touching the dreaded 'mouse' -- but truthfully keyboard typing is not much faster than a mouse, it's also more accurate, leaving less mistakes -- which means going even faster.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> So what did I learn?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First, the default system installation of Vim on macbook has some limitations. You're better off installing the brew version, by simply <code>brew install vim</code>. Make sure you restart your shell, so that the new installation can take effect -- or checking running <code>which vim</code> to see if it points to <code>/usr/local/bin</code>, instead of /usr/bin</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Next, you'll create to a vim configuration file in <code>~/.vimrc</code>. This file configures your vim settings, for my bare-bones setup to reconfigure vim for yaml, I used the following :</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<script src="https://gist.github.com/keithrozario/f3aaaef1b82c17eb7f5d57c92ce37572.js"></script>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><em>Side Note: Vim has a large plugin ecosystem. But unlike wordpress, or vscode there is no in-built marketplace to search and install them. The two plugins I installed, was done via git clones to a specific folder</em>: <code>~/.vim/pack/vendor/start/&lt;plugin_name&gt;</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There's too many vim commands to go through in one article, and certainly too many to memorize over a weekend. But I found that practicing my vim skills on frequent use-cases with my yaml files helped. So there they are:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To search for something on vim, we use the <code>/</code> followed by the string to search for. To exit the search function, we press &lt;ENTER&gt; and then use 'n' for the next instance of the string. You'd think that 'p' would be for previous, but unfortunately that was reserved for paste, so you'll have to use &lt;SHIFT&gt;-'n' (or N) to get the previous instance of the searched string.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So, if you're opening a config file and looking for the 3rd instance of a string like <code>POWERLEVEL9K_SHORTEN_STRATEGY</code>, you simply enter the following</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>/SHORTEN_STRATEGY&lt;ENTER&gt;nnn</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Neat! Sure beats scrolling through the file with nano, or having to exit the terminal by opening the file in vscode or sublimetext.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Next up, I decided to try some yaml editing, which is something I do often in my daily workflow. For this, I installed two plugins, namely indent-line-plugin and vim-yaml-folds. Both of these together with my <code>.vimrc</code> file, cause a 300 line cloudformation template to open like so:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7471,"sizeSlug":"large","linkDestination":"none"} -->
![](/uploads/Screenshot-2021-06-06-at-2.07.10-PM.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For YAML, we'd like to use some 'folding' that's when certain blocks of text are folded into a single line to long files readable on the terminal. To un-fold the entire file we just toggle folding off by entering <code>zi</code> , or just <code>za</code> to toggle the folding on a specific section. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I could then unpack the last folded line of that code to reveal this:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7473,"sizeSlug":"large","linkDestination":"none"} -->
![](/uploads/Screenshot-2021-06-06-at-5.58.07-PM-413x500.png)
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>From there, I could repeat that process over again, all without scrolling through on a keyboard. This method is more precise that the ctrl-f method I'd use in a text editor. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We can quickly scroll through a folded document using <code>zj</code>  and <code>zk</code>, which is kinda intutitive since j and k both map to down and up respectively.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Finally, I couldn't figure out how to select entire blocks in a single command -- I could select the start of block in 'visual' mode and then type in j for each line I would like to select, for example</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>vjjjjj</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>But that felt like a waste of keystrokes, instead I noticed that if you spaced out each block with a newline, you could select each block using the paragraph command. For example the following command would select 2 blocks of text, and deletes them. (there's 3 'ip' because you select one block, the new line between them, and the 2nd block).</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>vipipipd</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Lastly, if we're unpacking this via keyboard, it's usually recommended to use a single line cloudformation intrinsic functions rather than multi-line ones. It just makes it easier to unpack the entire resource:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7475,"sizeSlug":"large","linkDestination":"none"} -->
![](/uploads/Screenshot-2021-06-06-at-6.16.26-PM-820x157.png)
<!-- /wp:image -->