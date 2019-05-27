# -*- coding:utf-8 -*-

"""Brain even game functions."""

import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_question():
    """Create game question."""
    progression = _generate_progression()
    index = random.randrange(0, len(progression))

    expected_answer = str(progression[index])
    progression[index] = '..'
    question = ' '.join(progression)

    return question, expected_answer


def _generate_progression():
    start_num = random.randrange(1, 1000)
    step = random.randrange(2, 20)
    return [str(num * step) for num in range(start_num, start_num + 11)]
