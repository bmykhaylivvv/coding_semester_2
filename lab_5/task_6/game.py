'''
Module for adventure game. Game runs in "main.py" module.
'''

# Global variables
wons = 0


class Character:
    '''
    Represents a character with its properties.

    ...

    Attributes
    -------
    name: str
        the name of the character.
    description: str
        the description of the character.
    '''

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Enemy(Character):
    '''
    Represents an enemy with its properties.
    Enemy class is child of Character class.

    ...

    Attributes
    -------
    name: str
        the name of the enemy.
    description: str
        the description of the enemy.
    conversation: str
        the conversation of the enemy.
    weakness: str
        the weakness of the enemy.

    Methods
    -------
    set_conversation(self, conversation: str)
        Overwrites class "conversation" variable.

    set_weakness(self, weakness: str)
        Overwrites class "weakness" variable.

    describe(self)
        Prints instance "description" value.

    talk(self)
        Prints instance "conversation" value.

    fight(self, item: str)
        Checks if character overcame an enemy.

    get_defeated(self)
        Returns number of beaten enemies.
    '''

    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation: str):
        '''
        Overwrites class "conversation" variable.
        '''
        self.conversation = conversation

    def set_weakness(self, weakness: str):
        '''
        Overwrites class "weakness" variable.
        '''
        self.weakness = weakness

    def describe(self):
        '''
        Prints instance "description" value.
        '''
        print(self.description)

    def talk(self):
        '''
        Prints instance "conversation" value.
        '''
        print(self.conversation)

    def fight(self, item: str):
        '''
        Checks if character overcame an enemy.
        '''
        if item == self.weakness:
            global wons
            wons += 1
            return True
        return False

    def get_defeated(self):
        '''
        Returns number of beaten enemies.
        '''
        global wons
        return wons


class Place:
    '''
    Represents a room with its properties.

    ...

    Attributes
    -------
    name: str
        the name of the room.
    description: str
        the description of the room.
    side: str
        side of the world to move between rooms.
    links: list
        list with linked rooms.
    item: str
        name of given item.
    character
        name of given character.

    Methods
    -------
    set_description(self, description: str)
        Overwrites class "description" variable.
    link_room(self, room, side: str)
        Add linked rooms.
    set_character(self, character: str)
        Overwrites class "character" variable.
    get_character(self)
        Returns instance "character" value.
    set_item(self, item: str)
        Overwrites class "item" variable.
    get_item(self)
        Returns instance "item" value.
    move(self, side: str)
        Lets user move beetwen linked rooms.
    get_details(self)
     Prints description of the room and list of all available linked rooms.
    '''

    def __init__(self, name: str):
        self.name = name
        self.description = None
        self.side = None
        self.links = []
        self.item = None
        self.character = None

    def set_description(self, description: str):
        '''
        Overwrites class "description" variable.
        '''
        self.description = description

    def link_room(self, room, side: str):
        '''
        Add linked rooms.
        '''
        link = (room, side)
        self.links.append(link)

    def set_character(self, character: str):
        '''
        Overwrites class "character" variable.
        '''
        self.character = character

    def get_character(self):
        '''
        Returns instance "character" value.
        '''
        return self.character

    def set_item(self, item: str):
        '''
        Overwrites class "item" variable.
        '''
        self.item = item

    def get_item(self):
        '''
        Returns instance "item" value.
        '''
        return self.item

    def move(self, side: str):
        '''
        Lets user move beetwen linked rooms.
        '''
        for room in self.links:
            if side == room[1]:
                return room[0]

    def get_details(self):
        '''
        Prints description of the room and list of all available linked rooms.
        '''
        print(self.description)
        if self.links:
            for link in self.links:
                print(f'The {link[0].name} is {link[1]}')


class Item:
    '''
    Represents an item with its properties.

    ...
    Attributes
    -------
    name: str
        the name of the item.
    description: str
        the description of the item.


    Methods
    -------
    set_description(self, description: str)
        Overwrites class "description" variable.
    describe(self)
        Prints instance "description" value.
    get_name(self)
        Returns instance "name" value.
    '''

    def __init__(self, name: str):
        self.name = name
        self.description = None

    def set_description(self, description: str):
        '''
        Overwrites class "description" variable.
        '''
        self.description = description

    def describe(self):
        '''
        Prints instance "description" value.
        '''
        print(self.description)

    def get_name(self):
        '''
        Returns instance "name" value.
        '''
        return self.name
