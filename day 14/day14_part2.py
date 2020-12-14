from itertools import product
from math import floor, log


RUN_TEST = False
TEST_SOLUTION = 208
TEST_INPUT_FILE = 'test_input_2_day_14.txt'
INPUT_FILE = 'input_day_14.txt'


VALUE_LEN = 36

ARGS = [VALUE_LEN]


def main_part2(input_file, value_len):
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
    address = int(cmd[4:close_bracket_ind])
    num = int(get_line_value(cmd))
    masked_address = mask_address(address, mask, value_len)
    addresses_to_write_to = get_addresses_from_masked(masked_address)
    mem_dict_additions = {address: num for address in addresses_to_write_to}
    mem_dict.update(mem_dict_additions)
    return 'mem', mem_dict


def get_addresses_from_masked(masked_address):
    num_xs = masked_address.count('X')
    replacements = product((0, 1), repeat=num_xs)
    new_masked_address_str = ''.join(map(str, masked_address)).replace('X', '{}')
    for replacement in replacements:
        new_address = new_masked_address_str.format(*replacement)
        yield bin_iter_to_dec(new_address)


def mask_address(address, mask, value_len):
    bin_list = dec_to_bin_list(address, value_len)
    # z = zip(mask, bin_list)
    # masked_address_list = list(map(lambda tup: 1 if tup[0] == '1' else tup[1], z))

    masked_address_list = []
    for mask_bit, bin_bit in zip(mask, bin_list):
        if mask_bit == '0':
            masked_address_list.append(str(bin_bit))
        else:
            masked_address_list.append(mask_bit)
    return masked_address_list


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


def bin_iter_to_dec(bin_iter):
    bin_list = list(map(int, bin_iter))
    len_list = len(bin_list)
    total = 0
    for ind, bin_num in enumerate(bin_list):
        if bin_num:
            total += bin_num * 2 ** (len_list - 1 - ind)
    return total  # sum(map(lambda tup: tup[1] * 2 ** (len_list - 1 - tup[0]), enumerate(bin_list)))


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
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
