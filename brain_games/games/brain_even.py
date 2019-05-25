# -*- coding:utf-8 -*-

"""Brain even game functions."""
import random


def generate_question():
    """Create game question."""
    number = _create_random_number()
    question = '{num}'.format(num=number)
    expected_answer = _get_expected_answer(number)
    return question, expected_answer


def _create_random_number():
    """Create random number."""
    return random.randrange(1, 100)


def _get_expected_answer(number):
    return 'yes' if number % 2 == 0 else 'no'
