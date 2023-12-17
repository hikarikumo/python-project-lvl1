# -*- coding:utf-8 -*-

"""Main script for prime game."""


import sys
sys.path.append('/Users/vladimir.vasilenko/git/python-project-lvl1/brain_games/')
from cli import greet_first, welcome_user
from prime_game import prime_game, prime_goal


def main():
    """Run brain-prime game."""
    greet_first()
    prime_goal()
    name = welcome_user()
    prime_game(name)


if __name__ == '__main__':
    main()
