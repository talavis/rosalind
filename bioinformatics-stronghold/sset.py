#!/usr/bin/env python3
'''
A set is the mathematical term for a loose collection of objects,
called elements. Examples of sets include
{the moon, the sun, Wilford Brimley} and R, the set containing all
real numbers. We even have the empty set, represented by ∅ or {},
which contains no elements at all. Two sets are equal when they
contain the same elements. In other words, in contrast to
permutations, the ordering of the elements of a set is unimportant
(e.g., {the moon, the sun, Wilford Brimley} is equivalent to
{Wilford Brimley, the moon, the sun}). Sets are not allowed
to contain duplicate elements, so that
{Wilford Brimley,the sun, the sun} is not a set. We have already
used sets of 2 elements to represent edges from a graph.

A set A is a subset of B if every element of A is also an element of
B, and we write A⊆B. For example,
{the sun, the moon}⊆{the sun, the moon, Wilford Brimley}, and ∅ is a
subset of every set (including itself!).

As illustrated in the biological introduction, we can use subsets to
represent the collection of taxa possessing a character.
However, the number of applications is endless; for example, an
event in probability can now be defined as a subset of the set
containing all possible outcomes.

Our first question is to count the total number of possible subsets
of a given set.

Given: A positive integer nn (n≤1000).

Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
'''

import sys
import math


def no_subsets(number):
    '''
    Calculate the number of subsets for a set of <number> items
    Finding all subsets is the same as calculating the sum of all
    possible combinations
    '''
    total = 0
    for i in range(number+1):
        print('{}/({}-{})'.format(number, number, i))
        fact_n = math.factorial(number)
        fact_i = math.factorial(i)
        fact_n_i = math.factorial(number-i)
        permut = fact_n/(fact_i*fact_n_i)
        total += permut
    return total


def test_no_subsets():
    '''
    Test no_subsets()
    '''
    assert no_subsets(3) == 8


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <number>\n'.format(sys.argv[0]))
        sys.exit(1)
    print(no_subsets(int(sys.argv[1])) % 1000000)
