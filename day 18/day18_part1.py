from operator import add, mul


RUN_TEST = False
TEST_SOLUTIONS = sum([71, 51, 26, 437, 12240, 13632])
TEST_INPUT_FILE = 'test_input_day_18.txt'
INPUT_FILE = 'input_day_18.txt'

OPERATORS = {'+': add, '*': mul}

ARGS = [OPERATORS]


def main_part1(input_file, operators):
    with open(input_file) as file:
        expressions = list(map(lambda line: line.rstrip().replace(' ', ''),
                               file.readlines()))

    results = []
    for expression in expressions:
        # syntax_tree = parse(expression, operators)  # is a list
        results.append(myprocess(list(expression), operators))

    solution = sum(results)
    return solution


# def parse(expression, operators):
#     # using infix notation
#     syntax_tree = []
#     subexpr = []
#     was_last_token_digit = False
#     subexpr_contains_operator = False
#     depth = 0
#     operator_flags_stack = []
#
#     # expression = '((1+2*3)*4)+5'
#     # assume single-digit numbers
#     for ind, token in enumerate(expression):
#         subexpr = get_last_subexpr(syntax_tree, depth)
#         if token.isdigit():
#             if not was_last_token_digit and not subexpr_contains_operator:  # sense of condition???
#                 # reading first element in the sub-expr - just append
#                 subexpr.append(token)
#                 was_last_token_digit = True
#             else:
#                 # reading last element in sub-expr
#                 subexpr.append(token)
#                 if depth == 0 or expression[ind + 1] != ')':
#                     syntax_tree = [syntax_tree]
#                 was_last_token_digit = True
#                 subexpr_contains_operator = False
#         elif token in operators:
#             subexpr.append(token)
#             was_last_token_digit = False
#             subexpr_contains_operator = True
#         elif token == '(':
#             depth += 1
#             subexpr.append([])
#             operator_flags_stack.append(subexpr_contains_operator)
#             subexpr_contains_operator = False
#         elif token == ')':
#             depth -= 1
#             subexpr_contains_operator = operator_flags_stack.pop()
#         else:
#             raise ValueError(f'unknown token {token}')
#
#     syntax_tree = syntax_tree[0]
#     return syntax_tree
#
#
# def get_last_subexpr(syntax_tree, depth):
#     subexpr = syntax_tree
#     for _ in range(depth):
#         subexpr = subexpr[-1]
#     return subexpr
#
#
# def process(expr, operators):
#     if len(expr) == 1:
#         return expr
#     func = operators[expr[1]]
#     num1 = int(process(expr[0], operators))
#     num2 = int(process(expr[2], operators))
#     return func(num1, num2)


def myprocess(expr, operators):
    if len(expr) == 1:
        return int(expr[0])

    elif expr[0] == '(':
        last_closing_paren_ind = get_matching_closing_paren_ind(expr)
        subexpr = expr[1: last_closing_paren_ind]
        new_expr = [str(myprocess(subexpr, operators))] + expr[last_closing_paren_ind+1:]
        return myprocess(new_expr, operators)

    elif expr[2] == '(':
        last_closing_paren_ind = get_matching_closing_paren_ind(expr)
        subexpr = expr[3: last_closing_paren_ind]
        new_expr = expr[:2] + [str(myprocess(subexpr, operators))] + expr[last_closing_paren_ind+1:]
        return myprocess(new_expr, operators)

    else:
        arg1 = int(expr[0])
        func = operators[expr[1]]
        arg2 = int(expr[2])
        new_expr = [str(func(arg1, arg2))] + expr[3:]
        return myprocess(new_expr, operators)


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
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTIONS == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
