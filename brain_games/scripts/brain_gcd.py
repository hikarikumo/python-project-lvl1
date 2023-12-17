# -*- coding:utf-8 -*-

"""Main script for gcd game."""

import sys
sys.path.append('/Users/vladimir.vasilenko/git/python-project-lvl1/brain_games/')
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
