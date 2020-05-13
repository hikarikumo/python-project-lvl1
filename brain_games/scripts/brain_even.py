# -*- coding:utf-8 -*-

"""Main cli module for even game."""

import sys
sys.path.append('/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
from cli import greet_first, welcome_user
from even_game import even_game_logic


def main():
    """Run brain-even game."""
    greet_first()
    name = welcome_user()
    even_game_logic(name)


if __name__ == '__main__':
    main()
