# -*- coding:utf-8 -*-

"""Script for run cli."""

from brain_games.cli import ask, ask_name, greet_user
from brain_games.games.common import check_answer

GAME_STEP_COUNT = 3


def main(game_description, generate_question_func):
    """Run game."""
    print('Welcome to the Brain Games!')
    print(game_description, end='\n\n')

    user_name = ask_name()
    print(greet_user(user_name), end='\n\n')

    run_game(generate_question_func, user_name)


def run_game(generate_question_func, user_name):
    """Game proccess."""
    correct_answers_count = 0

    while correct_answers_count < GAME_STEP_COUNT:
        question, expected_answer = generate_question_func()
        print('Question: {question}'.format(question=question))

        user_answer = ask('Your answer: ')
        is_correct, message = check_answer(expected_answer, user_answer)
        print(message)

        if (not is_correct):
            print("Let's try again, {user_name}!".format(user_name=user_name))
            return
        correct_answers_count += 1
    print('Congratulations, {user_name}!'.format(user_name=user_name))
