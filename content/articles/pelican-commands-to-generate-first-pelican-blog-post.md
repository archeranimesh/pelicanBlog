Title: Pelican commands to generate the first blog.
Date: 2017-04-29 22:15:05
Modified: 2017-04-29 23:12:16
Category: Pelican
Tags: pelican
Slug: pelican-commands-to-generate-first-pelican-blog-post
Author: Animesh Bhadra
subtitle: Beyond HelloWorld
Summary: In this post we will check some of pelican commands, and how it helps us to generate a blog post.
keywords: pelican commands, pelican blog post.

We have our boilerplate pelican blog available, now we have still not seen the magic of pelican. In this post we will see our blog coming to life.

## First Pelican Blog ##

We have see the folder structure here

![pelicanFolderStructure]({filename}../images/pelicanQuickStart/pelicanFolderStructure.png "pelican folder structure")  

Now we will first execute some commands and see what happens with this boilerplate. Remember to be in the `pelican1` environment. We can do this by.

````shell
source activate pelican1
````

Once we are in `pelican1` environment, we have all the `pelican` commands at our disposal. Kindly execute this command.

````shell
pelican content
````

The above command we are passing `content` as a parameter, which is nothing but one of the directory of the folder structure.

The output will be
````shell
WARNING: No valid files found in content.
Done: Processed 0 articles, 0 drafts, 0 pages and 0 hidden pages in 0.12 seconds.
````

It clearly warn us about no valid files found in **content**, as we have not added any post to the directory. If you see inside the `output` folder, we will see some content in that namely these files

````shell
archives.html
authors.html
categories.html
index.html
tags.html
theme #directory which contains some predefined images and css.
````

Now let us see what the blog looks like. Just execute these commands.

````shell
cd output/
python -m pelican.server
````

Once you execute the above commands we can see the output on browser on this path [localhost:8000](http://localhost:8000/) and it will look something like this

![Pelican First Post]({filename}../images/pelicanCommands/firstPostPelican.png "The first post from pelican")

Nothing fancy here, but we will some content with some link and a default theme. It is petty good for being a boilerplate.

## The first post. ##

Now we are ready for our first post, we will do the sample hello world which is the de-facto standard in programming languages first program.

We will write the first post in **Markdown**. Create a file named `HelloWorld.md` in this directory `content`.

````md
Title: Hello World
Date: 2017-04-29 11:01
Category: Pelican

Hello World to Pelican

````

Once create and saved this file, just run this command.

````shell
pelican content
````

This will have the following output.

````shell
Done: Processed 1 article, 0 drafts, 0 pages and 0 hidden pages in 0.27 seconds.
````

This time it clearly states that we have `1` article. Then follow the other commands as discussed.

````shell
cd output/
python -m pelican.server
````

Again check the output on the browser at [localhost:8000](http://localhost:8000/). Now this time the output is different and it look like this.

![Pelican Hello World Post]({filename}../images/pelicanCommands/helloWorldPelicanPost.png "The HelloWorld post from pelican")

The area surrounded in ellipse are new. This shows us the power of pelican, we do not have to bother how the content is presented on screen, we have to only concentrate on writing content.

## Reference ##

* [Pelican Doc Quickstart](http://docs.getpelican.com/en/stable/quickstart.html)