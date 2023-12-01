from utilities.parsing import *

input_file = '..//inputs//day1.txt'


def main_fun():
    count = 0
    str_list = read_in_file_to_str_list(input_file)
    for line in str_list:
        count += int(get_calibration_part2(line))
    print(count)
    return count


def get_calibration_part1(line):
    string_of_digits = ""

    for character in line:
        if character.isdigit():
            string_of_digits += character
    return string_of_digits[0] + string_of_digits[len(string_of_digits) - 1]


def get_calibration_part2(line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers_in_string = []

    for index, character in enumerate(line):
        if character.isdigit():
            temp_inner = [character, index]
            numbers_in_string.append(temp_inner)

    for number in numbers:
        if number in line:
            if line.count(number) > 1:
                last_index_temp = [number, line.rfind(number)]
                numbers_in_string.append(last_index_temp)
            inner_list_value = [number, line.find(number)]
            numbers_in_string.append(inner_list_value)

    numbers_in_string.sort(key=lambda x: x[1])
    if not numbers_in_string:
        print("empty list found in: " + line)
        return "0"

    if numbers_in_string[0][0].isdigit():
        first = numbers_in_string[0][0]
    else:
        first = convert_string_number_to_int(numbers_in_string[0][0])

    if numbers_in_string[len(numbers_in_string) - 1][0].isdigit():
        last = numbers_in_string[len(numbers_in_string) - 1][0]
    else:
        last = convert_string_number_to_int(numbers_in_string[len(numbers_in_string) - 1][0])

    return str(first) + str(last)


def convert_string_number_to_int(string_number):
    match string_number.lower():
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return 0


main_fun()
