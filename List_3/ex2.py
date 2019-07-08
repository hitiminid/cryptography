import os
import random
import string
import uuid
import pdb
import subprocess
import key_store
from keystore_data import KeyStoreData


def main():

    key_identifier = "encryption_key"
    path = "keystore.jceks"
    password = "password"
    key = key_store.get_password(path, password, key_identifier)
    mode = "-aes-256-cbc"
    perform_challenge(key, mode)


def perform_challenge(key, mode):
    # QUERY
    # 1)
    # send random message and get iv and it's ciphertext
    base = generate_iv_base()
    iv = hex(int(base + "00", 2))[2:]

    # 2)
    # send IV+1 in order to receive E(IV+1 xor IV+1) = E(000...)
    iv_plus_one = hex(int(base + "01", 2))[2:]

    query_m = iv_plus_one
    query_iv = iv_plus_one

    query_c = run_encryption(query_m, query_iv, mode, key)

    # CHALLENGE
    # send m1 = IV+2 and m2 = some random message

    iv_plus_two = hex(int(base + "10", 2))[2:]
    challenge_iv = iv_plus_two

    challenge_m_1 = iv_plus_two
    challenge_m_2 = uuid.uuid4().hex

    selected_message = select_message()

    m = challenge_m_1 if selected_message == 1 else challenge_m_2

    challenge_c = run_encryption(m, challenge_iv, mode, key)

    print(f"Random selected message {selected_message+1} to encrypt")

    if challenge_c == query_c:
        print("It's IV")
    else:
        print("It's random message")


def select_message():
    return random.randint(0, 1)


def generate_iv_base():
    base = "".join([str(random.randint(0, 1)) for _ in range(126)])
    # os.urandom(15).hex()
    iv = base + "00"
    return base


def run_encryption(message, iv, encryption_mode, key):
    open_ssl_commands = [
        "openssl",
        "enc",
        "-e",
        f"{encryption_mode}",
        "-K",
        f"{key}",
        "-iv",
        f"{iv}",
        "-nopad",
    ]

    ciphertext = subprocess.check_output(
        open_ssl_commands, input=bytes.fromhex(message)
    )
    return ciphertext


if __name__ == "__main__":
    main()
