import pdb
import cipher


def run(keystore_data):
    text_or_files = input("Would you like to run oracle for [F]iles of [T]ext?: ")
    number_of_entities = int(input("How many entities would you like to encrypt?: "))

    if text_or_files == "F":
        oracle_files(number_of_entities, keystore_data)
    else:
        oracle_text(number_of_entities, keystore_data)


def oracle_files(number_of_entities, keystore_data):
    message = "File path: \n"
    file_paths = get_input(number_of_entities, message)
    encrypted_file_paths = cipher.perform_encryption(file_paths, keystore_data, False)

    for m_path, c_path in zip(file_paths, encrypted_file_paths):
        print(f"plain path: {m_path} encrypted path: {c_path}")


def oracle_text(number_of_entities, keystore_data):
    message = "Message: \n"
    messages = get_input(number_of_entities, message)
    plaintext_messages = messages
    messages = [bytes(m, "utf-8") for m in messages]
    ciphertexts = cipher.perform_encryption(messages, keystore_data, True)

    for m, c in zip(plaintext_messages, ciphertexts):
        c = "".join("{:02x}".format(b) for b in bytearray(c))
        print(f"m: {m} c: {c}")


def get_input(number_of_entities, message):
    return [input(message) for _ in range(number_of_entities)]
