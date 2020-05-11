# -*- coding:utf-8 -*-

"""Main script for gcd game."""

import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
import cli
from greet_first import greet_first
from brain_gcd_goal import gcd_goal_message
from gcd_game import gcd_game


def main():
    """
    Run brain-gcd game.

    returns:
    Correct answer on the screen with result and username.
    """
    greet_first()
    gcd_goal_message()
    name = cli.welcome_user()
    gcd_game(name)


if __name__ == '__main__':
    main()
