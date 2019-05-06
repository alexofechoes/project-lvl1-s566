# -*- coding:utf-8 -*-

"""Script for run cli."""

from brain_games.cli import ask_name, greet_user


def main():
    """Run cli."""
    print('Welcome to the Brain Games!')
    print()
    print(greet_user(ask_name()))


if __name__ == '__main__':
    main()
