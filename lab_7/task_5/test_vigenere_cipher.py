'''
Test module for vigenere_cipher module.
'''


import unittest
from vigenere_cipher import VigenereCipher
from vigenere_cipher import combine_character, separate_character


class VigenereCipherTest(unittest.TestCase):
    def test_encode_character(self):
        '''
        Test character encoding.
        '''
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        self.assertTrue(encoded == "X")

    def test_encode_spaces(self):
        '''
        Test spaces encoding.
        '''
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        self.assertTrue(encoded == "XECWQXUIVCRKHWA")

    def test_encode_lowercase(self):
        '''
        Test lowercase encoding.
        '''
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        self.assertTrue(encoded == "XECWQXUIVCRKHWA")

    def test_extend_keyword(self):
        '''
        Test keyword extending.
        '''
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        self.assertTrue(extended == "TRAINTRAINTRAINT")

    def test_decode(self):
        '''
        Test decoding.
        '''
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        self.assertTrue(decoded == "ENCODEDINPYTHON")

    def test_separate_character(self):
        '''
        Test character separating.
        '''
        self.assertTrue(separate_character("X", "T") == "E")
        self.assertTrue(separate_character("E", "R") == "N")

    def test_combine_character(self):
        '''
        Test character combining.
        '''
        self.assertTrue(combine_character("E", "T") == "X")
        self.assertTrue(combine_character("N", "R") == "E")


if __name__ == '__main__':
    unittest.main()
