#!/usr/bin/env python3
'''
Given: A permutation of at most 12 symbols defining an ordered
alphabet A and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered
lexicographically. (Note: As in “Enumerating k-mers Lexicographically”,
alphabet order is based on
the order in which the symbols are given.)
'''

import sys

import lib


def lexico_sort(string_list, alphabet):
    '''
    Sort a list according to the provided alphabet
    '''
    alph_map = dict(enumerate(alphabet))
    alph_map_inv = {a: b for b, a in alph_map.items()}

    string_list = [list(word) for word in string_list]

    string_list = [[alph_map_inv[letter] for letter in letter_list]
                   for letter_list in string_list]

    string_list.sort()
    string_list = [''.join([alph_map[letter] for letter in letter_list])
                   for letter_list in string_list]

    return string_list


def test_lexico_sort():
    '''
    Test lexico_sort
    '''
    expected = ['D', 'DD', 'DDD', 'DDN', 'DDA', 'DN', 'DND', 'DNN', 'DNA',
                'DA', 'DAD', 'DAN', 'DAA', 'N', 'ND', 'NDD', 'NDN', 'NDA',
                'NN', 'NND', 'NNN', 'NNA', 'NA', 'NAD', 'NAN', 'NAA', 'A',
                'AD', 'ADD', 'ADN', 'ADA', 'AN', 'AND', 'ANN', 'ANA', 'AA',
                'AAD', 'AAN', 'AAA']
    indata = ['NNA', 'AD', 'NAN', 'DDA', 'ADA', 'DN', 'NDA', 'AN', 'NAA',
              'AAA', 'DDD', 'AAN', 'DNN', 'ND', 'NND', 'NA', 'DND', 'NNN',
              'DAN', 'DDN', 'NAD', 'ANN', 'N', 'AND', 'DA', 'NDD', 'NN',
              'ADD', 'DAD', 'ADN', 'D', 'AA', 'A', 'ANA', 'DAA', 'AAD',
              'DD', 'DNA', 'NDN']
    alphabet = 'DNA'
    assert lexico_sort(indata, alphabet) == expected
    alphabet = 'DNASE'
    assert lexico_sort(indata, alphabet) == expected
    alphabet = 'CEFGHIKLMPQRSDNA'
    assert lexico_sort(indata, alphabet) == expected


def main(filename):
    '''
    Generate a list of possible strings and sort them lexicographically
    '''
    with open(filename) as infile:
        rawdata = infile.read()
    data = rawdata.split('\n')
    alphabet = data[0].replace(' ', '')

    num = int(data[1])

    kmers = list()
    for i in range(1, num+1):
        kmers += lib.gen_kmers(alphabet, i)
    kmers = lexico_sort(kmers, alphabet)
    for kmer in kmers:
        print(kmer)


def test_main(capsys):
    '''
    Test main()
    '''
    import tempfile
    filename = tempfile.mkstemp()[1]
    data = 'D N A\n3\n'
    with open(filename, 'w') as tmpf:
        tmpf.write(data)
    main(filename)
    out = capsys.readouterr()[0]
    expected = ('D\nDD\nDDD\nDDN\nDDA\nDN\nDND\nDNN\nDNA\nDA\nDAD\nDAN\n' +
                'DAA\nN\nND\nNDD\nNDN\nNDA\nNN\nNND\nNNN\nNNA\nNA\nNAD\n' +
                'NAN\nNAA\nA\nAD\nADD\nADN\nADA\nAN\nAND\nANN\nANA\nAA\n' +
                'AAD\nAAN\nAAA\n')
    assert out == expected

    data = 'D N A\n2\n'
    with open(filename, 'w') as tmpf:
        tmpf.write(data)
    main(filename)
    expected = 'D\nDD\nDN\nDA\nN\nND\nNN\nNA\nA\nAD\nAN\nAA\n'
    out = capsys.readouterr()[0]
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <data file>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
