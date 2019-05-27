# -*- coding:utf-8 -*-

"""Common functions for games."""

CORRECT_ANSWER_MESSAGE = 'Correct'
GAME_STEP_COUNT = 3


def run_game(reader, writer, generate_question, user_name):
    """Game proccess."""
    correct_answers_count = 0

    while correct_answers_count < GAME_STEP_COUNT:
        question, expected_answer = generate_question()
        writer(f'Question: {question}')

        user_answer = reader('Your answer: ')
        is_correct, message = _check_answer(expected_answer, user_answer)
        writer(message)

        if not is_correct:
            return "Let's try again, {user_name}!".format(user_name=user_name)
        correct_answers_count += 1
    return 'Congratulations, {user_name}!'.format(user_name=user_name)


def _check_answer(expected_answer, user_answer):
    """Check user answer."""
    if user_answer == expected_answer:
        return True, CORRECT_ANSWER_MESSAGE
    return False, _incorrect_answer_message(expected_answer, user_answer)


def _incorrect_answer_message(correct_answer, user_answer):
    res = "'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'."
    return res.format(user_answer=user_answer, correct=correct_answer)
