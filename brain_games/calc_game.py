# -*- coding:utf-8 -*-
"""Calc games function to ask questions and verify the answers."""

import random

import prompt


def calc_greet_first():
    """First greeting message."""
    print('What is the result of the expression?\n')


def calc_game_summ():
    """Summary operation."""
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    summ_result = number1 + number2
    return summ_result, number1, number2


def summ_check():
    """Check calculation of summary by user."""
    answer_sum, number1, number2 = calc_game_summ()
    question_sum = prompt.string('Question: ' + str(number1) + ' + ' + str(number2) + '\n')
    if question_sum == str(answer_sum):
        print('Your answer: ' + question_sum)
        print('Correct!')
        return True
    print("'" + str(question_sum) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_sum) + "'")
    return False


def calc_game_subtract():
    """Subtract operation."""
    number3 = random.randint(0, 100)
    number4 = random.randint(0, 100)
    answer_subtr = number3 - number4
    return answer_subtr, number3, number4


def subtract_check():
    """Check calculation of substract by user."""
    answer_subtr, number3, number4 = calc_game_subtract()
    question_subtr = prompt.string('Question: ' + str(number3) + ' - ' + str(number4) + '\n')
    if question_subtr == str(answer_subtr):
        print('Your answer: ' + question_subtr)
        print('Correct!')
        return True
    print("'" + str(question_subtr) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_subtr) + "'")
    return False


def calc_game_multiplication():
    """Multiplication operation."""
    number5 = random.randint(0, 10)
    number6 = random.randint(0, 10)
    answer_mult = number5 * number6
    return answer_mult, number5, number6


def multiplication_check():
    """Check calculation of multiplication by user."""
    answer_mult, number5, number6 = calc_game_multiplication()
    question_mult = prompt.string('Question: ' + str(number5) + ' * ' + str(number6) + '\n')
    if question_mult == str(answer_mult):
        print('Your answer: ' + question_mult)
        print('Correct!')
        return True
    print("'" + str(question_mult) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_mult) + "'")
    return False


def user_fail_message(name):
    """Report fail to user."""
    print("Let's try again, ", name, '!', sep='')


def calc_game_logic(name):
    """Calc game logic function."""
    counter = 1
    while counter <= 3:
        if summ_check() is False:
            user_fail_message(name)
            break
        elif subtract_check() is False:
            user_fail_message(name)
            break
        elif multiplication_check() is False:
            user_fail_message(name)
            break
        elif counter >= 3:
            print('Congratulations, ', name, '!', sep='')
        counter += 1
