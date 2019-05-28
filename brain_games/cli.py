# -*- coding:utf-8 -*-

"""Functions for cli."""

import sys

import prompt


def ask(message):
    """Read message."""
    return prompt.string(message)


def say(message=''):
    """Write message in stdout."""
    sys.stdout.write(message + '\n')
