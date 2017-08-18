#!/usr/bin/env python3                                                                                                                        

'''Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)'''

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

# calculate longest possible motif (shortest seq length)
shortest = len(seqs[0]) 
for i in range(1,len(seqs)) :
    if len(seqs[i]) < shortest :
        shortest = len(seqs[i])

# look for common motifs, the bruteforce way
for length in range(shortest,0,-1) :
    for s in range(len(seqs)) :
        i = 0
        while i + length < len(seqs[s]) :
#            print('testing: ', seqs[s][i:i+length+1])
            hit = True
            for seq in seqs :
                if seqs[s][i:i+length+1] not in seq :
                    hit = False
                    break
#                print(seqs[s][i:i+length+1], 'is in ', seq)
            if hit :
                print(seqs[s][i:i+length+1])
                sys.exit()
            i += 1
#        print('test next frame')
#    print('test next length')
    
