#!/usr/bin/env python3
'''
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
