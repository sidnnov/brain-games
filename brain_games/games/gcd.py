from brain_games.logics import try_again, welcome_user, comparison_answers
from brain_games.logics import congratulations, get_answer_user
from brain_games.logics import get_random_number, question


def get_gcd_answer(num_1, num_2):
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return num_1


def game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    for _ in range(3):
        num_1 = get_random_number(1, 100)
        num_2 = get_random_number(1, 100)
        answer = get_gcd_answer(num_1, num_2)
        action = f'{num_1} {num_2}'
        print(question(action))

        if comparison_answers(get_answer_user(), str(answer)):
            return try_again(name)

    return congratulations(name)

# print(game_gcd())
