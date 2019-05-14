# -*- coding:utf-8 -*-

"""Brain even game functions."""
import os


def check_answer(number, user_answer):
    """Check user answer."""
    expected_answer = _get_expected_answer(number)
    if (user_answer == expected_answer):
        return (True, _correct_answer_message())
    return (False, _incorrect_answer_message(expected_answer, user_answer))


def create_number():
    """Create random number."""
    return int.from_bytes(os.urandom(1), byteorder='big')


def _get_expected_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def _correct_answer_message():
    return 'Correct'


def _incorrect_answer_message(correct_answer, user_answer):
    res = "'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'."
    return res.format(user_answer=user_answer, correct=correct_answer)
