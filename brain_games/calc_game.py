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
    answer_sum, number1, number2 = calc_game_summ()
    question_sum = prompt.string(
        'Question: ' + str(number1) + ' + ' + str(number2) + '\n')
    if question_sum == str(answer_sum):
        print('Your answer: ' + question_sum)
        print('Correct!')
        return True
    else:
        print("'" + str(question_sum) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_sum) + "'")
        return False

def calc_game_subtract():
    """Subtract operation."""
    random_number3 = random.randint(0, 100)
    random_number4 = random.randint(0, 100)
    answer_subtraction = random_number3 - random_number4
    return answer_subtraction, random_number3, random_number4

def subtract_check():
    answer_subtraction, random_number3, random_number4 = calc_game_subtract()
    question_subtraction = prompt.string('Question: ' + str(random_number3) + ' - ' + str(random_number4) + '\n')
    if question_subtraction == str(answer_subtraction):
        print('Your answer: ' + question_subtraction)
        print('Correct!')
        return True
    else:
        print("'" + str(question_subtraction) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_subtraction) + "'")
        return False

def calc_game_multiplication():
    random_number5 = random.randint(0, 10)
    random_number6 = random.randint(0, 10)
    answer_multiplication = random_number5 * random_number6
    return answer_multiplication, random_number5, random_number6


def multiplication_check():
    answer_multiplication, random_number5, random_number6 = calc_game_multiplication()
    question_multiplication = prompt.string('Question: ' + str(random_number5) + ' * ' + str(random_number6) + '\n')
    if question_multiplication == str(answer_multiplication):
        print('Your answer: ' + question_multiplication)
        print('Correct!')
        return True
    else:
        print("'" + str(question_multiplication) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_multiplication) + "'")
        return False


def calc_game():
    """Play calculation game.

    Returns:
        True ot False according to the provided answer by user.
    """
    check_result = summ_check()
    subtrack_result = subtract_check()
    multiplication_result = multiplication_check()
    if check_result + subtrack_result + multiplication_result is 3:
        return True
    else:
        return False

def calc_game_logic(received_value, name):
    """Calc game logic function."""
    counter = 1
    while received_value is True and counter < 3:
        received_value = calc_game()
        if received_value is True and counter >= 3:
            print('Congratulations, ', name, '!', sep='')
        elif received_value is False:
            print("Let's try again, ", name, '!', sep='')
        counter += 1
