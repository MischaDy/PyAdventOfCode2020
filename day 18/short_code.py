from itertools import accumulate as acc

expr = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'.replace(' ', '')
solution = 23340
ops = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

def process(expr, ops):
    if len(expr) == 1:
        return int(expr[0])
    elif '(' in (expr[0], expr[2]):
        open_ind = 0 if '(' == expr[0] else 2
        closing_ind = get_closing_ind(expr)
        subexpr = expr[(open_ind + 1): closing_ind]
        new_expr = expr[: open_ind] + [str(process(subexpr, ops))] + expr[closing_ind + 1:]
        return process(new_expr, ops)
    else:
        arg1, op, arg2 = expr[0: 3]
        func = ops[op]
        if op == '+':  # add: first add, then continue processing
            return process([str(func(int(arg1), int(arg2)))] + expr[3:], ops)
        else:  # mul: first process rest of expr, then multiply
            return func(int(arg1), process(expr[2:], ops))

def get_closing_ind(expr):
    paren_indices = list(map(lambda tup: tup[0], filter(lambda tup: tup[1] in '()', enumerate(expr))))
    return paren_indices[ list(acc(map( lambda ind: 1 if expr[ind] == '(' else -1, paren_indices ))).index(0) ]

print(process(list(expr), ops) == solution)