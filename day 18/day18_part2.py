from operator import add, mul


RUN_TEST = False
TEST_SOLUTIONS = sum([231, 51, 46, 1445, 669060, 23340])
TEST_INPUT_FILE = 'test_input_day_18.txt'
INPUT_FILE = 'input_day_18.txt'

OPERATORS = {'+': add, '*': mul}

ARGS = [OPERATORS]


def main_part2(input_file, operators):
    with open(input_file) as file:
        expressions = list(map(lambda line: line.rstrip().replace(' ', ''),
                               file.readlines()))

    results = []
    for expression in expressions:
        results.append(process(list(expression), operators))

    solution = sum(results)
    return solution


def process(expr, operators):
    if len(expr) == 1:
        return int(expr[0])

    elif expr[0] == '(':
        last_closing_paren_ind = get_matching_closing_paren_ind(expr)
        subexpr = expr[1: last_closing_paren_ind]
        new_expr = [str(process(subexpr, operators))] + expr[last_closing_paren_ind + 1:]
        return process(new_expr, operators)

    elif expr[2] == '(':
        last_closing_paren_ind = get_matching_closing_paren_ind(expr)
        subexpr = expr[3: last_closing_paren_ind]
        new_expr = expr[:2] + [str(process(subexpr, operators))] + expr[last_closing_paren_ind + 1:]
        return process(new_expr, operators)

    else:
        arg1 = expr[0]
        op = expr[1]
        func = operators[op]
        arg2 = expr[2]
        if op == '+':
            new_expr = [str(func(int(arg1), int(arg2)))] + expr[3:]
            return process(new_expr, operators)
        else:  # op = '*'
            remaining_expr_result = process(expr[2:], operators)
            return func(int(arg1), remaining_expr_result)


def get_matching_closing_paren_ind(expr):
    num_unclosed_parens = 0
    for ind, token in enumerate(expr):
        if token == '(':
            num_unclosed_parens += 1
        elif token == ')':
            num_unclosed_parens -= 1
            if num_unclosed_parens == 0:
                return ind


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
