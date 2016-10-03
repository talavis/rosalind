#!/usr/bin/env python3

'''Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.'''

import sys

if len(sys.argv) != 3 :
    sys.stderr.write('Usage: {0} <n months> <m life expectancy>\n'.format(sys.argv[0]))
    sys.exit()

n = int(sys.argv[1])
m = int(sys.argv[2])


n2 = [1]
for i in range(1, m) :
    n2.append(0)
n1 = [0, 1]
for i in range(2, m) :
    n1.append(0)


for i in range(2, n) :
    n0 = [sum(n1[1:])] + n1[:-1]
    n2 = list(n1)
    n1 = list(n0)
print(sum(n1))
