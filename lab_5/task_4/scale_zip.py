'''
Module for scaling images in .zip archive.
'''
import os
import shutil
import sys
import zipfile
from pathlib import Path
from PIL import Image

class ZipProcessor:
    '''
    Class for work mainly with os sys, PIL, libraries.
    '''
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path(f'unzipped-{zipname[:-4]}')
        
    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)

        shutil.rmtree(str(self.temp_directory))

class ScaleZip(ZipProcessor):
    '''
    Class with methods for scaling images.
    '''
    def __init__(self,zipname, x, y):
        super().__init__(zipname)
        self.x = x
        self.y = y
    def process_files(self):
        '''
        Scale each image in the directory to 640x480
        '''
        for filename in self.temp_directory.iterdir():
            im=Image.open(str(filename))
            scaled = im.resize((self.x, self.y))
            scaled.save(str(filename))


# Test part
if __name__ == "__main__":
    x_length = int(input('Enter x length: '))
    y_length = int(input('Enter y length: '))
    ScaleZip('cats.zip', x_length, y_length).process_zip()


