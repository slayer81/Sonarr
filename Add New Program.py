#! /Users/scott/anaconda3/bin/python3

import requests
import json
import os
import sys

# Get title from input
series_title = str(sys.argv[1])

path_base = "/Volumes/Primary/Video/Fresh_Downloads/"
path_title = series_title.replace(' ', '.')
program_path = path_base + path_title
title_in = series_title.replace(' ', '%20')
series_lookup = "http://localhost:8989/api/series/lookup?term={s}&apikey={k}".format(s = title_in, k = os.environ.get('sonarr_api_key'))

# Query Sonarr for programID, titleSlug and images
lookup = requests.get(series_lookup)

# Convert to json object
response = json.loads(lookup.text)

# Now let's pop all the bits we need to POST into our new dictionary
data_dict = {}
data_dict["tvdbId"] = response[0]["tvdbId"]
data_dict["title"] = response[0]["title"]
data_dict["titleSlug"] = response[0]["titleSlug"]
data_dict["images"] = response[0]["images"]
data_dict["season"] = 1
data_dict["qualityProfileId"] = 3 # 3 = 720p
data_dict["path"] = program_path

# Now, let's add our new Program to Sonarr, via POST
series_add = "http://localhost:8989/api/series"

headers = {'X-Api-Key': "{}".format(os.environ.get('sonarr_api_key')), 'Content-Type': 'application/json'}

postNew = requests.post(series_add, data=json.dumps(data_dict), headers = headers)

if postNew.status_code == 201:
    # print("Return Status Code: {}".format(postNew.status_code))
    print("Successfully added {} to Sonarr".format(response[0]["title"]))
else:
    print("Return Status Code: {}".format(postNew.status_code))
    print("Error adding Program. You suck. Try again later")
    print("Error message: {}".format(postNew.raw))