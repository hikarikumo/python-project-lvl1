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
    counter = 1
    received_value = even_game.even_game()
    while received_value is True and counter < 3:
        received_value = even_game.even_game()
        counter += 1
        if received_value is True and counter >= 3:
            print('Congratulations, ', name, '!', sep='')
        elif received_value is False:
            print("Let's try again,")


if __name__ == '__main__':
    main()
