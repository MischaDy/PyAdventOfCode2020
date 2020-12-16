RUN_TEST = False
TEST_SOLUTION = 26
TEST_INPUT_FILE = 'test_input_day_11.txt'
INPUT_FILE = 'input_day_11.txt'

MIN_NUM_SEATS_TO_MAKE_EMPTY = 5

ARGS = [MIN_NUM_SEATS_TO_MAKE_EMPTY]


def main_part2(input_file, min_num_seats_to_make_empty):
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

    solution = count_total_occupied_seats(cur_seat_occupations)
    return solution


def evolve(seat_occupations, min_num_seats_to_make_empty):
    dim = len(seat_occupations)  # side length of occupations square
    evolved_seat_occupations = []
    for row_index, seat_row in enumerate(seat_occupations):
        evolved_seat_row = []
        for pos_index, position in enumerate(seat_row):
            num_vis_occ_seats = count_visible_occupied_seats(row_index, pos_index, seat_occupations, dim)
            if position == 'L' and num_vis_occ_seats == 0:
                new_position = '#'
            elif position == '#' and num_vis_occ_seats >= min_num_seats_to_make_empty:
                new_position = 'L'
            else:
                new_position = position

            evolved_seat_row.append(new_position)
        evolved_seat_occupations.append(evolved_seat_row)

    return evolved_seat_occupations


def count_visible_occupied_seats(row_index, pos_index, seat_occupations, dim):
    horiz_count = count_horizontally(row_index, pos_index, seat_occupations, dim)
    vert_count = count_vertically(row_index, pos_index, seat_occupations, dim)
    diag_count1 = count_topleft_bottomright(row_index, pos_index, seat_occupations, dim)
    diag_count2 = count_bottomleft_topright(row_index, pos_index, seat_occupations, dim)

    return horiz_count + vert_count + diag_count1 + diag_count2


def count_horizontally(row_index, pos_index, seat_occupations, dim):
    seats = seat_occupations[row_index]
    return count_in_seats(pos_index, seats, dim)


def count_vertically(row_index, pos_index, seat_occupations, dim):
    seats = [seat_occupations[i][pos_index] for i in range(dim)]
    return count_in_seats(row_index, seats, dim)


def count_topleft_bottomright(row_index, pos_index, seat_occupations, dim):
    seats = get_diagonal(row_index, pos_index, seat_occupations, dim, '\\')
    relevant_ind = pos_index if pos_index <= row_index else row_index
    return count_in_seats(relevant_ind, seats, dim)


def count_bottomleft_topright(row_index, pos_index, seat_occupations, dim):
    seats = get_diagonal(row_index, pos_index, seat_occupations, dim, '/')
    if row_index + pos_index <= dim - 1:  # top half = closer to top than to bottom
        relevant_ind = pos_index  # dist to left
    else:
        relevant_ind = (dim - 1) - row_index  # dist to bottom
    return count_in_seats(relevant_ind, seats, dim)


def count_in_seats(index, seats, dim):
    result = 0
    # before current index
    cur_index = index - 1
    while cur_index >= 0:
        if seats[cur_index] == 'L':
            break
        elif seats[cur_index] == '#':
            result += 1
            break
        cur_index -= 1

    # to right
    cur_index = index + 1
    while cur_index < len(seats):
        if seats[cur_index] == 'L':
            break
        elif seats[cur_index] == '#':
            result += 1
            break
        cur_index += 1

    return result


def get_diagonal(row_index, pos_index, seat_occupations, dim, mode):
    if mode == '/':
        # bottom left to top right
        dist_to_bottom = (dim - 1) - row_index  # dist of square to bottom
        dist_to_left = pos_index  # dist of square to left

        if dist_to_left <= dist_to_bottom:
            # row_index = how far down we are; dist_to_left = steps to go
            bottomleft_pos = (row_index + dist_to_left, 0)
        else:
            # row_index = how far down we are; dist_to_left = steps to go
            bottomleft_pos = (dim - 1, pos_index - dist_to_bottom)

        # range_bound = min(row_index, (dim - 1) - pos_index) + 1  # = min(dist_to_top, dist_to_right)
        range_bound = min(bottomleft_pos[0], (dim - 1) - bottomleft_pos[1]) + 1
        diag = [seat_occupations[bottomleft_pos[0] - i][bottomleft_pos[1] + i]
                for i in range(range_bound)]
    else:  # '\'
        # top left to bottom right
        row_pos_diff = row_index - pos_index
        topleft_pos = (row_pos_diff, 0) if row_pos_diff >= 0 else (0, -row_pos_diff)

        diag = [seat_occupations[topleft_pos[0] + i][topleft_pos[1] + i]
                for i in range(dim - max(topleft_pos))]

    return diag


def count_total_occupied_seats(seat_occupations):
    return sum(map(lambda seat_row: seat_row.count('#'), seat_occupations))


def print_seat_occupations(seat_occupations):
    output = '\n'.join(map(''.join, seat_occupations))
    print(output)


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
