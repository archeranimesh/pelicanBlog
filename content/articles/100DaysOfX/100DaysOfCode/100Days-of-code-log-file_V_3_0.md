Title: 100Days of Code Log File 3rd Attempt
Date: 2019-06-05 22:29:49
Modified: 2019-08-01 22:59:16
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

## Day 42 | Thursday August 1,2019 ##
### Days Progress ###
* Inheritance is the best way to share property and responsibility across the code.
	- Car has 4 wheels, but Bike has only 2 wheels, but most other parts are similar.
* It creates code re-usability.
* Divides the code from more generic to specific.
* Multiple inheritance is possible, but mostly restricted to Mixins.

![inheritance ]({filename}../../../images/100DaysOfCode/class_04.png "inheritance")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](#)


---
## Day 41 | Wednesday July 31,2019 ##
### Days Progress ###
* `str()`:
	- On our raw object, is we use `str()` it gives a completely non-relevant information.
	- We can change this by overriding the `__str__()` method in our class.
* `repr()`:
	- Its informs a way of creation of the object.
	- We can override `__repr__` method in our class for this information.

![__str__ and __repr__ ]({filename}../../../images/100DaysOfCode/class_03.png "__str__ and __repr__")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1156624050191364096?s=20)


---

## Day 40 | Monday July 29,2019 ##
### Days Progress ###
* `isinstance()` : 
	- returns `True` if an object is an instance of a class.
* `issubclass()` :
	- returns `True` is an object is a subclass of a class.
	- `bool` is a subclass and instance of `int`
	- `object` is the parent class of all object.
* `any()` :
	- returns `True`, if any value in the collection is True.
* `all()` :
	- returns `True`, if all the value in the collection is True.
* `bool` : 
	- `bool` being a subclass of `int`, we have some weird combination, which we can try.
		+ `True + True` : 2
		+ `{0,1, True, False}`: returns `{0, 1}`


![Class isinstance and isSubclass ]({filename}../../../images/100DaysOfCode/class_02.png "Class isinstance and isSubclass")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1155886130706780160?s=20)

---

## Day 39 | Sunday July 28,2019 ##
### Days Progress ###
* Class methods are unique methods, which operates on class variables.
* `@classmethod` : a special decorator to create a class method.
* Class methods take `cls` as argument and not `self`.
* The instance object can access the class methods, since it is aware of their existence.


![Class Method ]({filename}../../../images/100DaysOfCode/class_method_01.png "Class Method")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1155513534962266113?s=20)


---
## Day 38 | Saturday July 27,2019 ##
### Days Progress ###
* The journey into object oriented programming with python.
* Python has no protection of its class variables for modification unlike Java.
* `__init__(self) `
	- It is special function which python calls under the hood when initializing a object.
	- It takes `self` by default.


![dunder init ]({filename}../../../images/100DaysOfCode/init_01.png "dunder init")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1155323021835374592?s=20)


---

## Day 37 | Friday July 26,2019 ##
### Days Progress ###
* OOPs concept.
* Everything is an object in Python.
* Class is template, blue print of a object.
* Instance is a specific creation of a class.
* We can have both
	- Class Variables
		+ Accessed by class.
	- Instance Variable
		+ Accessed by instance of a class.
* `self` is a special name given to a instance in python.

![Class ]({filename}../../../images/100DaysOfCode/class_01.png "Class")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1154961918638997506?s=20)


---
## Day 36 | Thursday July 25,2019 ##
### Days Progress ###
* `.items()` on a `dict()` returns a list of tuples.
* A list of tuples can also be converted back to a dictionary.
* `zip()` function combines two lists into a list of tuples.
	- `for` loop can be used to iterate over a `zip` function.
	- Using `zip()` on asymmetrical list will create a list of tuples with the least no of elements common in the list.
	- `dict(zip(list1, list2))` : converts a list of tuple back to a dictionary.


![Zip Function ]({filename}../../../images/100DaysOfCode/zip_01.png "zip function")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1154448076569903104?s=20)


---

## Day 35 | Wednesday July 24,2019 ##
### Days Progress ###
* Enhanced the learning of list slice.
* Simple index gives an element of the list.
* The slice has the following format.
	- `[1:3]` : the index will start from 1, ends at 3 - 1 = 2
		+ No of elements will be 3 - 1 = 2
* Slice also supports negative index.
	- `-1` : give the last element
	- `-len(list)` : gives the first element
* Slice also has 3rd index, which is `step`.
	- `[::2]` : skips 2 elements.
	- `[::-1]` : short cut to reverse a list.

![List Slice ]({filename}../../../images/100DaysOfCode/list_slice_01.png "List Slice")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1154083653133074437)


---
## Day 34 | Tuesday July 23,2019 ##
### Days Progress ###
* Today is the day, when I am more confused than aware.
* There is no tuple comprehension in python, but there are Generator expressions.
* Generator expressions are created with this syntax.
	- `(num * num for num in range(11))`
		+ Ideally we expect it to be a tuple comprehension, but it is a generator object.
