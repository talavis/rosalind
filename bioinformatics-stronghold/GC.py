#!/usr/bin/env python3

'''Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all'''

import sys

def calc_gc(seq) :
    return (seq.count('G') + seq.count('C')) / len(seq)

if len(sys.argv) != 2 :
    sys.stderr.write('Usage: {0} <FASTA DNA file>\n'.format(sys.argv[0]))
    sys.exit()

seqs = list()
heads = list()
for line in open(sys.argv[1]) :
    if line[0] == '>' :
        seqs.append('')
        heads.append(line[1:].strip())
    else :
        seqs[-1] += line.strip()

highest = 0
highest_header = ''
for i in range(len(seqs)) :
    gc = calc_gc(seqs[i])
    if  gc > highest :
        highest = gc
        highest_header = heads[i]
print(highest_header)
print(highest*100)
