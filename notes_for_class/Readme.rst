Notes for Class
===============

This dir holds notes for the classroom sessions.

There is also a page for the lightning talks schedule.

These notes are in "ReStructured Text", and published by the Sphinx documentation system here:

https://uwpce-pythoncert-classrepos.github.io/SP_2019_210A_classroom/index.html

About Sphinx
------------

Sphinx and RST were originally developed to help document the Python language and standard library. It has grown to be the most widely used system for publishing documentation of Python packages, and is also used for many other documentation projects.

Sphinx allows you to write your documents in simple, human readable text files, and then publish is as html, PDF, eBook formats, etc.

It's a very useful tool to learn if you are going to be doing Python development.

Building These Docs
-------------------

These docs are quite readable in text form, but if you want them to look nice, or want to test any additions you may make, you can build them on your own machine with Sphinx:

http://www.sphinx-doc.org/en/master/

Sphinx is written in Python, so it can be installed as a python package, and the be ready to run::

  python -m pip install -r requirements.txt

will install Sphinx and a couple other packages.

Then you can build the docs with::

  make html

They will be put into the ``build/html`` dir, and you can read them by opening::

  build/html/index.html

in your browser.

Simple as that :-)





