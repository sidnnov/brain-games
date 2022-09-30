import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def parity_check(name=welcome_user()):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if (num % 2 == 0 and answer == 'yes') or (num % 2 != 0 and answer == 'no'):
            print('Correct!')
        else:
            y_or_n = ['yes', 'no'][num % 2]
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{y_or_n}".')
            return f"Let's try again, {name}!"
    return f'Congratulations, {name}!'
