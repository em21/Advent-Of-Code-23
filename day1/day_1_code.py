from utilities.parsing import *

input_file = '..//inputs//day1.txt'


def main_fun():
    count = 0
    str_list = read_in_file_to_str_list(input_file)
    for line in str_list:
        count += int(get_calibration(line))
    print(count)
    return count


def get_calibration(line):
    string_of_digits = ""

    for character in line:
        if character.isdigit():
            string_of_digits += character
    return string_of_digits[0] + string_of_digits[len(string_of_digits) - 1]


main_fun()
