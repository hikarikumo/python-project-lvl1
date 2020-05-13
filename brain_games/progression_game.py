# -*- coding:utf-8 -*-
"""Function to calculate ariphmetic progression."""

import random
import prompt


def progression_goal():
    """Information about the goal to the user."""
    print('What number is missing in the progression?\n')


def string_progression(progression):
    """Convert list into parsed string."""
    counter = 0
    string = ''
    while counter < len(progression):
        if counter == len(progression) - 1:
            string += str(progression[counter])
            return string
        string += str(progression[counter]) + ', '
        counter += 1


def question_progression():
    """
    Ask the question and return bool and value.

    Returns:
        True and value if answer is missing element.
        False and value if answer is not missing element.
    """
    miss_element, progression = progression_show()
    question_to_user = prompt.string('Question: ' + string_progression(progression) + '\n')
    if question_to_user == str(miss_element):
        return True, miss_element
    return False, miss_element


def progression_show():
    """
    Create ariphmetic progression.

    Returns:
        Progression with *hidden* element + value of that hidden element.
    """
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    random_number3 = random.randint(1, 10)
    progression = progression_calc(random_number2, random_number3)
    keep_value = progression[random_number1]
    progression[random_number1] = '..'
    return keep_value, progression


def progression_game(name):
    """Perform progression game logic."""
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


def progression_calc(random_step, random_initial):
    """
    Create progression.

    Input:
        Accept two random parameters: position and progression step.

    Returns:
        Returns progression list.
    """
    progression = []
    progression.append(random_initial)
    progression_length = 11
    counter = 1
    progression_member = random_initial
    while counter < progression_length:
        progression_member += random_step
        progression.append(progression_member)
        counter += 1
    return progression
