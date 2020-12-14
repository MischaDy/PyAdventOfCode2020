# from collections import deque
from math import floor, log


RUN_TEST = False
TEST_SOLUTION = 165
TEST_INPUT_FILE = 'test_input_day_14.txt'
INPUT_FILE = 'input_day_14.txt'


VALUE_LEN = 36

ARGS = [VALUE_LEN]


def main_part1(input_file, value_len):
    with open(input_file) as file:
        program = list(map(lambda line: line.rstrip(), file.readlines()))

    mem_dict = handle_program(program, value_len)
    solution = sum(mem_dict.values())
    return solution


def handle_program(program, value_len):
    mask = None
    mem_dict = dict()
    for cmd in program:
        cmd_type, result = handle_line(cmd, mem_dict, mask, value_len)
        if cmd_type == 'mask':
            mask = result
    return mem_dict


def handle_line(cmd, mem_dict, mask, value_len):
    """

    :param cmd: Command to interpret and execute
    :param mem_dict: Memory mapping. Will be modified in-place, if at all.
    :param mask: Mask to use when modifying mem_dict.
    :return: Command type ('mask' or 'mem'); mem_dict or new mask, depending on the command
    """
    if cmd.startswith('mask = '):
        # return new mask
        return 'mask', get_line_value(cmd)

    close_bracket_ind = cmd.find(']')
    address = cmd[4:close_bracket_ind]
    num = int(get_line_value(cmd))
    masked_num = mask_num(num, mask, value_len)
    mem_dict[address] = masked_num
    return 'mem', mem_dict


def mask_num(num, mask, value_len):
    bin_list = dec_to_bin_list(num, value_len)
    z = zip(mask, bin_list)
    masked_num_list = list(map(lambda tup: int(tup[0]) if tup[0] != 'X' else tup[1], z))
    return bin_list_to_dec(masked_num_list)


def get_line_value(line):
    return line.split(' = ')[1]


def dec_to_bin_list(num, min_length=1):
    # Why not implement it ourselves... :)
    if num == 0:
        return repeat(0, min_length)

    bin_list = []
    max_power_of_2 = get_max_power_of(num, 2)
    for power in reversed(range(max_power_of_2 + 1)):
        if get_max_power_of(num) == power:
            bin_list.append(1)
            num -= 2 ** power
        else:
            bin_list.append(0)
    bin_list = repeat(0, min_length - len(bin_list)) + bin_list
    return bin_list


def bin_list_to_dec(bin_list):
    len_list = len(bin_list)
    return sum(map(lambda tup: tup[1] * 2 ** (len_list - 1 - tup[0]), enumerate(bin_list)))


def get_max_power_of(num, base=2):
    """

    :param num:
    :param base:
    :return: Greatest power of base which is <= address
    """
    if num <= 0:
        return float('-inf')
    return floor(log(num, base))


def repeat(value, r=2):
    return [value for _ in range(r)]


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
