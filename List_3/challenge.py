import random
import cipher


def run():
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
        ciphertext = cipher.perform_encryption(message_1)
    else:
        ciphertext = cipher.perform_encryption(message_2)

    # print(ciphertext)


def challege_files():
    file_1_path = input('Specify 1st file path: ')
    file_2_path = input('Specify 2nd file path: ')

    b = random.getrandbits(1)

    if b == 0:
        ciphertext = cipher.perform_encryption(file_1_path, None)
    else:
        ciphertext = cipher.perform_encryption(file_2_path, None)
