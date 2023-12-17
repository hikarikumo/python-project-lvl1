# -*- coding:utf-8 -*-

"""Main script for calc game."""


import sys
import os
current_script_dir = os.path.dirname(__file__)
brain_games_path = os.path.join(current_script_dir, '..')
sys.path.append(brain_games_path)
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
