# -*- coding:utf-8 -*-

"""Main cli module for even game."""

import sys
import os
current_script_dir = os.path.dirname(__file__)
brain_games_path = os.path.join(current_script_dir, '..')
sys.path.append(brain_games_path)
from cli import greet_first, welcome_user
from even_game import even_game_logic


def main():
    """Run brain-even game."""
    greet_first()
    name = welcome_user()
    even_game_logic(name)


if __name__ == '__main__':
    main()
