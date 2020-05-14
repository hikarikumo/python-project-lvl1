# -*- coding:utf-8 -*-

"""Main script for calc game."""


import sys
sys.path.append('/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
from cli import greet_first, welcome_user
from calc_game import calc_greet_first, calc_game_logic


def main():
    """Run brain-calc game."""
    greet_first()
    calc_greet_first()
    name = welcome_user()
    calc_game_logic(name)


if __name__ == '__main__':
    main()
