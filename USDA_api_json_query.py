#!/usr/bin/env python

import os
import requests
import json

api_key = os.environ['MY_USDA_API_KEY']

url_json = 'https://api.nal.usda.gov/usda/ndb/nutrients/?fg=0400&format=json&api_key=' + api_key + '&nutrients=606&nutrients=645&nutrients=646'

r = requests.get(url_json)
data = json.loads(r.text)

print data
