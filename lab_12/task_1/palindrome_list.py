"""
Palindrome class realization.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack


class Palindrome:
    '''
    Class for finding palidromes in the file.
    '''

    def read_file(self, path):
        '''
        Functions reads file to the list.
        '''
        words = []
        with open(path, 'r', encoding='utf-8') as base:
            for line in base:
                if line.rstrip().split(' ')[0]:
                    words.append(line.rstrip().split(' ')[0])
        return words

    def find_palindromes(self, from_file, to_file):
        '''
        Find palindromes in the list.
        '''
        word_list = self.read_file(from_file)

        palidromes = []
        for wrd in word_list:
            stack1 = ArrayStack()
            stack2 = ArrayStack()
            for char in wrd:
                stack1.push(char)
            for char in wrd[::-1]:
                stack2.push(char)

            res = []
            res.append(stack1 == stack2)

            # if wrd == wrd[::-1]:
            #     palidromes.append(wrd)

            if all(res) is True:
                palidromes.append(wrd)

        self.write_to_file(palidromes, to_file)
        return palidromes

    @staticmethod
    def write_to_file(data, path):
        '''
        Write data to the file.
        '''
        with open(path, 'w') as result:
            res_string = ''
            for word in data:
                res_string += f'{word}\n'

            result.write(res_string)

palindrome = Palindrome()
palindrome.find_palindromes("words.txt", "palindrome_en.txt")

