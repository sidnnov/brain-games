from random import randint


def get_task_and_answer():
    number = randint(1, 31)
    counter = 0

    for i in range(2, number + 1):
        if number % i == 0:
            counter += 1

    if counter == 1:
        return number, 'yes'

    return number, 'no'


rules_of_the_game = 'Answer "yes" if given numberber is prime. \
Otherwise answer "no".'
