def write_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data + '\n')
