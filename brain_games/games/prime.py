from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 31
RULES_OF_THE_GAME = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime_number(number):
    counter = 0
    for i in range(2, number + 1):
        if number % i == 0:
            counter += 1
        if counter > 1:
            break

    if counter == 1:
        return True

    return False


def get_task_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    result = is_prime_number(number)
    correct_answer = ['no', 'yes'][result]
    taks = number

    return taks, correct_answer
