# -*- coding:utf-8 -*-
"""Function to calculate ariphmetic progression."""

from question_progression import question_progression


def progression_game(name):
    """Perform progression game logic."""
    counter = 1
    while counter <= 3:
        calc_value, miss_element = question_progression()
        if calc_value is True:
            print('Your answer: ' + str(miss_element))
            print('Correct!')
            if counter == 3:
                print('Congratulations, ', name, '!', sep='')
                return True
        else:
            print("Let's try again, ", name, '!', sep='')
            return False
        counter += 1
