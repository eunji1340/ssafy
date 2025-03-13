import requests
from pprint import pprint as print

dummy_data = []

for i in range(10):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i+1)
    response = requests.get(API_URL)
    parsed_data = response.json()
    dic = {'company' : parsed_data['company']['name']}

    if float(parsed_data['address']['geo']['lat']) < 80:
        dic['lat'] = parsed_data['address']['geo']['lat']

    if float(parsed_data['address']['geo']['lng']) > -80:
        dic['lng'] = parsed_data['address']['geo']['lng']
    
    dic['name'] = parsed_data['name']
    dummy_data.append(dic)

print(dummy_data)