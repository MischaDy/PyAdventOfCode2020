from helpers.cyclic_list import CyclicList
from helpers.coordinates2d import Coordinates2D
from helpers.misc_functions import prod


RUN_TEST = False
TEST_SOLUTION = 336
TEST_INPUT_FILE = 'test_input_day_03.txt'
INPUT_FILE = 'input_day_03.txt'

START = Coordinates2D((0, 0))  # top left corner
TRAJECTORIES = list(map(Coordinates2D, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))

ARGS = [START, TRAJECTORIES]


def main_part2(input_file, start, trajectories):
    with open(input_file) as file:
        tree_map = list(map(lambda line: CyclicList(line.rstrip()), file.readlines()))

    num_trees_total = prod(map(lambda traj: count_trees(tree_map, traj, start), trajectories))
    solution = num_trees_total
    return solution


def count_trees(tree_map, trajectory, start):
    bottom = len(tree_map)
    cur_pos = start
    num_trees = 0  # start is a tree-free square
    while cur_pos.y < bottom:
        num_trees += tree_map[cur_pos.y][cur_pos.x] == '#'
        cur_pos = cur_pos + trajectory

    return num_trees


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
