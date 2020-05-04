# -*- coding:utf-8 -*-
"""Function to check whether provided number is prime."""


def prime_div_result(number):
    """
    Check if the number is prime.

    Input:
        Accept one number as parameter.

    Returns:
        Returns True if number is prime - False otherwise.
    """
    check_sequence = []
    counter = 1
    while counter <= number:
        if number % counter == 0:
            check_sequence.append(counter)
        counter += 1
    if len(check_sequence) > 2:
        return False
    return True
