# -*- coding:utf-8 -*-

"""Main script for prime game."""


import sys
import os
current_script_dir = os.path.dirname(__file__)
brain_games_path = os.path.join(current_script_dir, '..')
sys.path.append(brain_games_path)
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
