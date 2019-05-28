# -*- coding:utf-8 -*-

"""Functions for cli."""

import sys

import prompt


def reader(message):
    """Ask message."""
    return prompt.string(message)


def writer(message):
    """Write message in stdout."""
    sys.stdout.write(message + '\n')
