#!/usr/bin/env python3

'''
Given: A positive integer n<=10000 followed by a permutation p of length n.

Return: A longest increasing subsequence of p, followed by a longest decreasing subsequence of p.
'''

import sys

def find_dec(numbers):
    '''
    Find the longest decreasing subsequence
    '''
    longest = []
    sorted_num = sorted(numbers)
    for i in range(len(sorted_num)):
        current = [numbers[i]]
        for j in range(i+1, len(numbers)):
            print(i,j,current)
            if numbers[j] < current[-1]:
                current.append(numbers[j])
        if len(current) > len(longest):
            longest = numbers[i:j]
    return longest


def test_find_dec():
    '''
    Test find_dec()
    '''
    numbers = (5, 1, 4, 2, 3)
    assert find_dec(numbers) == (4, 2, 3)


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

    
