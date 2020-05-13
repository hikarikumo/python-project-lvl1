# -*- coding:utf-8 -*-

"""Greeting messages and users representation."""

import sys
sys.path.append('/home/alabarym/git/alabarym/python-project-lvl1/brain_games/')
from cli import greet_first
from cli import welcome_user


def main():
    """Script to say hi to user."""
    greet_first()
    welcome_user()


if __name__ == '__main__':
    main()
