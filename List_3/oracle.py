import pdb
import cipher


def run(keystore_data):
    text_or_files = input(
        'Would you like to run oracle for [F]iles of [T]ext?\n')
    number_of_entities = int(input(
        'How many entities would you like to encrypt?: '))

    if text_or_files == 'F':
        oracle_files(number_of_entities, keystore_data)
    else:
        oracle_text(number_of_entities, keystore_data)


# TODO:
def oracle_files(number_of_entities, keystore_data):
    message = 'File path: \n'
    file_paths = get_input(number_of_entities, message)


def oracle_text(number_of_entities, keystore_data):
    message = 'Message: \n'
    messages = get_input(number_of_entities, message)
    messages = [bytes(m, 'utf-8') for m in messages]
    # pdb.set_trace()
    ciphertexts = cipher.perform_encryption(messages, keystore_data, True)

    for m, c in zip(messages, ciphertexts):
        print(f'm: {m} c: {c}')


def get_input(number_of_entities, message):
    return [input(message) for _ in range(number_of_entities)]
