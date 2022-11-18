###############################################################################
                     PYTHON TRAINING COURSE: PROBLEM SETS
###############################################################################

This repository contains various problem sets (aka tasks or challenges) for
the `Python training course`_. These challenges will help you to improve your
skills in some basic Python topics. Many tasks are collected from authors'
interview experience.

.. _Python training course:
    https://github.com/edu-python-course/edu-python-course.github.io

Getting started
===============

It's recommended to use `poetry`_ with this project. Otherwise you are to do
some additional work while installing dependencies and configuring internal
packages.

.. _poetry: https://python-poetry.org

Once you've cloned the repository to your local machine install dependencies:

.. code-block::

    poetry install

This will also install internal packages for future tests.

Project structure
=================

::

    /problem-sets
    |-- docs/
    |-- src/
    |-- tests/

There are two major directories: **src** and **tests**. Any useful code should
be included to the source (src). Test cases for functions, classes etc. should
lie inside of tests directory. It's ok to created nested packages within these
directories if needed.

The **docs** directory contains optional config for the documentation generator
and is used for documentation builds check only. The docs for this project are
to be generated within the main project and another configuration will be used.
