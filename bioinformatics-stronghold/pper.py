#!/usr/bin/env python3
'''
Given: Positive integers n and k such that 100>=n>0100>=n>0 and 10>=k>010>=k>0.

Return: The total number of partial permutations P(n,k)P, modulo 1,000,000.
'''

import sys
import math

n = int(sys.argv[1])
k = int(sys.argv[2])

print(int(math.factorial(n)/(math.factorial(n-k)) % 1000000))
