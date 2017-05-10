Title: Integrating 3rd party services with Pelican Blog.
Date: 2017-05-10 22:47:22
Modified: 2017-05-10 23:48:03
Category: Pelican
Tags: pelican
Slug: integrating-3rd-party-services-with-pelican
Author: Animesh Bhadra
subtitle: Mix and Match.
Summary: Pelican with its themes and plugins provides lots of functionality, but it also integrates well with 3rd party services like, MailChimp, DISQUS, Google analytics, Google Adsense, RSS feeds etc.
keywords: MailChimp, DISQUS, Google analytics, Google Adsense, RSS feeds 

[TOC]

We have already discussed two types of settings file in [pelican]({filename}pelican-settings-files.md "Pelican Settings File."), and we found that `publishconf.py` is the file which is picked along with `pelicanconf.py` when we are generating the blog for publishing.

These 3rd party service integration happen over this `publishconf.py` file, because we do not want these services to be activated when running on [localhost ](http://localhost:8000/).

## Google Analytics. ##

Google Analytics provide us with very valuable insights into how a user interacts with the website, like the links which users click the most etc. This is a free service which really helps when we are starting out.

When we create an account with [Google Analytics ](https://analytics.google.com/), we receive a tracking code which we need to provide to Pelican blog. This tracking code is generally of the form `UA-********-*`, which you can find in this menu flow `Administration ---> Property Settings ---> Tracking Id`, copy this tracking id and provide it to `publishconf.py` with this settings

````python
GOOGLE_ANALYTICS = "UA-********-*"
````

This is it, we will get all the analytics data from our website on Google Analytics.

## DISQUS ##

[DISQUS](https://disqus.com/ "Disqus") is a commenting system which is used extensively in the pelican blog world as we have to engage with our visitors for providing feedback and anything which is deemed important to the visitors.

Integrating Disqus with any blog requires a *ShortName*, which is a unique identifier for our site, which can be found in this path `https://<username>.disqus.com/admin/settings/general/`.

We need to add this setting into the `publishconf.py`.

````python
DISQUS_SITENAME = "shortName"
````
The [Elegant Theme](http://oncrashreboot.com/elegant-best-pelican-theme-features#collapsible-comments) provides a nice feature called *Collapsible Comments* in which we will not show all the comments when the page loads. This comments will only be shown when a user presses the `comment ` link.

We can use a `COMMENTS_INTRO` settings to draw the user for engaging with the site.

## MailChimp ##

[MailChimp](https://mailchimp.com/ "MailChimp ") is a way to provide newsletters to your active subscribers, in this way they can be informed for any new post also immediately. Mailchimp can also be used as an email marketing platform. This is also free for basic subscription.

We will need a `MAILCHIMP_FORM_ACTION`, URL which we can get by creating one list in MailChimp.

To create a mailing newsletter we can use these links

* [MailChimp Create a New List ](http://kb.mailchimp.com/lists/growth/create-a-new-list "MailChimp Create a New List")
* [Add a Signup Form to Your Website ](http://kb.mailchimp.com/lists/signup-forms/add-a-signup-form-to-your-website)

## Reference ##

* [What's a shortname?](https://help.disqus.com/customer/portal/articles/466208 "What's a Shortname? ")
* [Host Your Own Signup Forms](http://kb.mailchimp.com/lists/signup-forms/host-your-own-signup-forms)
