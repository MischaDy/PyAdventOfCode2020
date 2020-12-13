from numbers import Number

RUN_TEST = False
TEST_SOLUTION = 286
TEST_INPUT_FILE = 'test_input_day_12.txt'
INPUT_FILE = 'input_day_12.txt'

WAYPOINT = (10, 1)

ARGS = []


class CyclicList(list):
    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            corrected_i = i % len(self)
            return self[corrected_i]

    def get_item_k_left_of(self, item, k=1):
        return self[self.index(item) - k]

    def get_item_k_right_of(self, item, k=1):
        return self[self.index(item) + k]


class Ship:
    COMPASS_DIRECTIONS = CyclicList('NESW')

    def __init__(self, waypoint=WAYPOINT):
        self.pos = Coordinates([0, 0])
        self.waypoint = Coordinates(waypoint)

    def exec_instruction(self, instruction):
        direction, value = instruction[0], int(instruction[1:])

        if direction in self.COMPASS_DIRECTIONS:
            instr_coords = Coordinates.from_instruction(instruction)
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

    # def set_cur_pos(self, pos):
    #     self.pos = pos


class Coordinates(list):
    def __add__(self, other):
        # print('--- ADD ---')
        return self.__class__([self[0] + other[0], self[1] + other[1]])

    def __iadd__(self, other):
        # print('--- IADD ---')
        return self.__class__([self[0] + other[0], self[1] + other[1]])

    def __mul__(self, other):
        # print('--- MUL ---')
        if not isinstance(other, Number):
            return super().__mul__(other)
        return self.__class__([self[0] * other, self[1] * other])

    def __rmul__(self, other):
        # print('--- RMUL ---')
        if not isinstance(other, Number):
            return super().__rmul__(other)
        return self.__class__([self[0] * other, self[1] * other])

    def set_value(self, value):
        assert len(value) == 2
        self[0], self[1] = value

    @classmethod
    def from_instruction(cls, instruction):
        """Only accepts compass directions"""
        direction, value = instruction[0], int(instruction[1:])
        if direction == 'N':
            coord = cls([0, value])
        elif direction == 'S':
            coord = cls([0, -value])
        elif direction == 'E':
            coord = cls([value, 0])
        elif direction == 'W':
            coord = cls([-value, 0])
        else:
            raise ValueError()
        return coord


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
