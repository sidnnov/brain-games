from brain_games.logics import try_again, welcome_user, comparison, question
from brain_games.logics import congratulations, get_answer, get_random_number
import random


def calc():
    name = welcome_user()
    print('What is the result of the expression?')

    for _ in range(3):
        operation = random.choice(['-', '+', '*'])
        num_1 = get_random_number(1, 10)
        num_2 = get_random_number(1, 10)
        answer = eval(str(num_1) + operation + str(num_2))
        action = f'{num_1} {operation} {num_2}'
        print(question(action))

        if comparison(get_answer(), str(answer)):
            return try_again(name)

    return congratulations(name)

# print(calc())
