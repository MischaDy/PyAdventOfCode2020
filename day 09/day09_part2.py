from day09_part1 import *

RUN_TEST = False
TEST_SOLUTION = 62
TEST_INPUT_FILE = 'test_input_day_09.txt'
INPUT_FILE = 'input_day_09.txt'

PREAMBLE_LENGTH = 25
NUM_OF_PREVIOUS_NUMS = 25  # the number of previous nums which can be used to produce the next num
SUM_LENGTH = 2  # number of numbers to be summed to produce next number

ARGS = [PREAMBLE_LENGTH, NUM_OF_PREVIOUS_NUMS, SUM_LENGTH]


def main_part2(input_file, *args):
    with open(input_file) as file:
        lines = file.readlines()
    nums = list(map(int, lines))

    invalid_number = main_part1(input_file, *args)
    contiguous_sets = gen_contiguous_sets(nums)

    solution_contiguous_sets = None
    for set_ in contiguous_sets:
        if sum(set_) == invalid_number:
            solution_contiguous_sets = set_
            break
    else:
        raise RuntimeError('No adequate set found!')

    solution = min(solution_contiguous_sets) + max(solution_contiguous_sets)
    return solution


def gen_contiguous_sets(nums):
    len_nums = len(nums)
    for first_index in range(0, len_nums - 1):  # leave 2 nums 'space' at the end
        for second_index in range(first_index + 1, len_nums):  # leave 2 nums 'space' at start
            yield nums[first_index: second_index + 1]  # include last element


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)

    print(solution)
