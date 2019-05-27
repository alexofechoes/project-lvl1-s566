#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script for run cli."""
from brain_games.games import brain_calc
from brain_games.scripts import brain_games


def main():
    """Run game."""
    brain_games.main(brain_calc)


if __name__ == '__main__':
    main()
