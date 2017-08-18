#!/usr/bin/env python3

'''Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months if each pair of reproduction-age rabbits produces a litter of k rabbit pairs in each generation (instead of only 1 pair).'''

import sys

if len(sys.argv) != 3 :
    sys.stderr.write('Usage: {0} <n months> <k production>\n'.format(sys.argv[0]))
    sys.exit()

# x: n-2 y: n-1 z = n
nx = 1
ny = 1
nz = 0

n = int(sys.argv[1])
k = int(sys.argv[2])

for i in range(2, n) :
    nz = k * nx + ny
    nx = ny
    ny = nz

print(nz)
