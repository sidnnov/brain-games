from random import randint


def get_task_and_answer():
    task = randint(1, 100)
    correct_answer = ['yes', 'no'][task % 2]

    return task, correct_answer


rules_of_the_game = 'Answer "yes" if the number is even, otherwise answer "no".'
