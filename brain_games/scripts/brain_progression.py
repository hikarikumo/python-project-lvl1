# -*- coding:utf-8 -*-

"""Main script for progression game."""


import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
import cli
from greet_first import greet_first
from progression_goal import progression_goal
from progression_game import progression_game


def main():
    """
    Run brain-progression game.

    Returns:
        Return and verify the proper elemen inside of the ariphmetic progressio.
    """
    greet_first()
    progression_goal()
    name = cli.welcome_user()
    progression_game(name)


if __name__ == '__main__':
    main()
