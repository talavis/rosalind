#!/usr/bin/env python3
'''
Given: A collection of at most 10 symbols defining an ordered alphabet, and
a positive integer nn (n≤10n≤10).

Return: All strings of length nn that can be formed from the alphabet,
ordered lexicographically (use the standard order of symbols in the English alphabet).
'''

import sys


def gen_kmers(letters, length, current=0):
    '''
    Generate a alphabetical list of kmers of the wanted length using the given letters
    '''
    if current >= length:
        return ['']
    kmers = list()
    for letter in letters:
        kmers += [letter+kmer for kmer in gen_kmers(letters, length, current+1)]

    return sorted(kmers)


def test_gen_kmers():
    '''
    Test gen_kmers
    '''
    expected = ['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT',
                'GA', 'GC', 'GG', 'GT', 'TA', 'TC', 'TG', 'TT']
    assert gen_kmers('ACGT', 2) == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {0} <datafile>\n'.format(sys.argv[0]))
        sys.exit(1)
    DATA = open(sys.argv[1]).read()
    LETTERS = ''.join(DATA.split('\n')[0].replace(' ', ''))
    LENGTH = int(DATA.split('\n')[1])
    print('\n'.join(gen_kmers(LETTERS, LENGTH)))
