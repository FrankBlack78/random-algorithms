#!/usr/bin/env python3

def fib(n):
    """
    :param n: Create a fibonacci series up to but not including n.
    :return: List of fibonacci series.
    """
    result = list()
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print(fib(988))
