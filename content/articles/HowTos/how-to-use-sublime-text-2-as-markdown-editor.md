Title: How to use Sublime Text 2 as a MarkDown Editor.
Date: 2020-01-02 22:33:26
Modified: 2020-01-02 23:18:09
Category: SublimeText
Tags: SublimeText, Markdown, Sublime text 2
Slug: how-to-use-sublime-text-2-as-markdown-editor
Author: Animesh Bhadra
subtitle: The no hassle Markdown editor.
Summary: Sublime Text 2 is a great editor for text or code editing, as it is available on multiple platform. Using only 2 plugin-s we can covert Sublime Text into a great Markdown Editor.
keywords: #100DaysOfCode, #100DaysOfX, SublimeText 2, Sublime Text 2, MarkDown, Mark down.

[TOC]

## Sublime Text ##

Sublime Text is a great editor for code and text. There is nothing I can add to the above fact. Markdown is a great format to write the ReadMe's in GitHub, and a lot of other social media also allows MarkDown Format. 

Sublime Text 2 have basic code snippets triggered for MarkDown Editing. This itself is a huge plus for using Sublime Text for MarkDown Editing though the support is limited to these 6 Snippets, as a user we can always enhance these.

![Sublime Text MarkDown Snippets]({filename}../../images/HowTos/SublimeTextSnippet.png "Sublime Text MarkDown Snippets")

The basic assumption I am making that you have the [Package Control Plug-in](https://packagecontrol.io/installation#st2https://packagecontrol.io/installation#st2) installed.

Sublime Text 2 with the help of these 2 Plug-in makes Markdown Editing work like a charm.
* [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing)
* [InsertDate](https://github.com/FichteFoll/InsertDate/)

## Plug-ins ##

### MarkDown Editing ###
The basic support from Sublime Text 2 is enough to use it as a MarkDown Editor but the [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing) provides great support in terms of.

* Paring of Asterisks, underscores, brackets
* Creation of Numbered list and Un-numbered list, with tab support of Indents.
* Great key bindings.
* Good theme with decent syntax highlighting, though I will propose read the blog in the Reference section.

These basic settings in helps a lot in MarkDown editing. Save it in `Markdown (Standard).sublime-settings` file.

```
{
    # Sets the Color Theme.
    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme",
    # Sometime md is not recognized as a MarkDown Extensions.
    "extensions":
    [
        "md"
    ],
    # Enable Spell Check.
    "spell_check": true,
    # If you want the text to start in the left hand corner, default is Centered.
    "draw_centered": false,
    "wrap_width": 180
}
```

Kindly visit the documentation in the GitHub page for more configuration and settings.


### Insert Date ###
When writing a blog post using MarkDown we need to enter Date in the present Blog. This plug-in [InsertDate](https://github.com/FichteFoll/InsertDate/) is a great way to insert localized time into any documents based of few KeyStrokes. 

This plug-in is vastly configurable, so we can customize completely to our needs.

Change this configuration in the file `insert_date.sublime-settings`

```
{
    # Mention your local Time zone
    "tz_in": "Asia/Kolkata",    
    # Sunday July 28,2019 Prints in this format
    "format": "%A %B%e,%Y"
}

```

* [strftime reference and sandbox ](http://www.strfti.me/), use this to format the date according to your need.

The default Key combination to trigger this is `[Ctrl + f5] [Ctrl + f5]`. This works on all platform except Mac, as it triggers the VoiceOver App. Kindly see [this](https://github.com/FichteFoll/InsertDate/issues/28) issue for resolution.


## Conclusion ##
In Conclusion, I will only try to mention that both,
* [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing)
* [InsertDate](https://github.com/FichteFoll/InsertDate/)

are great Plug-ins to write MarkDown files, Lets use these to make a better ReadMe in Github. 


## Reference ##

* [How to Set Up Sublime Text for a Vastly Better Markdown Writing Experience ](https://mariusschulz.com/blog/how-to-set-up-sublime-text-for-a-vastly-better-markdown-writing-experience)
* [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing)
* [InsertDate](https://github.com/FichteFoll/InsertDate/)
* [Default keybindings don't work on OS X Yosemite #28](https://github.com/FichteFoll/InsertDate/issues/28)
