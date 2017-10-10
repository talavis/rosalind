#!/usr/bin/env python3
'''
Trie problem at Rosalind
'''
class TrieNode:
    '''
    Representing a node in a trie.
    '''
    def __init__(self, letter = '', parent = None):
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
            return self._letter == other._letter
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


    def printNodes(self, num):
        '''
        Print a representation of the underlying Nodes
        num: the base number
        Format: parent child letter
        '''
        base = num
        for child in self._children:
            num += 1
            print(base, num, child.letter)
            num = child.printNodes(num)
        return num


class Trie:
    '''
    Contains a Trie representing sequences
    '''
    def __init__(self, sequence = ''):
        '''
        sequence: initial sequence to add
        '''
        self._root = TrieNode()
        self.addSeq(sequence)


    def addSeq(self, sequence):
        '''
        Add nodes corresponding to the given sequence
        sequence: the sequence to be added
        '''
        current = self._root
        for letter in sequence:
            current = current.next(letter)


    def printTrie():
        '''
        Print a representation of the tree
        Format: node1 node2 letter
        '''
        num = 1
        
