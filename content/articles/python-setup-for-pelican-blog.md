Title: How to setup Anaconda Python environment for Pelican Blog.
Date: 2017-04-26 22:39:03
Modified: 2017-04-26 23:50:52
Category: Pelican
Tags: pelican
Slug: python-setup-for-pelican-blog
Author: Animesh Bhadra
subtitle: Using Conda.
Summary: Anaconda is a well know distribution of Python, supporting both python 2 and 3. We can setup a exclusive environment for Pelican blog using conda.
keywords: Conda, Anaconda, Python, Pelican, Envs.

[TOC]

## Installing Pelican ##

Pelican is a python package, so we can have multiple option to install pelican. There can be 3 option which I can think of.

* Direct Installation
    - If we have only one python installation on the system, and we do not have any issue if we screw up this installation just use `pip` to install pelican.
* Installation using VirtualEnv.
    - This approach is already mentioned in official documentation of [pelican](http://docs.getpelican.com/en/stable/install.html "Installing Pelican")
* Installation using Conda.
    - By now you could have understood that we will use Conda to install pelican. This is because Anaconda is already a pre-packaged installation of very well know python package in both version 2 and 3. In future I will will update this page if I wrote about Anaconda installation, for now refer any documents on the google search for installation.

### Configure Anaconda for Pelican Blog ###

The first thing we have to do is to create a environment using the python version 2. This can be done by this command.

````
conda create -n pelican1 python=2
````

Once we have executed the above command we will have `pelican1` as an environment.

We can see the list of environment in the system by using.

````
conda info --envs
````

Which will provide an output like this.

````
pelican1                 /home/username/anaconda3/envs/pelican1
py27                     /home/username/anaconda3/envs/py27
py35                     /home/username/anaconda3/envs/py35
root                  *  /home/username/anaconda3
````

This shows all the available environment.

We can activate the `pelican1` by using this command.

````
source activate pelican1
````

Now we have an environment which we can used for pelican development. The reason for this environment creation is to have a separate environment for experimentation with pelican, if anything goes wrong we do not disturb already existing programs.

### Configure Pelican Environment for Blog ###

Once we have the environment we have install few packages in this environment. The first is to install PiP to install other package. Install Pip by using.

````
conda install pip
````

With the completion of installing `pip`, the first and foremost package to install is pelican, with this command.

````
pip install pelican
````

Since we will be using Markdown to write our blogs we need the markdown package, which we can install using.

````
pip install Markdown
````

There are some plugin and themes in pelican which might need some additional packages, we will install these 2.

````
pip install Fabric
pip install beautifulsoup4
````

### Freeze the Requirement ###
When we have all our installation complete, we should save our package history into a `requirement.txt`. We can use this `requirement.txt` to install all the above mentioned packages with same version in one go.

We can freeze the details by using.

````
pip freeze > requirements.txt
````

## Dependencies ##

If we check the `requirement.txt` generated in the above step, we will see a lot of packages already installed apart from `pelican`, `markdown`, `Fabric` and `beautifulsoup4`. These extra packages are dependencies for running pelican.

* **feedgenerator:** to generate the Atom feeds
* **jinja2:** for templating support
* **pygments:** for syntax highlighting
* **docutils:** for supporting reStructuredText as an input format
* **pytz:** for timezone definitions
* **blinker:** an object-to-object and broadcast signaling system
* **unidecode:** for ASCII transliterations of Unicode text
* **six:** for Python 2 and 3 compatibility utilities
* **MarkupSafe:** for a markup safe string implementation
* **python-dateutil:** to read the date metadata


We have completed 2 important steps of our own blog publishing.

## Reference ##

* [Installing Pelican ](http://docs.getpelican.com/en/stable/install.html)
* [Managing Python ](https://conda.io/docs/py2or3.html)
