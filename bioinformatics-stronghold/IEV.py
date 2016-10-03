#!/usr/bin/env python3

'''Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.'''

import sys

if len(sys.argv) != 7 :
    sys.stderr.write('Usage: <#AA-AA> <#AA-Aa> <#AA-aa> <#Aa-Aa> <#Aa-aa> <#aa-aa>\n'.format(sys.argv[0]))
    sys.exit()

gt = list()
for i in range(6) :
    gt.append(int(sys.argv[i+1]))

expects = { 0: 1, 1: 1, 2: 1, 3: 0.75, 4: 0.5, 5: 0 }

tot = 0
for i in range(len(gt)) :
    tot += expects[i] * 2 * gt[i]
    
print(tot)
# 1: 2*1
# 2: 2*1
# 3: 2*1
# 4: 2*0.75
# 5: 2*0.5
# 6: 2*0

