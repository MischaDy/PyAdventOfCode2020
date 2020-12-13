from math import ceil

RUN_TEST = False
TEST_SOLUTION = 295
TEST_INPUT_FILE = 'test_input_day_13.txt'
INPUT_FILE = 'input_day_13.txt'

ARGS = []


def main_part1(input_file, ):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    earliest_dep = int(lines[0])
    bus_ids = [int(id_) for id_ in filter(lambda id_: id_ != 'x', lines[1].split(','))]
    earliest_dep
    next_hit_timestamps = list(map(
        lambda bus_id: get_next_hit_timestamp_after(earliest_dep, bus_id),
        bus_ids
    ))
    stamps_ids_tups = zip(next_hit_timestamps, bus_ids)
    next_dep, chosen_bus_id = min(stamps_ids_tups)
    waiting_time = next_dep - earliest_dep

    solution = waiting_time * chosen_bus_id
    return solution


def get_next_hit_timestamp_after(timestamp, factor):
    return ceil(timestamp / factor) * factor


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
