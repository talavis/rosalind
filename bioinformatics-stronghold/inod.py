#!/usr/bin/env python3
'''
Given: A positive integer nn (3≤n≤10000).

Return: The number of internal nodes of any unrooted binary
tree having n leaves.
'''

import sys


def count_ancestors(no_leaves):
    '''
    Calculate the number of ancestors (internal nodes) in a binary
    tree with no_leaves leaves.
    '''
    # An unrooted binary tree always has no_leaves - 2 internal nodes
    # (if more than 3 leaves)
    if no_leaves > 3:
        return no_leaves-2
    return 0


def test_count_ancestors():
    '''
    Test count_ancestors()
    '''
    assert count_ancestors(4) == 2
    assert count_ancestors(3) == 0
    assert count_ancestors(6) == 4
    assert count_ancestors(8) == 6
    assert count_ancestors(5) == 3
    assert count_ancestors(7) == 5


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <number of leaves>\n'.format(sys.argv[0]))
        sys.exit(1)

    print(count_ancestors(int(sys.argv[1])))
