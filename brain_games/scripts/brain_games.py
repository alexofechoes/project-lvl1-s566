#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script for run cli."""

from brain_games.cli import reader, writer
from brain_games.games.common import run_game


def main(game=None):
    """Run game."""
    print('Welcome to the Brain Games!')

    if game:
        print(game.DESCRIPTION)
    print()
    user_name = writer('May I have your name? ')
    print('Hello, {name}! \n\n'.format(name=user_name), end='\n\n')

    if game:
        message = run_game(reader, writer, game.generate_question, user_name)
        print(message)


if __name__ == '__main__':
    main()
