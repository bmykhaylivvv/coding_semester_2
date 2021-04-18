import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket


class TestFlower(unittest.TestCase):
    '''
    Class for testing flower module.
    '''

    def setUp(self):
        '''
        Setting values for test.
        '''
        self.rose1 = Rose(9, 23)
        self.rose2 = Rose(3, 20)
        self.tulip1 = Tulip(5, 18)
        self.chamolime1 = Chamomile(21, 11)

        self.flower1 = Flower(11, 26, 1)
        self.rose3 = Rose('9', '23')


    def test_check_color(self):
        self.assertTrue(self.rose1.check_color() == True,
                        'Check type of color value')

    def test_check_price(self):
        self.assertTrue(self.rose1.check_price() == True,
                        'Check type of price value')

    def test_check_petals(self):
        self.assertTrue(self.rose1.check_petals() == True,
                        'Check type of petals value')

    def test_color_input_correctness(self):
        with self.assertRaises(TypeError):
            self.flower1.check_color()

    def test_petals_input_correctness(self):
        with self.assertRaises(TypeError):
            self.rose3.check_petals()

    def test_price_input_correctness(self):
        with self.assertRaises(TypeError):
            self.rose3.check_price()


    def test_flower_set(self):
        self.flowerSet1 = FlowerSet()
        self.flowerSet1.add_flower(self.rose1)
        self.assertEqual(self.flowerSet1.flower_set, {self.rose1}, 'Problem in \'add_flower()\'\
 method in \'FlowerSet\' class')

    def test_bucket(self):
        self.flowerSet1 = FlowerSet()
        self.flowerSet1.add_flower(self.rose1)
        self.bucket1 = Bucket()
        self.bucket1.add_set(self.flowerSet1)
        self.assertEqual(self.bucket1.bucket, {self.rose1}, 'Problem in \'add_set()\'\
 method in \'Bucket\' class')

    def test_total_sum(self):
        self.flowerSet1 = FlowerSet()
        self.flowerSet1.add_flower(self.rose1)
        self.flowerSet1.add_flower(self.rose2)

        self.flowerSet2 = FlowerSet()
        self.flowerSet2.add_flower(self.tulip1)
        self.flowerSet2.add_flower(self.chamolime1)

        self.bucket1 = Bucket()
        self.bucket1.add_set(self.flowerSet1)
        self.bucket1.add_set(self.flowerSet2)
        self.assertTrue(self.bucket1.total_price() == 72, 'Problem in \'total_price()\'\
 method in \'Bucket\' class')


if __name__ == '__main__':
    unittest.main()
