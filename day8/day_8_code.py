from utilities.parsing import *

input_file = "..//inputs//day8.txt"


def main_fun():
    puzzle_input = read_in_file_to_string(input_file)
    directions = get_directions(puzzle_input)
    string_format_map = "{" + puzzle_input[puzzle_input.index("\n"):].replace("=", ":").strip().replace("\n", ",") + "}"
    puzzle_map = eval(string_format_map)
    print(traverse_map(directions, puzzle_map, "AAA", 0))


def traverse_map(directions, puzzle_map, starting_point, current_count):
    current_point = starting_point
    count = current_count
    for direction in directions:
        coordinate = puzzle_map.get(current_point)
        current_point = coordinate[int(direction)]
        count += 1
        if current_point == "ZZZ":
            return count
    return traverse_map(directions, puzzle_map, current_point, count)


def get_directions(in_string):
    directions = []
    digit_string = in_string.replace("L", "0").replace("R", "1")
    for direction in digit_string:
        if direction != "\n":
            directions.append(direction)
        else:
            break
    return directions


main_fun()
