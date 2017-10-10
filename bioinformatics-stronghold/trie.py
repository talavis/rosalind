#!/usr/bin/env python3
'''
Trie problem at Rosalind
'''
class TrieNode:
    '''
    Representing a node in a trie.
    '''
    def __init__(self, letter, parent = None):
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


    def next(self, letter):
        '''
        Follow the trie to the next node with the given character
        If it does not exist, it will be created
        Returns the matching node
        '''
        if letter not in self._children:
            self._children.append(TrieNode('letter', self))
        return self_children[self._children.index(letter)]


    def match(self, letter):
        '''
        Follow the trie to the next node with the given character
        Returns the node if it exists, otherwise None
        '''


def update_trie(sequence, trie):
    '''
    Update a trie with a new sequence
    '''
