#!/usr/bin/env python3

'''Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

This implementation requires |sort|uniq at the the end to get acceptable output.'''

import sys

complement_dna = {'T': 'A', 'A':'T', 'G': 'C', 'C':'G', 'X': 'X'}
complement_rna = {'U': 'A', 'A':'U', 'G': 'C', 'C':'G', 'X': 'X'}

def complementary(sequence, seqtype = 'DNA') :
    '''Generate the complementary strand of a DNA or RNA sequence'''

    if seqtype == 'DNA' :
        comp = complement_dna
    elif seqtype == 'RNA' :
        comp = complement_rna
    else :
        sys.stderr.write('E: complementary: incorrect sequencetype')
        return ''

    new_seq = ''
    for i in range(len(sequence)) :
        new_seq += comp[sequence[i]]

    return new_seq[::-1]

def find_orfs(sequence, seqtype = 'DNA') :
    '''Returns a list of start and end positions, and read frames, for orfs in the sequence.
    Positions in Python syntax (pos 1 = 0). 
    The end position will be the first nucleotide in the stop codon.'''
    if seqtype == 'DNA' :
        start = 'ATG'
        stop =  ('TAA', 'TAG', 'TGA')
    elif seqtype == 'RNA' :
        start = 'AUG'
        stop =  ('UAA', 'UAG', 'UGA')
    else :
        sys.stderr.write('E: find_orfs: incorrect sequencetype')
        return tuple()
    active = False
    orfs = list()
    for i in range(len(sequence)) :
        if sequence[i:i+3] == start :
            for j in range(i+3, len(sequence), 3) :
                if sequence[j:j+3] in stop :
                    orfs.append((i, j, i % 3))
                    break
    return orfs

def read_fasta(filename) :
    # read sequences
    seqs = list()
    heads = list()
    for line in open(filename) :
        if line[0] == '>' :
            seqs.append('')
            heads.append(line[1:].strip())
        else :
            seqs[-1] += line.strip()
    return seqs, heads

codons_dna = {'TTT':'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
              'TCT':'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
              'TAT':'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
              'TGT':'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
              
              'CTT':'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
              'CCT':'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
              'CAT':'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
              'CGT':'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
              
              'ATT':'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
              'ACT':'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
              'AAT':'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
              'AGT':'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
              
              'GTT':'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
              'GCT':'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
              'GAT':'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
              'GGT':'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

codons_rna = {'UUU':'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
              'UCU':'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
              'UAU':'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
              'UGU':'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
              
              'CUU':'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
              'CCU':'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
              'CAU':'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
              'CGU':'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
              
              'AUU':'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
              'ACU':'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
              'AAU':'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
              'AGU':'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
              
              'GUU':'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
              'GCU':'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
              'GAU':'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
              'GGU':'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

def translate(sequence, seqtype = 'DNA') :
    if seqtype == 'DNA' :
        codon = codons_dna
    elif seqtype == 'RNA' :
        codon = codons_rna
    else :
        sys.stderr.write('E: translate: incorrect sequencetype')
        return ''
    
    protein = ''
    for i in range(0, len(sequence), 3) :
        protein += codon[sequence[i:i+3]]
    
    return protein

if len(sys.argv) != 2 :
    sys.stderr.write('Usage: {0} <FASTA DNA sequence>\n'.format(sys.argv[0]))
    sys.exit()

seqs, heads = read_fasta(sys.argv[1])

orfs = find_orfs(seqs[0])

for i in range(len(orfs)) :
    print(translate(seqs[0][orfs[i][0]:orfs[i][1]]))

comp = complementary(seqs[0])

orfs = find_orfs(comp)


for i in range(len(orfs)) :
    print(translate(comp[orfs[i][0]:orfs[i][1]]))
