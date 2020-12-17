RUN_TEST = True
TEST_SOLUTION = 4
TEST_INPUT_FILE = 'test_input_day_07.txt'
INPUT_FILE = 'input_day_07.txt'

ARGS = []


def main_part1(input_file, ):
    with open(input_file) as file:
        rules = list(map(lambda line: line.replace('bags', 'bag').rstrip('.\n'),
                         file.readlines()))

    color_dict = get_color_dict(rules)

    solution = ...
    return solution


def get_color_dict(rules):
    color_dict = dict()
    for rule in rules:
        key_color, color_rules = rule.split(' bag contain ')
        if color_rules.startswith('no'):
            color_rules = (0, None)
        else:
            color_rules = color_rules.replace(' bag', '').split(', ')
            color_rules = list(map(lambda cr: (int(cr[0]), cr[1:]), color_rules))  # input only uses single digit numbers
        color_dict[key_color] = color_rules
    return color_dict


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
