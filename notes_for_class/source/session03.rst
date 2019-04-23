:orphan:

.. _notes_session03:

####################
Notes for Session 03
####################

April 23, 2019
**************


**NOTE:**  These notes are "live" -- they will change up until the class starts..

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Up today:

Charlie England

Ying Shen (Sally)

Are you ready? We'll do them in the middle of the session.

Issues that came up during the week.
====================================

``.gitignore``
--------------

You can make your own!

For those of you using PyCharm, this could be handy for those pesky ``.idea`` files. (and ``.vscode`` files, etc.)

Let's do that now.

git commit and PR messages
--------------------------

At this point, it's pretty obvious what you are doing. But as the projects get more complicated, it won't be.

So please put meaningful commit and PR messages -- particularly PR messages!

This is a **really good** habit to get into for future development work.


PEP08 and a linter
------------------

It is a really good idea to get in the habit of using consistent style in your code -- i.e. follow PEP08.

And this is really easy to do if you have a linter set up in your editor. If you haven't gotten that to work -- do try to do so soon!

https://www.python.org/dev/peps/pep-0008/

Even more important than all of the rest:

**Use four spaces per indent**

**ALWAYS**


Separation of Concerns
----------------------
From print_grid: if you are going to have separate functions, better for them to return a string, and then put all the printing in the calling function, in one place. That would make it more re-usable -- say you want to write to a file?

This is a tiny example of what's known as "separation of concerns"

``for`` vs ``while``
--------------------

Quite a few folks used a ``while`` loop in ``print_grid``,
and ``sum_series``, and ...

But for all these cases, a ``for`` loop (and ``range()``) is a better option.

So: When to use ``for`` vs ``while`` ?

* You can do everything with a ``while`` loop -- you never actually *need* ``for``

But:

``for`` is pretty handy primarily for looping through the items in am iterable -- doing the similar things to everything in a collection.

And ``range()`` is an easy-to-create collection of a sequence of integers of a given size.

So in short:

Use ``while`` when you want to repeat something some unknown amount -- maybe a few times maybe thousands...

Use ``for`` when you want to work with an entire collection, or a pre-determined number of times.


``is`` vs ``==``
----------------

In FizzBuzz, someone had code something like this:

```
if n % 3 is 0:
```

That works, but it's a "Bad Idea™"

"is" tests whether the objects are actually the same object -- not whether they have the same value. As you can easily have multiple objects that happen to have the same value, "is" will fail in the general case.

This works because cPython has an optimization called "interning" -- since small integers are used so often, the interpreter keeps a pool of them around to re-use, rather than creating multiple integer objects with the same value.

So "is" will work as a test for small integers, but not large ones:

.. code-block:: ipython

    In [65]: x = 5

    In [66]: y = 5

    In [67]: x is y
    Out[67]: True

    In [68]: x = 345678

    In [69]: y = 345678

    In [70]: x is y
    Out[70]: False

**NOTE:** This is also the case for small strings.

**Important:** This is an implementation detail. Do not count on it!

String formatting or concatenation?
-----------------------------------

As a rule, it's better to use string formatting than a bunch of concatenation (string addition) -- but if it's really simple, maybe not::

    grid_square = "|{}".format(' ' * grid_size)

What's actually going on here?

Let's time it ...


Review Solutions
================

Fibonacci, FizzBuzz, print_grid
-------------------------------

Anyone want to review their code?

Let's take a look at Lincoln's FizzBuzz::

  /students/Lincoln_Zhang/Session2/fizzbuzz



My Solutions:
-------------

I've posted my solutions to last week's assignments in the class repo::

  git pull upstream master

They are in::

  solutions/Lesson02


Lightning Talks
===============

Let's take a break and do the lightning talks...


Now some new stuff
==================


Labs:
-----

Get a start on your own, then we'll come together and finish it up.

:ref:`exercise_slicing`

:ref:`exercise_list_lab`

:ref:`exercise_string_formatting`

Mailroom
--------

Let's start this as a group:

:ref:`exercise_mailroom_part1`






