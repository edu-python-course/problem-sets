#################
Release 2023.04.2
#################

*********
Fixed #45
*********

Added docstrings to "settings" module. Updated `Enemy.__init__` documentation
to avoid misunderstanding of health attribute. Applied minor changes to game
overview section in "challenge" document.

**************************
Updated datasets functions
**************************

Included "swap keys-values" function. Added dict filtering functions for
the "students scores" challenge. Changed existing functions signatures.
Added more explanations for the "filter_by_values" function.
Added "flatten" list function.

*********************
Updated documentation
*********************

Fixed #24 with PR #44.

#################
Release 2023.04.1
#################

***************
Chess challenge
***************

Added a new challenge for the OOP block (by Vladyslav Ponomaryov).

- Implement class for each chess piece
- Implement function to filter pieces that can move to a specified place
  on a chess board

*****************
Convenience store
*****************

Added "Payment processors" description.

#################
Release 2023.01.2
#################

********************
Brick Wall Challenge
********************

Added brick wall challenge. Original problem set is published at:
https://leetcode.com/problems/brick-wall/

**************
Project Itself
**************

- Moved project dependencies to dev-section. Project has dev-deps only.
- From now pip package manage is supported as well.
- Removed legacy documentation section from README

###############
Release 2023-01
###############

***********************
Basic Python Challenges
***********************

Recursive Algorithms
====================

Added factorial and fibonacci number calculation functions.

Dynamic Programming
===================

Implemented the most common challenges (and solutions):

- fibonacci number getter function
- grid travel challenge
- target number against sequences of numbers checkers (can get, generate chunk)

Binary Search
=============

Added binary search algorithm challenge: find strings starting with prefix.

###############
Release 2022-11
###############

***********************
Basic Python Challenges
***********************

Primes
======

Implemented the most straight-forward approach to find primes within a given
range. Also added the implementation of "the Sieve of Eratosthenes" algorithm.
All functions are covered with tests.

Sequences
=========

Added the implementations of the most popular sequences tasks:

- palindrome checker
- palindrome substring finder
- balanced parentheses checker

All functions are covered with tests.

Sorting
=======

Added implementations of the most popular sorting algorithms:

- bubble sort
- selection sort
- insertion sort
- merge sort
- quick sort
- counting sort
- radix sort
- bucket sort
- heap sort
- shell sort

All functions are covered with tests.

**************************************
Object-Oriented Programming Challenges
**************************************

Convenience Store
=================

Added the basic "convenience store" challenge description and implementation.
Tests are included as well.

Warriors, Robbers and Wizards Game
==================================

Added the basic "wrw game" challenge description and implementation. This task
is considered to be the final exam for the OOP block. Tests are included as
well.
