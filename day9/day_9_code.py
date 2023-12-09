input_file = '..//inputs//day9.txt'


def get_steps(line, list_of_values):
    new_step = []
    if line.count(0) == len(line):
        return list_of_values
    for index in range(1, len(line)):
        difference = int(line[index]) - int(line[index - 1])
        new_step.append(difference)
    list_of_values.append(new_step)
    return get_steps(new_step, list_of_values)


def get_next_value(steps):
    count = 0
    for step in steps:
        count += int(step[-1])
    return count


def get_first_value(steps2):
    count = 0
    for x in reversed(steps2):
        count = int(x[0])-count
    return count

def main_fun():
    count = 0
    with open(input_file) as file:
        input_read = file.read().split("\n")
        for line in input_read:
            line_to_list = line.strip().split(" ")
            steps = get_steps(line_to_list, [line_to_list])
            count += get_first_value(steps)
    return count

print(main_fun())
