import pdb
import jks


def get_password(keystore_path, keystore_password, key_identifier):
    ks = jks.KeyStore.load(keystore_path, keystore_password)
    secret_key = ks.secret_keys[key_identifier]
    key = "".join("{:02x}".format(b) for b in bytearray(secret_key.key))
    return key
