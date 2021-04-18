'''
Module for GrayscaleImage ADT.
'''

from io import StringIO
import numpy as np
from PIL import Image, ImageOps
from arrays import Array2D


class InvalidImagePixelValue(Exception):
    '''
    Exception for invalid value of pixel.
    Invalid value must be in [0...255]
    '''

    pass


class InvalidImagePixelRange(Exception):
    '''
    Exception for invalid coordinats of Array2D.
    '''

    pass


class GrayscaleImage:
    '''
    Represent GrayscaleImage ADT for work with images.
    '''

    def __init__(self, ncols=1, nrows=1):
        self.image = Array2D(nrows, ncols)
        for row in range(nrows):
            for col in range(ncols):
                self.image[row, col] = 0

        self.before_compress_string = ''
        self.after_compress_string = ''  # string for check % of zipping.
        self.compressed_list = []
        self.decompressed_list = []
        self.decompressed_image = None

    @property
    def width(self):
        '''
        Return width of image in pixels.
        '''

        return self.image.num_cols()

    @property
    def height(self):
        '''
        Return height of image in pixels.
        '''

        return self.image.num_rows()

    def clear(self, value: int):
        '''
        Set the whole image (each pixel) to certain value.
        '''

        if value not in range(256):
            raise InvalidImagePixelValue

        for row in range(self.height):
            for col in range(self.width):
                self.image[row, col] = value

    def getitem(self,  col: int, row: int):
        '''
        Return value of pixel on given position.
        '''

        if row not in range(self.height) or col not in range(self.width):
            raise InvalidImagePixelRange
        return self.image[row, col]

    def setitem(self,  col: int, row: int, value: int):
        '''
        Set pixel on given position to certain value.
        '''
        if row not in range(self.height) or col not in range(self.width):
            raise InvalidImagePixelRange

        if value not in range(256):
            raise InvalidImagePixelValue

        self.image[row, col] = value

    def from_file(self, path: str):
        '''
        Turn instance of GrayscaleImage class to representation of greyscale image.
        '''
        image = Image.open(path)
        image_grayscale = ImageOps.grayscale(image)

        # create np array grom ImageOps
        img_array = np.array(image_grayscale)
        # size of np array
        np_array_shape = img_array.shape

        # overwrite class instance to appropriate size with size of given image
        self.image = Array2D(np_array_shape[0], np_array_shape[1])

        # fill Array2D (self.image) in this class
        for i in range(np_array_shape[0]):
            for j in range(np_array_shape[1]):
                self.image[i, j] = img_array[i, j]

    def lzw_compression(self):
        '''
        Compress a string to a list of output symbols.
        '''

        array_2d_string = ''
        for row in range(self.height):
            for col in range(self.width):
                array_2d_string += str(chr(self.image[row, col]))

        self.before_compress_string = array_2d_string

        # Build the dictionary.
        dict_size = 256
        dictionary = {chr(i): i for i in range(dict_size)}

        wrd = ""
        result = []
        for char in self.before_compress_string:
            wcc = wrd + char
            if wcc in dictionary:
                wrd = wcc
            else:
                result.append(dictionary[wrd])
                # Add wcc to the dictionary.
                dictionary[wcc] = dict_size
                dict_size += 1
                wrd = char

        # Output the code for wrd.
        if wrd:
            result.append(dictionary[wrd])

        self.compressed_list = result

        for j in self.compressed_list:
            # string for check % of zipping.
            self.after_compress_string += str(chr(j))

    def lzw_decompression(self):
        '''
        Decompress the list to the string.
        '''

        # Build the dictionary.
        dict_size = 256
        dictionary = {i: chr(i) for i in range(dict_size)}

        # use StringIO, otherwise this becomes O(N^2)
        # due to string concatenation in a loop
        result = StringIO()
        wrd = chr(self.compressed_list.pop(0))
        result.write(wrd)
        for k in self.compressed_list:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = wrd + wrd[0]
            else:
                raise ValueError('Bad compressed k: %s' % k)
            result.write(entry)

            # Add w+entry[0] to the dictionary.
            dictionary[dict_size] = wrd + entry[0]
            dict_size += 1

            wrd = entry

        self.decompressed_list = result.getvalue()

        self.decompressed_image = Array2D(self.height, self.width)

        image_pixel = 0
        for row in range(self.height):
            for col in range(self.width):
                char = ord(self.decompressed_list[image_pixel])
                self.decompressed_image[row, col] = char
                image_pixel += 1
