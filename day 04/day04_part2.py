from helpers.misc_functions import split_string


RUN_TEST = False
TEST_1_SOLUTION = 0
TEST_2_SOLUTION = 4
TEST_INPUT_1_FILE = 'test_input_1_day_04.txt'
TEST_INPUT_2_FILE = 'test_input_2_day_04.txt'
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

HEXDIGITS = ''.join(map(str, range(10))) + 'abcdef'

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
    if not field_names.issuperset(required_fields):
        return False
    return are_valid_fields(passport_fields_dict)


def are_valid_fields(fields_dict):
    byr_check = check_byr(fields_dict['byr'])
    iyr_check = check_iyr(fields_dict['iyr'])
    eyr_check = check_eyr(fields_dict['eyr'])
    hgt_check = check_hgt(fields_dict['hgt'])
    hcl_check = check_hcl(fields_dict['hcl'])
    ecl_check = check_ecl(fields_dict['ecl'])
    pid_check = check_pid(fields_dict['pid'])

    return all([byr_check, iyr_check, eyr_check, hgt_check, hcl_check, ecl_check, pid_check])


def check_byr(byr):
    return len(byr) == 4 and 1920 <= int(byr) <= 2002


def check_iyr(iyr):
    return len(iyr) == 4 and 2010 <= int(iyr) <= 2020


def check_eyr(eyr):
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030


def check_hgt(hgt):
    if not (len(hgt) > 2 and hgt[:-2].isdigit() and hgt[-2:] in ('cm', 'in')):
        return False
    if hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    # case 'in'
    return 59 <= int(hgt[:-2]) <= 76


def check_hcl(hcl):
    return hcl[0] == '#' and all(map(lambda char: char in HEXDIGITS, hcl[1:]))


def check_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_pid(pid):
    return len(pid) == 9 and pid.isdigit()


def _temp_run_checks():
    print(check_byr('2002') == True)
    print(check_byr('2003') == False)

    print(check_hgt('60in') == True)
    print(check_hgt('190cm') == True)
    print(check_hgt('190in') == False)
    print(check_hgt('190') == False)

    print(check_hcl('#123abc') == True)
    print(check_hcl('#123abz') == False)
    print(check_hcl('123abc') == False)

    print(check_ecl('brn') == True)
    print(check_ecl('wat') == False)

    print(check_pid('000000001') == True)
    print(check_pid('0123456789') == False)


def get_fields(passport_lines):
    fields_lines = split_string(passport_lines, ['\n', ' '])
    return read_fields(fields_lines)


def read_fields(passport_fields):
    return dict(map(lambda string: string.split(':'), passport_fields))



if __name__ == '__main__':
    if RUN_TEST:
        _temp_run_checks()

        solution1 = main_part1(TEST_INPUT_1_FILE, *ARGS)
        print(solution1)
        solution2 = main_part1(TEST_INPUT_2_FILE, *ARGS)
        print(solution2)
        assert (TEST_1_SOLUTION == solution1)
        assert (TEST_2_SOLUTION == solution2)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
