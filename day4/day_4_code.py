input_file = '..//inputs//day4.txt'


def main_fun():
    total_point = 0
    file1 = open(input_file, 'r')
    lines = file1.readlines()

    for line in lines:
        game_card = line[line.index(":") + 1:]
        game_list = game_card.strip().split("|")
        winning_numbers = game_list[0].strip().replace(" ", ",").split(",")
        lottery_numbers = game_list[1].strip().replace("  ", " ").replace(" ", ",").split(",")

        card_score = get_card_score(winning_numbers, lottery_numbers)

        total_point += card_score
    return total_point


def get_card_score(winning_numbers, lottery_numbers):
    card_score = 0
    for winning_number in winning_numbers:
        if winning_number in lottery_numbers:
            if card_score == 0:
                card_score = 1
            else:
                card_score *= 2
    return card_score


print(main_fun())
