#!/usr/bin/env python3
'''
Given: A positive integer n≤10000n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
'''

import sys


def find_longest_subseq(sequence):
    '''
    Find the longest increasing subsequence
    '''
    lg_subseqs = [0]*len(sequence)
    for i in range(len(sequence)):
        lg_subseqs[i] = (max([lg_subseqs[j] for j in range(i)
                              if lg_subseqs[j][-1] < sequence[i]] or [[]], key=len) + [sequence[i]])
    return max(lg_subseqs, key=len)


def test_find_longest_subseq():
    '''
    test find_longest_subseq
    '''
    test = [8, 2, 1, 6, 5, 7, 4, 3, 9]
    assert find_longest_subseq(test) == [2, 6, 7, 9]
    assert find_longest_subseq(test[::-1])[::-1] == [8, 6, 5, 4, 3]
    test = [5, 1, 4, 2, 3]
    assert find_longest_subseq(test) == [1, 2, 3]
    assert find_longest_subseq(test[::-1])[::-1] == [5, 4, 3]


def lgis(infile):
    '''
    Read data in infile
    Find longest increasing and decreasing subsequence
    '''
    data = open(infile).read()
    sequence = [int(val) for val in data.split('\n')[1].split(' ')]
    inc = find_longest_subseq(sequence)
    dec = find_longest_subseq(sequence[::-1])[::-1]
    print(' '.join([str(val) for val in inc]))
    print(' '.join([str(val) for val in dec]))


def test_lgis(capsys):
    '''
    Test lgis
    '''
    import tempfile

    data = '5\n5 1 4 2 3'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)
    lgis(filename)
    out = capsys.readouterr()[0]
    assert out == '1 2 3\n5 4 3\n'

    data = '9\n8 2 1 6 5 7 4 3 9'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)

    lgis(filename)
    out = capsys.readouterr()[0]
    assert out == '2 6 7 9\n8 6 5 4 3\n'

    data = '9\n8 2 1 6 5 7 4 3 15'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)

    lgis(filename)
    out = capsys.readouterr()[0]
    assert out == '2 6 7 15\n8 6 5 4 3\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <datafile>\n'.format(sys.argv[0]))
        sys.exit(1)
    lgis(sys.argv[1])
