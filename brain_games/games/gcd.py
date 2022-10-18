from random import randint
from math import gcd


MIN_NUMBER = 1
MAX_NUMBER = 100
RULES_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'


def get_task_and_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    task = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))

    return task, correct_answer
