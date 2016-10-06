#!/usr/bin/env python3

import re
import requests
import sys


def get_protein(accession):
    '''
    Retrieve a protein sequence from UniProt
    '''
    try:
        acc = accession[:accesion.index('_')]
    except:
        acc = accession
    base_url = 'http://www.uniprot.org/uniprot/{}.fasta'
    page_req = requests.get(base_url.replace('{}', acc))
    fasta = page_req.text
    if fasta[0] != '>':
        sys.stderr.write('Returned data not a FASTA file for {}\n'.format(acc))
    seq = ''.join(fasta.split('\n')[1:])
    return seq


def test_get_protein(capsys):
    '''
    Test get_protein()
    '''
    acc = 'P28332'
    seq = ('MCTTGQVIRCKAAILWKPGAPFSIEEVEVAPPKAKEVRIKVVATGLCGTEMKVLGSKHLD' +
           'LLYPTILGHEGAGIVESIGEGVSTVKPGDKVITLFLPQCGECTSCLNSEGNFCIQFKQSK' +
           'TQLMSDGTSRFTCKGKSIYHFGNTSTFCEYTVIKEISVAKIDAVAPLEKVCLISCGFSTG' +
           'FGAAINTAKVTPGSTCAVFGLGGVGLSVVMGCKAAGAARIIGVDVNKEKFKKAQELGATE' +
           'CLNPQDLKKPIQEVLFDMTDAGIDFCFEAIGNLDVLAAALASCNESYGVCVVVGVLPASV' +
           'QLKISGQLFFSGRSLKGSVFGGWKSRQHIPKLVADYMAEKLNLDPLITHTLNLDKINEAV' +
           'ELMKTGKW')
    assert get_protein(acc) == seq
    acc = 'NOTANACC'
    get_protein(acc)
    out, err = capsys.readouterr()
    assert err == 'Returned data not a FASTA file for {}\n'.format(acc)

def find_all_regex(regex, seq):
    '''
    Find all matches for a regex,
    including overlapping ones
    '''

    hits = []
    pos = 0
    while True:
        hit = regex.search(seq, pos)
        if hit is None:
            break
        hits.append(hit.start())
        pos = hit.start() + 1
    return hits


def test_find_all_regex():
    '''
    Test find_all_regex()
    '''
    NOT_P = 'ACDEFGHIKLMNQRSTVWY'
    motif = 'N[{}][ST][{}]'.format(NOT_P, NOT_P)
    pattern = re.compile(motif)
    acc = 'B5ZC00'
    seq = get_protein(acc)
    assert find_all_regex(pattern, seq) == [84, 117, 141, 305, 394]
    acc = 'P07204'
    seq = get_protein(acc)
    assert find_all_regex(pattern, seq) == [46, 114, 115, 381, 408]

    
def find_motif(sequence):
    '''
    Find all regions containing the N-glycosylation motif
    '''
    NOT_P = 'ACDEFGHIKLMNQRSTVWY'
    motif = 'N[{}][ST][{}]'.format(NOT_P, NOT_P)
    pattern = re.compile(motif)
            
    return [m + 1 for m in find_all_regex(pattern, sequence)]


def test_find_motif():
    '''
    Test find_motif
    '''
    acc = 'B5ZC00'
    seq = get_protein(acc)
    assert find_motif(seq) == [85, 118, 142, 306, 395]
    acc = 'P07204'
    seq = get_protein(acc)
    assert find_motif(seq) == [47, 115, 116, 382, 409]


def main(filename):
    '''
    Look for the N-glycosylation motif in the sequences of the given proteins
    Input: accessions
    Output: positions with motif
    '''
    with open(filename) as infile:
        for line in infile:
            seq = get_protein(line.strip())
            hits = find_motif(seq)
            if len(hits) > 0:
                print(line.strip())
                print(' '.join([str(h) for h in hits]))


def test_main(capsys):
    '''
    Test main()
    '''
    import tempfile

    accs = ('A2Z669\n' +
            'B5ZC00\n' +
            'P07204_TRBM_HUMAN\n' +
            'P20840_SAG1_YEAST\n')
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpf:
        tmpf.write(accs)
        
    main(filename)
    out, err = capsys.readouterr()
    expected = ('B5ZC00\n' +
                '85 118 142 306 395\n' +
                'P07204_TRBM_HUMAN\n' +
                '47 115 116 382 409\n' +
                'P20840_SAG1_YEAST\n' + 
                '79 109 135 248 306 348 364 402 485 501 614\n')
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <file with accessions>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])

