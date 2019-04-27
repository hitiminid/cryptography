import pdb
import unittest
import random
import parameterized

import key_store
import cipher
from keystore_data import KeyStoreData

MODES = {'blowfish', 'camellia-128-cbc', 'camellia-128-cfb8',
         'des-ede3-ofb', 'camellia128', 'bf-ecb', 'aes-128-cfb8',
         'bf-cbc', 'camellia-256-cfb8', 'bf', 'camellia-192-ofb',
         'desx', 'des-ede-cbc', 'des-ede3', 'rc2-64-cbc', 'des-ede-cfb',
         'des-ede', 'camellia-128-cfb1', 'camellia-128-ofb', 'bf-cfb',
         'aes-256-cfb8', 'aes-128-cfb', 'aes256', 'camellia-256-ecb',
         'des-cfb', 'rc2-cbc', 'aes-192-ofb', 'des-ede3-cfb8', 'des-cbc',
         'camellia-192-cfb8', 'aes-128-ofb', 'aes-256-ctr', 'camellia-192-ecb',
         'gost89-ecb', 'des-ede3-cbc', 'aes128', 'gost89-cnt', 'rc2-40-cbc',
         'camellia-256-cbc', 'des-cfb1', 'camellia-256-cfb', 'cast', 'cast5-cbc',
         'gost89', 'cast-cbc', 'des-ede3-cfb', 'rc2-cfb', 'des3', 'aes-192-cfb1',
         'aes-256-cfb1', 'aes-256-cbc', 'rc2-ofb', 'chacha', 'camellia192', 'aes-128-cbc',
         'aes-128-cfb1', 'cast5-ecb', 'aes-192-cbc', 'des-cfb8', 'des-ecb', 'des-ede-ofb',
         'camellia-192-cbc', 'aes-256-ecb', 'aes-192-cfb', 'camellia256', 'camellia-192-cfb1',
         'rc4', 'rc4-hmac-md5', 'camellia-128-ecb', 'aes-128-ctr', 'camellia-192-cfb', 'cast5-cfb', 'des',
         'camellia-256-ofb', 'rc2-ecb', 'aes-128-ecb', 'camellia-256-cfb1', 'des-ofb',
         'aes-192-cfb8', 'aes-256-cfb', 'rc2', 'desx-cbc', 'cast5-ofb', 'bf-ofb', 'rc4-40',
         'aes-192-ecb', 'aes-192-ctr', 'aes192', 'camellia-128-cfb', 'aes-256-ofb'}


class Testing(unittest.TestCase):

    def setUp(self):
        keystore_path = 'keystore.jceks'
        keystore_password = 'test1234'
        key_identifier = 'secretkey1'

        self.key = key_store.get_password(keystore_path,
                                          keystore_password,
                                          key_identifier)

    @parameterized.parameterized.expand(MODES)
    def test_mode(self, mode):

        message = '123456'
        message = bytes(message, 'utf-8')
        message = [message]

        encrypted = self.encrypt_data(message, mode)
        decrypted = self.decrypt_data(encrypted, mode)

        self.assertEqual(message, decrypted)

    def encrypt_data(self, message, mode):
        encrypted = cipher.encrypt_text(message, mode, self.key)
        return encrypted

    def decrypt_data(self, ciphertext, mode):
        decrypted = cipher.decrypt_text(ciphertext, mode, self.key)
        return decrypted


if __name__ == '__main__':
    unittest.main()
