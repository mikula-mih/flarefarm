''' JavaScript Object Notation '''

import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)
print(type(data))

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

######################

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

data.sort(key=state, reverse=True)
# list comprehension
data = [item for item in data if 'state' in item['description']]

########################

import urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/\
        quote?format=json") as response:
        source = response.read()

data = json.loads(source)
print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['name']
    usd_rates[name] = price

##########################

import requests

r = requests.get('https://xkcd.com/353/')
print(dir(r))
print(help(r))
r = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png', 'wb') as f:
    f.write(r.content)
