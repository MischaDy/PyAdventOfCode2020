RUN_TEST = False
TEST_SOLUTION = 1
TEST_INPUT_FILE = 'test_input_day_02.txt'
INPUT_FILE = 'input_day_02.txt'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    rule_pw_tuples = list(map(lambda line: line.split(': '), lines))
    solution = sum(map(lambda tup: is_valid_pw_part2(*tup), rule_pw_tuples))
    return solution


def is_valid_pw_part2(rule, pw):
    index1, index2, char = analyze_rule(rule)
    return xor(pw[index1] == char, pw[index2] == char)


def analyze_rule(rule):
    # return minimum and maximum number of appearances of that character
    indexes, char = rule.split(' ')
    index1, index2 = map(int, indexes.split('-'))
    return index1 - 1, index2 - 1, char  # shift down to get zero-indexing


def xor(a, b):
    # Only valid for boolean inputs
    return a ^ b


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)

    print(solution)
