#!/usr/bin/env python3                                                                                                                         
'''Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.'''

import sys

if len(sys.argv) not in (2,3) :
    sys.stderr.write('Usage: {0} <DNA FASTA file> [O_k = 3]\n'.format(sys.argv[0]))
    sys.exit()

if len(sys.argv) == 3 :
    k = int(sys.argv[2])
else :
    k = 3
# read sequences
seqs = list()
heads = list()
for line in open(sys.argv[1]) :
    if line[0] == '>' :
        seqs.append('')
        heads.append(line[1:].strip())
    else :
        seqs[-1] += line.strip()

# create prefix and suffix list
prefs = list()
suffs = list()
for s in seqs :
    prefs.append(s[:k])
    suffs.append(s[-k:])

matches = list()
for p in range(len(prefs)) :
    matches.append(list())
    pos = 0
    while True :
        try :
            pos = suffs.index(prefs[p], pos)
        except ValueError :
            break
        if pos != p :
            matches[-1].append(pos)
        pos += 1

for m in range(len(matches)) :
    for p2 in range(len(matches[m])) :
        print(heads[matches[m][p2]], heads[m])
        
                
