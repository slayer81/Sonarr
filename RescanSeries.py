#! /Users/scott/anaconda3/bin/python3

import requests
import os
import json

# Now, let's add our new Program to Sonarr, via POST
command_url = "http://localhost:8989/api/command/"

headers = {'x-api-key': "{}".format(os.environ.get('sonarr_api_key')), 'Content-Type': 'application/json'}
body = { "name" : "RescanSeries" }

rescan_post = requests.post(command_url, data=json.dumps(body), headers = headers)

if rescan_post.status_code == 201:
    print("Rescanning All Series")
else:
    print("Return Status Code: {}".format(rescan_post.status_code))
    print("Error message: {}".format(rescan_post.raw))