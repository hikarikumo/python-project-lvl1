# -*- coding:utf-8 -*-

"""Question user in progression game."""


import prompt
import random


def question_prime():
    """
    Ask the question and return bool and value.

    Returns:
        Question and number to guess to the user.
    """
    number_to_guess = random.randint(1, 100)
    user_answer = prompt.string('Number: ' + str(number_to_guess) + '\n')
    return number_to_guess, user_answer
