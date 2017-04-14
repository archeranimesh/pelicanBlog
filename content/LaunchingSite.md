Title: Configuring Github pages with Custom Domain
Date: 2017-04-14 21:30
Modified: 2017-04-14 21:30
Category: Pelican
Tags: pelican, publishing
Slug: configure-github-custom-domain
Authors: Animesh Bhadra
Summary: How to configure a Pelican blog using Github Pages and a Custom domain.

I have mentioned some of the links in references, have visited all of the below and few more, but the configuration is much simpler.

The process can be broken into 2 broad steps.
1. Configure your Github repo
2. Configure the DNS at [GoDaddy](https://in.godaddy.com/)

## Configure your Github repo ##

The prequsite is that we have a github pages of like this [archeranimesh.github.io](http://archeranimesh.github.io), if not kindly visit this [link](https://pages.github.com/) for generating one.

The first thing we would like to do is to configure a CNAME in the above repo.

There are two ways to do this.

1. Local Repo
2. Directly on Github.

### Local Repo ###

1. Create a local file in the repo with the name CNAME.
2. Just have one line in the file. `example.com`, where `example.com` is your domain you have bought from [GoDaddy](https://in.godaddy.com/).
3. Push the changes to [Github](https://github.com/)

### Directly on GitHub ###

On the repository in [Github](https://github.com/), you will see something like this.

![GitHub Settings](images/launchSite/Settings.png "GitHub Setting")

In the above Click on the `Settings`, Scroll down you will see something like this.

![GitHub Pages Settings](images/launchSite/gitHubPages.png "GitHub Pages Setting")

Enter the domain you have purchased from [GoDaddy](https://in.godaddy.com/).

These are the only changes required to be done in GitHub.

## Configure the DNS at [GoDaddy](https://in.godaddy.com/) ##

The most easiest of the all the below references is [Configuring a Godaddy domain name with github pages](http://andrewsturges.com/blog/jekyll/tutorial/2014/11/06/github-and-godaddy.html).

The real issue is all of the links shows the old UI of [GoDaddy](https://in.godaddy.com/), so some things get confusing.

1. Go to the account setting page, which mostly will like in this [link](https://mya.godaddy.com/?pc=urlargs).
2. The link will look like this.
3. ![Godaddy Accounts Settings](images/launchSite/accountSettingsGodaddy.png "Godaddy Accounts Settings")
4. Click on the `+` Symbols in Front of Domain, and Click on the `Manage DNS ` Link
5. ![Godaddy DNS Management](images/launchSite/manageDNS.png "Godaddy DNS Management")
6. The link will show a lot of `Records`, go to the end of the `Records`, and click on the link **ADD**
7. ![Godaddy Add Options](images/launchSite/AddOption.png "Godaddy Add Options")
8. From the above option we have to add 3 entries.
9. These is how all the 3 would look like after adding.

![Godaddy A Options](images/launchSite/AOptions.png "Godaddy A Options")
![Godaddy www Options](images/launchSite/wwwOption.png "Godaddy www Options")

Now you can launch and check your desired domain. Kindly wait 48 hrs for these changes to reflect, do not try to configure multiple times, if it does not work even after 48 hours kindly search for help, till then take a coffee break and have a nice time out of this screen.

## The domain XYX is no longer parked by godaddy ##

When we are doing the above process, even after 24 hours, when you launch your website, we find one of these error.

1. The domain XYX is no longer parked by godaddy
2. It is detected as a Malware in the office network.

The website might launch for some times and sometimes you might get any one of the above 2 errors. kindly check this in the **Manage DNS** page.

* We had added two **A** Names pointing to the GitHub URL as shown below.
![Godaddy A Options](images/launchSite/AOptions.png "Godaddy A Options")

Check if you have any other **A** Names in addition to the above two, if you have, kindly delete that. The detailed issue can be read [GoDaddy domain (randomly) not resolving to GitHub Pages](https://serverfault.com/questions/743327/godaddy-domain-randomly-not-resolving-to-github-pages)

## References ##

1. [Setting Up a GoDaddy Domain Name With GitHub](http://www.mycowsworld.com/blog/2015/07/12/setting-up-a-godaddy-domain-name-with-github/)
2. [Configuring a Godaddy domain name with github pages](http://andrewsturges.com/blog/jekyll/tutorial/2014/11/06/github-and-godaddy.html)
3. [Using a custom domain with GitHub Pages](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)
4. [Using GitHub Pages To Host Your Website](http://blog.teamtreehouse.com/using-github-pages-to-host-your-website)
5. [GoDaddy domain (randomly) not resolving to GitHub Pages](https://serverfault.com/questions/743327/godaddy-domain-randomly-not-resolving-to-github-pages)
6. [[Help]: How to correctly connect my github pages blog to a custom domain?](https://www.reddit.com/r/webdev/comments/653q6z/help_how_to_correctly_connect_my_github_pages/)
7. [Redirecting GitHub Page to a custom domain](https://ongspxm.github.io/blog/2016/08/github-custom-domain-godaddy/)
    1. Kindly read the above site, to understand what is the use of CNAME and A Record. Great introduction. 

