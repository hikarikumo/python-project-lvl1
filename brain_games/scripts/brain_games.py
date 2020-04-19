# -*- coding:utf-8 -*-

"""Greeting messages and users representation."""

import sys

sys.path.insert(1, 'brain_games')

import cli

# checking possibility to resolve import


def main():
    """First greeting message."""
    print('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()
    cli.welcome_user()
