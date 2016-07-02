#!/usr/bin/env python3

'''
Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string ss of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
20 12 17 21
'''

import sys

def count_dna(seq) :
    return (seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T'))

def test_count_dna() :
    count_dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC') == (20, 12, 17, 21)

if __name__ == '__main__' :
    seq = open(sys.argv[1]).read()
    print('{} {} {} {}'.format(*count_dna(seq)))
