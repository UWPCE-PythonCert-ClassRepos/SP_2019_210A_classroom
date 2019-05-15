
:orphan:

.. _notes_session06:

####################
Notes for Session 06
####################

May 14, 2019
************


**NOTE:**  These notes are "live" -- they will change up until the class starts.


A collection of notes to go over in class, to keep things organized.

So I don't forget!!!
====================

I (Chris) will be out of town this weekend, next week, and the following weekend: Bryan will be covering class next week, and hopefully office hours over the weekends. Look for info from him about that.

I'll be back the following week, then off again, so we're starting to transition to Bryan for the rest of the class.


Lightning Talks
===============

Sarah Rickli

Fred Ballyns

As usual -- we'll do these mid-class

mailroom 4!!!!
==============

**WTF?**

What if I haven't gotten version 2 done yet???

It all builds on itself -- so no need to do each intermediate step if you haven't already. If you submit a well tested mailroom with some use of dictionaries and exception handling, we'll give you credit for all of them.


Issues that came up during the week.
====================================


dict as switch -- how do you leave the loop?
--------------------------------------------

Let's look at my solution:

``solutions/Lesson04/mailroom2.py``


quit()
------

In my solution to mailroom, I created a function called ``quit`` to quit the program. That is not a great idea, as there is a built-in called ``quit``.  In my defense, the ``quit()`` built-in didn't exist when I learned Python :-).

but you can simply put the built-in ``quit`` in your switch dict.

``readlines()`` ?
-----------------

quite a few of you have code like this:

.. code-block:: python

    with open(filename, "r") as f:
        full_lines = f.readlines()

    for line in full_lines:
        ...

Nothing wrong with that, but ...

``.readlines()``  reads the entire contents of the file into memory all at once.  Memory is big and cheap these days, but what if it's a REALLY big file?

If you are going to process the file line by line anyway, you might as well do:

.. code-block:: python

    with open(filename, "r") as f:
        for line in f:
            ...

That will loop though the file line by line, but only store one line at a time in memory.  The file system and disk should have a smart cache, so that it will be just as fast, but more memory efficient.

And one less line of code :-)

binary vs text files
--------------------

``open()`` uses text mode (utf-8) by default. It will try to decode the file into text. If you open a binary file that way it will likely barf.

try: ``open(the_filename, 'rb'``

For more on what "decode" means:

`Unicode in Python <https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Unicode.html?highlight=unicode>`_


Any Questions about the homework -- or anything?
------------------------------------------------

review trigrams?

review mailroom?


Break and Lightning talks
=========================


Testing?
--------

Did y'all do the testing exercise with a coding bat example?

We could do one now.

Or...


Advanced Argument Passing
-------------------------

All this ``*arg``, ``**kwargs`` stuff a bit confusing?

Let's explore it a bit.

AND -- we'll use TDD to do it.

Exercise here:

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/args_kwargs_lab.html








