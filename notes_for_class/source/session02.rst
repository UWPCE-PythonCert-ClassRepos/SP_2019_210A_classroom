:orphan:

.. _notes_session02:

####################
Notes for Session 02
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Up today:

|
| Habtamu H Asfaw
| Jim Jenkins
| Eric Streit
| Vincent M Aquila
|

Are you ready? We'll do them in the middle of the session.

Class Outline
=============


git / gitHub
============

In general, most of you seem to have got the basics down:

 - creating a new file
 - adding it to git
 - pushing it to your fork of the class repo
 - making a "pull request" on gitHub.

Any conceptual questions?

**Issue:**

Quite a few folks have changed or added files that they should not have:
 - The central readme in the studetns folder
 - and extra file here or there
 - etc....

git is very flexible, and does not lose data easily. However, it is **much** harder to undo things than it is to make changes.  So you will be happier if you take some extra care to not commit changes that you don't want. Some hints:

* Always do a ``git status`` before you commit -- make sure that the stuff you are going to commit is what you want!

  - note that if you do ``git commit`` it will only commit those files listed under "staged for commit". But if you do ``git commit -a`` (-a for all) then it will commit everything modified, i.e. "Changes not staged for commit:".

Note in the status report::

    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   notes_for_class/source/session02.rst

    ...

It even tells you want to do: use ``git add`` to stage particular files, or ``git checkout`` to revert a file back to its state as of the last commit. It doesn't mention ``git commit -a``, but that will commmit everyting that is "not staged for commit".

If you are careful before the commit stage, then you won't have to "roll back" changes very often.

But if you do:

https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/dev_environment/git_hints.html#backing-out-a-change

Let's play around with that a bit.


Exceptions
==========

Most of you seemed to do fine making the few key exceptions -- any questions?

**Note:**

We were not expecting you to catch the exceptions -- we're really starting at the bottom here, just making sure you get used to seeing Exceptions, and what they mean.

We'll get into Exception handling later.


Coding Bat
==========

Anyone stuck on any of them?

Anyone not like their solution?

Let's talk about it!


Lightning Talks
===============

Let's take a break and do some lightning talks...

Now some new stuff
==================

Grid Printer
------------

Get a start on your own, then we'll come together and finish it up.

:ref:`exercise_grid_printer`


Fizz Buzz
---------

Get a start on your own, then we'll come together and finish it up.

:ref:`exercise_grid_printer`

Recursion
---------

Get a start on your own, then we'll come together and finish it up.

(seeing a pattern here?)

:ref:`exercise_fibonacci`


