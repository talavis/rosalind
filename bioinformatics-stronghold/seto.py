#!/usr/bin/env python3
'''
If A and B are sets, then their union A∪B is the set comprising any
elements in either A or B; their intersection A∩B is the set of
elements in both A and B; and their set difference A−B is the set of
elements in A but not in B.

Furthermore, if A is a subset of another set U, then the set
complement of A with respect to U is defined as the set Ac=U−A.

Given: A positive integer n (n≤20,000) and two subsets A and B of
{1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set
complements are taken with respect to {1,2,…,n}).
'''

import sys


def calc_sets(set1, set2, number):
    '''
    Calculate the new sets
    '''
    new_sets = []
    # A∪B
    new_sets.append(set1 | set2)
    # A∩B
    new_sets.append(set1 & set2)
    # A−B
    new_sets.append(set1-set2)
    # B−A
    new_sets.append(set2-set1)
    # Ac
    set_u = set(range(1, number+1))
    new_sets.append(set_u-set1)
    # Bc
    new_sets.append(set_u-set2)

    return new_sets


def test_calc_sets():
    '''
    Test calc_sets()
    '''
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 8, 5, 10}
    number = 10
    expected = [{1, 2, 3, 4, 5, 8, 10},
                {2, 5}, {1, 3, 4}, {8, 10},
                {6, 7, 8, 9, 10},
                {1, 3, 4, 6, 7, 9}]
    assert calc_sets(set1, set2, number) == expected


def seto(filename):
    '''
    Read the input from file and calculate the new sets
    '''
    data = open(filename).read().split('\n')
    number = int(data[0])
    set1 = set(int(dat) for dat in data[1][1:-1].split(', '))
    set2 = set(int(dat) for dat in data[2][1:-1].split(', '))

    for new_set in calc_sets(set1, set2, number):
        outstr = [str(val) for val in sorted(list(new_set))]
        outstr = ', '.join(outstr)
        outstr = '{' + outstr + '}'
        print(outstr)


def test_seto(capsys):
    '''
    Test seto()
    '''
    import tempfile

    filename = tempfile.mkstemp()[1]
    data = '10\n{1, 2, 3, 4, 5}\n{2, 8, 5, 10}\n'
    with open(filename, 'w') as tmpf:
        tmpf.write(data)
    expected = ('{1, 2, 3, 4, 5, 8, 10}\n{2, 5}\n' +
                '{1, 3, 4}\n{8, 10}\n{6, 7, 8, 9, 10}\n' +
                '{1, 3, 4, 6, 7, 9}\n')

    seto(filename)
    out = capsys.readouterr()[0]
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <filename>\n'.format(sys.argv[0]))
        sys.exit(1)
    seto(sys.argv[1])
