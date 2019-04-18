import argparse


def get_arguments():
    args = parse_arguments()

    type = select_type(args.type)
    enc_mode = select_encryption_mode(args.enc_mode)

    data = dict(
        type=type,
        enc_mode=enc_mode
    )

    return data


def parse_arguments():
    parser = argparse.ArgumentParser()

    # MODES
    parser.add_argument('--type', type=str)  # oracle or challenge
    parser.add_argument('--mode', type=str)
    parser.add_argument('--enc_mode', type=str)

    # KEYSTORE
    parser.add_argument('--key_store', type=str)
    parser.add_argument('--key_store_pass', type=str)
    parser.add_argument('--key_id', type=str)

    args = parser.parse_args()
    return args


def select_type(type):
    types = ['oracle', 'challenge']
    default = 'oracle'

    return get_value(type, types, default)


def select_encryption_mode(mode_name):
    options = ['OFB', 'CTR', 'CBC']
    default = 'CBC'
    exception_msg = 'Error on selecting mode!'
    return get_value(mode_name, options, default, exception_msg)


def get_value(choice, options, default, exception_msg='Error during argument parsing!'):
    if choice is None:
        return default
    elif choice in options:
        return choice
    else:
        raise Exception(exception_msg)


def get_values(arguments):
    mode = arguments.mode
    key_store = arguments.key_store
    key_id = arguments.key_id
    return mode, key_store, key_id
