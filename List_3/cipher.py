import subprocess
import key_store
import pdb


def perform_encryption(messages: list, keystore_data, is_text_encryption: bool):

    messages = messages if isinstance(messages, list) else [messages]
    key = key_store.get_password(
        keystore_data.path, keystore_data.password, keystore_data.key_identifier
    )
    if is_text_encryption:
        return encrypt_text(messages, keystore_data.encryption_mode, key)
    else:
        return encrypt_files(messages, keystore_data.encryption_mode, key)


def encrypt_text(plaintexts: list, encryption_mode: str, key: str):

    ciphertexts = []

    for message in plaintexts:

        open_ssl_commands = [
            "openssl",
            "enc",
            f"-{encryption_mode}",
            "-nosalt",
            "-k",
            f"{key}",
        ]
        ciphertext = subprocess.check_output(open_ssl_commands, input=message)
        ciphertexts.append(ciphertext)

    return ciphertexts


def encrypt_files(file_paths: list, encryption_mode: str, key: str, challenge: bool):

    if challenge:
        for path in file_paths:
            open_ssl_commands = [
                "openssl",
                "enc",
                f"-{encryption_mode}",
                "-nosalt",
                "-k",
                f"{key}",
                "-in",
                f"{path}",
                "out",
                f"challenge.enc",
            ]
            subprocess.check_output(open_ssl_commands)

    else:
        for path in file_paths:
            open_ssl_commands = [
                "openssl",
                "enc",
                f"{encryption_mode}",
                "-nosalt",
                "-k",
                f"{key}",
                "-in",
                f"{path}",
                "out",
                f"{path}.enc",
            ]
            subprocess.check_output(open_ssl_commands)


##### DECRYPTION #####


def perform_decryption(
    ciphertexts: list, keystore_data, encryption_mode: str, is_text_decryption: bool
):

    ciphertexts = ciphertexts if isinstance(ciphertexts, list) else [ciphertexts]

    key = key_store.get_password(
        keystore_data.path, keystore_data.password, keystore_data.key_identifier
    )

    if is_text_decryption:
        encrypt_text(ciphertexts, encryption_mode, key)
    else:
        decrypt_files(ciphertexts, encryption_mode, key)


def decrypt_text(ciphertexts: list, encryption_mode: str, key: str) -> list:
    plaintexts = []

    for ciphertext in ciphertexts:
        open_ssl_commands = [
            "openssl",
            "enc",
            "-d",
            f"{encryption_mode}",
            "-nosalt",
            "-k",
            f"{key}",
        ]
        plaintext = subprocess.check_output(open_ssl_commands, input=ciphertext)
        plaintexts.append(plaintext)

    return plaintexts


def decrypt_files(file_paths, encryption_mode, key):

    for path in file_paths:
        open_ssl_commands = [
            "openssl",
            "enc",
            "-d",
            f"{encryption_mode}",
            "-nosalt",
            "-k",
            f"{key}",
            "-in",
            f"{path}",
            "-out",
            f"{path}.dec",
        ]
        output = subprocess.check_output(open_ssl_commands)
