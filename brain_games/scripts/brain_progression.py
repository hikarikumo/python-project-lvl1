# -*- coding:utf-8 -*-

"""Main script for progression game."""


import sys
import os
current_script_dir = os.path.dirname(__file__)
brain_games_path = os.path.join(current_script_dir, '..')
sys.path.append(brain_games_path)
from cli import greet_first, welcome_user
from progression_game import progression_game, progression_goal


def main():
    """
    Run brain-progression game.

    Returns:
        Return and verify the proper elemen inside of the ariphmetic progressio.
    """
    greet_first()
    progression_goal()
    name = welcome_user()
    progression_game(name)


if __name__ == '__main__':
    main()
