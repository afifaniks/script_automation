#!/usr/bin/env python
"""
This script shall download files from URL
__author__: Afif Al Mamun
__date__: August 4, 2020
"""

import os
import zipfile


def extract_zip(directory, out_dir):
    dir = os.listdir(directory)

    for path in dir:
        print('Extracting zip: ' + path)
        dir_name = path.split('.')[0]
        with zipfile.ZipFile(os.path.join(directory, path), 'r') as zip_file:
            zip_file.extractall(os.path.join(out_dir, dir_name))


# Extract all the zip files located in 'zip' directory to 'zip_out' directory
extract_zip('zip', 'zip_out')