from utilities.parsing import *

input_file = '..//inputs//day2mini.txt'


def main_fun():
    bag_contents = {"red": 12, "green": 13, "blue": 14}
    games = parse_input()

def colour_list(game):
    print("in colour list")
    edited_string = game.replace(";", ",")
    print(edited_string)
    print(edited_string.split(","))
    print("edited string " + edited_string)

def max_cubes_shown(colour, game):

    colour_list(game)

    instances_of_colour = game.count(colour)

    if instances_of_colour == 0:
        return 0

    # from space reverse to space
    # for x in range(instances_of_colour):
    #     index = game.find(colour)
    #     print(int(game[index - 2]))

def parse_input():
    game_list = []

    str_list = read_in_file_to_str_list(input_file)
    print(str_list)

    for game in str_list:
        game_start = game.find(":") + 1
        game_dictionary = {
            "id": game[5],
            "blue": max_cubes_shown("blue", game[game_start:]),
            "red": max_cubes_shown("red", game[game_start:]),
            "green": max_cubes_shown("green", game[game_start])
        }

        game_list.append(game_dictionary)

    print(game_list)
    return game_list


parse_input()
