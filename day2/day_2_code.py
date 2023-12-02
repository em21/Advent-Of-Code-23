from utilities.parsing import *

input_file = '..//inputs//day2mini.txt'


def main_fun():
    bag_contents = {"red": 12, "green": 13, "blue": 14}
    games = parse_input()

def max_cubes_shown(colour, game):
    current_max = 0
    instances_of_colour = game.count(colour)

    index = game.find(colour)

    print(game[index-2])
    return game[index-2]

def parse_input():
    game_list =[]

    str_list = read_in_file_to_str_list(input_file)
    print(str_list)

    for game in str_list:
        game_dictionary = {
            "id": game[5],
            "blue": max_cubes_shown("blue", game),
            "red": max_cubes_shown("red", game),
            "green": max_cubes_shown("green", game)
        }

        game_list.append(game_dictionary)

    print(game_list)
    return game_list


parse_input()
