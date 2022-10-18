from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 31
RULES_OF_THE_GAME = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False

    return True


def get_task_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    result = is_prime_number(number)
    correct_answer = 'yes' if result else 'no'
    taks = str(number)

    return taks, correct_answer
