# -*- coding:utf-8 -*-

"""Engine game."""

CORRECT_ANSWER_MESSAGE = 'Correct'
GAME_STEP_COUNT = 3


def run(ask, say, game=None):
    """Run game."""
    say('Welcome to the Brain Games!')

    if game:
        say(game.DESCRIPTION)
    say()

    user_name = ask('May I have your name? ')
    say('Hello, {name}!'.format(name=user_name))
    say()

    if game:
        _game_proccess(ask, say, game.generate_question, user_name)


def _game_proccess(ask, say, generate_question, user_name):
    """Game proccess."""
    correct_answers_count = 0

    while correct_answers_count < GAME_STEP_COUNT:
        question, expected_answer = generate_question()
        say('Question: {question}'.format(question=question))

        user_answer = ask('Your answer: ')
        is_correct, message = _check_answer(expected_answer, user_answer)
        say(message)

        if not is_correct:
            say("Let's try again, {user_name}!".format(user_name=user_name))
            return
        correct_answers_count += 1
    say('Congratulations, {user_name}!'.format(user_name=user_name))


def _check_answer(expected_answer, user_answer):
    """Check user answer."""
    if user_answer == expected_answer:
        return True, CORRECT_ANSWER_MESSAGE
    return False, _incorrect_answer_message(expected_answer, user_answer)


def _incorrect_answer_message(correct_answer, user_answer):
    res = "'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'."
    return res.format(user_answer=user_answer, correct=correct_answer)
