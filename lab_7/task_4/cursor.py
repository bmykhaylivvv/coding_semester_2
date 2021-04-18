'''
Module which represents a cursor for document engine.
'''


class Cursor:
    '''
    Class represents a cursor in the text.
    '''

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        '''
        Move a cursor one character forward.
        '''
        self.position += 1

    def back(self):
        '''
        Move a cursor one character backward.
        '''
        self.position -= 1

    def home(self):
        '''
        Move a cursor to the beginning of the text.
        '''
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        '''
        Move a cursor to the end of the text.
        '''
        while self.position < len(self.document.characters
                                  ) and self.document.characters[
                self.position].character != '\n':
            self.position += 1
