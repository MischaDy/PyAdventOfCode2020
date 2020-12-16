from helpers.coordinates2d import Coordinates2D
from helpers.cyclic_list import CyclicList


RUN_TEST = True
TEST_SOLUTION = 25
TEST_INPUT_FILE = 'test_input_day_12.txt'
INPUT_FILE = 'input_day_12.txt'

FACING_DIR = 'E'

ARGS = [FACING_DIR]


class Ship:
    COMPASS_DIRECTIONS = CyclicList('NESW')

    def __init__(self, facing_dir='E'):
        assert facing_dir in self.COMPASS_DIRECTIONS
        self.facing_dir = facing_dir
        self.pos = Coordinates2D([0, 0])

    def exec_instruction(self, instruction):
        instruction = instruction.replace('F', self.facing_dir)
        direction, value = instruction[0], int(instruction[1:])

        if direction in self.COMPASS_DIRECTIONS:
            instr_coords = Coordinates2D.from_instruction(instruction)
            self.pos += instr_coords
        elif direction == 'L':
            num_quarter_turns = value // 90
            self.facing_dir = self.COMPASS_DIRECTIONS.get_item_k_left_of(self.facing_dir, num_quarter_turns)
        elif direction == 'R':
            num_quarter_turns = value // 90
            self.facing_dir = self.COMPASS_DIRECTIONS.get_item_k_right_of(self.facing_dir, num_quarter_turns)
        else:
            raise ValueError()

    def get_cur_pos(self):
        return self.pos


def main_part1(input_file, facing_dir):
    with open(input_file) as file:
        instructions = list(map(lambda line: line.rstrip(), file.readlines()))

    ship = Ship(facing_dir)
    for instr in instructions:
        ship.exec_instruction(instr)

    final_pos = ship.get_cur_pos()
    solution = manhattan_dist(final_pos)
    return solution


def manhattan_dist(pos1, pos2=(0, 0)):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
