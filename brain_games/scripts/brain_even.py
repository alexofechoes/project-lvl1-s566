# -*- coding:utf-8 -*-

"""Script for run cli."""

from brain_games.cli import ask, ask_name, greet_user
from brain_games.games.brain_even import check_answer, create_number

GAME_STEP_COUNT = 3
GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def main():
    """Run script."""
    print('Welcome to the Brain Games!')
    print(GAME_DESCRIPTION, end='\n\n')

    user_name = ask_name()
    print(greet_user(user_name), end='\n\n')
    run_game(user_name)


def run_game(user_name):
    """Game proccess."""
    correct_answers_count = 0

    while correct_answers_count < GAME_STEP_COUNT:
        number = create_number()
        print('Question: {number}'.format(number=number))

        user_answer = ask('Your answer: ')
        is_correct, message = check_answer(number, user_answer)
        print(message)

        if (not is_correct):
            print("Let's try again, {user_name}!".format(user_name=user_name))
            return
        correct_answers_count += 1
    print('Congratulations, {user_name}!'.format(user_name=user_name))


if __name__ == '__main__':
    main()
