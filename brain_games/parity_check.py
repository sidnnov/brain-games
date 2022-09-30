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
        yes_or_no = ['yes', 'no'][num % 2]
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if yes_or_no == answer:
            print('Correct!')

        else:
            print(f'"{answer}" is wrong answer ;(.'
                  f' Correct answer was "{yes_or_no}".')

            return f"Let's try again, {name}!"

    return f'Congratulations, {name}!'
