from functools import reduce
from typing import Tuple, Optional, List, Mapping

from timeit import default_timer

"""
Runtime current implementation up until 10 Mio:
17.1414813s

Replacing try-except by if-else (unpythonic!, undone):
+-0.5s

Baseline without printing (kept):
-1.5s

Baseline, map and tuple instead of for-loop (undone):
-0.1s

Baseline, map and reduce instead of for-loop (undone):
+0.4s

Baseline, remember last spoken number in variable rather than using turn history (kept):
-2.8s

Baseline, remove history from turn history object (kept):
-2.7s

Baseline, remove last spoken number from turn history object:
-3.1s

Baseline, store only one turn per spoken number (kept!!):
-16.4!!!

Baseline, remove get older times spoken method (kept) (what happened?? random fluctuations?):
-9.4

Baseline, don't use class (kept):
-13.4

Baseline, retry if-else instead of try-except - same result (undone):
-13.5

*Correct switching places of starting_nums and enumeration*
 
Baseline, use strings as dict keys (undone):
-11.0


"""

_TEMP_BASELINE = 17.1414813


RUN_TEST = False
TEST_SOLUTIONS = [175594, 2578, 3544142, 261214, 6895259, 18, 362]  # 436 (for 2020)
TEST_INPUT_FILE = 'test_input_day_15.txt'
INPUT_FILE = 'input_day_15.txt'

TURNS_LIM = 30000000

ARGS = [TURNS_LIM]


def main_part2(input_file, turns_lim):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    if RUN_TEST:
        solutions = []
        for line in lines:
            solution = play_game(line, turns_lim)
            solutions.append(solution)
        return solutions
    else:
        solution = play_game(lines[0], turns_lim)
        return solution


def play_game(line, turns_lim):
    starting_nums = get_starting_nums(line)
    # store last times the number was spoken
    last_times_spoken_dict = dict(zip(starting_nums,
                                      range(1, len(starting_nums) + 1)))
    last_time_spoken = None  # assume that starting nums contain no duplicates
    for turn in range(len(starting_nums) + 1, turns_lim + 1):
        if last_time_spoken is None:
            spoken_num = 0
        else:
            spoken_num = (turn - 1) - last_time_spoken

        try:
            last_time_spoken = last_times_spoken_dict[spoken_num]
        except KeyError:
            last_time_spoken = None

        last_times_spoken_dict[spoken_num] = turn

    solution = spoken_num
    return solution


def get_starting_nums(line):
    return list(map(int, line.split(',')))


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        t1 = default_timer()
        solution = main_part2(INPUT_FILE, *ARGS)
        t2 = default_timer()
        t_diff = t2 - t1
        print(solution, '\n', t_diff)  #  - _TEMP_BASELINE)
