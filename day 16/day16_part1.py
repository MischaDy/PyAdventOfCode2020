from helpers.misc_functions import flatten_list_1_level


RUN_TEST = False
TEST_SOLUTION = 71
TEST_INPUT_FILE = 'test_input_day_16.txt'
INPUT_FILE = 'input_day_16.txt'

ARGS = []


def main_part1(input_file, ):
    with open(input_file) as file:
        data = file.read()

    field_rules, my_ticket, nearby_tickets = format_data(data)
    valid_ranges = get_ranges(field_rules)
    error_rate = sum(map(lambda ticket: get_invalid_values_sum(ticket, valid_ranges), nearby_tickets))
    solution = error_rate
    return solution


def get_ranges(field_rules):
    rules_text = map(lambda rule: rule.split(': ')[1], field_rules)
    ranges_strs = flatten_list_1_level(list(map(lambda rule: rule.split(' or '), rules_text)))

    ranges = []
    for range_str in ranges_strs:
        lower, upper = map(int, range_str.split('-'))
        ranges.append(range(lower, upper + 1))
    return ranges


def get_invalid_values_sum(ticket, valid_ranges):
    invalid_values_sum = 0
    ticket_values = list(map(int, ticket.split(',')))
    for ticket_value in ticket_values:
        is_value_valid = any(map(lambda range_: ticket_value in range_, valid_ranges))
        if not is_value_valid:
            invalid_values_sum += ticket_value
    return invalid_values_sum


def format_data(data):
    field_rules, my_ticket, nearby_tickets = data.split('\n\n')
    my_ticket = my_ticket.split('\n')[1]
    nearby_tickets = nearby_tickets.split('\n')[1:]
    field_rules = field_rules.split('\n')
    return field_rules, my_ticket, nearby_tickets


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
