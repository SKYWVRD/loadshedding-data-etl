import requests
import json

MY_HEADERS = {'token': ''}

response = requests.get('https://developer.sepush.co.za/business/2.0/status', headers = my_headers)
json_object = json.loads(response.text)

print(json_object["status"]['capetown']['stage'])
print(json_object["status"]['eskom']['stage'])

# with open('test.json', 'w') as json_file:
#     json_file.write(response.text)
