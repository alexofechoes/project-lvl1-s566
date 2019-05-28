#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script for run cli."""

from brain_games.cli import ask, say
from brain_games.engine import run


def main(game=None):
    """Run game engine."""
    run(ask, say, game)


if __name__ == '__main__':
    main()
