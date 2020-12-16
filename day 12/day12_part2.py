from helpers.coordinates2d import Coordinates2D
from helpers.cyclic_list import CyclicList


RUN_TEST = True
TEST_SOLUTION = 286
TEST_INPUT_FILE = 'test_input_day_12.txt'
INPUT_FILE = 'input_day_12.txt'

WAYPOINT = (10, 1)

ARGS = []


class Ship:
    COMPASS_DIRECTIONS = CyclicList('NESW')

    def __init__(self, waypoint=WAYPOINT):
        self.pos = Coordinates2D([0, 0])
        self.waypoint = Coordinates2D(waypoint)

    def exec_instruction(self, instruction):
        direction, value = instruction[0], int(instruction[1:])

        if direction in self.COMPASS_DIRECTIONS:
            instr_coords = Coordinates2D.from_instruction(instruction)
            self.waypoint += instr_coords
        elif direction == 'L':
            east_val, north_val = self.waypoint
            num_quarter_turns = value // 90
            if num_quarter_turns == 1:
                self.waypoint.set_value([-north_val, east_val])
            elif num_quarter_turns == 2:
                self.waypoint.set_value([-east_val, -north_val])
            elif num_quarter_turns == 3:
                self.waypoint.set_value([north_val, -east_val])
            else:
                raise RuntimeError()
        elif direction == 'R':
            east_val, north_val = self.waypoint
            num_quarter_turns = value // 90
            if num_quarter_turns == 1:
                self.waypoint.set_value([north_val, -east_val])
            elif num_quarter_turns == 2:
                self.waypoint.set_value([-east_val, -north_val])
            elif num_quarter_turns == 3:
                self.waypoint.set_value([-north_val, east_val])
            else:
                raise RuntimeError()
        elif direction == 'F':
            self.pos += value * self.waypoint
        else:
            raise ValueError()

    def get_cur_pos(self):
        return self.pos


def main_part2(input_file):
    with open(input_file) as file:
        instructions = list(map(lambda line: line.rstrip(), file.readlines()))

    ship = Ship()
    for instr in instructions:
        ship.exec_instruction(instr)

    final_pos = ship.get_cur_pos()
    solution = manhattan_dist(final_pos)
    return solution


def manhattan_dist(pos1, pos2=(0, 0)):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
