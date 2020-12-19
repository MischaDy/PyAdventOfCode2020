RUN_TEST = False
TEST_SOLUTION = 2
TEST_INPUT_FILE = 'test_input_day_19.txt'
INPUT_FILE = 'input_day_19.txt'

ARGS = []


def main_part1(input_file, ):
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
    is_valid_msg, unprocessed_submsg = is_valid_message_worker(msg, rule_dict['0'], rule_dict)
    return is_valid_msg and unprocessed_submsg == ''


def is_valid_message_worker(msg, cur_rules, rule_dict):
    # for instructions in cur_rules:
    #     for rule in instructions:
    #         if not rule.isdigit():
    #             return msg[0] == rule, msg[1:]
    #
    #         is_valid_submsg, rest = is_valid_message_worker(msg, rule_dict[rule], rule_dict)
    #         if is_valid_submsg:
    #             return is_valid_message_worker(rest, ..., rule_dict)
    # return False, ''

    for instruction in cur_rules:
        try:
            rule = instruction[0]
        except IndexError:
            return True, msg

        if not rule.isdigit():
            return msg[0] == rule, msg[1:]

        is_valid_for_first_rule, rest = is_valid_message_worker(msg, rule_dict[rule], rule_dict)
        if not is_valid_for_first_rule:
            continue
        is_valid_rest, unprocessed_submsg = is_valid_message_worker(rest, [instruction[1:]], rule_dict)
        if is_valid_rest:
            return True, unprocessed_submsg
    return False, ''


    # for instructions in cur_rules:
    #     for rule in instructions:
    #         if not rule.isdigit():
    #             return msg[0] == rule, msg[1:]
    #
    #         is_valid_submsg, rest = is_valid_message_worker(msg, rule_dict[rule], rule_dict)
    #         if is_valid_submsg:
    #             return is_valid_message_worker(rest, ..., rule_dict)


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
