from itertools import product

RUN_TEST = True
TEST_SOLUTION = 37
TEST_INPUT_FILE = 'test_input_day_11.txt'
INPUT_FILE = 'input_day_11.txt'


MIN_NUM_SEATS_TO_MAKE_EMPTY = 4

ARGS = [MIN_NUM_SEATS_TO_MAKE_EMPTY]


def main_part1(input_file, min_num_seats_to_make_empty):
    with open(input_file) as file:
        seat_occupations = list(map(lambda line: line.rstrip(), file.readlines()))

    prev_seat_occupations = None
    cur_seat_occupations = list(map(list, seat_occupations))

    iteration_num = 0
    while cur_seat_occupations != prev_seat_occupations:
        print(iteration_num)
        prev_seat_occupations = cur_seat_occupations
        cur_seat_occupations = evolve(cur_seat_occupations, min_num_seats_to_make_empty)
        iteration_num += 1
    print()

    solution = count_occupied_seats(cur_seat_occupations)
    return solution


def evolve(seat_occupations, min_num_seats_to_make_empty):
    dim = len(seat_occupations)  # side length of occupations square
    evolved_seat_occupations = []
    for row_index, seat_row in enumerate(seat_occupations):
        evolved_seat_row = []
        for pos_index, position in enumerate(seat_row):
            num_adj_occ_seats = count_adjacent_occupied_seats(row_index, pos_index, seat_occupations, dim)
            if position == 'L' and num_adj_occ_seats == 0:
                new_position = '#'
            elif position == '#' and num_adj_occ_seats >= min_num_seats_to_make_empty:
                new_position = 'L'
            else:
                new_position = position

            evolved_seat_row.append(new_position)
        evolved_seat_occupations.append(evolved_seat_row)

    return evolved_seat_occupations


def count_adjacent_occupied_seats(row_index, pos_index, seat_occupations, dim):
    # relative_positions_to_count
    rel_pos_to_count = list(product([-1, 0, 1], repeat=2))
    rel_pos_to_count.remove((0, 0))  # don't consider position itself, only neighbors

    potential_abs_pos_to_count = list(map(lambda tup: (row_index + tup[0], pos_index + tup[1]),
                                          rel_pos_to_count))
    abs_pos_to_count = list(filter(lambda tup: 0 <= tup[0] < dim and 0 <= tup[1] < dim,
                                   potential_abs_pos_to_count))
    num_occ_adj_seats = list(map(lambda tup: seat_occupations[tup[0]][tup[1]],
                                 abs_pos_to_count)
                             ).count('#')
    return num_occ_adj_seats


def count_occupied_seats(seat_occupations):
    return sum(map(lambda seat_row: seat_row.count('#'), seat_occupations))


def print_seat_occupations(seat_occupations):
    output = '\n'.join(map(''.join, seat_occupations))
    print(output)


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
