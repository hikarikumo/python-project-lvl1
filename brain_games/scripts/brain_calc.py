# -*- coding:utf-8 -*-

"""Main script for calc game."""

import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games')
import cli
import greet_first
import brain_calc_question
import calc_game


def main():
    """Run brain-calc game."""
    greet_first.greet_first()
    brain_calc_question.calc_greet_first()
    name = cli.welcome_user()
    received_value = calc_game.calc_game()
    calc_game.calc_game_logic(received_value, name)


if __name__ == '__main__':
    main()
