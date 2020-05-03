# -*- coding:utf-8 -*-

"""Question user in progression game."""


import prompt

from progression_show import progression_show


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
