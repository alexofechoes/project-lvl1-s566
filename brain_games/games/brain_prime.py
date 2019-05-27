# -*- coding:utf-8 -*-

"""Brain even game functions."""

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    """Create game question."""
    number = random.randrange(1, 1000)
    question = str(number)
    expected_answer = 'yes' if _is_prime(number) else 'no'
    return question, expected_answer


def _is_prime(number):
    for num in range(2, int(number ** 0.5) + 1):
        if not number % num:
            return False
    return True
