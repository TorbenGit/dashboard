import requests
import json
import sys

try:
  categorie = str(sys.argv[1])
except:
  categorie = 'e5'

output = ''
key = open('key.json')
for line in key:
 output += line
key.close()
api_key = json.loads(output)['key'] 

stations = ''

output = ''
stellen = open('tankstellen.json', 'r')
for line in stellen:
 output += line 
stellen.close()
output = json.loads(output)

for i, stns in enumerate(output):
  stations += stns['id']
  if i+1 < len(output):
    stations += ',' 

req = 'https://creativecommons.tankerkoenig.de/json/prices.php?ids='
req += stations
req += '&apikey=' + api_key

r = requests.get(req)
answer = json.loads(r.text)

result = []

for x in output:
  if answer['prices'][x['id']]['status'] == 'open':
    result.append({
        "name": x['brand'] + ' ' + x['place'],
        "price": str(answer['prices'][x['id']][categorie])[:-1]
    })

print(result)