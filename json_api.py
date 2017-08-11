
import urllib.parse
import requests

main_api = 'http://maps.google.com/maps/api/geocode/json?'

#address = 'karachi'

while True:
 
 address = input('address: ')
 if address == 'quit' or address == 'q':
  break
  
 url = main_api + urllib.parse.urlencode({'address':address})

 json_data = requests.get(url).json()
 #print(json_data)

 print(url)

 json_status = json_data['status']
 print('API Status >> ' + json_status)
 print()

 if json_status == 'OK':
   for each in json_data['results'][0]['address_components']:
     print (each['long_name'])
   formatted_address = json_data['results'][0]['formatted_address']
   print(formatted_address)




