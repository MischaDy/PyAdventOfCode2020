from functools import lru_cache, reduce
from itertools import combinations
from math import ceil, sqrt

import numpy as np

RUN_TEST = False
TEST_SOLUTIONS = [3417, 1068781, 754018, 779210, 1261476, 1202161486]
TEST_INPUT_FILE = 'test_input_day_13.txt'
INPUT_FILE = 'input_day_13.txt'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    if not RUN_TEST:
        inds_and_nums = [(ind, int(elem)) for ind, elem in enumerate(lines[1].split(',')) if elem != 'x']

        rests, divisors = [], []
        for (ind, num) in inds_and_nums:
            rests.append((-ind) % num)
            divisors.append(num)

        solution = chinese_remainder(rests, divisors)
        return solution

    else:
        print(chinese_remainder([2, 1, 3], [3, 4, 5]))

        solutions = []
        for line in lines:
            inds_and_nums = [(ind, int(elem)) for ind, elem in enumerate(line.split(',')) if elem != 'x']

            rests, divisors = [], []
            for (ind, num) in inds_and_nums:
                rests.append((-ind) % num)
                divisors.append(num)

            solution = chinese_remainder(rests, divisors)
            solutions.append(solution)
        return solutions


def chinese_remainder(remainders, divisors):
    M = prod(divisors)
    as_ = list(map(lambda d: int(M / d), divisors))
    eea_results = map(lambda tup: extended_gcd(*tup), zip(as_, divisors))
    is_ = [result[0] % div for result, div in zip(eea_results, divisors)]
    # is_ = list(map(lambda tup: tup[0] % tup[1], zip(as_, divisors)))
    Z = sum(map(prod, zip(is_, remainders, as_)))
    x = Z % M
    return x


def prod(nums):
    return reduce(lambda a, b: a * b, nums, 1)


def extended_gcd(a, b):
    # EEA
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return Bezout coefficient 1, 2, and the gcd
    return old_s, old_t, old_r



# @lru_cache
# def is_prime(n):
#     for possible_div in range(2, ceil(sqrt(n)) + 1):
#         if n % possible_div == 0:
#             return False
#     return True


# def get_next_hit_timestamp_after(timestamp, factor):
#     return ceil(timestamp / factor) * factor

# def are_pairwise_coprime(nums):
#     nums_combos = list(combinations(nums, 2))
#     return all(map(lambda tup: are_coprime(*tup), nums_combos))
#
#
# def are_coprime(a, b):
#     return gcd(a, b) == 1
#
#
# def gcd(a, b):
#     if a == b:
#         return a
#     elif a > b:
#         return gcd(a - b, b)
#     else:
#         return gcd(a, b - a)


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
