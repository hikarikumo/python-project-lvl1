# -*- coding:utf-8 -*-

"""Calc games function to ask questions and verify the answers"""

import prompt
import random


def calc_game():
    """
    Verify the correct answer.

    Test what does the user type in: yes or not.
    Other characters are not allowed.
    Verify the correct answer provided by user.

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
    question_sum = prompt.string(prompt="Question: " + str(random_number1) + ' + ' + str(random_number2) + '\n')
    if question_sum == str(answer_sum) :
        print('Your answer: ' + question_sum)
        print('Correct!')
        answer_subtraction = random_number3 - random_number4
        question_subtraction = prompt.string(
        prompt="Question: " + str(random_number3) + ' - ' + str(random_number4) + '\n')
        if question_subtraction == str(answer_subtraction):
            print('Your answer: ' + question_subtraction)
            print('Correct!')
            answer_multiplication = random_number5 * random_number6
            question_multiplication = prompt.string(
            prompt="Question: " + str(random_number5) + ' * ' + str(random_number6) + '\n')
            if question_multiplication == str(answer_multiplication):
                print('Your answer: ' + question_multiplication)
                print('Correct!')
                return True
            else:
                print("'" + str(question_multiplication) + "' " +
                      "is wrong answer ;(. Correct answer was " + "'" + str(answer_multiplication) + "'")
                return False
        else:
            print("'" + str(question_subtraction) + "' " +
                  "is wrong answer ;(. Correct answer was " + "'" + str(answer_subtraction) + "'")
            return False
    else:
        print("'" + str(question_sum) + "' " + "is wrong answer ;(. Correct answer was " + "'" + str(answer_sum) + "'")
        return False
