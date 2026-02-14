+++
title = "The Tyranny of Best Practice"
slug = "the-tyranny-of-best-practice"
date = "2024-08-12T14:00:45"
draft = false
categories = ['Misc']
+++

<!-- wp:paragraph -->
<p>All architects know what's best practice, but only good architects know when to use them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I've been in plenty conversations where someone goes "we should do X because it's best practice" -- and act that the discussion ended. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Best practice is what works for <em>most</em> people, <em>most</em> of the time. It isn't something that works for everyone all of the time -- otherwise we would mandate it across the board and architects would be out of their jobs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What is best for a multi-billion dollar bank, is not what is best for a small startup with 4 employees straight out of college -- and vice-versa.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's true that if you don't know what you're doing, blindly following best practice might put you in a better situation that not. But even just a little thought into whether a best practice is applicable to your use-case goes a long way. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sometimes trying to chase the 'best' actually takes time away for useful work. Be careful not to chase best practice too far down the rabbit hole -- you might end up with a great architecture but no useful features.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Take for example a Rubiks Cube. There are algorithms to solve a cube, and regardless of how scrambled the cube is, the algorithm will solve it to perfection. You will reach the solved state by blindly applying the algorithm regardless of how the cube starts out.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But life isn't like a Rubiks Cube -- not everyone starts off at the same place, and wants to go to the same destination. Plus, the cube applies no constraints, it does not involve trade-offs, it's just a fun puzzle that is always solveable.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Life is more like Chess. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In Chess, everyone may start at the same place, but the game very quickly descends into some new permutation you've never seen before. And unlike the Rubiks Cube, there is no one set algorithm that determines success. Every move has a trade-off, and every move invites your opponent to do respond in some unpredictable way.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So in Chess, we don't have algorithms. We have principles.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Principles like <em>Knights before Bishops</em>, or <em>Don't move the same piece twice</em>. And learning these principles will make you a better chess player -- but the good players (and certainly the great ones) know when to ignore the principles. Blindly following principles will actually make you a poor player -- <span style="text-decoration: underline;">you will not win a single Game of chess if you stick to all the principles</span>. If you want to win, you have to break the principles -- and more importantly know when to break them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And you can't break the Principles unless you know why they're there in the first place. Which brings us back to the 'best practice'. Do not listen to anyone spouting best practice, if they cannot backup their claim for <strong>why</strong> it is best practice -- and 'the spec says so' is not a good answer.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Know why a standard is there, know when it is applicable, and then decide if it makes sense based on your context.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Working Example</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The best example of this is the Access Token vs. ID token debate for oAuth and OIDC. The oAuth spec says very clearly: </p>
<!-- /wp:paragraph -->

<!-- wp:pullquote -->
<figure class="wp-block-pullquote"><blockquote><p>ID tokens should never be sent to an API.</p><cite>https://oauth.net/id-tokens-vs-access-tokens/</cite></blockquote></figure>
<!-- /wp:pullquote -->

<!-- wp:paragraph -->
<p>So here the best practice is to use Access Tokens to access an API. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Cool. Got it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But Access tokens don't have user identity, and it's much easier to just send the ID token with the user identity, and so many people do. But of course, you have the chorus of people who will tell you that access tokens are "following the spec" and ID tokens will introduce issues -- and those same people won't be able to articulate their point any further, other than some arcane specifications or edge cases that don't apply to you.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now there's a lot of developers out there who are trying to do the right thing, but are confused, they can't see any reason why an access token would be preferred over an ID token? See <a href="https://stackoverflow.com/questions/46681889/clarification-on-id-token-vs-access-token" target="_blank" rel="noopener" title="">here</a>, <a href="https://stackoverflow.com/questions/72048935/access-tokens-and-id-tokens" target="_blank" rel="noopener" title="">here</a>, <a href="https://stackoverflow.com/questions/72048935/access-tokens-and-id-tokens" target="_blank" rel="noopener" title="">here</a> and <a href="https://stackoverflow.com/questions/73851733/id-token-and-access-token-handling" target="_blank" rel="noopener" title="">here</a> .... and <a href="https://stackoverflow.com/questions/52213841/in-openid-connect-is-it-okay-to-pass-an-id-token-instead-of-an-access-token-to" target="_blank" rel="noopener" title="">here</a> and <a href="https://stackoverflow.com/questions/54204170/should-i-send-identity-token-to-my-api-resources" target="_blank" rel="noopener" title="">here</a> and <a href="https://stackoverflow.com/questions/63901860/why-shouldnt-i-use-idtoken-as-bearer-token-in-an-idp-context" target="_blank" rel="noopener" title="">here</a>... and <a href="https://stackoverflow.com/questions/63901860/why-shouldnt-i-use-idtoken-as-bearer-token-in-an-idp-context" target="_blank" rel="noopener" title="">here</a>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then there are people who go to projects like <a href="https://discuss.kubernetes.io/t/why-use-id-tokens-instead-of-access-tokens-for-authorization/27105" target="_blank" rel="noopener" title="">Kubernetes</a> and <a href="https://github.com/oauth2-proxy/oauth2-proxy/issues/1548" target="_blank" rel="noopener" title="">oauth2-proxy</a> and ask them "hey why do you use ID tokens instead of access tokens when the spec says otherwise" ... and the standard answer back is "<em>Defacto standards vs standards written</em>". Defacto standards are what people build applications with, standards written are what people build powerpoint slides for -- pick the right standard for your use-case.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So let's understand <strong>why</strong> the best practice is there -- but before that we need to understand what is the objective of OAuth:</p>
<!-- /wp:paragraph -->

<!-- wp:pullquote -->
<figure class="wp-block-pullquote"><blockquote><p>The OAuth 2.0 authorization framework enables a <strong>third-party application</strong> to obtain <strong>limited access</strong> to an HTTP service, ...</p><cite>https://datatracker.ietf.org/doc/html/rfc6749</cite></blockquote></figure>
<!-- /wp:pullquote -->

<!-- wp:paragraph -->
<p>Ah, so here we understand OAuth is for interaction between 3rd-parties, but I'm building my own application for my own users. 90% of people are building first-party apps that <s>in theory</s> don't need a protocol whose stated objective is 3rd-party delegation with limited access.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So really if we're building a first-party application where the "resource server" and the "client application" are the same thing, we don't need to follow a spec of something that has a different objective than us. Of course if they were different, there would be a case for access tokens, but not in our context. We need to dive deeper.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What is the difference between an Access Token and ID Token? </p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>The Access Token has a Scopes, but not Identity information</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>The ID token has Identity information but not scopes.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>And if we don't need scopes, because in a first-party scenario, users will have complete access to all of their data anyway. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But we need identity, because when a requests hits an API we need to understand which user this belongs to. It's much easier to use ID Tokens than it is to use Access Tokens to get those .... so......</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We'll just use ID Tokens. It make sense, it's generally cheaper and easier to implement, and as far as we can tell introduces no security risk.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And maybe this decision isn't correct, that I missed out something critical. But if there were something so critical, it would be better articulated in the reasons for using access tokens. Good architects must be bold enough to take risk, but still remain humble enough to accept that they are wrong. A lot of us suffer for analysis paralysis because we're afraid to give advice that breaks the 'norms' -- it's much safer just recommending best practice.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And like I said, all architects can recommend best practice. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But the good ones know when not too.</p>
<!-- /wp:paragraph -->