import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censord_user_list = {}
    
    for user in user_list:
        filter_user_list= {user['company']['name'] : user['name']}
        result = censorship(filter_user_list)

        if result == True:
            censord_user_list[user['company']['name']] = [user['name']]
    
    return censord_user_list


def censorship(filter_user_list):
    for key in filter_user_list:
        if key in black_list:
            print(f'{key}소속의 {filter_user_list[key]} 은/는 등록할 수 없습니다.')
            return False
        else:
            print(f'이상 없습니다.')
            return True

user_list = []

for i in range(6):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i+1)
    response = requests.get(API_URL)
    parsed_data = response.json()
    user_list.append(parsed_data)

print(create_user(user_list))