* Generator expressions are a memory efficient way of creating a big list.
* We cannot index on the generator object, gives a `TypeError`.
* `next()` and `for/each` can be used to iterate over a generator.

![Generator comprehensions ]({filename}../../../images/100DaysOfCode/generator_comp_01.png "Generator comprehensions")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* References.
	- [Generator Unpacking ](https://stackoverflow.com/questions/51811061/can-i-turn-a-generator-object-into-a-tuple-without-using-tuple/51811147#51811147)
	- [Why is there no tuple comprehension in Python?](https://stackoverflow.com/questions/16940293/why-is-there-no-tuple-comprehension-in-python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1153716904554463232)

---
## Day 33 | Monday July 22,2019 ##
### Days Progress ###
* The `set` and `dict` comprehensions are very similar in syntax.
	- `set` comprehensions.
		+ `{num * num for num in range(11)}`
	- `dict` comprehensions.
		+ `{num: num * num for num in range(11)}`
* Both `set` and `dict` comprehensions are not ordered.

![Set comprehensions ]({filename}../../../images/100DaysOfCode/set_comp_01.png "Set comprehensions")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1153360497732751360)

---

## Day 32 | Friday July 19,2019 ##
### Days Progress ###
* Built-in function which works on the `list`
	- `sum()` : returns the sum of a list
	- `min()` : returns the smallest element in the list.
	- `max()` : returns the biggest element in the list.
	- `sorted()` : returns a sorted list.
		+ `reverse=True` as a default argument will reverse the list.


![List comprehensions ]({filename}../../../images/100DaysOfCode/list_comp_03.png "List comprehensions")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1152274282329735168)

---

## Day 31 | Thursday July 18,2019 ##
### Days Progress ###
* Continued with List comprehensions.
* We can use conditionals in list comprehension to filter values.
	- `[num**2 for num in numbers if num %2 == 0]`
		+ The conditional comes at the end.
		+ This conditional works as a filter.
* We have 3 ways to use List comprehensions.
	- Map - All values are used
	- Filter - Some values are used
	- Map/Filter - Some values filtered and then modified.

![List comprehensions ]({filename}../../../images/100DaysOfCode/list_comp_02.png "List comprehensions")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1151907365383360512)


---
## Day 30 | Tuesday July16,2019 ##
### Days Progress ###
* There are various type conversion which we can use.
	- `split()` : convert string to a list.
	- `join()` : convert a list to string. `",".join(my_list)`
	- tuple unpacking can also be used when using `.split()`
* Learned about list comprehensions.
	- `[num**2 for num in numbers]` : list of square of numbers.
		+ We right the square brackets first
		+ Followed by the `for` loop.
		+ The variable used in the `for` loop is available to the left of loop, `num`
		+ Apply mapping on the variable left of `for` loop.
	- We can combine with `tuple` and `f` strings to get more valuable information.

![List comprehensions ]({filename}../../../images/100DaysOfCode/list_comp_01.png "List comprehensions")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/intermediate_python)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1151181246510161920)



---
## Day 29 | Saturday July 13,2019 ##
### Days Progress ###
* Worked on the Github Api Project using these concepts.
	- `requests`
	- `exceptions`
	- `APIs`
	- Query Parameters.


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1150102077391036422)

---

## Day 28 | Friday July 12,2019 ##
### Days Progress ###
* learned mostly about `requests` library.
* 4 HTTP methods
	- `GET`
	- `POST`
	- `PUT`
	- `DELETE`
* HTTP code
	- `1XX` : Information
	- `2XX` : Success
	- `3XX` : Redirection
	- `4XX` : Client error
	- `5XX` : Server error


![Shibe URL for dogs ]({filename}../../../images/100DaysOfCode/dog_01.png "Shibe URL for dogs")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1149743435944824832)

---
## Day 27 | Thursday July 11,2019 ##
### Days Progress ###
* `__name__` is a nice way to put code when we want to execute as a script.
	- The above code is not invoked when called as a library.
* `try/except` is a great way to catch error's in code, and give alternate execution path.

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1149376500728078336)

---
## Day 26 | Wednesday July 10,2019 ##
### Days Progress ###
* Mostly learned about python file's and debugging techniques.

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1149011262996660225)

---
## Day 25 | Tuesday July 9,2019 ##
### Days Progress ###
* `while` loop is used to iterate over numbers in place of sequence.
	- Also when we are not sure about the no of iteration
* `break`: 
	- It stops the execution of loop, and jumps to end of loop.
	- If present in nested loop, it breaks the loop it is present in.
* `continue`:
	- It stops the loop execution and jump to start of the loop.
* `return`: 
	- It also return the loop control to outside of the loop.


![break, continue and return statement. ]({filename}../../../images/100DaysOfCode/break_01.png "break, continue and return statement")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1148637195948843008)


---

## Day 24 | Friday July 5,2019 ##
### Days Progress ###
* Today's learning was mostly on the Control flow.
* We have different variant of `if` condition.
	- `if`
	- `if-else`
	- `if-elif-else`
