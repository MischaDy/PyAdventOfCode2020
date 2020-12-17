from functools import reduce

RUN_TEST = False
TEST_SOLUTION = 6
TEST_INPUT_FILE = 'test_input_day_06.txt'
INPUT_FILE = 'input_day_06.txt'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        data = file.read()

    groups = data.split('\n\n')
    # one set of answers per group member
    groups = map(lambda group: list(map(set, group.split('\n'))),
                 groups)
    intersections = map(lambda group: reduce(lambda s1, s2: s1.intersection(s2), group),
                        groups)
    solution = sum(map(len, intersections))
    return solution


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
