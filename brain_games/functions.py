from prompt import string
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_random_number(a, b):
    return randint(a, b)


def question(action):
    return f'Question: {action}'


def get_answer_user():
    answer = string('Your answer: ')
    return answer


def is_comparison_answers(answer_user, answer):
    if answer_user == answer:
        print('Correct!')
        return False

    else:
        print(f'"{answer_user}" is wrong answer ;(. '
              f'Correct answer was "{answer}".')
        return True


def try_again(name):
    return f"Let's try again, {name}!"


def congratulations(name):
    return f'Congratulations, {name}!'
