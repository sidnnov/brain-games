from random import randint
from math import gcd


MIN_NUMBER = 1
MAX_NUMBER = 100
RULES_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'


def get_task_and_answer():
    first_nember = randint(MIN_NUMBER, MAX_NUMBER)
    second_nember = randint(MIN_NUMBER, MAX_NUMBER)
    task = f'{first_nember} {second_nember}'
    correct_answer = gcd(first_nember, second_nember)

    return task, str(correct_answer)
