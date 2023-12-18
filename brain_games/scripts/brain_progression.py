# -*- coding:utf-8 -*-

"""Main script for progression game."""


import sys
import os
current_script_dir = os.path.dirname(__file__)
brain_games_path = os.path.join(current_script_dir, '..')
sys.path.append(brain_games_path)
from progression_game import main


if __name__ == '__main__':
    main()
