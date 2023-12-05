input_file = '..//inputs//day4.txt'


def main_fun():
    total_point = 0
    file1 = open(input_file, 'r')
    lines = file1.readlines()

    for line in lines:
        card_score = 0
        game_card = line[line.index(":") + 1:]
        game_list = game_card.strip().split("|")
        winning_numbers = game_list[0].strip().replace(" ", ",").split(",")
        lottery_numbers = game_list[1].strip().replace("  ", " ").replace(" ", ",").split(",")

        for winning_number in winning_numbers:
            if winning_number in lottery_numbers:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        total_point += card_score
    return total_point


print(main_fun())
