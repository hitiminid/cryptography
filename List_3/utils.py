import json


def get_default_values():
    with open(file_path, 'r') as f:
        data = json.load(f)
        key = data['key_store_path']
    return key


file_path = '/home/pietrek/UCZELNIA/MGR/cryptography/List_3/data.json'
print(get_default_values())
