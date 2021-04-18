'''
Module for validation data.
'''
import re


class Validator:
    '''
    Represents validator with different methods.
    '''
    @staticmethod
    def validate_name_surname(name_surname: str):
        '''
        Validate given name and surname string.
        '''
        expression = re.fullmatch(
            r'[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]{2,30}', name_surname)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_age(age: str):
        '''
        Validate given age sting.
        '''
        expression = re.fullmatch(r'1[6-9]|[2-9][0-9]', age)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_country(country: str):
        '''
        Validate given country string.
        '''
        expression = re.fullmatch(r'[A-Z][a-zA-Z]{1,9}', country)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_region(region: str):
        '''
        Validate given region string.
        '''
        expression = re.fullmatch(r'[A-Z][a-zA-Z0-9]{1,9}', region)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_living_place(living_place: str):
        '''
        Validate given living place string.
        '''
        expression = re.fullmatch(
            r'[A-Z][\w]+ [st.|av.|prosp.|rd.]+ \d[\d|a-z]', living_place)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_index(index: str):
        '''
        Validate given index string.
        '''
        expression = re.fullmatch(r'\d{5}', index)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_phone(phone: str):
        '''
        Validate given phone number string.
        '''
        expression = re.fullmatch(
            r'\+\d{9,12}|\+38 \(\d{3}\) \d{2,3}-\d{2,3}-\d{2,3}', phone)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_email(email: str):
        '''
        Validate given email address string.
        '''
        expression = re.fullmatch(
            r'[a-zA-Z](?![^@]*\.\.[^@]*)[a-zA-Z!#$%&\'*+\-\/=?^_`{|}~\"\.\
]{1,63}(?<!\.)@[a-z\.]{1,255}\.(com|org|edu|gov|net|ua)',
            email)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate_id(identificator: str):
        '''
        Validate given id string.
        '''
        expression = re.fullmatch(
            r'0[1-9]{5}|[1-9]0[1-9]{4}|[1-9]{2}0[1-9]{3}|[1-9]{3}0[1-9]{2}|[1-9]{4}0[1-9]{1}\
|[1-9]{5}0', identificator)
        if expression is not None:
            return True
        return False

    @staticmethod
    def validate(data: str):
        '''
        Validate the whole info string.
        '''
        name_surname = r'[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]{2,30}'
        age = r'1[6-9]|[2-9][0-9]'
        country = r'[A-Z][a-zA-Z]{1,9}'
        region = r'[A-Z][a-zA-Z0-9]{1,9}'
        living_place = r'[A-Z][\w]+ [st.|av.|prosp.|rd.]+ \d[\d|a-z]'
        index = r'\d{5}'
        phone = r'\+\d{9,12}|\+38 \(\d{3}\) \d{2,3}-\d{2,3}-\d{2,3}'
        email = r'[a-z][a-z!#$%&\'*+\-\/=?^_`{|}~\"]{1,64}@[a-z\.]{1,255}\.(com|org|edu|gov|net|ua)'
        identificator = r'\d{6}'

        expression = re.fullmatch(f'({name_surname})(,|;|, |; )({age})(,|;|, |; )({country}\
)(,|;|, |; )({region})(,|;|, |; )({living_place})(,|;|, |; )({index})(,|;|, |; )({phone}\
)(,|;|, |; )({email})(,|;|, |; )({identificator})', data)
        if expression is not None:
            return True
        return False
