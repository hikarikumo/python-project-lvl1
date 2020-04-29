# -*- coding:utf-8 -*-

"""Greeting messages and users representation."""

import sys

sys.path.insert(
    1, '/home/alabarym/git/alabarym/python-project-lvl1/brain_games')
import cli
import greet_first

def main():
    greet_first.greet_first()
    cli.welcome_user()

if __name__ == '__main__':
    main()