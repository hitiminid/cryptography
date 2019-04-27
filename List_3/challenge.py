import random
import cipher


def run(keystore_data):
    text_or_file = input('[T]ext or [F]iles? ')

    if text_or_file == 'T':
        challenge_text(keystore_data)
    else:
        challege_files(keystore_data)


# TODO:
def challenge_text(keystore_data):

    message_1 = input('Specify 1st message: ')
    message_2 = input('Specify 2nd message: ')

    b = random.getrandbits(1)

    if b == 0:
        ciphertext = cipher.perform_encryption(message_1, keystore_data, True)
    else:
        ciphertext = cipher.perform_encryption(message_2, keystore_data, True)
    print(ciphertext)


# TODO:
def challege_files(keystore_data):
    file_1_path = input('Specify 1st file path: ')
    file_2_path = input('Specify 2nd file path: ')

    b = random.getrandbits(1)

    if b == 0:
        ciphertext = cipher.perform_encryption(file_1_path,
                                               keystore_data, False)
    else:
        ciphertext = cipher.perform_encryption(file_2_path,
                                               keystore_data, False)
