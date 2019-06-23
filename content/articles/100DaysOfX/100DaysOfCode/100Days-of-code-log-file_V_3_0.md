Title: 100Days of Code Log File 3rd Attempt
Date: 2019-06-05 22:29:49
Modified: 2019-06-23 22:15:26
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

## Day 15 | Sunday June 23,2019 ##
### Days Progress ###
* Started learning about dictionaries.
* Dictionaries store `key:value` pair.
* Dictionaries are mutable but the `keys` are immutable.
* The search is very fast, just like `sets`.
* Retrieve the value with index as the `key`  `a["one"]`
* `get()` method can be used when we do not want an error while retrieving a value.
	- Its returns a default value if the key is not present.


![Dictionaries Basics ]({filename}../../../images/100DaysOfCode/dict_01.png "Dictionaries Basics")


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](#)

---
## Day 14 | Saturday June 22,2019 ##
### Days Progress ###
* Important set operation.
	- `union()` or `|` : Returns the union of two sets.
	- `intersection()` or `&`: Returns the intersection of two sets.
	- `difference()` or `-`: present in 1 set but not in other.

![set Operation ]({filename}../../../images/100DaysOfCode/set_03.png "Set Operation")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1142493860150439936)



---

## Day 13 | Thursday June 20,2019 ##
### Days Progress ###
* Updated my RAM with set operation for CRUD.
	- `add()` - Adds item to the set.
	- `discard()` - Removes item from the set, if not present, gives no error.
	- `remove()` - Removes item from the set, if not present. gives `KeyError`.
	- `update()` - Adds item from a sequence into a set.

![set crud ]({filename}../../../images/100DaysOfCode/set_02.png "Set CRUD")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1141757313604173824)

---
## Day 12 | Wednesday June 19,2019 ##
### Days Progress ###
* Understood the basic premise around sets.
	- Empty sets can only be created using `set()` function, empty `{}` creates a dict.
	- Sets stores only immutable data type which can give a `hash()` value.
		+ `a = {"a", (1, 2, 3), [1, 2, 3]}` `  # TypeError: unhashable type: 'list'`
	- Sets are used to remove duplicates from List.
	- Sets searching is very fast.
	- Sets do not have a indexing order.


![set creation ]({filename}../../../images/100DaysOfCode/set_01.png "Set creation")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1141395988881367040)


---

## Day 11 | Tuesday June 18,2019 ##
### Days Progress ###
* Explored the different ways to create a `tuple`
	- Create a empty tuple.
		+ `a = tuple()` 
		+ `b = ()`
	- Create a single item tuple.
		+ `a = (1,)` and not
		+ `a = (1)`
	- Brackets are not mandatory for tuple.
		+ `b = 1, 2, 3, 4, 5`
	- indexing in tuple, same as list.
		+ `b[0]`


![tuple creation ]({filename}../../../images/100DaysOfCode/tuple_01.png "tuple creation")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1141031483282317312)


---

## Day 10 | Monday June 17,2019 ##
### Days Progress ###
* Established some basic understanding on list operations
* Operations to add item to the list.
	- `append()`: add an item to end of the list.
	- `insert(2, "bbbb")`: insert at an index.
	- `extend()`: concatenates two list.
* Operation on list look-up, which is very slow, almost linear.
	- `index(value)`: returns first index of value
		+ `ValueError:` if the value is not present in list.
	- `count(value)`: returns the no of times a value is present.
		+ return's `0` is the value is not present.
* Operation to remove item from list.
	- `remove(value)`: removes the value from the list, if not present does not throw error.
	- `pop()`: remove and returns the last element of the list or the index.
* List are heterogeneous.


![Heterogeneous list. ]({filename}../../../images/100DaysOfCode/list_03.png "Heterogeneous list.")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1140663343528599554)

---
## Day 09 | Sunday June 16,2019 ##
### Days Progress ###
* Understood the list's sort and the built-in sorted function.
* `sorted()` returns a list
* `list.sort()` or `list.reverse()` returns `None`

![sorted() and built-in sort ]({filename}../../../images/100DaysOfCode/list_02.png "sorted() and built-in sort")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1140304997944401920)

---
## Day 08 | Saturday June 15,2019 ##
### Days Progress ###
* Started after a gap of 1 cheat day.
* List was the focus today.
	- list can be created using `[]` or `list()`
	- list is a ordered collection.
	- list is a heterogeneous collection.
	- list elements can be accessed using index start at `0`
* List has 1 efficient way of declaring.

```python
names = [
    "XXX",
    "YYY",
    "ZZZ",  # unlike json, we can have comma at the last element, 
  			# it helps with git diff
]
```
![Multi Line list declaration.]({filename}../../../images/100DaysOfCode/list_01.png "Multi Line list declaration.")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1139956001749123072)


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
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1139222966279892992)

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