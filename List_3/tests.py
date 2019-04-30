import pdb
import unittest
import random
import parameterized

import key_store
import cipher
from keystore_data import KeyStoreData


def load_encryption_modes():
    modes = []
    with open("modes") as file:
        for line in file:
            mode = line.strip()
            modes.append(mode)
    return modes


MODES = load_encryption_modes()


class Testing(unittest.TestCase):
    def setUp(self):
        keystore_path = "keystore.jceks"
        keystore_password = "password"
        key_identifier = "encryption_key"

        self.key = key_store.get_password(
            keystore_path, keystore_password, key_identifier
        )

    @parameterized.parameterized.expand(MODES)
    def test_mode(self, mode):

        message = "123456"
        message = bytes(message, "utf-8")
        message = [message]
        mode = "-" + mode

        encrypted = self.encrypt_data(message, mode)
        decrypted = self.decrypt_data(encrypted, mode)

        self.assertEqual(message, decrypted)

    def encrypt_data(self, message, mode):
        encrypted = cipher.encrypt_text(message, mode, self.key)
        return encrypted

    def decrypt_data(self, ciphertext, mode):
        decrypted = cipher.decrypt_text(ciphertext, mode, self.key)
        return decrypted


if __name__ == "__main__":
    unittest.main()
