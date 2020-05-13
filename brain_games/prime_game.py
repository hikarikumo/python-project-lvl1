# -*- coding:utf-8 -*-
"""Function to check whether provided number is prime."""

import prompt, random


def question_prime():
    """
    Ask the question and return bool and value.

    Returns:
        Question and number to guess to the user.
    """
    number_to_guess = random.randint(1, 100)
    user_answer = prompt.string('Number: ' + str(number_to_guess) + '\n')
    return number_to_guess, user_answer


def prime_goal():
    """Information about the goal of the prime game to the user."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')


def prime_div_result(number):
    """
    Check if the number is prime.

    Input:
        Accept one number as parameter.

    Returns:
        Returns True if number is prime - False otherwise.
    """
    check_sequence = []
    counter = 1
    while counter <= number:
        if number % counter == 0:
            check_sequence.append(counter)
        counter += 1
    if len(check_sequence) > 2:
        return False
    return True


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
