#!/usr/bin/env python3
'''
For DNA strings s1 and s2 having the same length, their 
transition/transversion ratio R(s1,s2) is the ratio 
of the total number of transitions to the total number of 
transversions, where symbol substitutions are inferred from 
mismatched corresponding symbols as when calculating 
Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
'''

import sys


def calculate_tstv_ratio(seq1, seq2):
    '''
    Calculate the transition/transversion ratio of two sequences
    with identical length
    '''
    ts = 0
    tv = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            merged = seq1[i] + seq2[i]
            if merged in 'AGGA' or merged in 'CTTC':
                ts += 1
            else:
                tv += 1
    return round(ts/tv, 11)


def test_calculate_tstv_ratio():
    '''
    Test calculate_tstv_ratio()
    '''
    seq1 = ('GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA' +
            'AGTACGGGCATCAACCCAGTT')
    seq2 = ('TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC' +
            'GGTACGAGTGTTCCTTTGGGT')

    assert calculate_tstv_ratio(seq1, seq2) == 1.21428571429


def main(data):
    '''
    Extract sequences and calculate the ratio
    '''
    heads, seqs = read_fasta(data)
    ratio = calculate_tstv_ratio(seqs[0], seqs[1])
    print('{:.12}'.format(ratio))
    return 0


def test_main(capsys):
    '''
    Test main()
    '''
    data = '''
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
'''
    main(data)
    assert capsys.readouterr()[0] == '1.21428571429\n'


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


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <FASTA file>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(open(sys.argv[1]).read())

