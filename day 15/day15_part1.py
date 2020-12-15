from typing import Tuple, Optional, List, Mapping

RUN_TEST = False
TEST_SOLUTIONS = [436, 1, 10, 27, 78, 438, 1836]
TEST_INPUT_FILE = 'test_input_day_15.txt'
INPUT_FILE = 'input_day_15.txt'

TURNS_LIM = 2020

ARGS = [TURNS_LIM]


class TurnHistory:
    def __init__(self, starting_nums: List[int]):
        self.history = starting_nums.copy()
        # store last two times the number was spoken as tuple: (older, newer)
        self.last_times_spoken_dict: Mapping[int, Tuple[Optional[int], int]] = dict()
        for ind, num in enumerate(starting_nums, start=1):
            self.last_times_spoken_dict[num] = (None, ind)
        self.last_spoken_num = starting_nums[-1]

    def record(self, num: int, turn: int) -> None:
        try:
            recent_entry = self.last_times_spoken_dict[num][1]
        except KeyError:
            recent_entry = None
        self.last_times_spoken_dict[num] = (recent_entry, turn)
        self.last_spoken_num = num

    def get_recent_time_spoken(self, num) -> int:
        return self.last_times_spoken_dict[num][1]

    def get_older_time_spoken(self, num) -> Optional[int]:
        return self.last_times_spoken_dict[num][0]

    def get_last_spoken_num(self):
        return self.last_spoken_num


def main_part1(input_file, turns_lim):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # store members of form {number : (turn when it was last spoken, number of times it was spoken)}
    # mem_dict = dict((num, (turn, 1)) for num, turn in zip(starting_nums, range(1, len(starting_nums) + 1)))
    # last_spoken_num = starting_nums[-1]
    # for turn in range(len(starting_nums) + 1, TURNS_LIM + 1):
    #     if mem_dict[last_spoken_num][1] == 1:
    #         spoken_num = 0
    #     else:
    #

    if RUN_TEST:
        solutions = []
        for line in lines:
            starting_nums = get_starting_nums(line)
            turn_history = TurnHistory(starting_nums)
            next_turn = len(starting_nums) + 1
            for turn in range(next_turn, turns_lim + 1):
                last_spoken_num = turn_history.get_last_spoken_num()
                if turn_history.get_older_time_spoken(last_spoken_num) is None:
                    spoken_num = 0
                else:
                    prev_turn = turn_history.get_recent_time_spoken(last_spoken_num)
                    spoken_num = prev_turn - turn_history.get_older_time_spoken(last_spoken_num)
                turn_history.record(spoken_num, turn)

            solutions.append(turn_history.get_last_spoken_num())
        return solutions


    starting_nums = get_starting_nums(lines[0])
    turn_history = TurnHistory(starting_nums)
    next_turn = len(starting_nums) + 1
    for turn in range(next_turn, turns_lim + 1):
        last_spoken_num = turn_history.get_last_spoken_num()
        if turn_history.get_older_time_spoken(last_spoken_num) is None:
            spoken_num = 0
        else:
            prev_turn = turn_history.get_recent_time_spoken(last_spoken_num)
            spoken_num = prev_turn - turn_history.get_older_time_spoken(last_spoken_num)
        turn_history.record(spoken_num, turn)

    solution = turn_history.get_last_spoken_num()
    return solution



def get_starting_nums(line):
    return list(map(int, line.split(',')))


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
