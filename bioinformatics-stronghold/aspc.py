#!/usr/bin/env python3
'''
Given: Positive integers n and m with 0≤m≤n≤2000.

Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n,
modulo 1,000,000. In shorthand, ∑nk=m(nk).
'''

from math import factorial as fact
import sys


def no_combinations(num, chosen):
    '''
    Calculate the number of combinations
    '''
    return fact(num)//(fact(chosen)*fact(num-chosen))


def test_no_combinations():
    '''
    Test no_combinations()
    '''
    assert no_combinations(4, 2) == 6


def aspc(filename):
    '''
    Read the numbers and calculate the number of combinations
    '''
    n_num, m_num = [int(num) for num in
                    open(filename).read().split()[:2]]
    combsum = 0
    for i in range(m_num, n_num+1):
        combsum += no_combinations(n_num, i)

    print(int(combsum) % 1000000)


def test_aspc(capsys):
    '''
    Test aspc()
    '''
    import tempfile

    filename = tempfile.mkstemp()[1]
    data = '6 3\n'
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)
    aspc(filename)
    out = capsys.readouterr()[0]
    assert out == '42\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <data file>\n'.format(sys.argv[0]))
        sys.exit(1)

    aspc(sys.argv[1])
