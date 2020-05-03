# -*- coding:utf-8 -*-
"""Function to calculate ariphmetic progression."""


def progression_calc(random_step, random_initial):
    """
    Create progression.

    Input:
        Accept two random parameters: position and progression step.

    Returns:
        Returns progression list.
    """
    progression = []
    progression.append(random_initial)
    progression_length = 11
    counter = 1
    progression_member = random_initial
    while counter < progression_length:
        progression_member += random_step
        progression.append(progression_member)
        counter += 1
    return progression
