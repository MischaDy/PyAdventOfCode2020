RUN_TEST = True
TEST_SOLUTION = 12
TEST_INPUT_FILE = 'test_input_2_day_19.txt'
INPUT_FILE = 'input_2_day_19.txt'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        rules, msgs = file.read().replace('"', '').split('\n\n')
    rules, msgs = rules.split('\n'), msgs.split('\n')
    rule_dict = make_rule_dict(rules)
    solution = sum(map(lambda msg: is_valid_message(msg, rule_dict), msgs))
    return solution


def make_rule_dict(rules):
    rule_dict = dict()
    for rule in rules:
        key, rest = rule.split(': ')
        # store value as 2D-list of strings
        value = list(map(lambda s: s.split(' '), rest.split(' | ')))
        rule_dict[key] = value
    return rule_dict


def is_valid_message(msg, rule_dict):
    # msg = 'aaaaabbaabaaaaababaa'
    msg = 'ababbb'
    rule_dict = {'0': [['4', '1', '5']],
                 '1': [['2', '3'], ['3', '2']],
                 '2': [['2', '4', '4'], ['4', '4'], ['5', '5']],
                 '3': [['4', '1', '5']],
                 '4': [['a']],
                 '5': [['b']]
                 }

    is_valid_msg, unprocessed_submsg = is_valid_message_worker(msg, rule_dict['0'], rule_dict, 0)
    return is_valid_msg and unprocessed_submsg == ''


def is_valid_message_worker(msg, cur_rules, rule_dict, min_len_instr):
    """

    :param msg:
    :param cur_rules:
    :param rule_dict:
    :param min_len: Minimum length the processed message(?) will have
    :param orig_msg_len:
    :return:
    """
    for instruction in cur_rules:
        if len(instruction) == 0:
            continue

        # use fact that each rule in instruction will become at least one letter
        if min_len_instr + len(instruction) > len(msg):
            return False, msg

        rule = instruction[0]

        if not rule.isdigit():
            return msg[0] == rule, msg[1:]

        is_valid_for_first_rule, rest = is_valid_message_worker(msg, rule_dict[rule], rule_dict,
                                                                min_len_instr + (len(instruction) - 1))  # TODO: correct!
        if not is_valid_for_first_rule:
            continue
        is_valid_rest, unprocessed_submsg = is_valid_message_worker(rest, [instruction[1:]], rule_dict, min_len_instr)
        if is_valid_rest:
            return True, unprocessed_submsg
    return False, ''


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
