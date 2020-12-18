# from enum import Enum
from itertools import product

from helpers.misc_functions import flatten_list_1_level

RUN_TEST = False
TEST_SOLUTION = 112
TEST_INPUT_FILE = 'test_input_day_17.txt'
INPUT_FILE = 'input_day_17.txt'

RULES = {'#': [2, 3], '.': [3]}
ITERATIONS = 6

ARGS = [RULES, ITERATIONS]


# class Layer:
#     def __init__(self, init_state=None, size=None):
#         if size is not None:
#             self.state = [['.' for x in range(size)]
#                           for y in range(size)]
#         else:
#             self.state = init_state
#
#     def __len__(self):
#         return len(self.state)
#
#
# class PocketDim:
#     def __init__(self, z0_init_state, rules):
#         self.layers = [Layer(z0_init_state)]
#         self.rules = rules
#
#     def get_layer(self, z_index):
#         # layers indexed symmetrically around the "middle" one
#         shifted_z_ind = z_index + self.get_num_layers() // 2
#         if 0 <= shifted_z_ind < self.get_num_layers():
#             return self.layers[shifted_z_ind]
#
#         if shifted_z_ind < 0:
#             num_iterations = 0 - shifted_z_ind
#             ind = 0
#         else:
#             num_iterations = shifted_z_ind - self.get_num_layers()
#             ind = -1
#         new_neg_layers = [Layer(size=self.get_layer_size()) for _ in range(num_iterations)]
#         new_pos_layers = [Layer(size=self.get_layer_size()) for _ in range(num_iterations)]
#         self.layers = new_neg_layers + self.layers + new_pos_layers
#         return self.layers[ind]
#
#     def get_index_range(self):
#         pass
#
#     def get_num_layers(self):
#         return len(self.layers)
#
#     def get_layer_size(self):
#         # size of all layers should be the same; returned as side length
#         return len(self.z0)
#
#     def perform_cycle(self):
#         for z, layers in enumerate(self.layers, start=-1):
#             new_layer = layers.copy()
#
#             for x, row in enumerate(layers):
#                 for y, cube_state in enumerate(row):
#                     pass
#
#     def count_active_cubes(self):
#         num_active_cubes = 0
#         for layers in self.layers.values():
#             num_active_cubes += sum(map(lambda row: row.count('#'), layers))
#         return num_active_cubes


# TODO: also *remove* rows/layers, if outer hull is "double-empty"?
def main_part1(input_file, rules, iterations):
    with open(input_file) as file:
        z0 = list(map(lambda line: line.rstrip(), file.readlines()))

    layers = [z0]
    print_layers(layers)
    for i in range(iterations):
        # print(i)
        layers = add_margins_if_needed(layers)
        layers = perform_cycle(layers, rules)
        print_layers(layers)

    solution = count_active_cubes(layers)
    return solution


def perform_cycle(layers, rules):
    # We assume: All cubes in/on outer hull are inactive
    new_layers = []
    num_layers = len(layers)
    num_rows_cols = len(layers[0])
    for z in range(num_layers):
        new_layer = []
        for x in range(num_rows_cols):
            new_row = []
            for y in range(num_rows_cols):
                cube_state = get_cube_state(x, y, z, layers)
                active_neighbors_needed = rules[cube_state]
                if count_active_neighbors(x, y, z, layers) in active_neighbors_needed:
                    new_row.append('#')
                else:
                    new_row.append('.')
            new_layer.append(''.join(new_row))
        new_layers.append(new_layer)
    return new_layers


def count_active_neighbors(x, y, z, layers):
    return get_neighbors(x, y, z, layers).count('#')


def get_neighbors(x, y, z, layers):
    ind_shifts = list(product((-1, 0, 1), repeat=3))
    ind_shifts.remove((0, 0, 0))
    neighbors_inds = [(x + x_shift, y + y_shift, z + z_shift) for (x_shift, y_shift, z_shift) in ind_shifts]
    neighbors = [get_cube_state(*indices, layers) for indices in neighbors_inds]
    return neighbors


def add_margins_if_needed(layers):
    if not should_add_margins(layers):
        return layers

    new_layers = []
    for layer in layers:
        new_layer = add_inactive_rows(['.' + row + '.' for row in layer])
        new_layers.append(new_layer)
    new_layers = add_inactive_layers(new_layers)
    return new_layers


def add_inactive_rows(layer):
    """
    Add an inactive row to beginning and end of layer, respectively.
    :param layer:
    :return:
    """
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


def should_add_margins(layers):
    # return True iff >= 1 active cubes are in/on the outer perimeter of stored cube
    if not are_inactive_layers([layers[0], layers[-1]]):
        return True

    for layer in layers[1:-1]:  # check for 'perimeter activity' in inner layers
        first_row, last_row = layer[0], layer[-1]
        if '#' in first_row or '#' in last_row:
            return True
        first_and_last_cols = [row[0] + row[-1] for row in layer]
        if '#' in first_and_last_cols:
            return True
    return False


def create_inactive_layer(example_layer):
    return [create_inactive_row(row) for row in example_layer]


def create_inactive_row(example_row):
    return len(example_row) * '.'


def get_cube_state(x, y, z, layers):
    try:
        return layers[z][x][y]
    except IndexError:
        return '.'


def are_inactive_layers(layers):
    return count_active_cubes(layers) == 0


def count_active_cubes(layers):
    return ''.join(flatten_list_1_level(layers)).count('#')


def print_layers(layers):
    output_list = ['']
    start_ind = -1 * (len(layers) // 2)
    for z_ind, layer in enumerate(layers, start=start_ind):
        output_list.append(f'z={z_ind}')
        output_list.extend(layer)
        output_list.append('')
    print('\n'.join(output_list), end='\n\n')


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
