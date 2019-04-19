
def run():
    text_or_files = input(
        'Would you like to run oracle for [F]iles of [T]ext?\n')
    number_of_entities = int(input(
        'How many entities would you like to encrypt?: '))

    if text_or_files == 'F':
        oracle_files(number_of_entities)
    else:
        oracle_text(number_of_entities)


def oracle_files(number_of_entities):
    message = 'File path: \n'
    file_paths = get_input(number_of_entities, message)
    print(file_paths)


def oracle_text(number_of_entities):
    message = 'Message: \n'
    messages = get_input(number_of_entities, message)
    print(messages)


def get_input(number_of_entities, message):
    return [input(message) for _ in range(number_of_entities)]
