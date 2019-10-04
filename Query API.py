import requests, os, json

sonarrAPIKey = os.environ.get('sonarr_api_key')
status_url = "http://localhost:8989/api/system/status?apikey={}".format(sonarrAPIKey)
url = 'http://localhost:8989/api/series?apikey={}'.format(sonarrAPIKey)
sonarr_series_title = 'City on a Hill'


response = json.loads(requests.get(url).text)

# Here is a List of Dictionaries for all the Series
# series = json.loads(response.text)
print("type: {}".format(type(series)))

# How many Program Titles
print("The number of Series Titles is {}".format(len(series)))

oldschoolSeries = []
# Standard way to loop through List of Dictionaries to get complete list of all Series
for row in series:
    for k, v in row.items():
        if k == 'title':
            oldschoolSeries.append(v)
            # print(v)

# Using List Comprehension to do the same:
SeriesInfo = [[(k,v) for k,v in s.items()] for s in series]
# print(series.items())
print("Series Info: {}".format(SeriesInfo))

# >> [[(k,v) for k,v in d.items() if k not in ['b','u']] for d in ld]
SeriesValues = [[(v) for k,v in s.items() if k =='title'] for s in series]
print("Series Values: {}".format(SeriesValues))

'''
LIST COMPREHENSION EXAMPLES
ld = [{'a': 10, 'b': 20}, {'p': 10, 'u': 100}]

> [[(k,v) for k,v in d.items()] for d in ld]
[[('a', 10), ('b', 20)], [('p', 10), ('u', 100)]]

>> [[(k,v) for k,v in d.items() if k not in ['b','u']] for d in ld]
[[('a', 10)], [('p', 10)]]
'''