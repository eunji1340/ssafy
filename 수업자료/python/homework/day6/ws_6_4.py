# 아래 함수를 수정하시오.
def get_keys_from_dict(dict):
    return list(dict.keys())

# def get_all_keys_from_dict(dictionary):
#     result = []
#     for key in dictionary.keys():
#         result.append(key)
#         if type(dictionary[key]) == dict:
#             for key in dictionary[key].keys():
#                 result.append(key)

#     return result

def get_all_keys_from_dict(dictionary):
    result = []

    def extract_keys(d):
        for key, value in d.items():
            result.append(key)
            if isinstance(value, dict):
                extract_keys(value)

    extract_keys(dictionary)
    return result

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'country':{'city':'Seoul', 'population':25}, 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
