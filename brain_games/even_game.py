# -*- coding:utf-8 -*-

"""Function declaration to verify the answers."""

import prompt
import random


def check_if_even(number):
    """Return true if even."""
    if number % 2 == 0:
        return True
    return False


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
    even_result = check_if_even(random_number)
    print(random_number)
    answer = prompt.string("Answer 'yes' if number even otherwise answer 'no'.\n")
    while (answer != 'no') and (answer != 'yes'):
        answer = prompt.string("Answer 'yes' if number even otherwise answer 'no'.\n")
    if answer == 'yes' and even_result is True:
        return True
    elif answer == 'no' and even_result is False:
        return True
    elif answer == 'yes' and even_result is False:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False
    elif answer == 'no' and even_result is True:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False


def even_game_logic(name):
    """Even game main logic."""
    counter = 1
    while counter <= 3:
        received_value = even_game()
        if received_value is True:
            print('Correct!')
            if counter == 3:
                print('Congratulations, ', name, '!', sep='')
        elif received_value is False:
            print("Let's try again,")
            break
        counter += 1
