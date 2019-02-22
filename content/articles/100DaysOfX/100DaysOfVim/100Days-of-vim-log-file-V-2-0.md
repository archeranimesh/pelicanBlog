Title: 100Days of Vim Log File
Date: 2019-02-16 23:28:02
Modified: 2019-02-22 22:40:50
Category: #100DaysOfVim
Tags: #100DaysOfVim, #100DaysOfX
Slug: 100Days-of-vim-log-file-V-2-0
Author: Animesh Bhadra
subtitle: Fling Reloaded
Summary: Vim is really hard to learn, time and again I have failed to use it consistently. I understand the basics of vim and can get some work done with VIM. I am targeting to become efficient at this. Hopefully the 100DaysOfVim will help me to be consistent.
keywords: #100DaysOfVim, #100DaysOfX

[TOC]

![Vim Help Screen ]({filename}../../../images/100DaysOfVim/vimHelp.png "Vim Help Screen")

I am starting this new journey into the world of VIM, with a hope that this time the mistakes of my past attempts will be rectified. This journey's goal is pre-decided so that there is no deviation from the plan of learning VIM. 

In the last attempt of learning VIM, I was doing the classic mistakes of learning vim as described by Mr. Bram Moolenaar in [this](https://www.youtube.com/watch?v=p6K4iIMlouI) video, that is, **Learn every feature the editor offers and use the most efficient command all the time.** 

The approach this time will be learning a little bit of commands in VIM and apply it daily for a few days, as it becomes part of the muscle memory move to the next set. In addition, I have also set my goals for this 100 Days to have a razor sharp focus and not deviating.

The goal of this **100DaysofVim** are:-

* Edit text effectively.
* Scroll and move in a file quickly.
* Navigate source code with ctags and key board shortcuts.
* Edit multiple files using buffers.
* No use of any vim plugins.
* Read and understand the vim help system.
* Integrate debugging with source code navigation in VIM.

---

## Day 05 | Friday 22 February 2019 ##

### Days Progress ###

* Complete the `vimtutor ` exercise.
* Studied the quick reference in vim help.
* Saw 1 screen cast from [VimCast | Episodes ](http://vimcasts.org/episodes/working-with-tabs/)
* Completed the course [Udemy | Vim MasterClass | Jason Cannon ](https://www.udemy.com/vim-commands-cheat-sheet/) 	
	- Received the course completion certificate.
![Vim Master Class Certificate ]({filename}../../../images/100DaysOfVim/vimMasterClass.jpg "Vim Master Class Certificate")


### Thoughts ###

* Learned about the gVIM clipboard buffers `"+` and `"*`
* Tab's command
	- `:tabe` : open a tab with file name
	- `CTRL-W T`: move current split into a tab.
	- `tabc` : close current tab
	- `tabo[nly]`: one 1 tab open.
	- `gT` and `gt`: to switch between tabs.
	- `tabmove`: move tabs
* Completed these help topics
	- ** Visual Mode **
	- ** Text Object **

* [link to tweet](link)	



---
## Day 04 | Thursday 21 February 2019 ##

### Days Progress ###

1. Complete the `vimtutor ` exercise.
2. Studied the quick reference in vim help.
3. Lecture on buffers from [Udemy | Vim MasterClass | Jason Cannon ](https://www.udemy.com/vim-commands-cheat-sheet/)
4. Saw 1 screen cast from [VimCast | Episodes ](http://vimcasts.org/episodes/working-with-windows/)


### Thoughts ###

* Learned about the various windows commands.
	- `CTRL +w s` or :sp `: horizontal split
	- `CTRL +w v` `:vsp`: vertical split
	- `:only`: closes all window except the active one
	- Navigation is done by `CTRL + w w`, `CTRL + w h`, `CTRL + w j`, `CTRL + w k`, `CTRL + w l`
	- Resize windows
		+ `CTRL + w +`, `CTRL + w -`, increase or decrease the size by 1 line
		+ `CTRL + W _`, `CTRL + w |`, increase size of current window in height and width 
	- Moving window is done by `CTRL + w R`, `CTRL + w H`, `CTRL + w J`, `CTRL + w K`, `CTRL + w L`
	- like `bufdo` we have a command `windo` which works only on opened window.
* Studied the **Complex Changes** from vim helps, did not understood much from this.


* [link to tweet](https://twitter.com/animeshkbhadra/status/1098634646991065089)


---

## Day 03 | Wednesday 20 February 2019 ##

### Today's Progress ###

![Vim Help Screen for changing text ]({filename}../../../images/100DaysOfVim/vim_changingText.png "Vim Help Screen for changing text")

1. Complete the `vimtutor ` exercise.
2. Studied the quick reference in vim help.
3. Lecture on buffers from [Udemy | Vim MasterClass | Jason Cannon ](https://www.udemy.com/vim-commands-cheat-sheet/)


### Thoughts ###
* Learned about these buffers commands.
	- `:buffers` or `:ls`
	- `:bn` or `:bnext`
	- `:bp` or `:bprevious`
	- `:bf` or `:bfirst`
	- `:bl` or `:blast`
	- `CTRL + ^` : last open buffers
	- `:set hidden`
	- `:qall!`
	- `:wall!`
	- `:badd`
	- `:bd`
	- `:bufdo`
	- `:Explore`
* Studied the **Changing Text** from Vim help.
	- `cc`, `S`, `C`, `s` all work on line.
	- `CTRL + A` and `CTRL + X` has a very nice implementation.
	- `:ce`, `:le` & `:ri` changes the alignment of line, center, left and right.

* [link to tweet](https://twitter.com/animeshkbhadra/status/1098270900154236928)

---

## Day 2 | Tuesday 19 February 2019 ##

### Today's Progress ###

1. Complete the `vimtutor ` exercise.
2. Studied the quick reference in vim help.
3. Saw 1 screen cast from [VimCast | Episodes ](http://vimcasts.org/episodes/)


### Thoughts ###

* Studied the **Copying and Moving text.** section of vim help.
* `_` behaves the same as `^` without a count preceding it. When count is preceding it, this behaves as `j`.
	- [What does the underscore motion do in vim?](https://unix.stackexchange.com/questions/155926/what-does-the-underscore-motion-do-in-vim)
* While learning about vim help file, I found that all the commands which are similar are generally kept together.
 
* [Link To Tweet](https://twitter.com/animeshkbhadra/status/1097924386038915072)

---

## Day 1 | Monday 18 February 2019 ##

### Today's Progress ###

1. Complete the `vimtutor ` exercise.
2. Studied the quick reference in vim help.


### Thoughts ###
* Few commands which was very good.
	- Using `C` to change the text from the cursor till end of line.
	- Using `D` to delete the text from the cursor till end of line.
* Few Insert Mode commands.
	- `CTRL-T` : insert one shiftwidth of indent in front of line.
	- `CTRL-D` : deletes one shiftwidth of indent in front of line.

* [Link to Tweet](https://twitter.com/animeshkbhadra/status/1097560432850685954)

---

## References ##

1. [How To Learn Vim: A Four Week Plan ](https://medium.com/@peterxjang/how-to-learn-vim-a-four-week-plan-cd8b376a9b85)
2. [100daysOfX](http://100daysofx.com/) 
3. [YouTube | 7 Habits For Effective Text Editing 2.0](https://www.youtube.com/watch?v=p6K4iIMlouI)
4. [VimCast | Episodes ](http://vimcasts.org/episodes/)
