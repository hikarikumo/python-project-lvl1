# -*- coding:utf-8 -*-

"""Main script for gcd game."""

import sys
import os
current_script_dir = os.path.dirname(__file__)
brain_games_path = os.path.join(current_script_dir, '..')
sys.path.append(brain_games_path)
from cli import greet_first, welcome_user
from gcd_game import gcd_game, gcd_goal_message


def main():
    """
    Run brain-gcd game.

    returns:
    Correct answer on the screen with result and username.
    """
    greet_first()
    gcd_goal_message()
    name = welcome_user()
    gcd_game(name)


if __name__ == '__main__':
    main()
