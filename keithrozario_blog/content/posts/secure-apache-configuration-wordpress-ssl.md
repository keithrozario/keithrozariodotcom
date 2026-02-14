+++
title = "Secure Apache configuration for Wordpress & SSL"
slug = "secure-apache-configuration-wordpress-ssl"
date = "2015-03-30T20:00:47"
draft = false
categories = ['Blog', 'Security &amp; Privacy']
+++

[caption id="attachment_4859" align="alignleft" width="256"]

![Apache runs nearly 50% of all active websites](/uploads/images5.jpg)

 Apache runs nearly 50% of all active websites[/caption]

Recently I moved the hosting for keithRozario.com from a regular hosted platform called WPWebhost to my own Virtual machine on digitalOcean. The results have been great, but the migration process was a bit tedious and took some effort.

I thought I'd share my Apache configurations, so that if you're thinking of hosting your own WordPress site on an SSL server, you'll at least have a solid base to start off from. I'm by no means an expert here, but this is what makes sense to me, and if you have any feedback please let me know in the comments.

So let's start.<!--more-->

If you install wordpress from the one-click install on digitalOcean, by default you get an Ubuntu Linux instance with Apache2 installed. Apache2 has two configurations file:
<pre>/etc/apache2/apache2.conf</pre>
and
<pre>/etc/apache2/sites-enabled/000-default.conf</pre>
By default, the second file is optional and probably doesn't exist, but my preference was to create it, and keep the virtual host definitions here, while storing the general apache settings in the apache2.conf file.

The contents of each file can be downloaded <a title="Apache2 configuration" href="/uploads/apache2.conf.zip" target="_blank">here</a>. For now, I'll go through the key elements in each to ensure we have a safe configuration.
<h2>1. Hide Apaches sensitive information</h2>
<pre>ServerSignature Off
ServerTokens Prod</pre>
<p style="text-align: justify;">By setting <strong><span style="color: #999999;">ServerSignature</span></strong> to 'Off' and<span style="color: #999999;"><strong> ServerTokens</strong></span> to 'Prod', you're essentially telling Apache to not reveal its version number or other essential information to the outside world. True, this is somewhat <em>security through obscurity</em>, but the less information the bad guys know, the less likely they are to attack you.</p>
<p style="text-align: justify;">A common attack pattern is and attacker will take an already known exploit and then search the web for vulnerable servers on Shodan or just automating a process of request information from a bunch of IPs. Once they determined the version of software you're running they can then determine if you're vulnerable <em>(and then they exploit you)</em> or if you're patched<em> (in which case they move on)</em>.</p>
<p style="text-align: justify;">If the attackers are unable to determine the version of software you're running you'll be in much better shape.</p>

<h2 style="text-align: justify;">2. Ensure Apache isn't run as root.</h2>
<pre style="text-align: justify;">User ${APACHE_RUN_USER}
Group ${APACHE_RUN_GROUP}</pre>
<p style="text-align: justify;">Apache needs to be run as a user, and by default the DigitalOcean image runs it as <span style="color: #999999;"><strong>www-data</strong></span>, which is the same user as WordPress. What this means is that if Apache were ever compromised it still won't be able to reconfigure itself because only root is able to change the configuration files (make sure the configuration files have a 0644 permissions and are owned by root).</p>
<p style="text-align: justify;">You always have the option of running Apache under a totally different user, so that even WordPress and Apache are isolated, but I think this is good enough.</p>
<p style="text-align: justify;"><em>*the user information is stored in /etc/apache2/envvars</em></p>

<h2 style="text-align: justify;">3. Restrict access to non-www folders</h2>
<pre style="text-align: justify;">&lt;Directory /&gt;
 Order Deny,Allow
 Deny from all
 Options None
 AllowOverride None
 &lt;Limit PUT DELETE CONNECT OPTIONS PATCH PROPFIND PROPPATCH MKCOL COPY MOVE LOCK UNLOCK&gt;
 deny from all
 &lt;/Limit&gt;
&lt;/Directory&gt;</pre>
<p style="text-align: justify;">And then in the 000-default.conf file:</p>

<pre style="text-align: justify;"> &lt;Directory /var/www/&gt;
 Options Indexes FollowSymLinks MultiViews
 AllowOverride All
 Order allow,deny
 allow from all
 &lt;/Directory&gt;</pre>
<p style="text-align: justify;">These 2 snippets of code ensure that only files in the <span style="color: #999999;"><strong>/var/www/</strong></span> directory is served, and restricts access to all other directories. Of course depending on your implementation '<span style="color: #999999;"><strong>/var/www/</strong></span>' could be any directory you determine to be your wordpress installation.</p>
<p style="text-align: justify;">Limiting access from web users, to only those folders you designate for web access isn't just good practice, it's good security :)</p>

<h2 style="text-align: justify;">4. Re-direct non-SSL traffic to SSL</h2>
<pre style="text-align: justify;">&lt;IfModule mod_rewrite.c&gt;
 RewriteEngine On
 RewriteCond %{HTTPS} off
 RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
 &lt;/IfModule&gt;</pre>
