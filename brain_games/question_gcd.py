# -*- coding:utf-8 -*-

"""Question user in gcd game."""


import random

import prompt

from gcd_calc import gcd_calc


def question_gcd():
    """
    Ask the question and return bool and value.

    Returns:
        True and value if answer is gcd.
        False and value if answer is not gcd.
    """
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    gcd = gcd_calc(random_number1, random_number2)
    question_to_user_gcd = prompt.string('Question: ' + str(random_number1) + ' ' + str(random_number2) + '\n')
    if question_to_user_gcd == str(gcd):
        return True, gcd
    return False, gcd
