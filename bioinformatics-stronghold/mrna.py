#!/usr/bin/env python3

'''
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
'''

import sys

REVERSE_CODON = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
                 'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
                 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6,
                 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2}

def calculate(sequence):
    total = 3 # stop codon
    for c in sequence:
        total *= REVERSE_CODON[c]
    return total


def test_calculate():
    assert calculate('MA') == 12

if __name__ == '__main__':
    print(calculate(sys.argv[1]) % 10**6)
