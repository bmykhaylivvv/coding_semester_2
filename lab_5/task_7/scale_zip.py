'''
Module for work with .zip files.
'''


import os
import shutil
import sys
import zipfile
from pathlib import Path
from PIL import Image


class ScaleZip():
    '''
    Class with methods for scaling images.

    ...

    Attributes
    -------
    zipname: str
        the name of the zip file.
    x: int
        width of the image.
    y: int  
        height of the image.
    temp_directory:
        path to the given file via pathlib library.


    Methods
    -------
    process_files(self)
        Scale each image in the directory to given size.
    '''

    def __init__(self, zipname, x, y):
        self.zipname = zipname
        self.x = x
        self.y = y
        self.temp_directory = Path(f'unzipped-{self.zipname[:-4]}')

    def process_files(self):
        '''
        Scale each image in the directory to given size.
        '''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((self.x, self.y))
            scaled.save(str(filename))
