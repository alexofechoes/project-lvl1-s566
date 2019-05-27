#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script for run cli."""

from brain_games.games import brain_progression
from brain_games.scripts import brain_games


def main():
    """Run game."""
    brain_games.main(brain_progression)


if __name__ == '__main__':
    main()
