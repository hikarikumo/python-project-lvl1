# -*- coding:utf-8 -*-

"""Main cli module for even game."""

import sys
sys.path.insert(
    1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games')
import cli
import greet_first
import brain_games
import even_check
import even_game
import prompt
import random

def main():
    greet_first.greet_first()
    name = cli.welcome_user()
    counter = 1
    result = even_game.even_game()
    while result == True and counter < 3:
        result = even_game.even_game()
        counter += 1
        if result == True and counter >= 3:
            print("Congratulations, ", name, "!", sep="")
        elif result == False:
            print("Let's try again,")


if __name__ == '__main__':
    main()