# -*- coding:utf-8 -*-

"""Function declaration to verify the answers."""

import prompt
import random
import general_module


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
    random_number = random.randint(0, 1000)
    even_result = check_if_even(random_number)
    print(random_number)
    general_module.even_question()
    answer = prompt.string()
    while answer == 'yes':
        if even_result:
            return True
        general_module.even_wrong_answer_yes(answer)
        return False
    while answer == 'no':
        if not even_result:
            return True
        general_module.even_wrong_answer_no(answer)
        return False


def even_game_logic(name):
    """Even game main logic."""
    counter = 1
    while counter <= 3:
        received_value = even_game()
        if received_value:
            general_module.correct_answer()
            if counter == 3:
                general_module.game_success_finish(name)
        else:
            general_module.try_again(name)
            break
        counter += 1
