# -*- coding:utf-8 -*-
"""Function to check whether provided number is prime."""

from prime_check import prime_div_result
from question_prime import question_prime


def prime_game(name):
    """Brain game prime logic."""
    counter = 1
    while counter <= 3:
        random_number, user_answer = question_prime()
        is_prime = prime_div_result(random_number)
        if is_prime is True and user_answer == 'yes':
            print('Your answer: ' + 'yes ' + str(random_number) + ' is prime')
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
