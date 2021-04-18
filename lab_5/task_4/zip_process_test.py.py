'''
Module for checking "scale_zip.py" module.
'''
import os
import shutil
import sys
import zipfile
from pathlib import Path
from PIL import Image

from scale_zip import ZipProcessor, ScaleZip

class ZipCheck(ScaleZip):
    '''
    Class for checking images scaling.
    '''
    def __init__(self, zipname, x, y):
        super().__init__(zipname, x, y)
        
    def check_process(self):
        '''
        Runs all method to show images resolution changes.
        '''
        self.unzip_files()
        print('Current images size')
        self.image_size()
        self.process_files()
        print("\nImages size after scaling")
        self.image_size()
        self.zip_files()



    def image_size(self):
        '''
        Outputs resolution of images.
        '''
        for filename in self.temp_directory.iterdir():
            img=Image.open(str(filename))
            img_size = img.size
            print(img_size)




if __name__ == "__main__":
    x_length = int(input('Enter x length: '))
    y_length = int(input('Enter y length: '))

    ZipCheck('cats.zip', x_length, y_length).check_process()