<p style="text-align: justify;">My blog is an SSL/TLS blog and this directive found inside the Virtualhost *:80 re-directs all traffic from port 80 to port 443 and https.</p>
<p style="text-align: justify;">There are other ways to do this, and you could also run this in the .htaccess file for wordpress,but I try to avoid using the .htaccess file for anything other than apache configurations that wordpress plug-ins need to modify.</p>
<p style="text-align: justify;">A general rule of thumb though is to remove the .htaccess file entirely, which makes it much easier, since nothing in the web accessible folders can change apache configurations. Another less secure way is to change the owner of .htaccess to root, and change it back only when changes are needed (which shouldn't be too often).</p>

<h2 style="text-align: justify;">5. Setup SSL 'correctly'</h2>
<pre style="text-align: justify;">SSLEngine <em>on</em> 
SSLProtocol <em>all -SSLv2 -SSLv3</em> 
SSLHonorCipherOrder<em> on </em>
SSLCipherSuite <em>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:AES256-SHA:AES128-SHA:DES-CBC3-SHA:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4</em></pre>
<p style="text-align: justify;">This one is a bit tricky, but there's a lot of debate as to what is the 'correct'  SSL implementation, and the controversy is focused on the Ciphersuite.</p>
<p style="text-align: justify;">You see in order to be secure, it's recommended you turn off all vulnerable protocols and Ciphers. Which makes perfect sense.</p>
<p style="text-align: justify;">Turning of <a title="Maxis Forum needs an upgrade" href="https://www.keithrozario.com/2014/12/maxis-forum-needs-an-upgrade.html" target="_blank">SSL3 is a no-brainer</a>, but there's a debate about the use of RC4 in the CipherSuite as well as the best priority ciphers. The example above is what I took from the <a title="Server Side TLS configuration" href="https://wiki.mozilla.org/Security/Server_Side_TLS" target="_blank">Mozilla Foundation</a> which removes support for RC4, utilizes Perfect Forward Secrecy for all but the oldest browsers, and scored me an 'A' in my SSLLabs test<em> (sweeet!!)</em></p>
<p style="text-align: justify;">But, there's a whole chunk of people out there who are running antiquated browsers on antiquated Operating systems, like Internet Explorer 6 on Windows XP. If you want to reach everyone, you can't be fully secure--and if you want to be fully secure, you'll have to deny entry to some. These trade-offs shouldn't be made lightly and you'll have to evaluate them based on your own personal considerations.</p>

<h2 style="text-align: justify;">6. Setup Basic Auth for wp-admin</h2>
<pre style="text-align: justify;"> &lt;DirectoryMatch ^.*/wp-admin/&gt;
 AuthType Basic
 AuthName "Restricted Area"
 AuthUserFile /etc/apache2/.htpasswd
 Require valid-user
 &lt;/DirectoryMatch&gt;</pre>
<p style="text-align: justify;">The snippet above, found in the apache2.conf file is used to authenticate users access to anything in the /wp-admin section of WordPress. This is an Apache level authentication, and will be authenticated against a list of Apache users found in the .htpasswd file (from the example above). Note this isn't authenticated against <span style="color: #999999;"><strong>root</strong> </span>or <span style="color: #999999;"><strong>www-data</strong></span>, those are OS users. More info <a title="Apache2 basic authorization" href="https://httpd.apache.org/docs/2.2/howto/auth.html" target="_blank">here</a>.</p>
<p style="text-align: justify;">While this isn't 2FA (since both factors are username/passwords), because 2 applications would be authenticating access to the wp-admin section (i.e. WordPress and Apache), it provides some solid security as most WordPress exploits would be limited without access to wp-admin, and that's the most likely attack vector on the WordPress site. In other words, in order for an attacker to gain admin privileges on your WordPress site, they'd need to crack both WordPress <span style="text-decoration: underline;">and</span> Apache.</p>
<p style="text-align: justify;">That being said this is a pain for most users, and the pain may not commensurate with the security it gives, but I use it.</p>

<h2 style="text-align: justify;">7. HTTP Strict Transport Security</h2>
<pre style="text-align: justify;">#Header add Strict-Transport-Security "max-age=3600"</pre>
<p style="text-align: justify;">I commented out this, since I'm still putting changes on my blog. HSTS is a double-edge sword so you <span style="text-decoration: underline;">must</span> be careful.What HSTS will do is tell the users browser that your site will continue using SSL/TLS for the next<strong> x</strong> seconds, where <strong>x</strong> is the <strong><span style="color: #999999;">max-age</span> </strong>parameter of the configuration. <em>(*the highest possible value is 2 years long, and SSLLabs recommends at least 180 days)</em></p>
<p style="text-align: justify;">If the browser ever detects that your site is not using SSL/TLS within this time it will prompt and error and not allow the user to view the site. Resetting the setting on the users end is quite tedious, and possibly beyond the capability of most users. Essentially once you set this value to something like 180 days or more, you'll be forcing yourself to use SSL/TLS damn near forever, and if you ever lost the ability to serve up an SSL/TLS connection you'll be unable to reach your readers any more--period.</p>

<h2 style="text-align: justify;">8. Give me feedback</h2>
<p style="text-align: justify;">If you're an Apache guru, or just a web-master</p>
<p style="text-align: justify;">extro-di-naire, please leave me comments where you think the security could be improved. Otherwise these are the configurations I run on my website, and hopefully they can help you with yours.</p>