#!/usr/bin/env python3
'''
Given: A DNA string s of length at most 100 bp and an array A
containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k]
represents the common logarithm of the probability that a random
string constructed with the GC-content found in A[k] will match
s exactly.
'''

import math
import sys


def calc_probability(sequence, gcprob):
    '''
    Calculate the probability of the given sequence based on the
    expected gc content
    '''
    probs = {'G': gcprob/2, 'C': gcprob/2,
             'A': (1-gcprob)/2, 'T': (1-gcprob)/2}
    seqprob = 1.0
    for pos in sequence:
        seqprob *= probs[pos]

    return round(math.log10(seqprob), 3)


def test_calc_probability():
    '''
    Test calc_probability()
    '''
    seq = 'ACGATACAA'
    gcs = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]
    expected = [-5.737, -5.217, -5.263, -5.360, -5.958, -6.628, -7.009]
    for i in range(len(gcs)):
        assert calc_probability(seq, gcs[i]) == expected[i]


def prob(filename):
    '''
    Read data and calculate the probability of the given sequence
    based on the expected gc content
    '''
    data = open(filename).read().split('\n')
    seq = data[0]
    gcprobs = [float(dat) for dat in data[1].split(' ')]
    res = list()
    for gcprob in gcprobs:
        res.append('{:.3f}'.format(calc_probability(seq, gcprob)))

    print(' '.join(res))


def test_prob(capsys):
    '''
    Test prob()
    '''
    import tempfile
    filename = tempfile.mkstemp()[1]
    data = 'ACGATACAA\n0.129 0.287 0.423 0.476 0.641 0.742 0.783\n'
    with open(filename, 'w') as tmpf:
        tmpf.write(data)

    prob(filename)
    out = capsys.readouterr()[0]
    expected = '-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009\n'
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <data file>\n'.format(sys.argv[0]))
        sys.exit(1)

    prob(sys.argv[1])
