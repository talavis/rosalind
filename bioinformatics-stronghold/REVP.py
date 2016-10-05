#!/usr/bin/env python3

'''
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''

import sys


COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def check_palindromes(sequence):
    palindromes = list()
    complement = make_complement(sequence)
    for i in range(len(sequence)):
        pali_length = 0
        for j in range(i+4, i+13):
            if j > len(sequence):
                break
            if sequence[i:j] == complement[i:j][::-1]:
                pali_length = j-i
        if pali_length >= 4:
            palindromes.append([i+1, pali_length])
    return palindromes



def test_check_palindromes():
    seq = 'TCAATGCATGCGGGTCTATATGCAT'
    expected_out = [[4, 6], [5, 4], [6, 6], [7, 4], [17, 4], [18, 4], [20, 6], [21, 4]]
    assert check_palindromes(seq) == expected_out

def make_complement(sequence):
    complement = ''
    for c in sequence:
        complement += COMPLEMENT[c]
    return complement


def test_make_complement():
    assert make_complement('ACGT') == 'TGCA'
    assert make_complement('TTAACCGG') == 'AATTGGCC'


def read_fasta(filename):
    '''Read a FASTA file and return the headers and sequences as lists'''
    with open(filename) as infile:
        seqs = list()
        headers = list()
        for line in infile:
            if line[0] == '>':
                headers.append(line[1:].strip())
                seqs.append('')
            elif len(line.strip()) > 0:
                seqs[-1] += line.strip()

    return (headers, seqs)

        
if __name__ == '__main__':
    headers,seqs = read_fasta(sys.argv[1])
    palis = check_palindromes(seqs[0])
    for p in palis:
        print(p[0], p[1])
