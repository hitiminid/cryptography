import random
import string
import uuid
import pdb
import subprocess
import key_store
from keystore_data import KeyStoreData


def main():

    keystore_data = KeyStoreData(
        key_identifier='secretkey1',
        path='keystore.jceks',
        password='test1234',
        encryption_mode='aes-256-cbc'
    )

    key = key_store.get_password(keystore_data.path,
                                 keystore_data.password,
                                 keystore_data.key_identifier)
    iv, iv_plus_one = generate_ivs()

    ciphertext_1 = run_ecryption(iv, keystore_data.encryption_mode, iv, key)
    # ciphertext_2 = run_ecryption(iv_plus_one, keystore_data.encryption_mode,
    #                              iv_plus_one, key)

    cpa(keystore_data, iv_plus_one, key, ciphertext_1)
    # pdb.set_trace()


def cpa(keystore_data, iv_plus_one, key, old_ciphertext):
    m0 = ''.join(random.choices(string.ascii_letters + string.digits, k=256))
    m1 = '0' * 256

    b = random.randint(0, 1)
    m = m1 if b == 1 else m0

    ciphertext = run_ecryption(m, keystore_data.encryption_mode,
                               iv_plus_one, key)
    # pdb.set_trace()
    if ciphertext == old_ciphertext:
        print('First one')
    else:
        print('Second one')

    # pdb.set_trace()


def generate_ivs():
    iv = uuid.uuid4().int >> 32
    iv_plus_one = iv + 1
    iv = hex(iv)
    iv_plus_one = hex(iv_plus_one)
    return iv, iv_plus_one


def run_ecryption(message, encryption_mode, iv, key):
    # pdb.set_trace()
    echo_message = ['echo', '-n', f"{message}"]
    open_ssl_commands = ['openssl', 'enc',
                         f'{encryption_mode}', '-nosalt',
                         '-k', f'{key}',
                         '-IV', f'{iv}',
                         '-nopad'
                         ]

    ps = subprocess.Popen(echo_message, stdout=subprocess.PIPE)
    ciphertext = subprocess.check_output(
        open_ssl_commands, stdin=ps.stdout)
    return ciphertext


if __name__ == '__main__':
    main()
