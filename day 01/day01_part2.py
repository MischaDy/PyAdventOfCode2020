import os
from itertools import combinations
from functools import reduce


RUN_TEST = False
TEST_SOLUTION = 241861950
TEST_INPUT_FILE = 'test_input_day_01.txt'
INPUT_FILE = 'input_day_01.txt'

COMBO_LENGTH = 3


def main(input_file, combo_length):
    with open(input_file) as file:
        lines = file.readlines()

    nums = list(map(int, lines))
    num_combinations = combinations(nums, combo_length)
    solution_num_combo = next(filter(lambda num_combo: sum(num_combo) == 2020, num_combinations))
    solution = prod(solution_num_combo)  # solution_num_combo[0] * solution_num_combo[1]

    return solution


def prod(factors):
    return reduce(lambda a, b: a * b, factors, 1)


if __name__ == '__main__':
    if RUN_TEST:
        solution = main(TEST_INPUT_FILE, COMBO_LENGTH)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main(INPUT_FILE, COMBO_LENGTH)

    print(solution)

