Title: Tips to improve work flow in pelican blog.
Date: 2017-05-11 23:05:38
Modified: 2017-05-12 00:10:48
Category: Pelican
Tags: pelican
Slug: tips-for-improving-workflow-in-pelican
Author: Animesh Bhadra
subtitle: Cleaning Up
Summary: We all know a lot of meta-data is required for writing a pelican blog, we can use Sublime Text to improve this meta-data collection, and also see some useful commands to improve the output.
keywords: OUTPUT_RETENTION, FileHeader, Sublime Text

[TOC]

We all know a lot of meta-data is required for writing a pelican blog, we can use Sublime Text to improve this meta-data collection, and also see some useful commands to improve the output.

## FileHeader to Write Meta-Data in Sublime Text ##

[Sublime Text](https://www.sublimetext.com/, " Sublime Text ") is a very nice Text editor for writing Markdown. There are already a lot of articles on how to configure Sublime text for Markdown.

We will discuss about one specific package in Sublime Text called [FileHeader](https://github.com/shiyanhui/FileHeader "FileHeader Package"), this package helps in writing custom File Header, so we can use this package to provide some Meta-Data to the pelican blog by default.

FileHeader comes with predefined header template, if we want to change the content of these templates we can use a custom fileHeader template.

Since we are writing our content in markdown, I have extended the default Markdown template. The modified Markdown Template have to saved in this path `/home/username/.config/sublime-text-2/Packages/User/fileHeaderTemplatesUser` named as `Markdown.tmpl`.

FileHeader uses Jinja2 template, the Markdown template looks like [this](https://gist.github.com/archeranimesh/dcd1773af0ad41e9e1572d293becaa87 "Gist Markdown ").

````
Title: 
Date: {{create_time}}
Modified: {{last_modified_time}}
Category: Pelican
Tags: pelican
Slug: {{file_name_without_extension}}
Author: {{author}}
subtitle: 
Summary: 
keywords:

[TOC]
````

We have to give some configuration for it to work. Kindly add this in the `FileHeader.sublime-settings`.

````json
{
    "custom_template_header_path": "/home/username/.config/sublime-text-2/Packages/User/fileHeaderTemplatesUser",
    "Default": {
        "author": "ABC"
    }
    
}
````

After this every time you create a new Markdown file, the above template will be automatically applied.


## Clean the Output Directory ##

We are working with two git repositories when writing a pelican blog.

* `root `
    - This is the folder which has the `content ` and all the setting file.
* `output `
    - This is the actual HTML page generated by Pelican.

Most often than not we might want to generate the complete blog with a clean build with commands like this.

````shell
pelican content -ds publishconf.py  # While Publishing
pelican content -d                  # Local host.
````

The problem with these above commands is they might delete the `.git ` or even the `CNAME` directory inside `output ` losing the link with version control. We can prevent this by adding this configuration into our `pelicanconf.py`

````python
OUTPUT_RETENTION = [".hg", ".git", "CNAME"]
````

This change will make sure that the above mentioned file are not deleted. Kindly keep in mind this works for only the above 2 version of the command, if you use `make clean ` then this configuration is of no use.


## Reference ##

* [clean should not remove .git metadata #574 ](https://github.com/getpelican/pelican/issues/574 "clean should not remove .git metadata #574")