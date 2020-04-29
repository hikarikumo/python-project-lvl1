# -*- coding:utf-8 -*-

"""Main cli module for even game."""

import sys
import brain_games
import cli
import even_check
import prompt
import random

def even_game():
    random_number = random.randint(0,100)
    even_result = even_check.check_if_even(random_number)
    print(random_number)
    answer = prompt.string(prompt="Answer 'yes' if number even otherwise answer 'no'.\n")
    if str(answer) == 'yes' and even_result == True:
        print ("Your answer: yes")
        return True
    elif str(answer) == 'no' and even_result == False:
        print("Your answer: yes")
        return True
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again,")
        return False