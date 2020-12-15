from numbers import Number


class Coordinates2D(list):
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

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

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
