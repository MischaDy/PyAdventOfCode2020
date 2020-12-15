RUN_TEST = False
TEST_SOLUTIONS = [(44, 5, 357), (70, 7, 567), (14, 7, 119), (102, 4, 820)]
TEST_INPUT_FILE = 'test_input_day_05.txt'
INPUT_FILE = 'input_day_05.txt'

NUM_ROWS = 128
NUM_COLS = 8
LOWER_HALF_CHARS = 'FL'
UPPER_HALF_CHARS = 'BR'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        passes = list(map(lambda line: line.rstrip(), file.readlines()))

    seat_ids = []
    for pass_ in passes:
        row, col = get_seat(pass_)
        seat_ids.append(row * 8 + col)

    seat_ids.sort()
    my_seat_id = find_missing_seat_id(seat_ids)
    solution = my_seat_id
    return solution


def find_missing_seat_id(seat_ids):
    shifted_seat_ids = seat_ids[1:] + [seat_ids[-1] + 1]
    diffs = list(map(lambda tup: tup[0] - tup[1], zip(shifted_seat_ids, seat_ids)))
    seat_before_missing = seat_ids[diffs.index(2)]
    return seat_before_missing + 1


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

    return low_bound  # should = high_bound


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
