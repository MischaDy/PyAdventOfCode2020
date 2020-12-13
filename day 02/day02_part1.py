RUN_TEST = False
TEST_SOLUTION = 2
TEST_INPUT_FILE = 'test_input_day_02.txt'
INPUT_FILE = 'input_day_02.txt'

ARGS = []


def main_part1(input_file, ):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    rule_pw_tuples = list(map(lambda line: line.split(': '), lines))
    solution = sum(map(lambda tup: is_valid_pw(*tup), rule_pw_tuples))
    return solution


def is_valid_pw(rule, pw):
    min_num_apps, max_num_apps, char = analyze_rule(rule)
    real_num_apps = pw.count(char)
    return min_num_apps <= real_num_apps <= max_num_apps


def analyze_rule(rule):
    # return minimum and maximum number of appearances of that character
    nums_apps, char = rule.split(' ')
    min_num_apps, max_num_apps = map(int, nums_apps.split('-'))
    return min_num_apps, max_num_apps, char


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)

    print(solution)
