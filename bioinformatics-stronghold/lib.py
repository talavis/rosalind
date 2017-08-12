#!/usr/bin/env python3

import sys


if __name__ == '__main__':
    sys.stderr.write('This file is not intended for stand-alone use')
    sys.exit(1)

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


def read_fasta(data):
    '''
    Read data in the FASTA format
    '''
    heads = list()
    seqs = list()
    
    for line in data.split('\n'):
        if len(line.strip()) == 0:
            continue
        if line[0] == '>':
            seqs.append('')
            heads.append(line[1:].strip())
        else:
            seqs[-1] += line.strip()
    return heads, seqs
    
def test_read_fasta():
    '''
    Test read_fasta()
    '''
    data = '''
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
'''
    expected = (('Rosalind_0209', 'Rosalind_0220'),
                ('GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTT' +
                 'GTAGTTATTGGAAGTACGGGCATCAACCCAGTT',
                 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTG' +
                 'CTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'))
