from brain_games.logics import try_again, welcome_user, comparison, question
from brain_games.logics import congratulations, get_answer, get_random_number


def gcd(num_1, num_2):
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
        answer = gcd(num_1, num_2)
        action = f'{num_1} {num_2}'
        print(question(action))

        if comparison(get_answer(), str(answer)):
            return try_again(name)

    return congratulations(name)

# print(game_gcd())
