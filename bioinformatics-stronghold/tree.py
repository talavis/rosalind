#!/usr/bin/env python3
'''
Given: A positive integer nn (n≤1000) and an adjacency list
corresponding to a graph on nn nodes that contains no cycles.

Return: The minimum number of edges that can be added
to the graph to produce a tree.
'''

import sys


def gen_graphs(adj_list, no_nodes):
    '''
    Generate the graphs based on the adjacency list
    '''
    graphs = list()
    for edge in adj_list:
        hits = list()
        for i in range(len(graphs)):
            if edge[0] in graphs[i] or edge[1] in graphs[i]:
                hits.append(i)
        if not hits:
            graphs.append({edge[0], edge[1]})
        elif len(hits) == 1:
            graphs[hits[0]].add(edge[0])
            graphs[hits[0]].add(edge[1])
        elif len(hits) > 1:
            graphs[hits[0]] = graphs[hits[0]] | graphs[hits[1]]
            graphs.pop(hits[1])
    used = set(node for graph in graphs for node in graph)
    lonely = set(range(1, no_nodes+1)) - used
    graphs += [[num] for num in lonely]

    return([list(graph) for graph in graphs])


def test_gen_graphs():
    '''
    Test gen_graphs()
    '''
    adj_list = [[1, 2],
                [2, 8],
                [4, 10],
                [5, 9],
                [6, 10],
                [7, 9]]

    expected = [[1, 2, 8], [3], [4, 6, 10], [5, 7, 9]]
    graphs = gen_graphs(adj_list, 10)
    graphs = sorted([sorted(graph) for graph in graphs])
    assert graphs == expected

    adj_list = [[1, 2],
                [2, 8],
                [4, 10],
                [5, 9],
                [6, 10],
                [7, 9],
                [9, 1]]
    expected = [[1, 2, 5, 7, 8, 9], [3], [4, 6, 10]]
    graphs = gen_graphs(adj_list, 10)
    graphs = sorted([sorted(graph) for graph in graphs])
    assert graphs == expected


def tree(filename):
    '''
    Parse input data and generate graphs.
    Return the number of edges needed to make
    a unified tree from the graphs
    '''
    indata = open(filename).read().split('\n')
    no_nodes = int(indata[0])
    edges = list()
    for line in indata[1:]:
        if line:
            cols = line.split(' ')
            edges.append([int(cols[0]), int(cols[1])])
    graphs = gen_graphs(edges, no_nodes)
    print(len(graphs)-1)


def test_tree(capsys):
    '''
    Test tree()
    '''
    import tempfile

    data = '10\n1 2\n2 8\n4 10\n5 9\n6 10\n7 9\n'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpf:
        tmpf.write(data)
    tree(filename)
    out = capsys.readouterr()[0]
    assert out == '3\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <datafile>\n'.format(sys.argv[0]))
        sys.exit(1)
    tree(sys.argv[1])
