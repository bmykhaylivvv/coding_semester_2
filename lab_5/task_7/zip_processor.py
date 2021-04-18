'''
Module for work with .zip files.
'''


import os
import shutil
import sys
import zipfile
from pathlib import Path
from PIL import Image
from scale_zip import ScaleZip
from zip_replace import ZipReplace


class ZipProcessor:
    '''
    Class for work with .zip files.

    ...

    Attributes
    -------
    zipname: str
        the name of the file.
    todo: str
        option that will be done with file.
    temp_directory: 
        path to the given file via pathlib library.

    Methods
    -------
    process_zip(self)
        Method unzips file, execute process_files method depending on user input and zip given file.
    unzip_files(self)
        Method unzips file.
    zip_files(self)
        Method zips file.
    '''

    def __init__(self, zipname, todo):
        self.zipname = zipname
        self.todo = todo
        self.temp_directory = Path(f'unzipped-{zipname[:-4]}')

    def process_zip(self):
        '''
        Function unzips file, execute process_files method depending on user input and zip given file.
        '''
        self.unzip_files()
        if self.todo == 'scale':
            self.x_length = int(input('Enter x length: '))
            self.y_length = int(input('Enter y length: '))
            composition_class = ScaleZip(
                self.zipname, self.x_length, self.y_length)

        if self.todo == 'replace':
            self.before = input('Take away: ')
            self.after = input('Replace on: ')
            composition_class = ZipReplace(
                self.zipname, self.before, self.after)

        composition_class.process_files()
        self.zip_files()

    def unzip_files(self):
        '''
        Function unzips file.
        '''
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        '''
        Function zips file.
        '''
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)

        shutil.rmtree(str(self.temp_directory))
