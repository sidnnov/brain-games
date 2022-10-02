from brain_games.functions import try_again, welcome_user, is_comparison_answers
from brain_games.functions import congratulations, get_answer_user
from brain_games.functions import get_random_number, question


def get_answer(num):
    counter = 0
    for i in range(2, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 1:
        return 'yes'
    return 'no'


def game_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        number = get_random_number(1, 31)
        answer = get_answer(number)
        print(question(number))

        if is_comparison_answers(get_answer_user(), answer):
            return try_again(name)

    return congratulations(name)

# print(game_prime())
