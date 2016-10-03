#!/usr/bin/env python3 

'''Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.'''

import sys

if len(sys.argv) != 3 :
    sys.stderr.write('Usage: {0} <DNA sequence> <Motif>\n'.format(sys.argv[0]))
    sys.exit()

seq = sys.argv[1]
motif = sys.argv[2]

hits = seq.count(motif)

pos = 0
hits = ''

while True :
    try : 
        pos = seq.index(motif, pos+1)
    except ValueError :
        break
    hits += str(pos+1) + ' '
print(hits)
