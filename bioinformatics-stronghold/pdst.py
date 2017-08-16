#!/usr/bin/env python3
'''
For two strings s1 and s2 of equal length, the p-distance between
them, denoted dp(s1,s2), is the proportion of corresponding symbols
that differ between s1 and s2.

For a general distance function dd on nn taxa s1,s2,…,sn (taxa are
often represented by genetic strings), we may encode the distances
between pairs of taxa via a distance matrix DD in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length
(at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given
strings. As always, note that your answer is allowed an absolute
error of 0.001.
'''

import sys
import lib


def calc_distance(seq1, seq2):
    '''
    Calculate the distance between two sequences with the same length

    Return: number of differences/total sequence length
    '''
    diffs = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            diffs += 1
    return diffs/len(seq1)


def test_calc_distance():
    '''
    Test calc_distance()
    '''
    seqs = ('TTTCCATTTA',
            'GATTCATTTC',
            'TTTCCATTTT',
            'GTTCCATTTA')
    assert calc_distance(seqs[0], seqs[1]) == 0.40000
    assert calc_distance(seqs[0], seqs[2]) == 0.10000
    assert calc_distance(seqs[0], seqs[3]) == 0.10000
    assert calc_distance(seqs[1], seqs[1]) == 0.00000
    assert calc_distance(seqs[1], seqs[2]) == 0.40000
    assert calc_distance(seqs[2], seqs[3]) == 0.20000


def gen_dist_matrix(seqs):
    '''
    Generate a matrix of the distances between the sequences in
    the provided list.
    '''
    matrix = [[0]*len(seqs) for item in range(len(seqs))]
    for i in range(len(seqs)):
        matrix[i][i] = 0.00000
        for j in range(i, len(seqs)):
            dist = calc_distance(seqs[i], seqs[j])
            matrix[i][j] = dist
            matrix[j][i] = dist

    return matrix


def test_gen_dist_matrix():
    '''
    Test gen_dist_matrix()
    '''
    seqs = ('TTTCCATTTA',
            'GATTCATTTC',
            'TTTCCATTTT',
            'GTTCCATTTA')
    expected = [[0.00000, 0.40000, 0.10000, 0.10000],
                [0.40000, 0.00000, 0.40000, 0.30000],
                [0.10000, 0.40000, 0.00000, 0.20000],
                [0.10000, 0.30000, 0.20000, 0.00000]]

    assert gen_dist_matrix(seqs) == expected


def pdst(filename):
    '''
    Read data and generate a distance matrix
    '''
    seqs = lib.read_fasta(filename)[1]
    matrix = gen_dist_matrix(seqs)
    for line in matrix:
        print(' '.join(['{:.5f}'.format(i) for i in line]))


def test_pdst(capsys):
    '''
    Test pdst()
    '''
    import tempfile

    data = ('>Rosalind_9499\nTTTCCATTTA\n' +
            '>Rosalind_0942\nGATTCATTTC\n' +
            '>Rosalind_6568\nTTTCCATTTT\n' +
            '>Rosalind_1833\nGTTCCATTTA\n')
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpf:
        tmpf.write(data)
    pdst(filename)
    out = capsys.readouterr()[0]
    expected = ('0.00000 0.40000 0.10000 0.10000\n' +
                '0.40000 0.00000 0.40000 0.30000\n' +
                '0.10000 0.40000 0.00000 0.20000\n' +
                '0.10000 0.30000 0.20000 0.00000\n')
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <FASTA file>\n'.format(sys.argv[0]))
        sys.exit(1)
    pdst(sys.argv[1])
