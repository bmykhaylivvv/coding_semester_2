'''
Module for River object (part of ecosystem).
'''
from animals_2 import Fish, Bear
import random
import logging


class River:
    '''
    Represent river with its properties.
    '''

    def __init__(self, river_length=10):
        self.river_state = []
        self.current_info = None
        self.river_length = river_length

    def __str__(self):
        return f'River with state: {self.river_state}'


    @staticmethod
    def represent_river_state(river_state: list):
        '''
        Returns river state in string type.
        '''
        river_state_str = ''
        for item in river_state:
            if item is None:
                river_state_str += 'N, '
                continue
            river_state_str += f'{item}({str(item.power)[:4]}, {item.gender}), '

        return river_state_str[:-2]

    def insert_animal(self, position: int, animal):
        '''
        Parameters:
        animal (class): instance of animal to insert.

        Inserts animal to certain position.
        '''
        self.river_state.insert(position, animal)

    def random_river_state(self):
        '''
        Generates random river state.
        '''
        self.river_state = [random.choice(
            [Fish(), Bear(), None]) for position in range(self.river_length)]


    def animal_move(self, current_position: int, next_position: int):
        '''
        Move animal from current_position to next_position.
        '''
        self.river_state[next_position] = self.river_state[current_position]
        self.river_state[current_position] = None

    def eat_animal(self, animal_1, animal_2):
        '''
        Animal_1 eats animal_2.
        Animal_1 -- stronger animal.
        '''
        logging.info(
            f'animal {self.river_state[animal_1]} ate {self.river_state[animal_2]} at position {animal_2}')
        self.river_state[animal_2] = None

    def fight(self, animal_1: int, animal_2: int):
        '''
        Simulate fight between two animals.
        '''

        if self.river_state[animal_1].power > self.river_state[animal_2].power:
            logging.info(
                f'animal {self.river_state[animal_2]} lost a fight at position {animal_2} and disappeared...')
            self.river_state[animal_2] = None
            return

        if self.river_state[animal_2].power > self.river_state[animal_1].power:
            logging.info(
                f'animal {self.river_state[animal_1]} lost a fight at position {animal_1} and disappeared...')
            self.river_state[animal_1] = None
            return

    def born_animal(self, animal_1: int, animal_2: int):
        '''
        New animal is born on nearby position.
        '''
        # if animal_1 on the next position in the list
        if animal_1 == (len(self.river_state) - 1):
            if self.river_state[0] == None:
                self.river_state[0] = self.river_state[animal_1]
                logging.info(
                    f'a new animal was born: {self.river_state[animal_1]} at position {0}')
                return
            if self.river_state[animal_1 - 1] == None:
                self.river_state[animal_1 - 1] = self.river_state[animal_1]
                logging.info(
                    f'a new animal was born: {self.river_state[animal_1]} at position \
{len(self.river_state)-1 if (animal_1 - 1) == -1 else animal_1 - 1}')
                return
            return

        # if animal_1 on the next position in the list
        if animal_2 == (len(self.river_state) - 1):
            if self.river_state[0] == None:
                # change animal_1 to animal_2
                self.river_state[0] = self.river_state[animal_2]
                # change animal_1 to animal_2
                logging.info(
                    f'a new animal was born: {self.river_state[animal_2]} at position {0}')
                return

            if self.river_state[animal_2 - 1] == None:
                self.river_state[animal_2 - 1] = self.river_state[animal_2]
                logging.info(
                    f'a new animal was born: {self.river_state[animal_2]} at position \
{len(self.river_state)-1 if (animal_2 - 1) == -1 else animal_2 - 1}')
                return
            return

        # check leftside position near animal_1
        if self.river_state[animal_1 - 1] == None:
            self.river_state[animal_1 - 1] = self.river_state[animal_1]
            logging.info(
                f'a new animal was born: {self.river_state[animal_1]} at position \
{len(self.river_state)-1 if (animal_1 - 1) == -1 else animal_1 - 1}')
            return

        # check leftside position near animal_2
        if self.river_state[animal_2 - 1] == None:
            self.river_state[animal_2 - 1] = self.river_state[animal_2]
            logging.info(
                f'a new animal was born: {self.river_state[animal_2]} at position \
{len(self.river_state)-1 if (animal_2 - 1) == -1 else animal_2 - 1}')
            return

        # check rightside position near animal_1
        if self.river_state[animal_1 + 1] == None:
            self.river_state[animal_1 + 1] = self.river_state[animal_1]
            logging.info(
                f'a new animal was born: {self.river_state[animal_1]} at position {animal_1 + 1}')
            return

        # check rightside position near animal_1
        if self.river_state[animal_2 + 1] == None:
            self.river_state[animal_2 + 1] = self.river_state[animal_2]
            logging.info(
                f'a new animal was born: {self.river_state[animal_2]} at position {animal_2 + 1}')
            return

    def move_river(self):
        '''
        Moves river one time in random direction.
        '''
        while True:
            current_position = random.randint(0, len(self.river_state)-1)
            next_position = current_position + random.choice([-1, 1])

            # if next_position is the last position in the list
            if next_position > len(self.river_state)-1:
                next_position = next_position - len(self.river_state)
            if next_position == -1:
                next_position = len(self.river_state)-1

            if self.river_state[current_position] != None:
                break

        logging.info(f'animal: {self.river_state[current_position]}, current_position: {current_position}, \
next_position: {next_position}')

        # animal to the next_position if next_position is Empty
        if self.river_state[next_position] == None:
            self.animal_move(current_position, next_position)

        # new animal born when animal_1 == animal_2 (with different gender)/ two animal fight (the same gender)
        if self.river_state[current_position] != None and self.river_state[next_position] != None and \
                self.river_state[current_position].typo == self.river_state[next_position].typo:

            if self.river_state[current_position].gender != self.river_state[next_position].gender:
                self.born_animal(current_position, next_position)

            if self.river_state[current_position].gender == self.river_state[next_position].gender:
                self.fight(current_position, next_position)

        # Stronger animal eats weaker animal.
        if isinstance(self.river_state[current_position], Bear) and isinstance(self.river_state[next_position], Fish):
            self.eat_animal(current_position, next_position)

        # Stronger animal eats weaker animal.
        if isinstance(self.river_state[next_position], Fish) and isinstance(self.river_state[current_position], Bear):
            self.eat_animal(next_position, current_position)

        return f'River with state: {self.represent_river_state(self.river_state)}\n'

    def certain_animal_number(self, animal_typo: str):
        '''
        Return number of animal with given type in the river.
        '''
        string_river_state = self.represent_river_state(self.river_state)
        return string_river_state.count(animal_typo)
