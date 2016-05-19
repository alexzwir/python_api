import urllib.request
import json
import codecs


locu_api = 'd54541cb310f27b16cc1501ccca69687d8de1571'

url = 'https://api.locu.com/v1_0/venue/search/?country=Brazil&api_key=d54541cb310f27b16cc1501ccca69687d8de1571'
reader = codecs.getreader("utf-8")

obj = urllib.request.urlopen(url)
data = json.load(reader(obj))

for d in data['objects']:
	print('Restaurante: '+ str(d['name'])+' na cidade de: '+str(d['locality']))

 