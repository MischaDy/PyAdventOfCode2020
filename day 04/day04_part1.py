from helpers.misc_functions import split_string


RUN_TEST = False
TEST_SOLUTION = 2
TEST_INPUT_FILE = 'test_input_day_04.txt'
INPUT_FILE = 'input_day_04.txt'

PASSPORT_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
}

REQUIRED_PP_FIELDS = PASSPORT_FIELDS.difference({'cid'})


ARGS = [REQUIRED_PP_FIELDS, ]


def main_part1(input_file, required_fields):
    with open(input_file) as file:
        data = file.read()

    passports_lines = split_into_passports_lines(data)
    solution = sum(map(lambda pp_lines: are_valid_passport_lines(pp_lines, required_fields),
                       passports_lines))
    return solution


def split_into_passports_lines(data):
    return data.split('\n\n')


def are_valid_passport_lines(passport_lines, required_fields):
    passport_fields_dict = get_fields(passport_lines)
    field_names = set(passport_fields_dict.keys())
    return field_names.issuperset(required_fields)


def get_fields(passport_lines):
    fields_lines = split_string(passport_lines, ['\n', ' '])
    return read_fields(fields_lines)


def read_fields(passport_fields):
    return dict(map(lambda string: string.split(':'), passport_fields))


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
