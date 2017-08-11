#!/usr/bin/env python3

'''
Given: A positive integer n<=10000 followed by a permutation p of length n.

Return: A longest increasing subsequence of p, followed by a longest decreasing subsequence of p.
'''

import sys

def find_dec(numbers):
    '''
    Find the longest decreasing subsequence

    >>> find_dec((5, 1, 4, 2, 3))
    (4, 2, 3)
    '''
    longest = []
    i = 0
    total = len(numbers)
    while i + len(longest) < total:
    return longest


def test_find_dec():
    '''
    Test find_dec()
    '''
    numbers = (5, 1, 4, 2, 3)
    assert find_dec(numbers) == (4, 2, 3)
    numbers = (8, 2, 1, 6, 5, 7, 4, 3, 9)
    assert find_dec(numbers) == (8, 6, 5, 4, 3)


def find_inc(numbers):
    '''
    Find the longest increasing subsequence
    '''
    pass


def test_find_inc():
    '''
    Test find_inc()
    '''
    numbers = (5, 1, 4, 2, 3)
    assert find_inc(numbers) == (1, 2, 3)
    numbers = (8, 2, 1, 6, 5, 7, 4, 3, 9)
    assert find_inc(numbers) == (2, 6, 7, 9)
