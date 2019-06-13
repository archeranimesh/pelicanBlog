Title: 100Days of Code Log File 3rd Attempt
Date: 2019-06-05 22:29:49
Modified: 2019-06-13 22:51:54
Category: #100DaysOfCode, python
Tags: #100DaysOfCode, #100DaysOfX, Python
Slug: 100Days-of-code-log-file_V_3_0
Author: Animesh Bhadra
subtitle: Try Again.
Summary: This is 3rd attempt at completing the #100DaysOfCode. Hope to be consistent longer this time.
keywords: #100DaysOfCode, #100DaysOfX, python, learnpython

[TOC]

![Motivational Quotes]({filename}../../../images/100DaysOfCode/quote_fancy_01.jpg "If we fail, let us try again and again until we succeed, by  Joseph Chamberlain")


Hello World!, You are about the witness the beginning of an epic third coming of the 100-Day coding journey, A story that great sages
will pass down from generation to generation. This quest will feature a potpourri of unfiltered joy, unrivaled pain, and 
unexpected epiphanies.

Some moments, I will be the smartest man alive. Others moments, I will be a stupid idiot. But each day, I will be a valiant warrior, fighting to develop and perfect the skills necessary to evolve into a true beast with these keys.

I have failed in my previous attempt for the challenge, which you can find [here]({filename}../../../articles/100DaysOfX/100DaysOfCode/100Days-of-code-log-file_V_2_0.md "Second attempt for 100Daysofcode").

There are learning from the previous failure, here are the modification which was done to the challenge according to my handicap.

* Selected the resource in advance, 
	- [Learn Python Track from Team TreeHouse](https://teamtreehouse.com/tracks/learn-python)
	- [FrontEndMasters | Python Fundamentals | Nina Zakharenko ](https://frontendmasters.com/courses/python/)
	
* Complete first 21 Days first.

Ladies and gentleman, I present to you, #100DaysofCode with @ [animeshkbhadra ](https://twitter.com/animeshkbhadra "Twitter Handle")

---

## Day 07 | Thursday June 13,2019 ##
### Days Progress ###
* Function scope is little confusing without practice.
	- There is a global scope and a local scope to a function.
	- If same variable name is same, local scope gets preference.
		+ Global variable cannot be modified even thought it share the same name.
* This code will work.
![Function Scope Working case.]({filename}../../../images/100DaysOfCode/functions_scope_01.png "Function Scope Working case.")
* But this code will not work, gives `UnboundLocalError:`.
![Function Scope Not Working case.]({filename}../../../images/100DaysOfCode/functions_scope_error.png "Function Scope Not Working case.")
* The explanation is mentioned in the Python [Documentation](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value).

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](#)

---
## Day 06 | Wednesday June 12,2019 ##
![List as a function argument.]({filename}../../../images/100DaysOfCode/functions_03_01.png "List as a function argument.")
![List as a function argument.]({filename}../../../images/100DaysOfCode/functions_03_02.png "List as a function argument.")

### Days Progress ###
* List or any other mutable data type should not be used as the default arguments.
	- The list is initialized when the function is called the 1st time, and then it modifies the same list. 

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1138870851497934848)


---

## Day 5 | Tuesday June 11,2019 ##
![Functions Arguments]({filename}../../../images/100DaysOfCode/functions_02.png "Function Arguments")

### Days Progress ###
* Started with the *Function's Arguments*.
* Positional arguments must be passed to functions.
* Default arguments are always provide at the end of function's argument list.
* We can give *none*, *one*, *all* arguments to a function with only default arguments list.
* Labeled arguments can be passed in any order to a function. 

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1138501823415951360)

---
## Day 04 | Monday June 10,2019 ##

![Functions]({filename}../../../images/100DaysOfCode/functions_01.png "Different return type of functions.")

### Days Progress ###
* Started the `functions` section of the lecture.
* This lesson, teaches about different function type.
	- Function with no arguments and no return type
	- Function with no arguments and a return type
	- Function with 2 arguments and a return type
	- Function with multi-line function body.
	- return is always optional in function, it returns `<class 'NoneType'>`

### Thoughts ###
* The function returning `<class 'NoneType'>` was a eye opener.
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1138147827287187457)

---

## Day 03 | Sunday June 9,2019 ##

### Days Progress ###

* Completed the Data Type chapter in the FrontEnd Master's Python fundamentals.
* This chapter introduces some nice concept about data types
	- `45j`  is a complex data type `<class 'complex'>` but not `45i`, so `j` is the identifier for complex number.
	- `new_name f"Hello, {name}"` is a format string, `name` in `{}` is the variable name which will be replaced.
	- Same variable can be used to store number, or strings.
	- String can be created by both `'string 1 '` or `" String 2 "`
	- Integer division gives the result in floating point `3/2 = 1.5`

### Thoughts ###
* Python Data types have lot of power inside them with very less ambiguity.
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1137766857312616453)


---

## Day 02 | Saturday June 8,2019 ##

### Days Progress ###

* Understood the VSCode basic settings, got help from a great tutorial by [Corey Schafer](https://www.youtube.com/watch?v=06I63_p-2A4)
* The tutorials talks about these topics
	- Change the way settings is displayed as JSON, in place of UI.
	- Select virtual environment.
	- Change color theme.
	- Change file icons.
	- Set the global python path - `"python.pythonPath": "<Path>"`
	- Set a global python file formatter, we are using Black for this. `"python.formatting.provider": "black",`
		+ Also change the option to run the formatter on saving the file. `"editor.formatOnSave": true,`
	- Enable Linting.
	- Git Integration.
	- Unit Testing.

### Thoughts ###

* VScode has lot of power, lets see how much I learn from it.
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1137427179573092353)

---

## Day 01 |  Friday June 7,2019 ##

### Days Progress ###

* Started the Python Fundamentals course by Nina Zakharenko.
* Today's main focus was setting my these things.
	- Virtual environment.
	- VScode setup.
* Faced few issues, which [stackoverflow ](https://stackoverflow.com/questions/41687841/there-is-no-activate-when-i-am-trying-to-run-my-virtual-env) helped in solving

### Issues and Solutions ###

* There was no activate script when the virtual environment was created by using the command `python -m venv .env`
	- On doing Google for the problem found that running the same command again solves the issue, so ran `python -m venv env` again and viola the activate script appeared.
* VScode was not recognizing the virtual environment created inside a sub folder in the project.
	- Deleted the pre-existing environment and created a new virtual environment at the project root.

### Thoughts ###

* Programming is just efficient Google technique.
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1137047401137549312)


## Reference ##

* [QuoteFancy | Image Source ](https://quotefancy.com/quote/1733403/Joseph-Chamberlain-If-we-fail-let-us-try-again-and-again-until-we-succeed)
* [100DaysOfCode Official Website ](https://www.100daysofcode.com/)
* [Learn Python Track from Team TreeHouse](https://teamtreehouse.com/tracks/learn-python)
* [MIT 6.00SC Introduction to Computer Science and Programming ](https://www.youtube.com/playlist?list=PLB2BE3D6CA77BB8F7)
* [Create a Tweet With image Preview for Free ](https://nealschaffer.com/tweet-link-preview-image-twitter/)
* [FrontEndMasters | Python Fundamentals | Nina Zakharenko ](https://frontendmasters.com/courses/python/)
* [Corey Schafer](https://www.youtube.com/watch?v=06I63_p-2A4)