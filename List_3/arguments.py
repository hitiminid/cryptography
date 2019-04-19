import json
import argparse


def get_arguments():
    args = parse_arguments()
    program_type = select_type(args.type)
    enc_mode = select_encryption_mode(args.enc_mode)

    data = dict(
        type=program_type,
        enc_mode=enc_mode
    )

    with open('data.json', 'r') as f:
        json_object = json.load(f)
        data['key_store_password'] = json_object['store_password']

    return data


def parse_arguments():
    parser = argparse.ArgumentParser()

    # MODES
    parser.add_argument('--type', type=str)  # oracle or challenge
    parser.add_argument('--mode', type=str)  # enc dec
    parser.add_argument('--enc_mode', type=str)  # OTB CTR

    # KEYSTORE
    parser.add_argument('--key_store', type=str)
    parser.add_argument('--key_store_pass', type=str)
    parser.add_argument('--key_id', type=str, required=True)

    return parser.parse_args()


def select_type(selected_type):
    types = ['oracle', 'challenge']
    default = 'oracle'
    exception_msg = 'Error on selecting type!'

    return get_value(selected_type, types, default, exception_msg)


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
    return tuple(getattr(arguments, attr_name) for attr_name in ('mode', 'key_store', 'key_id'))
    # mode = arguments.mode
    # key_store = arguments.key_store
    # key_id = arguments.key_id
    # return mode, key_store, key_id
