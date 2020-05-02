# -*- coding:utf-8 -*-
"""Function to return value of gcd between two random values."""


def gcd_calc(random_number1, random_number2):
    """
    Calculate gcd of two random values.

    random_number1: random interger value.
    random_number1: int
    random_number2: random interger value.
    random_number2: int

    Returns:
        Return value of gcd between two generated random numbers.
    """
    list_div1 = []
    list_div2 = []
    n = 1
    m = 1
    while n <= random_number1:
        res = random_number1 % n
        if res == 0:
            list_div1.append(n)
        n += 1
    while m <= random_number2:
        res = random_number2 % m
        if res == 0:
            list_div2.append(m)
        m += 1
    common_list = [i for i in list_div1 + list_div2 if i in list_div1 and i in list_div2]
    return common_list[-1]
