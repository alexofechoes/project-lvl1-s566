# -*- coding:utf-8 -*-

"""Brain even game functions."""

import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question():
    """Create game question."""
    num1 = _create_random_number()
    num2 = _create_random_number()
    question = '{num1} {num2}'.format(num1=num1, num2=num2)
    expected_answer = str(_gcd(num1, num2))
    return question, expected_answer


def _create_random_number():
    """Create random number."""
    return random.randrange(1, 100)


def _gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
