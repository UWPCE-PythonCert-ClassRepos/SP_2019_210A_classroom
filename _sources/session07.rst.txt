
:orphan:

.. _notes_session07:

####################
Notes for Session 07
####################

May 21, 2019
************


**NOTE:**  These notes are "live" -- they will change up until the class starts.

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============




Issues that came up during the week.
====================================

Naming and Style
----------------

Read this again:

https://uwpce-pythoncert.github.io/PythonCertDevel/modules/NamingThings.html

And watch this video:

https://www.youtube.com/watch?v=hZ7hgYKKnF0

Some of you are still not following PEP 8 style. If you can't (or don't want to) set up a linter in your editor or IDE, you can run ``pycodestyle`` on your code.

https://pycodestyle.readthedocs.io

``python3 -m pip install pycodestyle``

Let's give it a quick try.

Auto-fixing style
-----------------

If you don't want to fix all that by hand, there are tools to do it for you.

one really nice one is yapf:

https://github.com/google/yapf

Maybe give ``yapf`` a try.


Chaining ``or``, etc.
---------------------

This looks pretty nifty:

.. code-block:: python

    while answer != 'x' or 'r' or 't' or 'a':
        do_something()

But does that mean what you expect it to?

will it ever be ``False``?

Let's play with that...

Operator Precedence
...................

This table tells you which operators have "Precedence" over each other -- that is, which are evaluated first:

https://docs.python.org/3/reference/expressions.html#operator-precedence

When in doubt -- add parenthesis to make it clear. Is there any way to add parentheses that works for the above?

Comparison Chaining
...................

Another complication in all this is chaining of comparisons:

https://docs.python.org/3/reference/expressions.html#comparisons

It allows you to do nifty (and very readable) things like:

.. code-block:: python

    if a < b < c:
        do_something()

That's nice, 'cause it looks a lot like math -- simple and clear.

and that means:

.. code-block:: python

    if (a < b) and (b < c):
        do_something()


So with chaining, you can't just add parentheses to make it clear.

Also -- like with ``and`` and ``or``, chaining "shortcuts".  In the example above, if ``a`` is not less than ``b``, then ``c`` will never be evaluated. And ``b`` will only be evaluated once in any case.

So what's going on here?

.. code-block:: ipython

    In [41]: 2 < 5 in range(3)
    Out[41]: False

    In [42]: (2 < 5) in range(3)
    Out[42]: True

    In [43]: 2 < (5 in range(3))
    Out[43]: False


Turns out that ``in``, ``not``, ``not in`` are considered comparison operators too.


Mutating vs. re-assigning
-------------------------

I've seen code like this in a few trigram solutions:

``output = output + [follower]``

(``output`` is a list of strings, follower is a single string)

What it does is add a new item to a list.

But is that an efficient way to do that?

If you are adding one element to a list -- ``append()`` is the way to go.

``output_list.append(random_trigram_followers)``

Using addition works fine, but it's creating a whole new list (actually: *two* new lists) just to throw it away again.

And if you are adding another list of objects, you want to use ``extend()``.

With this code:

``output = output + [follower]``

This is what happens:

1) Create a one-element list with ``follower`` in it.
2) Create a new list with the contents of ``output`` and that just created list.
3) Re-assign the name ``output`` to that new list.
4) Throw away the original list ``output`` was bound to, and the temporary list created for ``follower``.

That's a LOT of overhead!

Be cognizant of when you are mutating (changing) an object vs. creating a new one and assigning it to the same name. When you do assignment (``=``) you are probably creating a new object -- is that what you want?


``+=`` is different -- it is the "in_place" operator, so:

``a_list += another_list``

does not create an new list -- it adds to the original list "in place" -- it is identical to:

``a_list.extend(another_list)``

And it is an efficient operation.

The trick is that the "augmented assignment" operators, like ``+=`` **do** create new object when used with an immutable:

.. code-block:: ipython

    In [4]: tup1 = tup2 = (1, 2, 3)

    In [5]: tup1 is tup2
    Out[5]: True

    In [6]: tup1 += (4, 5)

    In [7]: tup1 is tup2
    Out[7]: False

    In [9]: tup1
    Out[9]: (1, 2, 3, 4, 5)

    In [10]: tup2
    Out[10]: (1, 2, 3)

Contrast this with (mutable) lists:

.. code-block:: ipython

    In [11]: list1 = list2 = [1, 2, 3]

    In [12]: list1 += [3, 4]

    In [13]: list1 is list2
    Out[13]: True

    In [14]: list1
    Out[14]: [1, 2, 3, 3, 4]

    In [15]: list2
    Out[15]: [1, 2, 3, 3, 4]

Personally, I think it's a "wart" that augmented assignment may or may not be a mutating operation.

But at the time it was added, there were two goals:

1) Efficient in-place operations on mutables (partly to support numpy)

2) Quick and easy incrementing of values, in particular integers:

``i += 1``

And no one wanted to add **two** new sets of operators.

https://www.python.org/dev/peps/pep-0203/

Working with dicts
------------------

Want to know if something is in a dict? You could do:

.. code-block:: python

    if name not in donors.keys():

But that requires python to loop through the entire keys object (I think).

You can simply do:

.. code-block:: python

    if name not in donors:

Cleaner -- but is it faster? It'll be a lot faster if the ``dict_keys`` object doesn't directly support ``in``.  Let's take a look:

passing args to functions in a dict
-----------------------------------

On MS Teams, Vincent M Aquila and serpasj had a converstaion about passing arguments to functions in a dict.

I'm not sure what the goal really was -- so let's talk about it now.


unit tests should be isolated
-----------------------------

Ideally, each unit test should be able to run all on its own, and it should NOT matter what order tests run in.

That can be a bit of a trick with mailroom -- as you might have a test of adding a new donor to the database, and another test that asserts that the report has the right number of donors in it.

Let's look a how to deal with that.

A Little Code Refactoring
-------------------------

(If we have time...)

After making a few comments on a block of mailroom code, I decided it might be instructive to review and refactor it live with the class. The code can be found in the class repo in:

``/examples/Session07/refactor.py``

That code works now -- so the first thing we're going to do is make tests for it. Then we can refactor away and know it still works.


Any other questions/issues before we get into classes?
------------------------------------------------------

Note that we'll be employing testing the rest of the class, so if you don't quite "get it",  you'll have more chances :-)


Break -- Then Lightning Talks
=============================

Adolphe Aime  Ndilingiye
Udo (Michael) Uduhiri
Zachary A Connaughton (Zach)


Classes!
========

Classes are the core of Object Oriented programming. Rather than talk about them in the abstract, we'll start doing a real problem, and talk about the pieces as we go.

html_render
-----------

So on to the the html_render assignment:

:ref:`exercise_html_renderer`



