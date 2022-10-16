from random import randint, choice


MIN_NUMBER = 1
MAX_NUMBER = 10
RULES_OF_THE_GAME = 'What is the result of the expression?'


def get_answer(first_nember, second_number, operation):

    if operation == '-':
        answer = first_nember - second_number

    elif operation == '+':
        answer = first_nember + second_number

    elif operation == '*':
        answer = first_nember * second_number

    return answer


def get_task_and_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operation = choice(['-', '+', '*'])
    correct_answer = get_answer(first_number, second_number, operation)
    task = f'{first_number} {operation} {second_number}'

    return task, str(correct_answer)
