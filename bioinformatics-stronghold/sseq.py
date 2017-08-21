#!/usr/bin/env python3
'''
Given: Two DNA strings s and t (each of length at most 1 kbp) in
FASTA format.

Return: One collection of indices of s in which the symbols of t
appear as a subsequence of s. If multiple solutions exist, you may
return any one.
'''
import sys

import lib


def find_subseq(seq, subseq):
    '''
    Find positions in seq that together match subseq
    First position = 1
    '''
    matches = []
    pos = 0
    for nuc in subseq:
        matches.append(seq.index(nuc, pos)+1)
        pos = matches[-1]

    return matches


def test_find_subseq():
    '''
    Test find_subseq
    '''
    seq = 'ACGTACGTGACG'
    subseq = 'GTA'
    expected = [3, 4, 5]
    assert find_subseq(seq, subseq) == expected


def sseq(filename):
    '''
    Read a FASTA file and identify the positions of the subsequence
    '''
    seqs = lib.read_fasta(filename)[1]
    positions = find_subseq(seqs[0], seqs[1])
    print(' '.join([str(pos) for pos in positions]))


def test_sseq(capsys):
    '''
    Test sseq()
    '''
    import tempfile

    data = '>Rosalind_14\nACGTACGTGACG\n>Rosalind_18\nGTA'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)
    sseq(filename)
    out = capsys.readouterr()[0]
    expected = '3 4 5\n'
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <FASTA file>\n'.format(sys.argv[0]))
        sys.exit(1)

    sseq(sys.argv[1])
