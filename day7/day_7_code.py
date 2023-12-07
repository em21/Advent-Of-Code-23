from utilities.parsing import read_in_file_to_str_list

input_file = '..//inputs//day7.txt'


def stronger_hand_three(actual_hand1, actual_hand2):
    full_house1 = is_x_oak(2, actual_hand1)
    full_house2 = is_x_oak(2, actual_hand2)

    if (full_house1 and full_house2) or (not full_house1 and not full_house2):
        return stronger_first_card(actual_hand1, actual_hand2)
    if full_house2:
        return True
    return False


def stronger_first_card(actual_hand1, actual_hand2):
    if actual_hand1[0].isdigit() and actual_hand2[0].isalpha():
        return True
    if actual_hand1[0].isalpha() and actual_hand2[0].isdigit():
        return False

    if actual_hand1[0].isdigit() and actual_hand2[0].isdigit():
        if int(actual_hand1[0]) == int(actual_hand2[0]):
            return stronger_first_card(actual_hand1[1:], actual_hand2[1:])
        if int(actual_hand1[0]) < int(actual_hand2[0]):
            return True
        else:
            return False

    # [a, k, q, j, t]
    if actual_hand1[0].isalpha() and actual_hand2[0].isalpha():
        if actual_hand1[0] == actual_hand2[0]:
            return stronger_first_card(actual_hand1[1:], actual_hand2[1:])

        if actual_hand2[0] == "A":
            return True
        if actual_hand1[0] == "A":
            return False
        if actual_hand2[0] == "K":
            return True
        if actual_hand1[0] == "K":
            return False
        if actual_hand2[0] == "Q":
            return True
        if actual_hand1[0] == "Q":
            return False
        if actual_hand2[0] == "J":
            return True
        if actual_hand1[0] == "J":
            return False
        if actual_hand2[0] == "T":
            return True
        if actual_hand1[0] == "T":
            return False

    return False


def is_fullhouse(actual_hand2):
    count = 0
    for char in actual_hand2:
        if actual_hand2.count(char) == 2:
            count += 1
    if count == 4:
        return True
    return False


def stronger_two_card(actual_hand1, actual_hand2):
    full_house1 = is_fullhouse(actual_hand1)
    full_house2 = is_fullhouse(actual_hand2)

    if (full_house1 and full_house2) or (not full_house1 and not full_house2):
        return stronger_first_card(actual_hand1, actual_hand2)
    if full_house2:
        return True
    return False


def should_swap(hand1, hand2):
    actual_hand1 = hand1.split(" ")[0]
    actual_hand2 = hand2.split(" ")[0]

    if actual_hand1[0].isdigit() and actual_hand2[0].isalpha():
        return True
    if actual_hand1[0].isalpha() and actual_hand2[0].isdigit():
        return False

    fiveoak1 = is_x_oak(5, actual_hand1)
    fiveoak2 = is_x_oak(5, actual_hand2)

    fouroak1 = is_x_oak(4, actual_hand1)
    fouroak2 = is_x_oak(4, actual_hand2)

    threeCard1 = is_x_oak(3, actual_hand1)
    threeCard2 = is_x_oak(3, actual_hand2)

    twoCard1 = is_x_oak(2, actual_hand1)
    twoCard2 = is_x_oak(2, actual_hand2)

    if fiveoak1 or fiveoak2:
        if fiveoak1 and fiveoak2:
            return stronger_first_card(actual_hand1, actual_hand2)
        if fiveoak1:
            return True
        return False

    if fouroak1 or fouroak2:
        if fouroak1 and fouroak2:
            return stronger_first_card(actual_hand1, actual_hand2)
        if fouroak1:
            return True
        return False

    if threeCard1 or threeCard2:
        if threeCard1 and threeCard2:
            return stronger_hand_three(actual_hand1, actual_hand2)
        if threeCard1:
            return False
        return True

    if twoCard1 or twoCard2:
        if twoCard1 and twoCard1:
            return stronger_two_card(actual_hand1, actual_hand2)
        if twoCard1:
            return False
        return True

    return stronger_first_card(actual_hand1, actual_hand2)


def is_x_oak(x, hand):
    for card in range(4):
        if hand.count(hand[card]) == x:
            return True
    return False


def sort_hands(input_hand_list):
    n = len(input_hand_list)

    for i in range(n):
        swapped = False
        for j in range(n - 1):

            if should_swap(input_hand_list[j], input_hand_list[j + 1]):
                temp = input_hand_list[j]
                input_hand_list[j] = input_hand_list[j + 1]
                input_hand_list[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return input_hand_list


def calculate_winnings(sorted_hands_list):
    ranks_available = len(sorted_hands_list)
    total = 0

    for hand in sorted_hands_list:
        total += (int(hand.split(" ")[1]) * ranks_available)
        ranks_available -= 1

    return total


hand_list = read_in_file_to_str_list(input_file)

sorted_hands_list = sort_hands(hand_list)
print(sorted_hands_list)

print(calculate_winnings(sorted_hands_list))

# TODO: '66TT7 634' & '669TT 208'