from utilities.parsing import *

input_file = '..//inputs//day2.txt'


def max_cubes_shown(colour, game):
    current_max = 0
    game_list = game.split(",")

    for cubes in game_list:
        number_of_cubes = int(cubes[:cubes.find(" ")])
        colour_of_cubes = cubes[cubes.find(" "):]

        if colour == colour_of_cubes.strip():
            if current_max < number_of_cubes:
                current_max = number_of_cubes

    return current_max


def is_possible(game_dictionary):
    bag_contents = {"red": 12, "green": 13, "blue": 14}

    red_possible = bag_contents["red"] >= game_dictionary["red"]
    green_possible = bag_contents["green"] >= game_dictionary["green"]
    blue_possible = bag_contents["blue"] >= game_dictionary["blue"]

    return red_possible and green_possible and blue_possible


def power_set(game_dictionary):
    return game_dictionary["red"] * game_dictionary["green"] * game_dictionary["blue"]


def main_fun():
    possible_count = 0

    file1 = open(input_file, 'r')
    lines = file1.readlines()

    for line in lines:
        game_id = int(line[line.find(" "): line.find(":")])
        index = line.find(":")
        game = line[index + 1:].strip().replace(", ", ",").replace("; ", ",")

        game_dictionary = {
            "id": game_id,
            "blue": max_cubes_shown("blue", game),
            "red": max_cubes_shown("red", game),
            "green": max_cubes_shown("green", game)
        }

        possible_count += power_set(game_dictionary)

        # if is_possible(game_dictionary):
        #
        #     possible_count += game_id

    return possible_count


print(main_fun())
