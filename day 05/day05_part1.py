RUN_TEST = False
TEST_SOLUTIONS = [(44, 5, 357), (70, 7, 567), (14, 7, 119), (102, 4, 820)]
TEST_INPUT_FILE = 'test_input_day_05.txt'
INPUT_FILE = 'input_day_05.txt'

NUM_ROWS = 128
NUM_COLS = 8
LOWER_HALF_CHARS = 'FL'
UPPER_HALF_CHARS = 'BR'

ARGS = []


def main_part1(input_file, ):
    with open(input_file) as file:
        passes = list(map(lambda line: line.rstrip(), file.readlines()))

    solutions = []
    for pass_ in passes:
        row, col = get_seat(pass_)
        seat_id = row * 8 + col
        solutions.append((row, col, seat_id))
    return max(solutions, key=lambda trip: trip[2])


def get_seat(pass_):
    row_spec, col_spec = pass_[:7], pass_[7:]
    row = bin_search(row_spec, NUM_ROWS - 1)
    col = bin_search(col_spec, NUM_COLS - 1)
    return row, col


def bin_search(spec, high_bound):
    low_bound = 0
    for char in spec:
        if char in LOWER_HALF_CHARS:
            high_bound = high_bound - int((high_bound - low_bound + 1) / 2)
        else:
            low_bound = low_bound + int((high_bound - low_bound + 1) / 2)

    return low_bound  # this should = high_bound


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
