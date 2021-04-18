'''
Test module for document engine.
'''


from document import Document, EmptyFileName, UnexistingSymbol
from character import Character
from cursor import Cursor

d = Document()
d.insert('h')
d.insert('e')
d.insert(Character('l', bold=True))
d.insert(Character('l', bold=True))
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
d.insert('l')
d.insert('d')
print(d.string)

d.insert('W')

try:
    d.delete()
except UnexistingSymbol:
    print('\n---\nThere is no character to delete on current position\n---\n')


d.cursor.home()

d.delete()
d.insert('😉')
print(d.string)
print()

d.characters[0].underline = True
print(d.string)

try:
    d.save()
except EmptyFileName:
    print('\n---\nYour file name is empty\n---\n')

d.filename = 'test_document'
d.save()
