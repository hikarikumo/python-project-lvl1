# -*- coding:utf-8 -*-

"""Main cli module for even game."""

import sys
import brain_games
import cli
import even_check
import even_game
import prompt
import random


if __name__ == '__main__':
    brain_games.greet_first()
    name = cli.welcome_user()
    counter = 1
    result = even_game.even_game()
    while result == True and counter < 3:
        result = even_game.even_game()
        counter += 1
    else:
        print("Congratulations, ", name, "!", sep="")
