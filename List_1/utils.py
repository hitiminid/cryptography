def save_output_to_file(prga):
    with open(file_name, 'a') as output:
        for value in prga:
            line = f'{str(value)}\n'
            output.write(line)
