#!/usr/bin/env python3
'''
For a collection of strings, a larger string containing every one of the
smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a
collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of equal length, not exceeding 1 kbp,
in FASTA format (which represent reads deriving from the same strand
of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there
exists a unique way to reconstruct the entire chromosome from these
reads by gluing together pairs of reads that overlap by more than
half their length.

Return: A shortest superstring containing all the given strings
(thus corresponding to a reconstructed chromosome).
'''

import sys

import lib


def main(filename):
    '''
    Read a FASTA file and assemble a sequence from the read sequence
    '''
    seqs = lib.read_fasta(filename)[1]
    print(assemble_seq(seqs))


def test_main(capsys):
    '''
    Test main()
    '''
    import tempfile
    filename = tempfile.mkstemp()[1]
    data = '''>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
'''
    with open(filename, 'w') as tmpf:
        tmpf.write(data)

    main(filename)
    out = capsys.readouterr()[0]
    expected = 'ATTAGACCTGCCGGAATAC\n'
    assert out == expected


def assemble_seq(seqs):
    '''
    Assemble a sequence from sequence reads
    Note: requires that more than half the sequence overlaps
    '''
    # get rid of potential duplicates
    seqs = list(set(seqs))
    final = seqs[0]
    seqs[0] = ''

    lengths = [len(seq) for seq in seqs]
    while [seq for seq in seqs if seq]:
        for i in range(1, len(seqs)):
            if not seqs[i]:
                continue
            try:
                # sequence to be added before final
                ind = seqs[i].index(final[:lengths[i]//2])
                final = seqs[i][:ind] + final
                seqs[i] = ''
                break
            except ValueError:
                try:
                    # sequence to be added after final
                    ind = seqs[i].index(final[len(final)-lengths[i]//2:])
                    final += seqs[i][ind+lengths[i]//2:]
                    seqs[i] = ''
                    break
                except ValueError:
                    continue
    return final


def test_assemble_seq():
    '''
    Test assemble_seq()
    '''
    data = ['ATTAGACCTG', 'CCTGCCGGAA', 'AGACCTGCCG', 'GCCGGAATAC']
    expected = 'ATTAGACCTGCCGGAATAC'
    assert assemble_seq(data) == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <FASTA file>\n'.format(sys.argv[0]))
        sys.exit(1)

    main(sys.argv[1])
