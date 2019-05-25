# -*- coding:utf-8 -*-

"""Script for run cli."""
from brain_games.games.brain_progression import generate_question
from brain_games.scripts.brain_games import main as game

GAME_DESCRIPTION = 'What number is missing in the progression?'


def main():
    """Run game."""
    game(GAME_DESCRIPTION, generate_question)


if __name__ == '__main__':
    main()
