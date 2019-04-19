import string
import collections.abc
import argparse
import subprocess
import json
import arguments
import random


ARGS = arguments.get_arguments()


def run_oracle():
    # name = raw_input("What's your name? ")
    # oracle_e = raw_input('Would you like to run oracle for [F]iles of [T]ext?\n')
    number_of_entities = input(
        'How many entities would you like to encrypt?\n')
    messages = oracle_text(number_of_entities)


def oracle_text(number_of_entities):
    messages = []
    for _ in range(int(number_of_entities)):
        msg = input('Message: \n')
        messages.append(msg)
    return messages


def run_challenge():
    text_or_file = input('[T]ext or [F]iles? ')

    if text_or_file == 'T':
        challenge_text()
    else:
        challege_files()


def challenge_text():

    message_1 = input('Specify 1st message: ')
    message_2 = input('Specify 2nd message: ')

    b = random.getrandbits(1)

    if b == 0:
        ciphertext = perform_encryption(message_1)
    else:
        ciphertext = perform_encryption(message_2)

    print(ciphertext)


def challege_files():
    file_1_path = input('Specify 1st file path: ')
    file_2_path = input('Specify 2nd file path: ')

    b = random.getrandbits(1)

    if b == 0:
        ciphertext = perform_encryption(file_1_path)
    else:
        ciphertext = perform_encryption(file_2_path)


def perform_encryption(messages):
    messages = messages if isinstance(messages, list) else [messages]
    ciphertexts = []

    passphrase = ARGS['key_store_password']

    for message in messages:
        echo_message = ['echo', '-n', f"{message}"]
        open_ssl_commands = ['openssl', 'enc',
                             '-aes-256-cbc', '-nosalt', '-k', f'{passphrase}']

        ps = subprocess.Popen(echo_message, stdout=subprocess.PIPE)
        ciphertext = subprocess.check_output(
            open_ssl_commands, stdin=ps.stdout)
        ciphertext = ciphertext.decode('ascii', 'ignore')
        ciphertexts.append(ciphertext)

    for m, c in zip(messages, ciphertexts):
        print(f'm:{m} c:{c}')

    return ciphertexts


def encrypt(data: bytearray):
    ...


def main():

    # breakpoint()
    if ARGS['type'] == 'oracle':
        run_oracle()
    else:
        run_challenge()


if __name__ == '__main__':
    main()


def generate_password(length=64):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_iv(length=64):
    return ''.join(random.choices(string.hexdigits, k=length))
