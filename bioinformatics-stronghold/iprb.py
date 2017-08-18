#!/usr/bin/env python3

'''Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.'''

import sys

if len(sys.argv) != 4 :
    sys.stderr.write('Usage: <k homodominant> <m heterozygous> <n homorecessive>\n'.format(sys.argv[0]))
    sys.exit()

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

tot = k+m+n

# combinations:
# 1) homodom + homodom -> pheno
# 2) homodom + hetero -> pheno
# 3) homodom + homorec -> pheno
# 4) hetero + hetero -> 50% pheno
# 5) hetero + homorec -> 25% pheno
# 6) homorec + homorec -> 0% pheno

ptot = 0
# 1)
ptot += k/tot*(k-1)/(tot-1)
# 2)
ptot += k/tot*m/(tot-1)
ptot += m/tot*k/(tot-1)
# 3)
ptot += k/tot*n/(tot-1)
ptot += n/tot*k/(tot-1)
# 4)
ptot += 0.75*m/tot*(m-1)/(tot-1)
# 5)
ptot += 0.5*m/tot*(n)/(tot-1)
ptot += 0.5*n/tot*(m)/(tot-1)

print(ptot)
