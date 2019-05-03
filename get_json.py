import requests
import json


def get_full_json(url):

	a = requests.get(url)
	publicbody = a.json()
	data = []
	
	for p in publicbody["objects"]["results"]:
		data.append(p)

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)


def generate_next_url(url):
	number = 50

	while True:
		full_url = url + str(number)

		number += 50 

		yield full_url, number

# davon dann full_json getten bis es nicht mehr geht

#generator = generate_next_url("https://fragdenstaat.de/api/v1/publicbody/?limit=50&offset=")
#next(generator)
#next(generator)
#next(generator)

# get_full_json("https://fragdenstaat.de/api/v1/publicbody/")