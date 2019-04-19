import random
import string
# import json
# def get_default_values():
#     with open(file_path, 'r') as f:
#         data = json.load(f)
#         key = data['key_store_path']
#     return key


# file_path = '/home/pietrek/UCZELNIA/MGR/cryptography/List_3/data.json'
# print(get_default_values())
def generate_password(key_len=64, iv_len=32):
    # return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    key = generate_random_hexdigits(key_len)
    iv = generate_random_hexdigits(iv_len)
    print(f'key: {key} iv: {iv}')
    return key + iv


def generate_random_hexdigits(length=64):
    return ''.join(random.choices(string.hexdigits, k=length))
