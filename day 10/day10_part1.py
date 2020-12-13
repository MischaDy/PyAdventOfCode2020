RUN_TEST = False
TEST1_SOLUTION = 7 * 5
TEST2_SOLUTION = 22 * 10
CUR_TEST_SOLUTION = TEST2_SOLUTION

TEST_INPUT1_FILE = 'test_input1_day_10.txt'
TEST_INPUT2_FILE = 'test_input2_day_10.txt'
CUR_TEST_INPUT_FILE = TEST_INPUT2_FILE

INPUT_FILE = 'input_day_10.txt'

ARGS = []


def main_part1(input_file, ):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    joltages = sorted(map(int, lines))
    joltages.insert(0, 0)
    joltages.append(max(joltages) + 3)

    all_but_first_joltages = joltages[1:]
    all_but_last_joltages = joltages[:-1]
    diffs = list(map(lambda tup: tup[0] - tup[1], zip(all_but_first_joltages, all_but_last_joltages)))
    num_ones = diffs.count(1)
    num_threes = diffs.count(3)

    solution = num_ones * num_threes
    return solution


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(CUR_TEST_INPUT_FILE, *ARGS)
        assert (CUR_TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)

    print(solution)
