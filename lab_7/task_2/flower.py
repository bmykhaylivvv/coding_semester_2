'''
Module represents Flower and interactions with flowers.
'''
import itertools


class Flower:
    '''
    Represents Flower with its properties.
    '''

    def __init__(self, petals: int, price: int, color: str):
        self.petals = petals
        self.price = price
        self.color = color

    def check_petals(self):
        '''
        Check correctness of petals input.
        '''
        if not (isinstance(self.petals, int) and self.petals > 0):
            raise TypeError('Incorrect petals number')
        return True

    def check_price(self):
        '''
        Check correctness of price input.
        '''
        if not (isinstance(self.price, int) and self.price > 0):
            raise TypeError('Incorrect price input')
        return True

    def check_color(self):
        '''
        Check correctness of color input.
        '''
        if not isinstance(self.color, str):
            raise TypeError('Incorrect color input')
        return True


class Tulip(Flower):
    '''
    Represent Tulip flower (Flower class`s child)
    '''

    def __init__(self, petals: int, price: int):
        super().__init__(petals, price, 'pink')


class Rose(Flower):
    '''
    Represent Rose flower (Flower class`s child)
    '''

    def __init__(self, petals: int, price:int):
        super().__init__(petals, price, 'red')


class Chamomile(Flower):
    '''
    Represent Chamoline flower (Flower class`s child)
    '''

    def __init__(self, petals: int, price:int):
        super().__init__(petals, price, 'white')


class FlowerSet:
    '''
    Represent FlowerSet (bundle of flowers).
    '''

    def __init__(self):
        self.flower_set = set()

    def add_flower(self, flower):
        '''
        Adds flower to flower_set.
        '''
        self.flower_set.add(flower)


class Bucket:
    '''
    Represents bucket of flowers.
    '''

    def __init__(self):
        self.bucket = set()

    def add_set(self, flowerset):
        '''
        Adds flowers from FlowerSet to bucket.
        '''
        for flower in list(flowerset.flower_set):
            self.bucket.add(flower)

    def total_price(self):
        '''
        Return total price of bucket.
        '''
        self.bucket_lst = list(self.bucket)
        self.merged_bucket_lst = list(itertools.chain(self.bucket_lst))
        self.sum = 0
        for flower in self.merged_bucket_lst:
            self.sum += flower.price

        return self.sum
