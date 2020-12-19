# from enum import Enum
from itertools import product

from helpers.misc_functions import flatten_list_1_level, flatten_list_n_levels

RUN_TEST = False
TEST_SOLUTION = 848
TEST_INPUT_FILE = 'test_input_day_17.txt'
INPUT_FILE = 'input_day_17.txt'

RULES = {'#': [2, 3], '.': [3]}
ITERATIONS = 6

ARGS = [RULES, ITERATIONS]


# TODO: also *remove* rows/layers, if outer hull is "double-empty"?
def main_part2(input_file, rules, iterations):
    with open(input_file) as file:
        z0 = list(map(lambda line: line.rstrip(), file.readlines()))

    hyperlayers = [[z0]]
    print_hyperlayers(hyperlayers)
    for i in range(iterations):
        print(i)
        hyperlayers = add_margins_if_needed(hyperlayers)
        hyperlayers = perform_cycle(hyperlayers, rules)
        # print_hyperlayers(hyperlayers)

    solution = count_active_cubes(hyperlayers)
    return solution


def perform_cycle(hyperlayers, rules):
    # We assume: All cubes in/on outer hull are inactive
    new_hyperlayers = []
    num_hyperlayers = len(hyperlayers)
    num_layers = len(hyperlayers[0])
    num_rows_cols = len(hyperlayers[0][0])
    for w in range(num_hyperlayers):
        new_hyperlayer = []
        for z in range(num_layers):
            new_layer = []
            for x in range(num_rows_cols):
                new_row = []
                for y in range(num_rows_cols):
                    hypercube_state = get_hypercube_state(x, y, z, w, hyperlayers)
                    active_neighbors_needed = rules[hypercube_state]
                    if count_active_neighbors(x, y, z, w, hyperlayers) in active_neighbors_needed:
                        new_row.append('#')
                    else:
                        new_row.append('.')
                new_layer.append(''.join(new_row))
            new_hyperlayer.append(new_layer)
        new_hyperlayers.append(new_hyperlayer)

    return new_hyperlayers


def count_active_neighbors(x, y, z, w, hyperlayers):
    return get_neighbors(x, y, z, w, hyperlayers).count('#')


def get_neighbors(x, y, z, w, hyperlayers):
    ind_shifts = list(product((-1, 0, 1), repeat=4))
    ind_shifts.remove((0, 0, 0, 0))
    neighbors_inds = [(x + x_shift, y + y_shift, z + z_shift, w + w_shift)
                      for (x_shift, y_shift, z_shift, w_shift) in ind_shifts]
    neighbors = [get_hypercube_state(*indices, hyperlayers) for indices in neighbors_inds]
    return neighbors


def add_margins_if_needed(hyperlayers):
    if not should_add_margins(hyperlayers):
        return hyperlayers

    # ex_row = hyperlayers[0][0][0]  # example_row
    # new_hyperlayers = []
    # for hyperlayer in hyperlayers:
    #     to_be_added = [[create_inactive_row(ex_row)] + layer + [create_inactive_row(ex_row)] for layer in hyperlayer]
    #     new_hyperlayer = add_inactive_layers(to_be_added)
    #     new_hyperlayers.append(new_hyperlayer)

    # new_hyperlayers = []
    # for hyperlayer in hyperlayers:
    #     to_be_added = [[create_inactive_row(ex_row)] + layer + [create_inactive_row(ex_row)] for layer in hyperlayer]
    #     new_hyperlayer = add_inactive_layers(to_be_added)
    #     new_hyperlayers.append(new_hyperlayer)

    new_hyperlayers = []
    for hyperlayer in hyperlayers:
        new_hyperlayer = []
        for layer in hyperlayer:
            new_layer = add_inactive_rows(['.' + row + '.' for row in layer])
            new_hyperlayer.append(new_layer)
        new_hyperlayer = add_inactive_layers(new_hyperlayer)
        new_hyperlayers.append(new_hyperlayer)
    new_hyperlayers = add_inactive_hyperlayers(new_hyperlayers)

    return new_hyperlayers


# def add_margins_if_needed_old(layers):
#     if not should_add_margins(layers):
#         return layers
#
#     new_layers = []
#     for layer in layers:
#         new_layer = add_inactive_rows(['.' + row + '.' for row in layer])
#         new_layers.append(new_layer)
#     new_layers = add_inactive_layers(new_layers)
#
#     return new_layers


def add_inactive_rows(layer):
    """
    Add an inactive row to beginning and end of layer, respectively.
    :param layer:
    :return:
    """
    # Note: layer = rows
    inactive_row = create_inactive_row(layer[0])  # row is just string, so pass by value
    return [inactive_row] + layer + [inactive_row]


def add_inactive_layers(layers):
    """
    Add an inactive layer before and after layers, respectively.
    :param layers:
    :return:
    """
    # layer is list, so pass by value --> create twice
    return [create_inactive_layer(layers[0])] + layers + [create_inactive_layer(layers[0])]


def add_inactive_hyperlayers(hyperlayers):
    """
    Add an inactive hyperlayer before and after hyperlayers, respectively.
    :param hyperlayers:
    :return:
    """
    return [create_inactive_hyperlayer(hyperlayers[0])] + hyperlayers + [create_inactive_hyperlayer(hyperlayers[0])]


def should_add_margins(hyperlayers):
    # return True iff >= 1 active cubes are in/on the outer perimeter of stored cube
    if not are_inactive_hyperlayers([hyperlayers[0], hyperlayers[-1]]):
        return True

    for hyperlayer in hyperlayers[1:-1]:  # check for 'perimeter activity' in inner layers
        for layer in hyperlayer:
            first_row, last_row = layer[0], layer[-1]
            if '#' in first_row or '#' in last_row:
                return True
            first_and_last_cols = [row[0] + row[-1] for row in layer]
            if '#' in first_and_last_cols:
                return True
    return False


def create_inactive_hyperlayer(example_hyperlayer):
    return [create_inactive_layer(layer) for layer in example_hyperlayer]


def create_inactive_layer(example_layer):
    return [create_inactive_row(row) for row in example_layer]


def create_inactive_row(example_row):
    return len(example_row) * '.'


def get_hypercube_state(x, y, z, w, hyperlayers):
    try:
        return hyperlayers[w][z][x][y]
    except IndexError:
        return '.'


def are_inactive_hyperlayers(hyperlayers):
    return count_active_cubes(hyperlayers) == 0


def count_active_cubes(hyperlayers):
    return ''.join(flatten_list_n_levels(hyperlayers, 2)).count('#')


def print_hyperlayers(hyperlayers):
    output_list = ['']
    start_ind_hyperlayers = -1 * (len(hyperlayers) // 2)
    for w_ind, hyperlayer in enumerate(hyperlayers, start=start_ind_hyperlayers):
        start_ind_layers = -1 * (len(hyperlayer) // 2)
        for z_ind, layer in enumerate(hyperlayer, start=start_ind_layers):
            output_list.append(f'z={z_ind}, w={w_ind}')
            output_list.extend(layer)
            output_list.append('')
    print('\n'.join(output_list), end='\n\n')


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
