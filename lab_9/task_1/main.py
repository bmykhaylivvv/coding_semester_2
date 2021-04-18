'''
Main module for modeling ecosystem.
'''

import logging
from ecosystem import River


def ecosystem_modeling(river_length_model=10, iterations_model=5, periods=3):
    '''
    Model ecosystem and log everything to the example.log.
    '''
    logging.basicConfig(filename='example.log',
                        encoding='utf-8', level=logging.INFO)

    river1 = River(river_length=river_length_model)
    river1.random_river_state()

    for period in range(1, periods+1):
        logging.info('Original ecosystem')
        logging.info(f'{river1.represent_river_state(river1.river_state)}\n')
        fishes = river1.certain_animal_number('F')
        bears = river1.certain_animal_number('B')
        logging.info(f'Number of fishes: {fishes}')
        logging.info(f'Number of bears: {bears}\n')

        iterations = []

        for move in range(iterations_model):
            next_iteration = river1.move_river()
            if next_iteration not in iterations:
                logging.info(next_iteration)
                iterations.append(next_iteration)
            else:
                logging.info(f'///')

        logging.info(f'Updated ecosystem at period {period}')
        logging.info(
            f'{river1.represent_river_state(river1.river_state)}\n\n\n\n')


if __name__ == "__main__":
    ecosystem_modeling()