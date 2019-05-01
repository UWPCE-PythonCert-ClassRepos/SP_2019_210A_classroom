:orphan:

.. _notes_session04:

####################
Notes for Session 04
####################

April 30, 2019
**************


**NOTE:**  These notes are "live" -- they will change up until the class starts..


A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

This week:

James S Ward

George J Kim


Issues that came up during the week.
====================================

Indexing vs Slicing
-------------------

A few of you ran into this issue in the slicing lab:

If you have a sequence, say a tuple, like this::

    (5, 3, 8, 12, 45, 13, 5)

What does an index return?

This comes up in the slicing lab: exchange the first and last items of the sequence:

Let's check it out. In the class repo:

``SP_2019_210A_classroom/examples/Session04/index_vs_slice.py``

(``git pull upstream master``)

Built in names
--------------

Python has a number of "key words" that are reserved. If you try to use them as a variable name, you will get an error:

.. code-block:: ipython

    In [1]: for = 5
      File "<ipython-input-1-36df406aa65d>", line 1
        for = 5
            ^
    SyntaxError: invalid syntax

Sometimes a bit confusing, as it's not REALLY a syntax error, but rather using a keyword as a variable....

But there are also a LOT of "built in" names. Try::

    dir(__builtins__)

You can use these names for variable, but when you do, it willwrite over the built-in one, which means that you then can't use it in the udual way. For instance, a ``list`` is the list type, you can make a list out of any sequence with it:

.. code-block:: ipython

    In [6]: list("this")
    Out[6]: ['t', 'h', 'i', 's']

But if you use it as a name, it then won't work in the usual way:

.. code-block:: ipython

    In [7]: list = [1,2,3,4,5]

    In [8]: list
    Out[8]: [1, 2, 3, 4, 5]

    In [9]: list("this")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-9-c89f7438771a> in <module>()
    ----> 1 list("this")

    TypeError: 'list' object is not callable

Moral of the story:

**Don't "shadow" built in names**

Use things like::

    my_list
    infile

or even misspellings or adding an underscore:

``klass`` or ``cls`` or ``_class`` instead of ``class``

Hopefully your editor will warn you -- otherwise, think about it when you get a strange error like:

.. code-block:: ipython

    In [14]: input = "this was some input"

    In [15]: input("=>")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-15-56a225daeb09> in <module>()
    ----> 1 input("=>")

    TypeError: 'str' object is not callable


Mutable default parameters
--------------------------

There was a video on this -- any questions about it?

If not then we'll move on...

This is a real "gotcha" in Python. Someone wrote a non-recursive solution to the sum_series problem. It worked great -- EXCEPT if it got called more than once! Any idea what the problem is?

(``examples\session04\series_with_mutable.py``)

.. code-block:: python

    def sum_series(nth=1, sequence=[0,1]):
        """
        Generate a list of sums given a seed and return the Nth number.
        """
        for i in range(2, nth):
            sequence.append(sequence[i-2] + sequence[i-1])
        return sequence[nth-1]

So this uses the logic of starting out with the first two values in the series, and then looping to build up the series from there.

And [0, 1] is set as a default to start the series off -- the start of the Fibonacci series.  So if you pass in only one argument, you should get the Fibonacci number:

Remember that the start of the Fibonacci series is::

  0, 1, 1, 2, 3, 5, 8, 13, ...

What happens when you run this code:

.. code-block:: python

    In [21]: sum_series(5)
    Out[21]: 3

All good.

    In [22]: sum_series(6)
    Out[22]: 1
    # WTF???

The issue is that:

Default Arguments get evaluated **when the function is defined**. So every time the function is called, it will use the *same* list! Each time adding more and more to the list.

Let's explore that some more, and some solutions....


Recursion in an interactive loop
--------------------------------

not a great idea!

you can do something like:

.. code-block:: python

    def mainloop():
        while True:
            ans = input("A question > ")
            ....
            if ans == "again"
                mainloop()

Let's look at this:

``examples/session04/recursive_mainloop.py``

(do a ``git pull upstream master`` if you don't see it.)

String formatting
-----------------

Here's an example::

    tup3 = tuple(range(10))
    print("{:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5}".format(*tup3))

Seems like a lot of typing to me :-)


Slicing and List labs
---------------------

Any questions?

Altering a list while looping through it
........................................

what could go wrong with this code?

.. code-block:: python

    for i in a_list:
        if some_condition:
            a_list.remove(i)

Let's try it out ...

``examples/session04/deleting_in_loop.py``

Sorting
.......

Anyone confused about sorting? Shall we go over it?

``examples/session04/sort_example.py``

My solutions
------------

Let's look at my solutions quickly.

mailroom
........

Anyone get it done?

Should we look at my solution -- or review one of yours?

Or wait ?


Lightning Talks:
----------------

Let's take a break and do them...

New Material
============

Any questions on dictionaries, set or files?

This gets fun now!

mailroom part 2
---------------

How might you use dictionaries in mailroom? If you haven't finished it without dicts, why not add them now?

trigrams
--------

This is a really fun one -- but challenging.

Let's get a start on it!


