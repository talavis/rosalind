#!/usr/bin/env python3
'''
Read and transcribe a DNA sequence
'''

import sys


def main(filename):
    '''
    Read and transcribe a DNA sequence
    '''
    seq = read_seq(filename)
    print(transcribe(seq))


def read_seq(filename):
    '''
    Read a DNA sequence from a file
    '''
    with open(filename) as infile:
        seq = ''
        for line in infile:
            if len(line.strip()) > 0:
                seq += line.strip()

    return seq


def transcribe(sequence):
    '''
    Transcribe a DNA sequence
    '''
    return sequence.replace('T', 'U')


def test_transcribe():
    '''
    Test transcribe()
    '''
    inseq = 'GATGGAACTTGACTACGTAAATT'
    expected = 'GAUGGAACUUGACUACGUAAAUU'
    assert transcribe(inseq) == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <DNA file>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
