from collections.abc import Hashable

def func(*args):
    result = set()
    for i in args:
        if isinstance(i, Hashable):
            result.add(i)

    return result