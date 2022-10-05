from random import randint


def get_task_and_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    task = f'{num_1} {num_2}'
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    correct_answer = num_1
    return task, str(correct_answer)


rules_of_the_game = 'Find the greatest common divisor of given numbers.'
