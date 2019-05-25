# -*- coding:utf-8 -*-

"""Script for run cli."""
from brain_games.games.brain_even import generate_question
from brain_games.scripts.brain_games import main as game

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def main():
    """Run game."""
    game(GAME_DESCRIPTION, generate_question)


if __name__ == '__main__':
    main()
