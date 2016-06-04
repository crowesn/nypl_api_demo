#!/usr/bin/python

import urllib
import csv

try:
   import xml.etree.cElementTree as ET
except ImportError:
   import xml.etree.ElementTree as ET

import requests

url = 'http://api.repo.nypl.org/api/v1/items/search.xml?q=cats&publicDomainOnly=true'

auth = 'Token token=<your_token>' # add your token here

call = requests.get(url, headers={'Authorization': auth},stream=True)

call.raw.decode_content = True
elems = ET.parse(call.raw)

with open('api_query_results.csv', 'wb') as f:
    writer = csv.writer(f)
    for element in elems.iter('result'):
        writer.writerow([x.text for x in element])
        print element

raw_input('\n\n*** query results saved to api_query_results.csv, press <enter>')
