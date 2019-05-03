import requests
import json

data = []

def get_full_json(url):

	a = requests.get(url)

	if a.status_code == 404:
		with open('data.json', 'a') as outfile:
			json.dump(data, outfile)

		return "404"
	
	publicbody = a.json()
	# data = []
	
	for p in publicbody["objects"]["results"]:
		data.append(p)


def generate_next_url(url):
	number = 50

	while True:
		full_url = url + str(number)

		number += 50

#		if number >= 1000:
#			raise StopIteration()

		yield full_url

# davon dann full_json getten bis es nicht mehr geht

for url in generate_next_url("https://fragdenstaat.de/api/v1/publicbody/?limit=50&offset="):
	b = get_full_json(url)
	if b == "404":
		print("404. Stopping")
		break

#generator = generate_next_url("https://fragdenstaat.de/api/v1/publicbody/?limit=50&offset=")
#next(generator)
#next(generator)
#next(generator)

# get_full_json("https://fragdenstaat.de/api/v1/publicbody/")