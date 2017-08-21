#!/usr/bin/env python3
'''
A signed permutation of length nn is some ordering of the positive
integers {1,2,…,n}{1,2,…,n} in which each integer is then provided
with either a positive or negative sign (for the sake of simplicity,
we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed
permutation of length 5.

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed
by a list of all such permutations (you may list the signed
permutations in any order).
'''

import itertools
import sys


def gen_permut(number):
    '''
    Generate all signed permutations for number
    '''
    nums = [num for num in range(-number, number+1) if num != 0]
    perms = [perm for perm in list(itertools.permutations(nums, number))
             if len(set([abs(val) for val in perm])) == number]

    return sorted(perms)


def test_gen_permut():
    '''
    Test gen_permut()
    '''
    expected = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    assert gen_permut(2) == expected


def sign(number):
    '''
    Generate all signed permutations of length number
    '''
    permuts = gen_permut(number)
    print(len(permuts))
    for permut in sorted(permuts):
        print(' '.join([str(num) for num in permut]))


def test_sign(capsys):
    '''
    Test sign()
    '''
    num = 2
    expected = '8\n-2 -1\n-2 1\n-1 -2\n-1 2\n1 -2\n1 2\n2 -1\n2 1\n'
    sign(num)
    out = capsys.readouterr()[0]
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <number>\n'.format(sys.argv[0]))
        sys.exit(1)

    sign(int(sys.argv[1]))
