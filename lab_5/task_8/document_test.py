'''
Test module for document engine.
'''


from document import Document
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
print()

# d.delete()
# This command arises an IndexError as the cursor is at the end of line.

d.cursor.home()
d.delete()
d.insert('W')
print(d.string)
print()

d.characters[0].underline = True
print(d.string)



# d.save()
# This command arises an FileNotFoundError as you can`t save a file with empty name.
