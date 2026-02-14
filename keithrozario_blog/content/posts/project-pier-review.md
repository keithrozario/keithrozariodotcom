+++
title = "Project Pier Review"
slug = "project-pier-review"
date = "2011-06-04T08:59:29"
draft = false
tags = ['PHP', 'Project Management']
categories = ['Blog']
+++



![Project_pier](/uploads/project_pier-150x38.jpg "project_pier")

Project Pier is a web-based Project Management tool written in PHP. It's got a whole lot of bells and whistles for a open-source platform, but it does have it shortcomings as well. It all depends on what you want to accomplish with your project management tool, ProjectPier could be perfect, or it could fall woefully short. So let's get digging:<!--more-->
<h2><span style="color: #993366;">Installing Project Pier.</span></h2>
Installing Project Pier is simple and straightforward. On a high level it's a 5 step process.
<ol>
	<li>Create a sub-domain (http://projectpier.example.com)</li>
	<li>Download the Latest Project Pier release from the website</li>
	<li>Copy the folder onto your web host</li>
	<li>Setup a MySQL database</li>
	<li>Browse to the install.php of project pier, and you're good to go.</li>
</ol>
In terms of ease of installing, I give Project Pier 5 stars.
<h2><span style="color: #993366;">User Interface.</span></h2>
Here's where it falls short. The interface while nice-looking wasn't intuitive. I didn't know if I was looking at milestones or task or task list. It doesn't show me if I'm looking at the project view or my individual view.

I also can't collapse tasklist to just single line items. So when I view the tasklist, it's display the whole task, just look at the screen below:

[caption id="attachment_837" align="aligncenter" width="300" caption="ProjectPier - Project View"]

![ProjectPier - Project View](/uploads/Project_pier_project_view-300x179.jpg "Project_pier_project_view")

[/caption]

And compare that to this:

[caption id="attachment_838" align="aligncenter" width="300" caption="ProjectPier - User View"]

![Project_pier_user_view](/uploads/Project_pier_user_view-300x172.jpg "Project_pier_user_view")

[/caption]

The similarity is striking, but my problem with it was that it was too similar, it wasn't intuitive when I was looking at it from the user view (what task are relevant to me across all my projects?) and when I was looking at it from a project view (what task are relevant across all people on this particular project).

While the idea is nice, and open source definitely helps out. I really didn't like how the interface panned out. One caveat though...<span style="color: #800080;"><strong><span style="color: #ff6600;">I didn't read the user manual, or any other documentation</span>.</strong></span> <span style="color: #000000;">It could be around somewhere, but this user interface, without any documentation was hard to get used to.</span>
<h2><span style="color: #000000;"><span style="color: #800080;">Features</span></span></h2>
<span style="color: #000000;"><span style="color: #800080;"><span style="color: #000000;">Now Project pier does have some nifty features, </span></span></span>
<blockquote>
<ul>
	<li>Multi-client capability lets you manage projects of different clients simultanously</li>
	<li>Complete flexibility regarding allocation of users to projects</li>
	<li>3-Level rights management:
<ol>
	<li>Administrator</li>
	<li>User of owner company</li>
	<li>User of client company</li>
</ol>
</li>
	<li>Possibility to limit rights of client users per project
<ol>
	<li>Manage messages</li>
	<li>Manage tasks</li>
	<li>Manage milestones</li>
	<li>Manage tickets</li>
	<li>Manage pages (wiki)</li>
	<li>Manage time</li>
	<li>Upload files</li>
	<li>Manage files</li>
	<li>Assign tasks to members of owner company</li>
	<li>Assign tasks to members of other clients</li>
	<li>Change milestone status</li>
	<li>Create project (as a non-administrator)</li>
</ol>
</li>
	<li>Messages and task lists can be linked to milestones</li>
	<li>Projects can be part of a hierarchy of projects</li>
	<li>Versioning can be used to manage revisions of uploaded files.</li>
	<li>Tags can be used to categorize messages, tasks, milestones, and files</li>
	<li>Fulltext search per project covering messages, tasks, milestones, and files</li>
	<li>Privacy: Messages, tasks, milestones, files, and comments can be flagged as 'private', hiding sensitive information from clients</li>
	<li>Simple form generator (forms can be used to create tasks or comments)</li>
</ul>
</blockquote>
The problem though was that it lacked certain key features, I wanted:

<strong>Sharing without registering</strong>- Allowing me to share a view-only project plan to stakeholders without them having to register as users.

<strong>Gantt charts</strong> - I really couldn't believe there was no Gantt features. That means task are only assigned end-dates by default, and no start dates. This also means no ability to design dependencies, meaning if one task gets delayed, you'll need to manually align all the other task dependant on it with 'new' start dates.

<strong>No time-writing function</strong> - While you can keep track of task on this thing, there is no specific time-writing function for cost accounting, etc etc.
<h2><span style="color: #993366;"><strong>Overall</strong></span></h2>
Overall, projectpier is a simple to install application, but the simplicity sort of ends there. It's not as user-friendly as other project management suites and not feature rich enough. That being said, it's good to manage a collboration team working across multiple projects, but not good if you want to really manage task-level activity. It's lack of gantt charts and sharing without registering, means it will have limited functionality in organizations with mature project management practices that demand more from their project managers.

I have a soft-spot for open source software and this one really does look nice, but I just can't recommend it to anyone, especially when there are other equally free and equally open-source software that are have more features and just as easy to install.

You can download Project pier <a title="Project Pier" href="http://www.projectpier.org/" target="_blank">here.</a>

View what others are saying about Project Pier <a title="Project Pier Review" href="http://osliving.com/business-applications/project-management/project-pier/" target="_blank">here</a> &amp; <a title="Project Pier" href="http://www.tarekshalaby.com/2010/03/manage-your-freelance-projects-with-projectpier/" target="_blank">here</a>.