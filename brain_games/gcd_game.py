# -*- coding:utf-8 -*-
"""Function to return value of gcd between two random values."""

import random
import prompt
from cli import greet_first, welcome_user


def question_gcd():
    """
    Ask the question and return bool and value.

    Returns:
        True and value if answer is gcd.
        False and value if answer is not gcd.
    """
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    gcd = gcd_calc(random_number1, random_number2)
    question_to_user_gcd = prompt.string('Question: ' + str(random_number1) + ' ' + str(random_number2) + '\n')
    if question_to_user_gcd == str(gcd):
        return True, gcd
    return False, gcd


def gcd_goal_message():
    """Information about the goal to the user."""
    print('Find the greatest common divisor of given numbers.\n')


def gcd_calc(random_number1, random_number2):
    """
    Calculate gcd of two random values.

    random_number1: random interger value.
    random_number1: int
    random_number2: random interger value.
    random_number2: int

    Returns:
        Return value of gcd between two generated random numbers.
    """
    list_div1 = []
    list_div2 = []
    count_n = 1
    count_m = 1
    while count_n <= random_number1:
        res = random_number1 % count_n
        if res == 0:
            list_div1.append(count_n)
        count_n += 1
    while count_m <= random_number2:
        res = random_number2 % count_m
        if res == 0:
            list_div2.append(count_m)
        count_m += 1
    common_list = [index for index in list_div1 + list_div2 if index in list_div1 and index in list_div2]
    return common_list[-1]


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


def main():
    """
    Run brain-gcd game.

    returns:
    Correct answer on the screen with result and username.
    """
    greet_first()
    gcd_goal_message()
    name = welcome_user()
    gcd_game(name)


if __name__ == '__main__':
    main()