# -*- coding:utf-8 -*-

"""Main script for prime game."""


import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
import cli
from greet_first import greet_first
from prime_goal import prime_goal
from prime_game import prime_game


def main():
    """Run brain-prime game."""
    greet_first()
    prime_goal()
    name = cli.welcome_user()
    prime_game(name)


if __name__ == '__main__':
    main()
