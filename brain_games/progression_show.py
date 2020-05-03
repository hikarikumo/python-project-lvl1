# -*- coding:utf-8 -*-
"""Function to show progression to user without element to calc."""

from progression_calc import progression_calc
import random


def progression_show():
    """
    Create ariphmetic progression.

    Returns:
        Progression with *hidden* element + value of that hidden element.
    """
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    random_number3 = random.randint(1, 10)
    progression = progression_calc(random_number2, random_number3)
    keep_value = progression[random_number1]
    progression[random_number1] = '..'
    return keep_value, progression
