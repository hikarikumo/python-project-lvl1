# -*- coding:utf-8 -*-
"""Function to return value of gcd between two random values."""

from question_gcd import question_gcd


def gcd_game(name):
    """Execute main game logic."""
    counter = 1
    while counter <= 3:
        status_calc, gcd = question_gcd()
        if status_calc is True:
            print('Your answer: ' + str(gcd))
            print('Correct!')
            if counter == 3:
                print('Congratulations, ', name, '!', sep='')
                return True
        else:
            print("Let's try again, ", name, '!', sep='')
            return False
        counter += 1
