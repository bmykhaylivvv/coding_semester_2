import unittest
from machine import VendingMachine
from machine import TextMachine


class MachineTest(unittest.TestCase):
    def setUp(self):
        self.tm1 = TextMachine((75, 125), (25, 245))

    def test_start(self):
        self.assertEqual(self.tm1.texts_count() == (75, 25))
        self.assertEqual(self.tm1.still_owe() == (125, 245))
        self.assertEqual(str(self.tm1) == "Text Machine:<74 texts; ₴1.25 each>; "
                         "<25 texts; ₴2.45 each>")

    def test_insert_func(self):
        self.assertEqual(self.tm1.insert_money((500, 'long')) == ("Got a text!", 255,
                                                                  "You can buy 1 long text or 2 short text"))
        self.assertEqual(self.tm1.texts_count() == (74, 24))
        self.assertEqual(self.tm1.still_owe() == (125, 245))
        self.assertEqual((str(tm1) == "Text Machine:<74 texts; ₴1.25 each>; "
                          "<24 texts; ₴2.45 each>"))
