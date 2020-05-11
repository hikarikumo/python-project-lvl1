# -*- coding:utf-8 -*-
"""Calc games function to ask questions and verify the answers."""

import random

import prompt


def calc_game():
    """Play calculation game.

    Returns:
        True ot False according to the provided answer by user.
    """
    random_number1 = random.randint(0, 100)
    random_number2 = random.randint(0, 100)
    random_number3 = random.randint(0, 100)
    random_number4 = random.randint(0, 100)
    random_number5 = random.randint(0, 10)
    random_number6 = random.randint(0, 10)

    answer_sum = random_number1 + random_number2
    question_sum = prompt.string('Question: ' + str(random_number1) + ' + ' + str(random_number2) + '\n')
    if question_sum == str(answer_sum):
        print('Your answer: ' + question_sum)
        print('Correct!')
        answer_subtraction = random_number3 - random_number4
        question_subtraction = prompt.string('Question: ' + str(random_number3) + ' - ' + str(random_number4) + '\n')
        if question_subtraction == str(answer_subtraction):
            print('Your answer: ' + question_subtraction)
            print('Correct!')
            answer_multiplication = random_number5 * random_number6
            question_multiplication = prompt.string('Question: ' + str(random_number5) + ' * ' + str(random_number6) + '\n')
            if question_multiplication == str(answer_multiplication):
                print('Your answer: ' + question_multiplication)
                print('Correct!')
                return True
            else:
                print("'" + str(question_multiplication) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_multiplication) + "'")
        else:
            print("'" + str(question_subtraction) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_subtraction) + "'")
    else:
        print("'" + str(question_sum) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_sum) + "'")
    return False


def calc_game_logic(received_value, name):
    """Calc game logic function."""
    counter = 1
    while received_value is True and counter < 3:
        received_value = calc_game()
        counter += 1
        if received_value is True and counter >= 3:
            print('Congratulations, ', name, '!', sep='')
        if received_value is False:
            print("Let's try again, ", name, '!', sep='')
