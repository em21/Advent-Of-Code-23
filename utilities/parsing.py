def read_in_file_to_string(input_file):
    contents = ""
    with open(input_file) as file:
        file_contents = file.read()
        contents += file_contents
    return contents


def read_in_file_to_str_list(input_file):
    contents = read_in_file_to_string(input_file)
    return str.splitlines(contents)


def read_in_file_to_int_array(input_file):
    array = read_in_file_to_str_list(input_file)
    return [int(x) for x in array]


def read_in_file_to_mixed_list(input_file):
    initial_list = read_in_file_to_str_list(input_file)
    new_list = list()
    for line in initial_list:
        x = str.split(line)
        new_list.append(x)

    return new_list
