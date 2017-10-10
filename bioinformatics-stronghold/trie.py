#!/usr/bin/env python3
'''
Trie problem at Rosalind
'''
import sys

class TrieNode:
    '''
    Representing a node in a trie.
    '''
    def __init__(self, letter='', parent=None):
        '''
        letter: a character to be represented by the node
        parent: the parent of the node
        '''
        self._children = []
        self._letter = letter
        self._parent = parent


    def __eq__(self, other):
        '''
        Equals implemented for TrieNode and Str
        Returns False otherwise
        '''
        if isinstance(other, str):
            return self._letter == other
        if isinstance(other, self.__class__):
            return self._letter == other.letter
        return False


    @property
    def letter(self):
        '''
        The represented letter
        '''
        return self._letter


    @letter.setter
    def letter(self, new_letter):
        '''
        Update the represented letter
        '''
        self._letter = new_letter


    def next(self, letter):
        '''
        Follow the trie to the next node with the given character
        If it does not exist, it will be created
        Returns the matching node
        '''
        if letter not in self._children:
            self._children.append(TrieNode(letter, self))
        return self._children[self._children.index(letter)]


    def match(self, letter):
        '''
        Follow the trie to the next node with the given character
        Returns the node if it exists, otherwise None
        '''
        if letter in self._children:
            return self._children[self._children.index(letter)]
        return None


    def print_nodes(self, num):
        '''
        Print a representation of the underlying Nodes
        num: the base number
        Format: parent child letter
        '''
        base = num
        for child in self._children:
            num += 1
            print(base, num, child.letter)
            num = child.print_nodes(num)
        return num


def test_trienode(capsys):
    '''
    Test TrieNode and its methods
    '''
    # init
    anode = TrieNode('a')
    assert anode == 'a'
    assert isinstance(anode, TrieNode)

    # new letter
    anode.letter = 'x'
    assert anode == 'x'
    assert anode.letter == 'x'
    assert isinstance(anode, TrieNode)

    # add a new child
    assert isinstance(anode.next('b'), TrieNode)
    assert anode.next('b') != anode
    anode.next('c')
    assert anode != 1

    # correct/incorrect match
    assert anode.match('b')
    assert not anode.match('x')

    # add children to child
    bnode = anode.next('d')
    bnode.next('e')
    bnode.next('f')

    # add another child to same child
    cnode = anode.next('d')
    cnode.next('g')
    assert bnode is cnode
    assert anode is not bnode

    # test print_nodes
    anode.print_nodes(1)
    out = capsys.readouterr()[0]
    expected = '1 2 b\n1 3 c\n1 4 d\n4 5 e\n4 6 f\n4 7 g\n'
    assert out == expected

    # add to children to another child
    cnode = anode.next('c')
    cnode.next('h')
    anode.print_nodes(1)
    out = capsys.readouterr()[0]
    expected = '1 2 b\n1 3 c\n3 4 h\n1 5 d\n5 6 e\n5 7 f\n5 8 g\n'


class Trie:
    '''
    Contains a Trie representing sequences
    '''
    def __init__(self, sequence=''):
        '''
        sequence: initial sequence to add
        '''
        self._root = TrieNode()
        self.add_seq(sequence)


    def add_seq(self, sequence):
        '''
        Add nodes corresponding to the given sequence
        sequence: the sequence to be added
        '''
        current = self._root
        for letter in sequence:
            current = current.next(letter)


    def matches(self, sequence):
        '''
        Tests whether a sequence matches any of the current ones
        '''
        current = self._root
        for letter in sequence:
            tmp = current.match(letter)
            if not tmp:
                return False
            current = tmp
        return True


    def print_trie(self):
        '''
        Print a representation of the tree
        Format: node1 node2 letter
        '''
        self._root.print_nodes(1)


def test_trie(capsys):
    '''
    Test Trie and its methods
    '''
    trie = Trie()
    trie.add_seq('abcdef')
    assert trie.matches('abcdef')
    assert not trie.matches('fedcba')
    trie.add_seq('abcabc')
    trie.print_trie()
    out = capsys.readouterr()[0]
    expected = ('1 2 a\n2 3 b\n3 4 c\n4 5 d\n5 6 e\n' +
                '6 7 f\n4 8 a\n8 9 b\n9 10 c\n')
    assert out == expected


def main(filename):
    '''
    Read input, generate and print trie
    '''
    with open(filename) as infile:
        sequences = infile.read().split('\n')
    tree = Trie()
    for seq in sequences:
        tree.add_seq(seq)
    tree.print_trie()


def test_main(capsys):
    '''
    Test main()
    '''
    import tempfile
    data = 'ATAGA\nATC\nGAT'
    filename = tempfile.mkstemp()[1]
    with open(filename, 'w') as tmpfile:
        tmpfile.write(data)
    main(filename)
    expected = ('1 2 A\n2 3 T\n3 4 A\n4 5 G\n5 6 A\n'
                '3 7 C\n1 8 G\n8 9 A\n9 10 T\n')
    out = capsys.readouterr()[0]
    assert out == expected


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <sequence file>\n'.format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
