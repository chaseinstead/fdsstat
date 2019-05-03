import requests
import json

data = []

def get_full_json(url):

	a = requests.get(url)

	if a.status_code != 200:
		print(a.status_code)

		with open('data_req.json', 'a') as outfile:
			json.dump(data, outfile)

		return "httperror"
	
	publicbody = a.json()
	
	#for p in publicbody["objects"]["results"]:
	for p in publicbody["objects"]:

		data.append(p)

	if publicbody["meta"]["next"] == None:
		with open('data_req.json', 'a') as outfile:
			json.dump(data, outfile)
		return "httperror"


def generate_next_url(url):
	number = 0

	while True:
		full_url = url + str(number)

		number += 50
		
		print("adding", full_url)
		yield full_url

for url in generate_next_url("https://fragdenstaat.de/api/v1/request/?limit=50&offset="):
	b = get_full_json(url)
	if b == "httperror":
		print("http error. Stopping")
		break