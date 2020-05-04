# -*- coding:utf-8 -*-

"""Main script for prime game."""


import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
import cli
from greet_first import greet_first
from prime_goal import prime_goal
from prime_check import prime_div_result
from question_prime import question_prime


def main():
    """
    Run brain-prime game.

    Returns:
        Return and verify the whether the provided number is prime.
    """
    greet_first()
    prime_goal()
    name = cli.welcome_user()
    counter = 1
    while counter <= 3:
        random_number, user_answer = question_prime()
        is_prime = prime_div_result(random_number)
        if is_prime is True and user_answer == 'yes':
            print('Your answer: ' + user_answer + str(random_number) + 'is prime')
            print('Correct!')
            if counter == 3:
                print('Congratulations, ', name, '!', sep='')
                return True
        elif is_prime is False and user_answer == 'no':
            print('Your answer: ' + 'yes ' + str(random_number) + ' is not prime')
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
