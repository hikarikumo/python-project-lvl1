# -*- coding:utf-8 -*-

"""Function declaration to verify the answers."""

import even_check
import prompt
import random


def even_game():
    """
    Verify the correct answer.

    Test what does the user type in: yes or not.
    Other characters are not allowed.
    Verify the correct answer provided by user.

    Returns:
        True ot False according to the provided answer by user.
    """
    random_number = random.randint(0, 10000)
    even_result = even_check.check_if_even(random_number)
    print(random_number)
    answer = prompt.string(prompt="Answer 'yes' if number even otherwise answer 'no'.\n")
    while (answer != 'no') and (answer != 'yes'):
        answer = prompt.string(prompt="Answer 'yes' if number even otherwise answer 'no'.\n")
    if answer == 'yes' and even_result is True:
        print('Correct!')
        return True
    elif answer == 'no' and even_result is False:
        print('Correct!')
        return True
    elif answer == 'yes' and even_result is False:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False
    elif answer == 'no' and even_result is True:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False
