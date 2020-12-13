from itertools import combinations


RUN_TEST = False
TEST_SOLUTION = 127
TEST_INPUT_FILE = 'test_input_day_09.txt'
INPUT_FILE = 'input_day_09.txt'

PREAMBLE_LENGTH = 25
NUM_OF_PREVIOUS_NUMS = 25  # the number of previous nums which can be used to produce the next num
SUM_LENGTH = 2  # number of numbers to be summed to produce next number

ARGS = [PREAMBLE_LENGTH, NUM_OF_PREVIOUS_NUMS, SUM_LENGTH]


def main_part1(input_file, preamble_length, num_of_previous_nums, sum_length):
    with open(input_file) as file:
        lines = file.readlines()
    nums = list(map(int, lines))

    for cur_index, cur_num in enumerate(nums[preamble_length:], start=preamble_length):
        previous_nums = nums[cur_index - num_of_previous_nums: cur_index]

        if not is_sum_of_previous_nums(previous_nums, cur_num, sum_length):
            break
    else:
        raise RuntimeError('No adequate sum found!')

    solution = cur_num
    return solution


def is_sum_of_previous_nums(previous_nums, cur_num, sum_length):
    num_combos = combinations(previous_nums, sum_length)
    solution_num_combos = list(filter(lambda num_combo: sum(num_combo) == cur_num, num_combos))
    return len(solution_num_combos) != 0


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)

    print(solution)

