'''
Test module for zip_processor module.
'''
import os
from zip_processor import ZipProcessor

filename = input('Enter a filename without extension: ')
while True:
    option = input('Available options:\n- scale\n- replace\nEnter an option\n> ')
    if option == 'scale' or option == 'replace':
        break

file_stats_before_changes = os.stat(f'{filename}.zip')

ZipProcessor(f'{filename}.zip', option).process_zip()

file_stats_after_changes = os.stat(f'{filename}.zip')

print()

print(f'Size before changes: {file_stats_before_changes.st_size} Bytes')
print(f'Size after changes: {file_stats_after_changes.st_size} Bytes')


