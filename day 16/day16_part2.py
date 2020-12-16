from helpers.misc_functions import flatten_list_1_level, prod


RUN_TEST = False
TEST_SOLUTION = 156  # = 12 * 13
TEST_INPUT_FILE = 'test_input_2_day_16.txt'  # Note: added 'departure' to test
INPUT_FILE = 'input_day_16.txt'

ARGS = []


def main_part2(input_file, ):
    with open(input_file) as file:
        data = file.read()

    field_rules, my_ticket, nearby_tickets = format_data(data)
    valid_tickets = list(filter(lambda ticket: is_valid_ticket(ticket, field_rules), nearby_tickets))
    # cast valid_tickets to list of int lists
    valid_tickets = list(map(lambda ticket: list(map(int, ticket.split(','))), valid_tickets))
    field_names = determine_field_names(valid_tickets, field_rules)
    departure_fields_inds = get_fields_starting_with('departure', field_names)
    my_ticket_dep_values = get_ticket_values_by_indices(my_ticket, departure_fields_inds)
    solution = prod(my_ticket_dep_values)
    return solution


def determine_field_names(tickets, field_rules):
    num_fields = len(field_rules)
    field_to_ranges_dict = get_named_ranges(field_rules)
    # e.g. { 0: {'class', 'row', 'seat'}, ... }
    ind_to_fields_dict = dict( [ind, list(field_to_ranges_dict.keys())] for ind in range(num_fields) )
    for ticket in tickets:
        for ind, value in enumerate(ticket):
            allowed_fields_for_ind = ind_to_fields_dict[ind]
            # don't check indices with one allowed value. assume that it will be legal anyways.
            if len(allowed_fields_for_ind) == 1:
                continue

            for field in allowed_fields_for_ind.copy():
                # check if value excludes field as possibility and update dict accordingly
                field_ranges = field_to_ranges_dict[field]
                if is_value_in_ranges(value, field_ranges):
                    continue

                allowed_fields_for_ind.remove(field)
                if len(allowed_fields_for_ind) > 1:
                    continue
                # assume len = 0 is impossible, so we have len = 1
                # remove the last allowed value from other inds, since we know it belongs to *this* ind

                only_valid_field_for_ind = allowed_fields_for_ind[0]
                removers = [(ind, only_valid_field_for_ind)]
                while len(removers) > 0:
                    cur_ind, only_valid_field_for_cur_ind = removers.pop(0)
                    for ind_key, fields_value in ind_to_fields_dict.items():
                        if len(fields_value) == 1 or only_valid_field_for_cur_ind not in fields_value:  # ind_key == ind
                            continue
                        fields_value.remove(only_valid_field_for_cur_ind)
                        if len(fields_value) == 1:
                            removers.append((ind_key, fields_value[0]))
    return invert_dict(ind_to_fields_dict, flatten_values=True)


def invert_dict(d, flatten_values=True):
    if flatten_values:
        d_inv = dict((value[0], key) for key, value in d.items())
    else:
        d_inv = dict((value, key) for key, value in d.items())
    return d_inv


def is_value_in_ranges(value, ranges):
    return any(map(lambda range_: value in range_, ranges))


def get_fields_starting_with(prefix, field_names):
    field_names_items = filter(lambda item: item[0].startswith(prefix), field_names.items())
    fields_indices = list(map(lambda item: item[1], field_names_items))
    return fields_indices


def get_ticket_values_by_indices(my_ticket, indices):
    return list(map(lambda ind: my_ticket[ind], indices))


def get_named_ranges(fields_rules):
    fields_rules_tuples = map(lambda line: line.split(': '), fields_rules)
    field_to_ranges_dict = dict()
    for field, ranges_str in fields_rules_tuples:
        field_to_ranges_dict[field] = list(map(str_to_range, ranges_str.split(' or ')))
    return field_to_ranges_dict


def str_to_range(string):
    lower, upper = map(int, string.split('-'))
    return range(lower, upper + 1)


def get_ranges(field_rules):
    rules_text = map(lambda rule: rule.split(': ')[1], field_rules)
    ranges_strs = flatten_list_1_level(list(map(lambda rule: rule.split(' or '), rules_text)))

    ranges = []
    for range_str in ranges_strs:
        lower, upper = map(int, range_str.split('-'))
        ranges.append(range(lower, upper + 1))
    return ranges


def is_valid_ticket(ticket, field_rules):
    valid_ranges = get_ranges(field_rules)
    ticket_values = list(map(int, ticket.split(',')))
    for ticket_value in ticket_values:
        is_value_valid = any(map(lambda range_: ticket_value in range_, valid_ranges))
        if not is_value_valid:
            return False
    return True


def format_data(data):
    field_rules, my_ticket, nearby_tickets = data.split('\n\n')
    my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
    nearby_tickets = nearby_tickets.split('\n')[1:]
    field_rules = field_rules.split('\n')
    return field_rules, my_ticket, nearby_tickets


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
