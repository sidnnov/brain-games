from brain_games.functions import try_again, welcome_user, comparison_answers
from brain_games.functions import congratulations, get_answer_user
from brain_games.functions import get_random_number, question
from random import choice


def game_calc():
    name = welcome_user()
    print('What is the result of the expression?')

    for _ in range(3):
        operation = choice(['-', '+', '*'])
        num_1 = get_random_number(1, 10)
        num_2 = get_random_number(1, 10)
        answer = eval(str(num_1) + operation + str(num_2))
        action = f'{num_1} {operation} {num_2}'
        print(question(action))

        if comparison_answers(get_answer_user(), str(answer)):
            return try_again(name)

    return congratulations(name)

# print(calc())
