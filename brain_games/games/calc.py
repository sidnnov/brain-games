from random import randint, choice


def get_task_and_answer():
    operation = choice(['-', '+', '*'])
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    correct_answer = eval(str(num_1) + operation + str(num_2))
    task = f'{num_1} {operation} {num_2}'

    return task, str(correct_answer)


rules_of_the_game = 'What is the result of the expression?'
