# -*- coding:utf-8 -*-
"""Greeing to the users by name."""
"""Return name of the person."""

import prompt


def welcome_user():
    """Ask users name and store it."""
    user_name = prompt.string('May I know your name? ')
    print('Hello, ', user_name, '!', sep='')
    return user_name
