# -*- coding:utf-8 -*-

"""Main script for gcd game."""

import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
import cli
from greet_first import greet_first
from brain_gcd_goal import gcd_goal_message
from question_gcd import question_gcd


def main():
    """
    Run brain-gcd game.

    Returns:
        Return correct answer on the screen with result and username.
    """
    greet_first()
    gcd_goal_message()
    name = cli.welcome_user()
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


if __name__ == '__main__':
    main()
