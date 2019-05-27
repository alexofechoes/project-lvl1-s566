# -*- coding:utf-8 -*-

"""Script for run cli."""
from brain_games.games.brain_gcd import GAME_DESCRIPTION, generate_question
from brain_games.scripts.brain_games import main as game


def main():
    """Run game."""
    game(GAME_DESCRIPTION, generate_question)


if __name__ == '__main__':
    main()
