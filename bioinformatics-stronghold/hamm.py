#!/usr/bin/env python3

'''Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t). (the number of mutations)'''

import sys

if len(sys.argv) != 3 :
    sys.stderr.write('Usage: {0} <DNA sequence 1> <DNA sequence 2>\n'.format(sys.argv[0]))
    sys.exit()

seq1 = sys.argv[1]
seq2 = sys.argv[2]

muts = 0
for i in range(len(seq1)) :
    if seq1[i] != seq2[i] :
        muts += 1

print(muts)

