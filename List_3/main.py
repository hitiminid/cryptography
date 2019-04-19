import arguments
import challenge
import oracle
import keyring


ARGS = arguments.get_arguments()


def main():
    # key_iv = generate_password()
    # key = key_iv[:64]
    # iv = key_iv[64:]

    # key_tool_command_1 = f'keytool - genseckey - keypass $(KEY_PASS) - storepass $(STORE_PASS) - alias test1key'
    # key_tool_command_2 = f'- keyalg AES - keysize 128 - storetype pkcs12 - keystore $(KEY_STORE_NAME)'

    # subprocess.call()
    # print(f'key: {len(key)} iv: {iv}')
    # abc = generate_password()
    # import pdb
    # pdb.set_trace()
    # # breakpoint()

    if ARGS['type'] == 'oracle':
        oracle.run()
    else:
        challenge.run()


# def experiment():
    # keyring.set_password("sy", "1", "password")
    # pwd = keyring.get_password("sy", "1")
    # print(pwd)


if __name__ == '__main__':
    main()
