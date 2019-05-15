
:orphan:

.. _notes_session09:

####################
Notes for Session 09
####################

June 4, 2019
************


**NOTE:**  These notes are "live" -- they will change up until the class starts..

A collection of notes to go over in class, to keep things organized.


Lightning Talks
===============

Rimlee Talukdar

Joseph Charles Nunnelley


Issues that came up during the week.
====================================

``sum()``
---------

You can use ``sum()`` for things other than numbers. Anything that you can add, you can use ``sum()`` for, but you need to give it a "start" value:

From trigrams:

.. code-block:: ipython

    In [14]: text
    Out[14]:
    ['him mention her under any other name. In his eyes she eclipses',
     'and predominates the whole of her sex. It was not that he felt',
     'any emotion akin to love for Irene Adler. All emotions, and that']

    In [15]: sum((line.split() for line in text), [])
    Out[15]:
    ['him',
     'mention',
     'her',
     'under',
     'any',
     'other',
     'name.',
     ...

Except not strings:

.. code-block:: ipython

    In [17]: sum(["this", "that", "something"], "")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-17-c882ae453790> in <module>
    ----> 1 sum(["this", "that", "something"], "")

    TypeError: sum() can't sum strings [use ''.join(seq) instead]

That's because you ``.join()`` is a lot more efficient.


"private" attributes and dunders
--------------------------------

``_something`` vs ``__something`` vs ``__something__``

Let's talk about that...


Adding parameters to a subclass ``__init__``
--------------------------------------------

In general, when you override a method in a subclass, you want the method signature to be the same. That is -- all the parameters should be the same.

However, sometimes, particularly with ``__init__``, you may need a couple extra parameters. To keep things clean and extensible, you want to put the extra parameters at the beginning, before the super class' parameters:

And this lets you use ``*args`` and ``**kwargs`` to pass along the usual ones.

.. code-block:: python

    class Base:
        def __init__(self, par1, par2, par3=something, par4=something):
            ...

    class Subclass(Base):
        def __init__(self, newpar1, newpar2, *args, **kwargs):
            self.newpar1 = newpar1
            self.newpar2 = newpar2
            super().__init__(*args, **kwarg)

**Example:** html_render Anchor tag:


.. code-block:: python

    class A(OneLineTag):
        """
        anchor element
        """
        tag = "a"

        def __init__(self, link, *args, **kwargs):
            kwargs['href'] = link
            super().__init__(*args, **kwargs)

This becomes particularly important with ``super()`` and subclassing...

Testing Challenges
------------------

.. image:: _static/test_joke.jpeg


Any other html_render questions?
--------------------------------

Brian: still up for a code review / debug session?

Magic Methods and Circle class
------------------------------

Any questions?

Should we look at mine?


Lightning Talks
===============


New Topics
==========

sorting
-------

maybe it's a good idea to add a sort_key method to your classes?

see ``examples/Session09/sort_key.py``

let's try it on Circle....

classmethod
-----------

``classmethod`` is really pretty simple to use, not much to talk about. But it can be a bit challenging to "get".

The key point is that classmethods work for subclasses -- like for alternate constructors.

Let's look at that with my Circle solution:

``solutions/Session08/circle.py``

(and answer any other questions about Circle, while we are at it)


multiple inheritance and super()
--------------------------------

``super()`` is a mixed bag -- it's actually a pretty complex topic, but can be pretty easy to use -- at least in the simple cases.

To get the hang of multiple inheritance, mix-ins, and ``super()``, we'll play around with object canvas:

See: ``examples/Session09/object_canvas.py``


Object Oriented Mailroom
------------------------

One more time!

Yes, it's time to make mailroom Object Oriented:

:ref:`exercise_mailroom_oo`







