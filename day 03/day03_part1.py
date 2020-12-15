from helpers.cyclic_list import CyclicList
from helpers.coordinates2d import Coordinates2D


RUN_TEST = False
TEST_SOLUTION = 7
TEST_INPUT_FILE = 'test_input_day_03.txt'
INPUT_FILE = 'input_day_03.txt'

START = Coordinates2D((0, 0))  # top left corner
TRAJECTORY = Coordinates2D((3, 1))  # right 3, down 1

ARGS = [START, TRAJECTORY]


def main_part1(input_file, start, trajectory):
    with open(input_file) as file:
        tree_map = list(map(lambda line: CyclicList(line.rstrip()), file.readlines()))

    solution = count_trees(tree_map, trajectory, start)
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
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
