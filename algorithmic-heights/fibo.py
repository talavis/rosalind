#!/usr/bin/env python3
'''
Given: A positive integer n≤25.

Return: The value of Fn.
'''

import sys


def fibo(number):
    '''
    Calculate the numberth Fibonacci number
    '''
    i = 0
    j = 1
    k = 1
    for i in range(2, number):
        i = j
        j = k
        k = i+j

    print(k)


def test_fibo(capsys):
    '''
    Test fibo()
    '''
    fibo(6)
    assert capsys.readouterr()[0] == '8\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <number>\n'.format(sys.argv[0]))
        sys.exit(1)

    fibo(int(sys.argv[1]))
