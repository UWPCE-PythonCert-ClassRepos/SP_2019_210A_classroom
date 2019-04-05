
:orphan:

.. _notes_session05:

####################
Notes for Session 05
####################

November 6, 2018 -- Election Day!!!

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Brian E Nisonger

Carol Louise  Farris

Dianna  Tingg

Manmeet S Dosanjh


Issues that came up during the week.
====================================

git and generated files
-----------------------

In general, you don't want to put generated files in git.

In this case, the letters your mailroom program created.

**Caution:** be very careful with ``git add .`` or ``git add *`` -- generally better to specifically add the files you now you need.

Style
-----

Use PEP8 style -- really!

https://www.python.org/dev/peps/pep-0008/

The ONLY exception is if you work in an organization that has a different style guide. It can make sense for your python code to match other code in an organization. But otherwise, use a style consistent with the rest of the Python world.

And don't use "Hungarian Notation" -- it is really non-pythonic, and sometimes actually wrong -- and a string called ``intSomething`` just adds confusion!

The best way to do this is with a linter in your editor -- like the Anaconda package in Sublime. A number of you are getting really annoyed by all the "noise" that the linter creates. But if you keep your code in PEP8 style, it won't be there!


Minor Issues
------------

Remember that:

``something in a_dict`` checks if ``this`` is a key

similarly:

``for k in dict:``

loops through the keys. So no need for:

``for k in dict.keys():``

``sum``
-------

Did everyone find the ``sum()`` built in function?

How about ``max()`` and ``min()``


Getting an arbitrary key from a dict
------------------------------------

See ``arbitrary_key.py`` in `examples/session05`

nifty formatting
----------------

what the heck is this?

.. code-block:: python

    def data_print(info, widths):
        """
        takes in donor information and widths and returns a string formatted for
        printing for a donor report.
        """
        output_string = ""
        output_string += '{:<{width0}} ${:>{width1}.2f} {:^{width2}} ${:>{width3}}'.format(info[0], info[1], info[2], info[3], width0=widths[0], width1=widths[1]-1, width2=widths[2], width3=widths[3]-1)

cleaned up a bit::

    '{:<{widths[0]}} ${:>{widths[1]}.2f}'.format( "fred", 100, widths=widths)

islice
------

This constuct is pertty cool for trigrams::

  for w1, w2, w3 in zip(word_list[:-2], word_list[1:-1], word_list[2:]):

but remeber that slicing makes a copy -- so this is making three copies of the full work list. Computers have a LOT of memory these days, but it's still better to not waste it.

Turns out there is a alternative:

https://docs.python.org/3.7/library/itertools.html#itertools.islice


Coding Workflow
---------------

As you are developing your code, you *really* want to have an quick and efficient way to run you code and see if it's working, how it's changed, etc.

You may have noticed that for a program like Mailroom, you may have to do a few steps if user interaction to get to the part of the code you are working on. So how do you work on that efficiently?

The "right" way to do it is something called "Test Driven Development", which we will get to soon. But in the meantime:

* You want to break your code down into small functions that each do one thing.

* You should be able to run each function by itself.

If you are doing that, then as you develop your code, you can write and run each function until it's doing what it's supposed to do, and THEN put it all together.

One way to run a function is to call it in the ``__name__ == "__main__"`` block. You can then comment and uncomment each call as you work on your code.

Also: you really, really need a way to run your code with a couple keystrokes!!

I'll demonstrate this when we review code.



Review of last week's assignments
=================================

Mailroom review
---------------

Anyone up for a review?

Trigrams review
---------------

Anyone want to look at theirs?


Lightning Talks
===============

Let's take a break and do them now.

New Assignments
===============

Comprehensions
--------------


Let's take a few minutes to go through it in class:

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/comprehensions_lab.html

Exceptions
----------

Exceptions take a little while to "wrap your head around".

Shall we do the Exercise together?

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/except_exercise.html

