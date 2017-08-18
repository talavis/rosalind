#!/usr/bin/env python3
'''Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.'''

import sys

if len(sys.argv) not in [2,3] :
    sys.stderr.write('Usage: {0} <filename> [readingframe (0-2)]\n'.format(sys.argv[0]))
    sys.exit()

codons = {'UUU':'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
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

last = ''
read_frame = 0
if len(sys.argv) == 3 :
    read_frame = int(sys.argv[2]) % 3
first = True
for line in open(sys.argv[1]) :
    if line[0] == '>' and first :
        continue
    if line[0] == '>' :
        sys.stdout.write('\n')
        last = ''
        continue
    query = last + line[:-1]
    if first :
        query = query[read_frame:]
        first = False

    for i in range(0, len(query)-2, 3) :
        if 'N' in query[i:i+3] :
            sys.stdout.write('X')
        else :
            sys.stdout.write(codons[query[i:i+3]])
    
    trailing = len(query) % 3
    if trailing != 0 :
        last = query[-trailing:]
    else :
        last = ''

sys.stdout.write('\n')
