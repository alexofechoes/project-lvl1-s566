# -*- coding:utf-8 -*-

"""Brain even game functions."""

import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate_question():
    """Create game question."""
    number = random.randrange(1, 100)
    question = str(number)
    expected_answer = 'yes' if not number % 2 else 'no'
    return question, expected_answer
