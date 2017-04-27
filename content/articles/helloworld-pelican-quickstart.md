Title: Pelican HelloWorld using pelican-quickstart
Date: 2017-04-27 23:26:43
Modified: 2017-04-28 01:12:50
Category: Pelican
Tags: pelican
Slug: helloworld-pelican-quickstart
Author: Animesh Bhadra
subtitle: base configuration
Summary: We all want to hit the ground rolling, and what better way then to start with a Pelican HelloWorld. pelican-quickstart is a great command to start a basic pelican blogs with most of the defaults working out of the box.
keywords: pelican, helloworld, pelican-quickstart

Pelican makes it very easy to make the ground rolling ASAP. Pelican provides a great command `pelican-quickstart`, which asks a few questions to you and makes a boilerplate blog ready in a few seconds. We will go through the entire process explaining each option is details.

## Activate Python environment ##

We had setup a separate python anaconda environment in our previous [post]({filename}python-setup-for-pelican-blog.md) now is the time to active the environment, we can do that by using a simple command.

````shell
source activate pelican1
````

It will activate the `pelican1` environment, and we can identify it by check the terminal prompt which will change to `(pelican1)`.

Once the work is done we can deactivate the same with a simple command.

````shell
source deactivate pelican1
````

All the above command will work for linux and Mac, kindly check the windows equivalent of the same.

## pelican-quickstart ##

Now we are ready to divulge in the world of pelican. Pelican has a ready to bake command to setup the basic boilerplate for the blog. The command is called

Before executing the below commands just create a directory where you want your blog files to be stored.

````shell
mkdir ~/myBlogDirectory
cd ~/myBlogDirectory
pelican-quickstart
````

Just execute this commands and it asks you these series of questions, which we will talk in details.

### pelican-quickstart options ###

The options shown after executing the `pelican-quickstart` are as below.

![pelican quickstart options]({filename}../images/pelicanQuickStart/pelicanQuickStartoptions.png "pelican quickstart options")

We will discuss each and every options and there usage, we can always choose the default shown in capital letter, `{Y|n}`.

* Where do you want to create your new Web site ? [.]
    - Most probably we will keep the default as we are already in that directory, if not you can specify the path `/home/pathtomyblog`
* What will be the title of the blog?
    - Provide a suitable title to your blog, do not worry even if you want to change it latter we can change it. 
* Who will be the author of this Web site ?
    - Just provide any name you want whose name should be present as a author on the blog post, it can be your name also.
* What will be the default language  of this Web site ? [en]
    - The default choice is `english`, else you can give any language format mentioned in ISO 639-1 Language Codes, the list can be found [ISO Language codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO Language codes")
* Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
    - If you already have purchased a domain give the domain name as shown in the example, else continue with `n`, we can later fill the domain name.
* Do you want to enable article pagination? (Y/n)
    - We can go with the default of having pagination, which means how many post of a the blogs will be displayed in one page, the choice of this is in the next question.
        + How many articles per page do you want? [10] 
            * The default choice is `10`, for the time being keep it that way.
* What is your time zone? [Europe/Paris]
    - To change the time zone, we should be aware that these are **tz database** time zone, to exactly get the time zone codes for your country visit [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "List of tz database time zones"), give the code without the `[]`.
* Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
    - There are multiple ways to automate the blog publishing process, makefile and fabic comes to our help, just chose the default and we will decide on this later. This creates two files in the directory, `fabfile.py` and `Makefile`
* Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
    - We have the help of auto-reload commands to automatically generates the preview as soon as we change anything in the themes, we might not require it initially, so keep it false.
* Do you want to upload your website using FTP? (y/N)
    - If we had an FTP site where we could upload, just choose the default and say `n`
* Do you want to upload your website using SSH? (y/N)
    - If your hosting uses SSH, for our use case we will choose `N`, which is the default.
* Do you want to upload your website using Dropbox? (y/N)
    - We can also use dropbox to upload out static files, but for this, we will try some other time, for now choose the default which is `N`.
* Do you want to upload your website using S3? (y/N)
    - We also have the facility of choosing amazon S3 for our site hosting, for now not needed chose `N`
* Do you want to upload your website using Rackspace Cloud Files? (y/N) 
    - Again the default `N`, we are not using Rackspace.
* Do you want to upload your website using GitHub Pages? (y/N)
    - We can choose `y` here, but we will try another mechanism, for now choose the default `N`
    - If you had chosen `y` in this option you will get this sub option.
        + Is this your personal page (username.github.io)? (y/N)
            * Choose `y`, 
        + After this we will get this message in either case.

````shell
Done. Your new project is available at /home/username/myWork/mySampleBlog
````

Our blogs boilerplate is available. Here is the folder structure.

![pelicanFolderStructure]({filename}../images/pelicanFolderStructure.png "pelican folder structure")  

## References ##

* [How I setup Pelican ](http://terriyu.info/blog/posts/2013/07/pelican-setup/ "How did the command option help")
* [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "List of tz database time zones")
* [List of ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "List of ISO 639-1 codes")
