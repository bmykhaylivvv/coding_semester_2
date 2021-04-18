'''
Main module of document engine.
'''

from cursor import Cursor
from character import Character


class EmptyFileName(Exception):
    pass


class UnexistingSymbol(Exception):
    pass


class Document:
    '''
    Class represents a text document with all properties.
    '''

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        '''
        Insert a character on the cursor position.

        You can`t enter more than one character at the same time.
        '''
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        '''
        Delete a character on the cursor position.

        You can`t delete a character on empty position in list.
        / IndexError: list assignment index out of range /
        '''
        try:
            del self.characters[self.cursor.position]
        except IndexError:
            raise UnexistingSymbol('No character on cursor position')

    def save(self):
        '''
        Save a text to the file.

        You can`t save a file without name ('').
        / FileNotFoundError: [Errno 2] No such file or directory: '' /
        '''
        try:
            f = open(self.filename, 'w')
            f.write(''.join(str(c) for c in self.characters))
            f.close()
        except FileNotFoundError:
            raise EmptyFileName("Your file has empty name")

    @property
    def string(self):
        '''
        Return a string of characters.
        '''
        return ''.join(str(c) for c in self.characters)
