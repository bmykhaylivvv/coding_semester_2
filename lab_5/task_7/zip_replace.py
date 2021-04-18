'''
Module for work with .zip files.
'''


import sys
import shutil
import zipfile
from pathlib import Path


class ZipReplace:
    '''
    Class for replacing words in directory with files.

    ...

    Attributes
    -------
    zipname: str
        the name of the zip file.
    search_string: str
        string which should be taken away from file.
    replace_string: str  
        string which should be replaced on.
    temp_directory:
        path to the given file via pathlib library.


    Methods
    -------
    process_files(self)
        Method replaces one string on another one.
    '''

    def __init__(self, zipname, search_string, replace_string):
        self.zipname = zipname
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f'unzipped-{self.zipname[:-4]}')

    def process_files(self):
        '''
        Funtions replaces words in directory with files.
        '''
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with filename.open('w') as file:
                file.write(contents)
