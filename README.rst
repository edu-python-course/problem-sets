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

Code health check
-----------------

There are few dependencies installed to check the code health:

* pytest-cov
* mypy
* pylint

They are acting as stand-alone commands, available from your terminal with
poetry:

.. code-block::

    poetry run pytest
    poetry run mypy
    poetry run pylint src

Running tox
-----------

`tox`_ aims to automate and standardize testing in Python. It is a generic
virtualenv management and test command line tool you can use for:

* checking that your package installs correctly with different Python versions
  and interpreters
* running your tests in each of the environments, configuring your test tool of
  choice
* acting as a frontend to Continuous Integration servers, greatly reducing
  boilerplate and merging CI and shell-based testing.

.. _tox: https://tox.wiki

It's also include to the project's deps, run it with:

.. code-block::

    poetry run tox

Building documentation
----------------------

It's good to have well documented functions and classes. This project has no
purpose to generate documents, but since it is a part of a bigger one project
it's good to get docstrings here. Sphinx documentation generator is included
to dev-dependencies. You can use it to check the documentation builds:

.. code-block::

    poetry run sphinx-build -b html docs _build

An **index.html** file will be generated inside of **_build** directory. Check
it to review the documentation.

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
