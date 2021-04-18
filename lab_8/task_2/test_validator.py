'''
Test module for validator module.
'''
import unittest
from validator import Validator


class TestValidator(unittest.TestCase):
    '''
    Class for testing flower module.
    '''

    def setUp(self):
        '''
        Setting values for test.
        '''
        self.valid = Validator()

    def test_name_surname(self):
        '''
        Test for name and surname string.
        '''
        self.assertTrue(self.valid.validate_name_surname(
            "Elvis Presley"), '\n1. Name - 1 word, Surname - 1 word\n2. Should be only first \
uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "ElvisPresley"), '\n1. Name - 1 word, Surname - 1 word\n 2. Should be only first \
uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "Elvis Presley forever"), '\n1. Name - 1 word, Surname - 1 word\n 2. Should be only \
first uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "elvis Presley"), '\n1. Name - 1 word, Surname - 1 word\n 2. Should be only first \
uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "Elvis presley"), '\n1. Name - 1 word, Surname - 1 word\n 2. Should be only first \
uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "Elvis PResley"), '\n1. Name - 1 word, Surname - 1 word\n 2. Should be only first \
uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"), '\n1. Name - 1 word, \
Surname - 1 word\n 2. Should be only first uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname("Elvis P"), '\n1. Name - 1 word, \
Surname - 1 word\n 2. Should be only first uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "Elvis P,resley"), '\n1. Name - 1 word, Surname - 1 word\n 2. Should be only first \
uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')
        self.assertFalse(self.valid.validate_name_surname(
            "El1vis Presley"), '\n1. Name - 1 word, Surname - 1 word\n 2. Should be only first \
uppercase letter in name and surname\n\
3. Size of both name and surname shoulb be between 2 and 30\n\
4. No digits or punctuation in name or surname')

    def test_age(self):
        '''
        Test for age string.
        '''
        self.assertTrue(self.valid.validate_age("20"),
                        '\n1. Valid age id digit between 16 and 99')
        self.assertFalse(self.valid.validate_age("7"),
                         '\n1. Valid age id digit between 16 and 99')
        self.assertFalse(self.valid.validate_age("100"),
                         '\n1. Valid age id digit between 16 and 99')
        self.assertFalse(self.valid.validate_age("20."),
                         '\n1. Valid age id digit between 16 and 99')
        self.assertFalse(self.valid.validate_age("20a"),
                         '\n1. Valid age id digit between 16 and 99')

    def test_country(self):
        '''
        Test for country string.
        '''
        self.assertTrue(self.valid.validate_country("Ukraine"),
                        '\n1. Valid country - between 2 and 10 chars, first letter should be \
uppercase, can`t contain numbers')
        self.assertFalse(self.valid.validate_country(
            "U"), '\n1. Valid country - between 2 and 10 chars, first letter should be uppercase, \
can`t contain numbers')
        self.assertFalse(self.valid.validate_country(
            "UUUUUUUUUUUUUUUUUUUUUUU"), '\n1. Valid country - between 2 and 10 chars, first letter \
should be uppercase, can`t contain numbers')
        self.assertFalse(self.valid.validate_country("Ukraine1"),
                         '\n1. Valid country - between 2 and 10 chars, first letter should be \
uppercase, can`t contain numbers')
        self.assertFalse(self.valid.validate_country("ukraine"),
                         '\n1. Valid country - between 2 and 10 chars, first letter should be \
uppercase, can`t contain numbers')
        self.assertTrue(self.valid.validate_country(
            "USA"), '\n1. Valid country - between 2 and 10 chars, first letter should be \
uppercase, can`t contain numbers')

    def test_region(self):
        '''
        Test for region string.
        '''
        self.assertTrue(self.valid.validate_region(
            "Lviv"), '\n1. Valid region - between 2 and 10 chars, first letter should be \
uppercase, can contain numbers')
        self.assertTrue(self.valid.validate_region(
            "Lviv1"), '\n1. Valid region - between 2 and 10 chars, first letter should be \
uppercase, can contain numbers')
        self.assertFalse(self.valid.validate_region(
            "L"), '\n1. Valid region - between 2 and 10 chars, first letter should be \
uppercase, can contain numbers')
        self.assertFalse(self.valid.validate_region(
            "lviv"), '\n1. Valid region - between 2 and 10 chars, first letter should be \
uppercase, can contain numbers')

    def test_living_place(self):
        '''
        Test for living place string.
        '''
        self.assertTrue(self.valid.validate_living_place(
            "Koselnytska st. 2a"), '\n1. Living place - should be in format: "Koselnytska st. 2a"\n\
2. Name of street - between 3 and 20 chars, first character uppercase, no digits in it\n\
3. Type of street - should be "st.", "av.", "prosp." or "rd."\n\
4. Number of building - exactly 2 symbols, first should be number, second can be number or small \
letter')
        self.assertFalse(self.valid.validate_living_place(
            "koselnytska st. 2a"), '\n1. Living place - should be in format: "Koselnytska st. 2a"\n\
2. Name of street - between 3 and 20 chars, first character uppercase, no digits in it\n\
3. Type of street - should be "st.", "av.", "prosp." or "rd."\n\
4. Number of building - exactly 2 symbols, first should be number, second can be number or small \
letter')
        self.assertFalse(self.valid.validate_living_place(
            "Koselnytska provulok 2a"), '\n1. Living place - should be in format: "Koselnytska \
st. 2a"\n\
2. Name of street - between 3 and 20 chars, first character uppercase, no digits in it\n\
3. Type of street - should be "st.", "av.", "prosp." or "rd."\n\
4. Number of building - exactly 2 symbols, first should be number, second can be number or small \
letter')
        self.assertFalse(self.valid.validate_living_place(
            "Koselnytska st. 2"), '\n1. Living place - should be in format: "Koselnytska st. 2a"\n\
2. Name of street - between 3 and 20 chars, first character uppercase, no digits in it\n\
3. Type of street - should be "st.", "av.", "prosp." or "rd."\n\
4. Number of building - exactly 2 symbols, first should be number, second can be number or small \
letter')
        self.assertFalse(self.valid.validate_living_place(
            "Koselnytska st. a2"), '\n1. Living place - should be in format: "Koselnytska st. 2a"\n\
2. Name of street - between 3 and 20 chars, first character uppercase, no digits in it\n\
3. Type of street - should be "st.", "av.", "prosp." or "rd."\n\
4. Number of building - exactly 2 symbols, first should be number, second can be number or small \
letter')
        self.assertTrue(self.valid.validate_living_place(
            "Koselnytska st. 22"), '\n1. Living place - should be in format: "Koselnytska st. 2a"\n\
2. Name of street - between 3 and 20 chars, first character uppercase, no digits in it\n\
3. Type of street - should be "st.", "av.", "prosp." or "rd."\n\
4. Number of building - exactly 2 symbols, first should be number, second can be number or small \
letter')

    def test_index(self):
        '''
        Test for index string.
        '''
        self.assertTrue(self.valid.validate_index("79000"),
                        '\n1. Valid index - exactly 5 digits')
        self.assertFalse(self.valid.validate_index("7900"),
                         '\n1. Valid index - exactly 5 digits')
        self.assertFalse(self.valid.validate_index("790000"),
                         '\n1. Valid index - exactly 5 digits')
        self.assertFalse(self.valid.validate_index("7900q"),
                         '\n1. Valid index - exactly 5 digits')
        self.assertFalse(self.valid.validate_index("790 00"),
                         '\n1. Valid index - exactly 5 digits')

    def test_phone_number(self):
        '''
        Test for phone number string.
        '''
        self.assertTrue(self.valid.validate_phone("+380951234567"), '\n1. Valid phone - in format \
"+380951234567" or "+38 (095) 123-45-67"\n\
2. Starts wit "+" and has from 9 to 12 numbers')
        self.assertTrue(self.valid.validate_phone(
            "+38 (095) 123-45-67"), '\n1. Valid phone - in format "+380951234567" or \
"+38 (095) 123-45-67"\n2. Starts wit "+" and has from 9 to 12 numbers')
        self.assertFalse(self.valid.validate_phone(
            "38 (095) 123-45-67"), '\n1. Valid phone - in format "+380951234567" or \
"+38 (095) 123-45-67"\n2. Starts wit "+" and has from 9 to 12 numbers')
        self.assertFalse(self.valid.validate_phone("380951234567"), '\n1. Valid phone - in format \
"+380951234567" or "+38 (095) 123-45-67"\n\
2. Starts wit "+" and has from 9 to 12 numbers')
        self.assertFalse(self.valid.validate_phone("-380951234567"), '\n1. Valid phone - in format \
"+380951234567" or "+38 (095) 123-45-67"\n\
2. Starts wit "+" and has from 9 to 12 numbers')
        self.assertFalse(self.valid.validate_phone("+3810951234567"), '\n1. Valid phone - in \
format "+380951234567" or "+38 (095) 123-45-67"\n\
2. Starts wit "+" and has from 9 to 12 numbers')
        self.assertTrue(self.valid.validate_phone("+20951234567"), '\n1. Valid phone - in format \
"+380951234567" or "+38 (095) 123-45-67"\n\
2. Starts wit "+" and has from 9 to 12 numbers')

    def test_email_address(self):
        '''
        Test for email address string.
        '''
        self.assertTrue(self.valid.validate_email(
            "username@domain.com"), '\n1. Valid email should be in format "username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it is not \
the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')
        self.assertTrue(self.valid.validate_email(
            "username+usersurname@domain.com"), '\n1. Valid email should be in format \
"username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it \
is not the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')
        self.assertTrue(self.valid.validate_email(
            "username@ucu.edu.ua"), '\n1. Valid email should be in format "username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it \
is not the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')
        self.assertFalse(self.valid.validate_email(
            "usernamedomain.com"), '\n1. Valid email should be in format "username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it \
is not the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')
        self.assertFalse(self.valid.validate_email(
            "username@domaincom"), '\n1. Valid email should be in format "username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it \
is not the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')
        self.assertFalse(self.valid.validate_email(
            "username@domain.aaa"), '\n1. Valid email should be in format "username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it \
is not the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')
        self.assertFalse(self.valid.validate_email("username@aaa"), '\n1. Valid email should be \
in format "username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it \
is not the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')
        self.assertFalse(self.valid.validate_email("@domain.com"), '\n1. Valid email should be \
in format "username@domain.type"\n\
2. Username - any letters, digits, any of "!#$%&\'*+-/=?^_`{|}~", dots (provided that it \
is not the first or last\n\
3. Character and provided also that it does not appear consecutively), at least 1, at most 64\n\
4. Domain - only lowercase letters, at least 1, at most 255, but\n\
5. Type : "com", "org", "edu", "gov", "net", "ua",....\n\
6. Be careful - can be also "." - for example @ucu.edu.ua')

    def test_id(self):
        '''
        Test for id string.
        '''
        self.assertTrue(self.valid.validate_id("123450"),
                        '\n1. Valid id - exactly 6 digits, but should contain exactly one zero - \
at any position')
        self.assertTrue(self.valid.validate_id("011111"),
                        '\n1. Valid id - exactly 6 digits, but should contain exactly one zero - \
at any position')
        self.assertFalse(self.valid.validate_id("123456"),
                         '\n1. Valid id - exactly 6 digits, but should contain exactly one zero - \
at any position')
        self.assertFalse(self.valid.validate_id("123006"),
                         '\n1. Valid id - exactly 6 digits, but should contain exactly one zero - \
at any position')
        self.assertFalse(self.valid.validate_id("1230916"),
                         '\n1. Valid id - exactly 6 digits, but should contain exactly one zero - \
at any position')
        self.assertFalse(self.valid.validate_id("12306"),
                         '\n1. Valid id - exactly 6 digits, but should contain exactly one zero - \
at any position')

    def test_general(self):
        '''
        Test for general string consisting of different parts written above.
        '''
        self.assertTrue(self.valid.validate(
            "Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,\
username@domain.com,123450"), '\nCheck all tests above')
        self.assertTrue(self.valid.validate(
            "Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;\
username@domain.com;123450"), '\nCheck all tests above')
        self.assertTrue(self.valid.validate(
            "Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; \
username@domain.com; 123450"), '\nCheck all tests above')
        self.assertTrue(self.valid.validate(
            "Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, \
username@domain.com, 123450"), '\nCheck all tests above')
        self.assertFalse(self.valid.validate(
            "Elvis Presley, 100, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, \
username@domain.com, 123450"), '\nCheck all tests above')


if __name__ == "__main__":
    unittest.main()
