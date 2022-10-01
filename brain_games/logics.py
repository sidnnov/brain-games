import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_random_number(a, b):
    return random.randint(a, b)


def question(action):
    return f'Question: {action}'


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def comparison(answer_user, answer):
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
