import zipfile
import os
import sys

def extract_zip(directory, out_dir):
    dir = os.listdir(directory)

    for path in dir:
        print('Extracting zip: ' + path)
        dir_name = path.split('.')[0]
        with zipfile.ZipFile(os.path.join(directory, path), 'r') as zip_file:
            zip_file.extractall(os.path.join(out_dir, dir_name))


extract_zip('zip', 'zip_out')