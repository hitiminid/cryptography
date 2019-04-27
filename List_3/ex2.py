import random
import string
import uuid
import pdb
import subprocess
import key_store
from keystore_data import KeyStoreData


def main():

    key_identifier = 'secretkey1'
    path = 'keystore.jceks'
    password = 'test1234'
    key = key_store.get_password(path,
                                 password,
                                 key_identifier)

    iv, iv_plus_one = generate_ivs()
    mode = '-aes-256-cbc'

    iv_0 = iv
    m_0 = iv_0
    c_0 = run_encryption(m_0, mode, iv_0, key)

    # Challenge
    iv_1 = iv_plus_one
    m_1 = iv_plus_one

    m_2 = bytes(random.getrandbits(8) for _ in range(16))

    c_1 = run_encryption(m_1, mode, iv_1, key)

    assert c_0 == c_1


def generate_ivs():
    base = ''.join([str(random.randint(0, 1)) for _ in range(127)])
    iv = base + '0'
    iv_plus_one = base + '1'

    iv = hex(int(iv, 2))[2:]
    iv_plus_one = hex(int(iv_plus_one, 2))[2:]

    return iv, iv_plus_one


def run_encryption(message, encryption_mode, iv, key):
    open_ssl_commands = ['openssl', 'enc', '-e',
                         f'{encryption_mode}', '-e',
                         '-K', f'{key}',
                         '-iv', f'{iv}', '-nopad'
                         ]
    # print(open_ssl_commands)
    ciphertext = subprocess.check_output(open_ssl_commands,
                                         input=bytes.fromhex(message))
    return ciphertext


def cpa(keystore_data, iv_plus_one, key, old_ciphertext):
    # m0 = ''.join(random.choices(string.ascii_letters + string.digits, k=128))

    m0 = bytes(random.getrandbits(8) for _ in range(16))
    m1 = bytes.fromhex(iv_plus_one)

    b = random.randint(0, 1)
    m = m1 if b == 1 else m0

    ciphertext = run_encryption(m, keystore_data.encryption_mode,
                                iv_plus_one, key)

    if ciphertext == old_ciphertext:
        print('b = 1')
    else:
        print('b = 0')


if __name__ == '__main__':
    main()

"""

import random
import string
import uuid
import pdb
import subprocess


def main():
    key = 'f5746ab5a66e86da6cbf79c9878bff04'
    iv, iv_plus_one = generate_ivs()
    mode = '-aes-128-cbc'

    iv_0 = iv
    m_0 = iv_0
    c_0 = run_encryption(m_0, mode, iv_0, key)

    m_1 = iv_plus_one
    iv_1 = iv_plus_one
    c_1 = run_encryption(m_1, mode, iv_1, key)

    assert c_0 == c_1


def cpa(enc_mode, iv_plus_one, key, old_ciphertext):
    m0 = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    m1 = iv_plus_one

    b = random.randint(0, 1)
    m = m1 if b == 1 else m0
    print(f'b should equal {b}')
    ciphertext = run_encryption(m, enc_mode,
                                iv_plus_one, key)
    if ciphertext == old_ciphertext:
        print('b = 1')
    else:
        print('b = 0')


def generate_ivs():
    base = ''.join([str(random.randint(0, 1)) for _ in range(127)])
    iv = base + '0'
    iv_plus_one = base + '1'

    iv = hex(int(iv, 2))[2:]
    iv_plus_one = hex(int(iv_plus_one, 2))[2:]

    return iv, iv_plus_one


def run_encryption(message, encryption_mode, iv, key):
    open_ssl_commands = ['openssl', 'enc', '-e',
                         f'{encryption_mode}', '-e',
                         '-K', f'{key}',
                         '-iv', f'{iv}', '-nopad'
                         ]
    ciphertext = subprocess.check_output(
      open_ssl_commands, input=bytes.fromhex(message))
    return ciphertext


if __name__ == '__main__':
    main()
"""
