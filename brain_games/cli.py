import prompt


def ask_name():
    name = prompt.string('May I have your name? ')
    return name


def greet_user(name):
    print(f'Hello, {name}!')
