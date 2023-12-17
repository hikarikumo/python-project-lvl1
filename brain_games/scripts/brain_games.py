# -*- coding:utf-8 -*-

"""Greeting messages and users representation."""

import sys
import os
# sys.path.append('/Users/vladimir.vasilenko/git/python-project-lvl1/brain_games/')
current_script_dir = os.path.dirname(__file__)
brain_games_path = os.path.join(current_script_dir, '..')
sys.path.append(brain_games_path)
from cli import greet_first
from cli import welcome_user


def main():
    """Script to say hi to user."""
    greet_first()
    welcome_user()


if __name__ == '__main__':
    main()
