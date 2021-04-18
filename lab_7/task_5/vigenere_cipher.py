'''
Module for work with Vigenere Cipher.
'''


class VigenereCipher:
    '''
    Represents Vigenere cipher.
    '''

    def __init__(self, keyword):
        self.keyword = keyword

    def extend_keyword(self, number):
        '''
        Returns extended keyword.
        '''
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def encode(self, plaintext):
        '''
        Returns encoded text.
        '''
        plaintext = plaintext.replace(" ", "").upper()
        cipher = []
        keyword = self.extend_keyword(len(plaintext))
        for p, k in zip(plaintext, keyword):
            cipher.append(combine_character(p, k))
        return "".join(cipher)

    def decode(self, ciphertext):
        '''
        Decodes cipher text.
        '''
        plain = []
        keyword = self.extend_keyword(len(ciphertext))
        for p, k in zip(ciphertext, keyword):
            plain.append(separate_character(p, k))
        return "".join(plain)


# Not class method
def combine_character(plain, keyword):
    '''
    Combines two characters. 
    '''
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    '''
    Separates two characters.
    '''
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)
