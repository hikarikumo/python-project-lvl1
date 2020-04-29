# -*- coding:utf-8 -*-

"""Greeting messages and users representation."""

import sys

sys.path.insert(
    1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games')
import cli

# checking possibility to resolve import


def greet_first():
    """First greeting message."""
    print('Welcome to the Brain Games!')

def main():
    greet_first()
    cli.welcome_user()


if __name__ == '__main__':
    main()
