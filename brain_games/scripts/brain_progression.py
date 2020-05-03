# -*- coding:utf-8 -*-

"""Main script for progression game."""


import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
import cli
from greet_first import greet_first
from progression_goal import progression_goal
from question_progression import question_progression


def main():
    """
    Run brain-progression game.

    Returns:
        Return and verify the proper elemen inside of the ariphmetic progressio.
    """
    greet_first()
    progression_goal()
    name = cli.welcome_user()
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


if __name__ == '__main__':
    main()
