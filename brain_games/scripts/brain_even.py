# -*- coding:utf-8 -*-

"""Main cli module for even game."""

import sys
sys.path.insert(1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games')
import cli
import greet_first
import even_game


def main():
    """Run brain-even game."""
    greet_first.greet_first()
    name = cli.welcome_user()
    even_game.even_game_logic(name)


if __name__ == '__main__':
    main()
