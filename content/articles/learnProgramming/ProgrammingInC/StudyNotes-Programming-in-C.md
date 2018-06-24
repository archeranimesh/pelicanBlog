Title: Study Notes for Programming in C
Date: 2018-06-23 18:50:35
Modified: 2018-06-24 17:15:17
Category: C Programming
Tags: C-Programming, Kernighan&Ritchie, KnR, The C Programming Language.
Slug: StudyNotes-Programming-in-C
Author: Animesh Bhadra
subtitle: Hello World
Summary: Study Notes for learning C programming from the legendary book *The C Programming Language* by "Brain W. Kenighan and Dennis M. Ritchie". This books is considered to be the bible for C Programming. This blog is my understanding's from the books and study notes, in case a reference is required in future.
keywords: C-Programming, KnR, The C Programming Language, Study Notes

[TOC]


![Hello World Programming ]({filename}../../../images/CProgramming/helloWorld.png "Hello World Image")



## Introduction ##

C is not only a "System programming language" but has a wide variety of use in other domain.

### Fundamental Data Types ###

* Characters `char`
* Integers `int`, `short`, `long`
* Floating point `double`, `float`

### Derived Data Types ###

* Pointers
	- **Pointers** provide for a machine-independent address arithmetic.
* Arrays
* Structure
* Unions.


### Expressions ###

**Expressions** are formed from **Operator** and **Operands**. Any expression including an assignment or a function call can be a **statement**.


### Functions ###

**Functions** performs a single set of operation within a block of code.

**Functions** may return values of 

* Fundamental data types.
* Derived Data types. except arrays
	- Pointers
	- Structure
	- Unions

#### Variables ####
* Variables can be internal to a function.
* External but known only within a single source file.
* Visible to the entire program.
	- This is frowned upon and we should rarely use.


### Preprocessing ###

Preprocessing step performs macro substitution on program text, inclusion of other source file or conditional compilation.

### UseCase not provided in C ###

* Operations directly dealing with Composite Objects, like
	- Array,
	- Structure, 
	- Unions
* No Storage other than `static` and `auto`matic.
* No Input/Output facilities.
* No built in file Access.

The above facilities are included by help of standard library defined by the **ANSI C Standard**.

### ANSI C Standard ###

* New syntax for declaring and defining functions.
* Definition of a standard library.
* C is not a strongly typed language.
* C frowns on but permits the interchange of pointer and integers which has been eliminated by ANSI.
* No Automatic conversion of incompatible data types.


## Reference ##

* [Image Source ](https://excelwithbusiness.com/blog/say-hello-world-in-28-different-programming-languages/)
