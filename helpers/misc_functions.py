from functools import reduce


def prod(factors):
    return reduce(lambda a, b: a * b, factors, 1)


def split_string(string, seps):
    return _split_string_worker([string], seps.copy())


def _split_string_worker(strings_list, seps):
    if not seps:
        return strings_list
    sep = seps.pop()
    new_strings_list = flatten_list_1_level(list(
        map(lambda string: string.split(sep), strings_list)
    ))
    return _split_string_worker(new_strings_list, seps)


def flatten_list_n_levels(list_, n):
    if n == 0:
        return list_

    flattened_list = flatten_list_1_level(list_)
    if n == 1:
        return flattened_list
    return flatten_list_n_levels(flattened_list, n - 1)


def flatten_list_1_level(list_):
    return sum(list_, start=[])
