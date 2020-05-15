# -*- coding:utf-8 -*-
"""Calc games function to ask questions and verify the answers."""

import random

import prompt


def calc_greet_first():
    """First greeting message."""
    print('What is the result of the expression?\n')


def calc_game_summ():
    """Summary operation."""
    random_number1 = random.randint(0, 100)
    random_number2 = random.randint(0, 100)
    summ_result = random_number1 + random_number2
    return summ_result, random_number1, random_number2


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
    random_number3 = random.randint(0, 100)
    random_number4 = random.randint(0, 100)
    answer_subtraction = random_number3 - random_number4
    return answer_subtraction, random_number3, random_number4


def subtract_check():
    """Check calculation of substract by user."""
    answer_subtraction, random_number3, random_number4 = calc_game_subtract()
    question_subtraction = prompt.string('Question: ' + str(random_number3) + ' - ' + str(random_number4) + '\n')
    if question_subtraction == str(answer_subtraction):
        print('Your answer: ' + question_subtraction)
        print('Correct!')
        return True
    print("'" + str(question_subtraction) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_subtraction) + "'")
    return False


def calc_game_multiplication():
    """Multiplication operation."""
    random_number5 = random.randint(0, 10)
    random_number6 = random.randint(0, 10)
    answer_multiplication = random_number5 * random_number6
    return answer_multiplication, random_number5, random_number6


def multiplication_check():
    """Check calculation of multiplication by user."""
    answer_multiplication, random_number5, random_number6 = calc_game_multiplication()
    question_multiplication = prompt.string('Question: ' + str(random_number5) + ' * ' + str(random_number6) + '\n')
    if question_multiplication == str(answer_multiplication):
        print('Your answer: ' + question_multiplication)
        print('Correct!')
        return True
    print("'" + str(question_multiplication) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_multiplication) + "'")
    return False


def user_fail_message(name):
    """Report fail to user."""
    print("Let's try again, ", name, '!', sep='')


def calc_game_logic(name):
    """Calc game logic function."""
    counter = 1
    while counter <= 3:
        received_value_summ = summ_check()
        if received_value_summ is False:
            user_fail_message(name)
            break
        received_value_subtract = subtract_check()
        if received_value_subtract is False:
            user_fail_message(name)
            break
        received_value_multiplication = multiplication_check()
        if received_value_multiplication is False:
            user_fail_message(name)
            break
        if received_value_multiplication is True and counter >= 3:
            print('Congratulations, ', name, '!', sep='')
        counter += 1
