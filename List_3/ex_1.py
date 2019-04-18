import argparse
import subprocess
import json
import arguments
import random


def run_oracle():
    # name = raw_input("What's your name? ")
    # oracle_e = raw_input('Would you like to run oracle for [F]iles of [T]ext?\n')
    number_of_entities = raw_input('How many entities would you like to encrypt?\n')
    messages = oracle_text(number_of_entities)


def oracle_text(number_of_entities):
    messages = []
    for i in range(int(number_of_entities)):
        msg = raw_input('Message: \n')
        messages.append(msg)
    return messages
    # print(messages)


def run_challenge():
    # get two messag
    b = random.getrandbits(1)
    # if b == 0:
    # return perform_encryption(message_1)
    # else:
    # return perform_encryption(message_2)


def perform_encryption(messages):
    ciphertexts = []
    for message in messages:
        # subprocess.call(f'echo -n "{message}" | openssl enc -e -aes-256-cbc -a -salt', shell=True),
        # subprocess.call(f'echo -n "{message}" |
        ps = subprocess.Popen(['echo', '-n', f"{message}"], stdout=subprocess.PIPE)
        ciphertext = subprocess.check_output(
            ['openssl', 'enc', '-aes-256-cbc', '-a', '-salt'], stdin=ps.stdout)
        ciphertext = ciphertext.decode('ascii', 'ignore')
        ciphertexts.append(ciphertext)

    for m, c in zip(messages, ciphertexts):
        print(f'm:{m} c:{c}')


def main():
    arg = arguments.get_arguments()
    print(arg)

    # if arguments.type == 'oracle':
    #     run_oracle()
    # else:
    #     run_challenge()


if __name__ == '__main__':
    main()
    # messages = ['aaaa']
    # perform_encryption(messages)

    # run_challenge()
