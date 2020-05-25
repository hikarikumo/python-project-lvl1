# -*- coding:utf-8 -*-

"""General games module."""



def correct_answer():
    print('Correct!')


def game_success_finish(name):
    print('Congratulations, ', name, '!', sep='')


def try_again(name):
    print("Let's try again, ", name, "!", sep='')


def even_question():
    print("Answer 'yes' if number even otherwise answer 'no'.")


def even_wrong_answer_yes(answer):
    print("'" + answer + "'" + " is wrong answer ;(. Correct answer was 'no'.")


def even_wrong_answer_no(answer):
    print("'" + answer + "'" + " is wrong answer ;(. Correct answer was 'yes'.")
