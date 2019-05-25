# -*- coding:utf-8 -*-

"""Common functions for games."""


def check_answer(expected_answer, user_answer):
    """Check user answer."""
    if (user_answer == expected_answer):
        return (True, _correct_answer_message())
    return (False, _incorrect_answer_message(expected_answer, user_answer))


def _correct_answer_message():
    return 'Correct'


def _incorrect_answer_message(correct_answer, user_answer):
    res = "'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'."
    return res.format(user_answer=user_answer, correct=correct_answer)
