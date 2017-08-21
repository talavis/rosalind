#!/usr/bin/env python3

'''
Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
'''

import sys

import lib


def main(fasta_file):
    '''
    Calculate the kmer prevalence in a sequence from a FASTA file
    '''
    kmers = lib.gen_kmers('ACTG', 4)
    sequence = lib.parse_fasta(open(fasta_file).read())[1][0]
    results = count_kmers(sequence, kmers)
    print(' '.join([str(res) for res in results]))


def test_main(capsys):
    '''
    Test main()
    '''
    import tempfile
    filename_fasta = tempfile.mkstemp()[1]
    data = '''>Rosalind_6431
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'''
    with open(filename_fasta, 'w') as tmpf:
        tmpf.write(data)
    main(filename_fasta)
    out = capsys.readouterr()[0]
    expected = ('4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 ' +
                '3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 ' +
                '5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 ' +
                '1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 ' +
                '3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 ' +
                '1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 ' +
                '0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 ' +
                '3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 ' +
                '2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 ' +
                '0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 ' +
                '3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 ' +
                '1 0 1 1 3 0 2 1 2 2 0 2 1 1\n')
    assert out == expected


def count_kmers(sequence, kmers):
    '''
    Calculate the prevalence of kmers in a sequence
    '''
    kmer_counts = [0]*len(kmers)
    for i in range(len(sequence)):
        if i+4 > len(sequence):
            break
        kmer_counts[kmers.index(sequence[i:i+4])] += 1
    return kmer_counts


def test_count_kmers():
    '''
    Test count_kmers()
    '''
    expected = [4, 1, 4, 3, 0, 1, 1, 5, 1, 3, 1, 2, 2, 1, 2, 0, 1, 1, 3, 1, 2, 1,
                3, 1, 1, 1, 1, 2, 2, 5, 1, 3, 0, 2, 2, 1, 1, 1, 1, 3, 1, 0, 0, 1,
                5, 5, 1, 5, 0, 2, 0, 2, 1, 2, 1, 1, 1, 2, 0, 1, 0, 0, 1, 1, 3, 2,
                1, 0, 3, 2, 3, 0, 0, 2, 0, 8, 0, 0, 1, 0, 2, 1, 3, 0, 0, 0, 1, 4,
                3, 2, 1, 1, 3, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1, 1, 2, 3, 2, 1, 1, 0,
                1, 1, 3, 2, 1, 2, 6, 2, 1, 1, 1, 2, 3, 3, 3, 2, 3, 0, 3, 2, 1, 1,
                0, 0, 1, 4, 3, 0, 1, 5, 0, 2, 0, 1, 2, 1, 3, 0, 1, 2, 2, 1, 1, 0,
                3, 0, 0, 4, 5, 0, 3, 0, 2, 1, 1, 3, 0, 3, 2, 2, 1, 1, 0, 2, 1, 0,
                2, 2, 1, 2, 0, 2, 2, 5, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 3, 4,
                0, 2, 1, 1, 0, 1, 2, 2, 1, 1, 1, 5, 2, 0, 3, 2, 1, 1, 2, 2, 3, 0,
                3, 0, 1, 3, 1, 2, 3, 0, 2, 1, 2, 2, 1, 2, 3, 0, 1, 2, 3, 1, 1, 3,
                1, 0, 1, 1, 3, 0, 2, 1, 2, 2, 0, 2, 1, 1]
    sequence = ('CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG' +
                'CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT' +
                'TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA' +
                'AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG' +
                'GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA' +
                'CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA' +
                'CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG')
    assert count_kmers(sequence, lib.gen_kmers('ACTG', 4)) == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <FASTA file>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
