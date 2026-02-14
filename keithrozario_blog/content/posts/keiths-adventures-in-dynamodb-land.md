+++
title = "Keith's Adventures in DynamoDB Land"
date = "2020-06-28T23:22:56"
draft = false
categories = ['Misc']
+++

<!-- wp:paragraph -->
<p>After reading the awesome <a href="https://www.dynamodbbook.com/" target="_blank" rel="noreferrer noopener nofollow">DynamoDBBook</a> from Alex DeBrie, I was prompted to fix a long running design issue with <a href="https://www.keithrozario.com/2019/08/klayers-part-0-introduction.html" title="Klayers Part 0: Introduction">Klayers</a> (a separate project I maintain).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Like everybody else that dives into DynamoDB headfirst, I made the mistake of using multiple tables, one for each data entity. After all, a single database consists of multiple tables -- so DynamoDB would logically involve multiple DynamoDB tables as well right?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">Wrong!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It turns out, a DynamoDB <span style="text-decoration: underline;">table</span> is equivalent to a <span style="text-decoration: underline;">database</span>, and having multiple tables is like having multiple databases, The 'correct' approach, is to load all data into a single DynamoDB table which would allow us to "join" multiple data entities into a single query. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The word "join" is in quotations, as there is no concept of joining data in DynamoDB, all data has to be pre-joined in some way to achieve the performance that DynamoDB promises (sub 10ms response times for tables of any size). If you split your data across multiple tables, you lose the ability to pre-join this data.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>So last month I decided to bite the bullet and began re-designing my application to use one table instead of two, and boy did it do my head-in, and wanted to write this post to capture my thoughts on the whole process.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First here's some background of the application.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>As-Is Architecture</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Klayers is a project that builds and publishes Python Packages as Lambda layers. Each week, it builds the latest version of the package, and then compares the latest build to what was deployed in all regions it currently deploys in. If the versions are different, we publish a new layer to that region, and schedule the previous version for deletion in the next 30 days.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence, we have two data entities, a <span style="text-decoration: underline;">Layer</span> and a <span style="text-decoration: underline;">Build</span>, with <em>1-to-Many</em> relationship between them. One build can be deployed to many layers, but each layer can only be associated with 1 build:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7231,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/data-model.png"><img src="/uploads/data-model-820x174.png" alt="" class="wp-image-7231"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Initially I had a <code>build</code> table and <code>layer</code> table, one for each entity and that was pretty OK, but there were 3 problems with that approach.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Problems</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I had designed the previous implementation to allow me to query for the latest version in every region, but I could only do this on a per region basis. During deployment I had to repeat this query for every region, which meant 20 requests (once per region) per package every time I tried to deploy. This was wasted RCUs and wasted lambda execution time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The next problem was in publishing the full list of arns by region, due to my limited knowledge, once a layer was deleted I had to remove the corresponding item from the DB -- otherwise the deleted layer would be still be in the published list (even though it wasn't available anymore). I would have liked to keep the deleted layers in the database so that I had a record of everything ever built, but be able to query for only the 'active' layers.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The final problem, was wanting to be able to query the <code>requirements.txt</code> data, together with the arn. The way the current setup worked was that build data was in the build table, and layer data in the layer table, which required one query to each table for that information, effectively a join at the application level (rather than DB), again wasted RCUs and wasted lambda execution times.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The re-design I set-out would need to address these 3 problems. So let's look at it once at a time.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Problem 1: Getting all regions in one request </h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Every layer is published as a version, starting from v1 to v2 to v3...etc, and each of these have their own item (record in DynamoDB). But there is also a special v0 item, that holds the latest version of that package. This allows us to query for the latest version without knowing the actual version number (just query for the package name and v0).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's an example of items for a Layer, including the <code>lyrVrsn0#</code> item. This item is updated every time a new version is added so that it reflects the latest version:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7224,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/uploads/Screen-Shot-2020-06-27-at-8.07.37-PM-820x173.png" alt="" class="wp-image-7224"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><em>As a side note, in DynamoDB it's recommended to keep attribute name small, as the name of the attribute takes up space (and hence cost). Some recommend a js-minify approach of naming them single characters like <code>a</code>, <code>b</code>, <code>c</code> , but this can get confusing. To help me save space, yet keep things sane, I took a simple approach of camelCasing the name of the attributes -- and then removing all vowels. </em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our problem is we can't query across regions, as the PK is a composite key that includes the region (e.g. <code>lyr#ap-southeast-1.requests</code>). The solution is to create a Global Secondary Index (GSI). A GSI allows us to index on different attributes other than the table's partition and sort key, it also gives us more flexibility as we can have multiple items with the same partition and sort key (something that isn't possible on the table's PK and SK).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But GSI's have a drawback, they replicate the data, and the more data you replicate the higher the cost. We could replicate the entire table into a new GSI but that would effectively double the tables storage cost, a better solution would be to use <strong>sparse indexes</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A sparse index is a GSI, that only replicates certain items. In our case only layer entities, and specifically only layers that are currently active (not those that are deleted). To achieve this we create a new attribute <code>dplySts</code> (short for Deploy Status), which can have 2 possible values <span style="text-decoration: underline;">latest</span> and <span style="text-decoration: underline;">deprecated</span>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But more interestingly, it can also be <strong>missing</strong> from the item (DynamoDB is <span style="text-decoration: underline;">schema-less</span> after all), any item that doesn't have the <code>dplySts</code> attribute will not populate into our new GSI, and not incur additional cost.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With this new attribute, we can create a GSI, where <code>pckg</code>(package) is the partition key and <code>dplySts</code> is the sort key. Because build entities don't have a <code>dplySts</code> they won't populate the GSI, similarly expired layers will have their <code>dplySts</code> fields deleted, keeping them out of the index as well. This keep the index 'sparse'. Look at the example below, and note that even our special <code>lyrVrsn0#</code> item is not in the index -- because it doesn't have a <code>dplySts</code> attribute.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7226,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/Screen-Shot-2020-06-27-at-9.41.52-PM.png"><img src="/uploads/Screen-Shot-2020-06-27-at-9.41.52-PM-820x237.png" alt="" class="wp-image-7226"/></a></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Now it's a simple matter of querying the GSI, with the <code>pckg</code> and <code>dplySts=latest</code>, and we'll get the latest package for all regions in a single query. This more efficient query is a double-win, saving both RCUs on DynamoDB, and execution time on Lambda.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7245,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/uploads/before-after-2-820x427.png" alt="" class="wp-image-7245"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Problem 2: Publishing full list of arns</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This wasn't a problem previously as we deleted expired layers from the table. But in our new setup, I wanted to keep a historical record of every layer ever published, yet be able to publish a full list of layers per region -- and do so in a single query.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The solution is rather simple, thanks to the <code>dplySts</code> field we introduced in the previous section. We create a new sparse index, this time with 'region' as the partition key instead of 'package' . Now we have a sparse GSI, which we can simply query on for all active packages in one region, by querying for the region partition key, and not specifying a sort key.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This might incur more than 1 RCU, depending on the size of data coming back, but its still very efficient.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7229,"sizeSlug":"large","linkDestination":"media"} -->
<figure class="wp-block-image size-large"><a href="/uploads/Screen-Shot-2020-06-27-at-10.00.42-PM.png"><img src="/uploads/Screen-Shot-2020-06-27-at-10.00.42-PM-820x239.png" alt="" class="wp-image-7229"/></a></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Problem 3: Get full list of dependencies for a package</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In python, we keep a list of all our dependencies in a <code>requirements.txt</code> file. This is the equivalent of the <code>pom.xml</code> or <code>package.json</code> file. The data is an output of the build, which we do only once -- then we might deploy that package to multiple regions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is a classic <span style="text-decoration: underline;">1-to-many</span> relationship, but it's special because the build and the corresponding <code>requirements.txt</code> is <strong>immutable</strong> -- it never changes. Also, unlike Javascript, Python packages rarely have a nightmarish number of dependencies, so the data in <code>requirements.txt</code> rarely exceeds a few KiloBytes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Given those requirements we'll simply denormalize that data into the layer item. Easy-peasy!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But...you're feeling a bit uncomfortable at this point, because this feels wrong! Denormalizing in a database is a bad thing -- they thought you this in school. Moses brought down this commandment from the mountain, when God told him that "Thou shall normalize your database to the 3rd-normal form".</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But in DynamoDB, we break this convention, because 3rd-normal form optimizes for storage space, while DynamoDB is optimize throughput. By normalizing our data, we eliminate a join on the read, and hence get faster performance. This is how DynamoDB can guarantee sub 10ms read speed for an item regardless of the database size.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's how the data looks from my console:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7230,"sizeSlug":"large","linkDestination":"media"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><a href="/uploads/Screen-Shot-2020-06-27-at-10.20.09-PM.png"><img src="/uploads/Screen-Shot-2020-06-27-at-10.20.09-PM-637x500.png" alt="" class="wp-image-7230"/></a></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>This might seem like a bit of a 'cheat' -- but because this data is replicated, I save 1 query per request, which can mean a lot of money depending on the request volume. Also, I can publish all dependencies for all layers (which I do by the way), simply by querying the table for <code>bldVrsn0#</code>, and then parsing the response.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Last comments</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Before we wrap-up, I used the <a href="https://aws.amazon.com/about-aws/whats-new/2020/03/nosql-workbench-for-amazon-dynamodb-is-now-generally-available/" target="_blank" rel="noreferrer noopener">NoSQL workbench</a> to model my data, and it was awesome -- but still an unfinished product. For example I didn't have the ability to write notes or remarks on anything, which left me having to document separately somewhere in my repo. But it still beats modelling this on Excel though. I also exported out the model, and keep the corresponding json file under the documentation directory of the repo as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To actually delete a layer, I used the wonderful <code>ttl</code> field of DynamoDB. The field allows us to schedule deletion of an item at a specific time, hence whenever a new version is deploy, we update the <code>ttl</code> field on the previous version to 30days from today.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then in 30 days, theitem is deleted from the table -- and flows into the DynamoDB stream that finally hits a lambda function that eventually deletes it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But.....</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I was afraid the function would grow too large, because of a single-table design could be updating, deleting and inserting multiple types of items into a DB. With just one Lambda function processing all those possible scenarios we might end up with a pretty complex function and the possibility of an infinite loop.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":7232,"sizeSlug":"large","linkDestination":"media"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><a href="/uploads/dynamoDB-stream.png"><img src="/uploads/dynamoDB-stream.png" alt="" class="wp-image-7232"/></a></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>So I split out the function, by placing all events onto an EventBridge (in a particular pattern) and then use EventBridge Rules to trigger specific functions based off what happened (insert, delete, update) and what item type (build, layer). Since we only needed to have delete layer events, only those events have rules in EventBridge that route them to a special Delete Layer function, every other event flows off into the ether. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In the future if I wanted to process update build events, I could easily add a new function and rule to EventBridge with little effort. The Serverless Framework supports these EventBridge events natively, via a intuitive and familiar interface, e.g:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7249,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="/uploads/delete_layer-654x500.png" alt="" class="wp-image-7249"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Although this example is by no means a 'hard' problem, it did help me learn one important lesson. DynamoDB is a complete paradigm change from anything in the RDBMS world. In this world we're not modelling to a 3rd-normal form, that handle any query we throw at it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Instead we're having to think long and hard (very hard!) about how the data would be accessed, and model for access patterns -- which might violate every tenet of data modelling we hold dear.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But what we get in return, is an optimized read/write of our data from the database -- and a performance guarantee that no other DB can touch. In the 3rd-normal form we could handle any query, but that also meant that we were limited in our optimization. In this world we optimize for performance over the flexibility -- which allows our DB to scale for anything our application can throw at it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's by no means a simple task, and I wouldn't begrudge anyone who thinks this is a mountain too high for their first serverless rodeo. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But if you've already wrestled with enough distributed computing problems, you know that the Database is usually the single choke-point of your application, and 'real' solution to that problem isn't throwing more compute at the DB -- instead it's optimizing your data model for your access patterns via something as mind-boggling as violating 3rd-normal form!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I've been building serverless stuff for nearly 3 years now -- and DynamoDB single table design is hardest thing I've ever had to learn in this space, I'm not an expert (yet!), but I'm sure glad I started this adventure.</p>
<!-- /wp:paragraph -->