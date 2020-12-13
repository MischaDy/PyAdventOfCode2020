from functools import lru_cache, reduce

"""
Arrangements for first test

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
"""

RUN_TEST = False
TEST1_SOLUTION = 8
TEST2_SOLUTION = 19208
CUR_TEST_SOLUTION = TEST2_SOLUTION

TEST_INPUT1_FILE = 'test_input1_day_10.txt'
TEST_INPUT2_FILE = 'test_input2_day_10.txt'
CUR_TEST_INPUT_FILE = TEST_INPUT2_FILE

INPUT_FILE = 'input_day_10.txt'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    joltages = sorted(map(int, lines))
    joltages.insert(0, 0)
    joltages.append(max(joltages) + 3)

    all_but_first_joltages = joltages[1:]
    all_but_last_joltages = joltages[:-1]
    diffs = list(map(lambda tup: tup[0] - tup[1], zip(all_but_first_joltages, all_but_last_joltages)))

    # is ignoring 2s correct???
    ones_diffs = list(filter(lambda diff_sublist: diff_sublist[0] == 1, split_list(diffs, 3)))
    ones_diffs_lens = list(map(len, ones_diffs))

    solution = prod(map(lambda ones_diff_len: tribonacci(ones_diff_len + 2), ones_diffs_lens))
    return solution


@lru_cache
def tribonacci(n):
    if 0 <= n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


def split_list(list_, separator):
    output_list = []

    lower_ind = 0
    for upper_ind, elem in enumerate(list_):
        if elem == separator:
            if lower_ind != upper_ind:
                output_list.append(list_[lower_ind: upper_ind])
            lower_ind = upper_ind + 1
    return output_list


def prod(list_):
    return reduce(lambda a, b: a * b, list_, 1)


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(CUR_TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (CUR_TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)




# def is_valid_sequence(nums):
#     nums = sorted(nums)
#     all_but_first_nums = nums[1:]
#     all_but_last_nums = nums[:-1]
#     diffs = list(map(lambda tup: tup[0] - tup[1], zip(all_but_first_nums, all_but_last_nums)))
#
#     return len(list(filter(lambda diff: diff > 3, diffs))) == 0
#
#
# def my_test():
#     from itertools import combinations
#     from functools import reduce
#
#     LIM = 12
#     for n in range(2, LIM+1):
#         nums = list(range(n))
#
#         nums_combos = [list(combinations(nums[1:-1], length)) for length in range(n - 1)]
#         nums_combos = flatten_one_level(nums_combos, reduce)
#
#         seqs = map(lambda nums_combo: remove_all(nums[:], nums_combo), nums_combos)
#         valid_seqs = filter(is_valid_sequence, seqs)
#         print(len(list(valid_seqs)))
#
#
# def remove_all(list_, elements):
#     # remove all elements from list_
#     list(map(list_.remove, elements))
#     return list_
#
#
# def flatten_one_level(list_, reduce):
#     return reduce(lambda l1, l2: l1 + l2, list_, [])
#
#
# my_test()
