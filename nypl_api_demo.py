#!/usr/bin/python3

# Import dependencies

import urllib
import csv
import requests

try:
   import xml.etree.cElementTree as ET
except ImportError:
   import xml.etree.ElementTree as ET

#  Create some constants for urls, etc and construct the base api call

base_query_url = 'http://api.repo.nypl.org/api/v1/items/search.xml?q=cats'
mods_query_url = 'http://api.repo.nypl.org/api/v1/mods/'
auth = 'Token token=<token>' # add your token here

call = requests.get(base_query_url, headers={'Authorization': auth},stream=True)
call.raw.decode_content = True
elems = ET.parse(call.raw)

# Get page count and print to screen

page_count = int(elems.find("./request/totalPages").text)
print(str(page_count) + " pages")

# Functions for parsing and joining terms

def find_all_geo_terms(mods_item):
    print(uuid, "|".join([x.text for x in mods_item.findall("./subject/geographic")]))
    return "|".join([x.text for x in mods_item.findall("./subject/geographic")])

#  Open file in write mode and query api for terms

with open('api_query_results.csv', 'w') as f:

    writer = csv.writer(f)

    # loop thru pages

    for page in range(page_count, 0, -1):
        call = requests.get(base_query_url + "&page={0}".format(page), headers={'Authorization': auth},stream=True)
        call.raw.decode_content = True
        elems = ET.parse(call.raw)

        # parse each result and yank uuid and make mods query

        for element in elems.iter('result'):
            uuid = element.find("./uuid").text
            mods_call = requests.get(mods_query_url + uuid + '.xml', headers={'Authorization': auth},stream=True)
            mods_call.raw.decode_content = True
            mods_items = ET.parse(mods_call.raw)

            # write uuid with all geo subject terms to file

            for mods_item in mods_items.iter('mods'):
                 writer.writerow([uuid, find_all_geo_terms(mods_item)])

input('\n\n*** query results saved to api_query_results.csv, press <enter>')
