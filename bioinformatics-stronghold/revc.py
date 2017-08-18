#!/usr/bin/env python3
'''reverse complement of a DNA sequence'''

import sys

if len(sys.argv) != 2 :
    sys.stderr.write('Usage: {0} sequence\n'.format(sys.argv[0]))
    sys.exit()

output = ''

complement = { 'A': 'T', 'T':'A', 'C': 'G', 'G':'C' }

for n in sys.argv[1] :
    output += complement[n]

print(output[::-1])
