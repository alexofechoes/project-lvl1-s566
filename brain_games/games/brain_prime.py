# -*- coding:utf-8 -*-

"""Brain even game functions."""
import random

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def generate_question():
    """Create game question."""
    number = _create_random_number()
    question = '{num}'.format(num=number)
    expected_answer = _get_expected_answer(number)
    return question, expected_answer


def _create_random_number():
    """Create random number."""
    return random.randrange(1, 1000)


def _get_expected_answer(number):
    return 'yes' if _is_prime(number) else 'no'


def _is_prime(number):
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True