* We can also check truthiness.

![if statement. ]({filename}../../../images/100DaysOfCode/if_01.png "if statement")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1147190975795646464)

---
## Day 23 | Thursday July 4,2019 ##
### Days Progress ###
* Continuing the process of learning loop, understood about looping with `dict`
* There are mainly 3 looping with `dict`
	- `.key()` - this is default, so do not have to specify in `for` loop.
	- `.items()` - returns a tuple of key, value pair.
	- `.values()` - returns only the values in `dict`.
	- `.enumerate(.items())` - gives, index and a tuple of key value.

![dict loop. ]({filename}../../../images/100DaysOfCode/dict_loop.png "dict loop")


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1146829703782625281)

---

## Day 22 | Wednesday July 3,2019 ##
### Days Progress ###
* Mostly improved the understanding of loops with list and range function.
* `for` loops create a temporary variable which is in scope outside of `for` loop.
* `range()`  is a good function for looping, it has 3 variant.
	- `range(5)` : default, creates the number from 0 to 4
	- `range(1,5)` : start and end index, creates the number from 1 to 4, 5 non inclusive.
	- `range(1,5,2)` : the 3rd argument is `steps`, will step those many numbers.
	- It does not take any Keyword arguments.

![list loop. ]({filename}../../../images/100DaysOfCode/list_loop.png "list loop")


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1146472085671124992)



---
## Day 21 | Monday July 1,2019 ##
### Days Progress ###
* I have reached that day, where it is said, 21 days is required minimum to form a habit.
	- Hope this habit stays with me.
* Learning continued on `and`, `or`, and `not` operator.
* It was an eye opener.
* `and` and `or` returns the value of one of the expression and not `True` or `False`
* `and`
	- It returns the value of 2nd operand if the first operand is `True` else value of first.

![and Operator. ]({filename}../../../images/100DaysOfCode/and.png "and Operator")


* `or`
	- It returns the value of 1st operand if it evaluates to `True`, else value of second.

![or Operator. ]({filename}../../../images/100DaysOfCode/or.png "or Operator")

* `not`
	- Returns the inverse of the operator.


![not Operator. ]({filename}../../../images/100DaysOfCode/not.png "not Operator")


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1145744575375409152)

---

## Day 20 | Sunday June 30,2019 ##
### Days Progress ###
* Comparison operators in Python.
	- `<` : Less than
	- `>` : greater than
	- `<=` : less than equal to
	- `>=` : greater than equal to
	- `==` : equal to
	- `!=` : Not equal to
	- `is` : Identity, when both object points to same.
* Strings are compared based on their ASCII value.
	- The capital letters are smaller than small letters.


![Comparison Operator. ]({filename}../../../images/100DaysOfCode/Booleans_02.png "Comparison Operator")


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](#)

---

## Day 19 | Friday June 28,2019 ##
### Days Progress ###
* What are the truthiness of various data types.
	- integers:
		+ `0` is `False`
		+ any other number is `True`
	- Collections:
		+ Empty list, tuple, Dictionary, sets are `False`
		+ Non Empty collections are `True`
	- Strings:
		+ Empty String is `False`
		+ Non Empty String are `True`.
	- `None` is `False`


![Booleans truthiness. ]({filename}../../../images/100DaysOfCode/Booleans_01.png "Booleans truthiness")

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1144659185348431872)

---

## Day 18 | Wednesday June 26,2019 ##
### Days Progress ###
* Learned about the list slice.
	- `my_list[0:3` : Returns 0 - 2nd index
	- `my_list[:]` : clone the entire list.
	- `my_list[-1]` : Special way to get the last item.


![List Slice. ]({filename}../../../images/100DaysOfCode/list_04.png "List Slice")


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1143935174394015744)


---
## Day 17 | Tuesday June 25,2019 ##

### Days Progress ###
* Finally crossed the last attempts days.
* Learned about mutability.
* Basic data type are immutable.
	*  `int`, `float`, `decimal`, `str`, `bool`
+  Containers data type are divided
	*  `list`, `set`, `dict` are mutable
	*  `tuple` is immutable.

### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1143575190632194049)


---
## Day 16 | Monday June 24,2019 ##
### Days Progress ###
* Adding/Accessing dictionary elements.
	- add new key/Value pair.	`nums["four"] = 4`
	- There are no duplicate key in Dictionaries.
	- If new value is assigned to same key, it will override the old value.
	- Existence of a key in Dictionaries. `"one" in nums`
	- `.update()`: Combine two list.
	- 3 important functions on Dictionaries
		+ `.keys()`: returns special list called dict keys
		+ `.values()`: returns a special list called dict values
		+ `.item()`: returns a list of tuple, called dict items


![Dictionaries Operation ]({filename}../../../images/100DaysOfCode/dict_02.png "Dictionaries Operation")


### Thoughts ###
* [My Github Url](https://github.com/archeranimesh/pythonFundamentals)
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1143211092597825536)

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
* [Link to tweet](https://twitter.com/animeshkbhadra/status/1142836839323095040)

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