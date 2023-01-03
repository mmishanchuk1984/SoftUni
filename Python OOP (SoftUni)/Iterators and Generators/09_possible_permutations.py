from itertools import permutations


def possible_permutations(data: list):
    result = list(permutations(data))
    for el in result:
        el = list(el)
        yield el



[print(n) for n in possible_permutations([1, 2, 3])]