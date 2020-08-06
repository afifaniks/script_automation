#!/usr/bin/env python
"""
This script shall download files from URL
__author__: Afif Al Mamun
__date__: August 4, 2020
"""

import urllib.request
from tqdm import tqdm
import os


class UpdateProgressbar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_dir=''):
    '''
    :param url: The URL of the web content
    :param output_dir: Optional
    :return:
    '''
    down_path = url.split('/')[-1]
    down_path = os.path.join(output_dir, down_path)
    with UpdateProgressbar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=down_path, reporthook=t.update_to)