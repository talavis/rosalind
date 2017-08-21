#!/usr/bin/env python3
'''
Given: Two DNA strings s and t (each having length at most 1 kbp) in
FASTA format.

Return: A longest common subsequence of s and t. (If more than one
solution exists, you may return any one.)
'''

import sys

import lib


def find_longest_subseq(seq1, seq2):
    '''
    Find the longest common subsequence
    '''
    # use an adaption of dynamic programming
    # matrix - match = +1
    matrix = [[0]*(len(seq2)+1) for x in range(len(seq1)+1)]
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            matrix[i][j] = max(matrix[i][j-1],
                               matrix[i-1][j],
                               matrix[i-1][j-1] +
                               (seq1[i-1] == seq2[j-1]))

    # find best score
    best = max([max(line) for line in matrix])
    i, j = [(i, val.index(best)) for i, val in
            enumerate(matrix) if max(val) == best][-1]

    # traceback
    substr_rev = ''
    while i > 0 and j > 0:
        if matrix[i-1][j] == matrix[i][j]:
            i -= 1
        elif matrix[i][j-1] == matrix[i][j]:
            j -= 1
        elif matrix[i-1][j-1] == matrix[i][j]-1:
            i -= 1
            j -= 1
            substr_rev += seq1[i]
        else:
            sys.stderr.write('Error')

    return substr_rev[::-1]


def test_find_longest_subseq():
    '''
    Test find_longest_subseq()
    '''
    expected = ('AACTGG', 'ACCTTG', 'AACTTG')
    seqs = ('AACCTTGG', 'ACACTGTGA')
    assert find_longest_subseq(*seqs) in expected


def lcsq(filename):
    '''
    Read a FASTA file and calculate the longest common subsequence
    '''
    seqs = lib.read_fasta(filename)[1]
    print(find_longest_subseq(seqs[0], seqs[1]))


def test_lcsq(capsys):
    '''
    Test lcsq()
    '''
    import tempfile

    data = '>Rosalind_23\nAACCTTGG\n>Rosalind_64\nACACTGTGA\n'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)

    expected = ('AACTGG\n', 'ACCTTG\n', 'AACTTG\n')
    lcsq(filename)
    out = capsys.readouterr()[0]
    assert out in expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <FASTA file>\n'.format(sys.argv[0]))
        sys.exit(1)

    lcsq(sys.argv[1])
