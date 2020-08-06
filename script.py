import urllib.request
import re
from downloder import download_url

fp = urllib.request.urlopen("https://ouvert.canada.ca/data/fr/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2")
mybytes = fp.read()

html_data = mybytes.decode("utf8")
fp.close()

tr_list = re.findall('<tr>.*?</tr>', html_data, re.DOTALL)

data_row = ''
for tr_data in tr_list:
    if 'Sociétés de régime fédéral' and ".zip" in tr_data:
        data_row = tr_data;

zip_url_matcher = re.search('(?i)http.*?\.zip', data_row, re.DOTALL)
zip_url = zip_url_matcher.group(0)

# zip_url contains the url of the zip file, that will be downloaded.
print(zip_url)

download_url(zip_url, 'zip')