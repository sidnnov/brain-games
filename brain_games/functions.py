from prompt import string


def welcome_user():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_comparison_answers(answer_user, answer):
    if answer_user == answer:
        print('Correct!')
        return False

    else:
        print(f'"{answer_user}" is wrong answer ;(. '
              f'Correct answer was "{answer}".')
        return True
