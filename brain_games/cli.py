# -*- coding:utf-8 -*-

"""Functions for cli."""

import prompt


def ask_name():
    """Ask user name."""
    name = prompt.string('May I have your name? ')
    return name


def greet_user(name):
    """Greet user."""
    return 'Hello, {name}!'.format(name=name)


def ask(message):
    """Ask question and return answer."""
    return prompt.string(message)
