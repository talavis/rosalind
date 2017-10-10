#!/usr/bin/env python3
'''
Rosalind problem scsp
'''

import sys

import lcsq


def find_shortest_superseq(seq1, seq2):
    '''
    Find the shortest supersequence of the two sequences
    Start by finding longest shared subsequence, then add the rest
    '''
    subseq = lcsq.find_longest_subseq(seq1, seq2)

    pos1 = 0
    pos2 = 0
    possub = 0
    possup = 0

    lenseq1 = len(seq1)
    lenseq2 = len(seq2)
    lensub = len(subseq)
    superseq = [''] * (lensub+lenseq1+lenseq2-2*lensub)
    while possub < lensub:
        if pos1 < lenseq1 and seq1[pos1] != subseq[possub]:
            superseq[possup] = seq1[pos1]
            pos1 += 1
        elif pos2 < lenseq2 and seq2[pos2] != subseq[possub]:
            superseq[possup] = seq2[pos2]
            pos2 += 1
        else:
            superseq[possup] = subseq[possub]
            possub += 1
            pos1 += 1
            pos2 += 1
        possup += 1

    while pos1 < lenseq1:
        superseq[possup] = seq1[pos1]
        possup += 1
        pos1 += 1
    while pos2 < lenseq2:
        superseq[possup] = seq2[pos2]
        possup += 1
        pos2 += 1

    return ''.join(superseq)


def test_find_shortest_superseq():
    '''
    Test find_shortest_superseq()
    '''
    seqs = ['ATCTGAT', 'TGCATA']
    assert find_shortest_superseq(*seqs) == 'ATGCTGATA'


def main(filename):
    '''
    Read sequences, find and print supersequence
    '''
    with open(filename) as infile:
        sequences = infile.read().split('\n')
    superseq = find_shortest_superseq(sequences[0], sequences[1])
    print(superseq)


def test_main(capsys):
    '''
    Test main()
    '''
    import tempfile
    data = 'ATCTGAT\nTGCATA\n'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)
    main(filename)
    expected = ('ATGCTGATA\n')
    out = capsys.readouterr()[0]
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <sequence file>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
