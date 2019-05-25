# -*- coding:utf-8 -*-

"""Brain even game functions."""
import random


def generate_question():
    """Create game question."""
    progression = _generate_progression()
    index = random.randrange(0, len(progression))
    progression_question = progression[:]
    progression_question[index] = '..'
    question = ' '.join(progression_question)
    expected_answer = _get_expected_answer(progression, index)
    return question, expected_answer


def _generate_progression():
    step = _create_random_number()
    return [str(num * step) for num in range(1, 11)]


def _create_random_number():
    """Create random number."""
    return random.randrange(1, 100)


def _get_expected_answer(progression, index):
    return str(progression[index])
