from brain_games.logics import try_again, welcome_user, comparison_answers
from brain_games.logics import congratulations, get_answer_user
from brain_games.logics import get_random_number, question


def game_parity_check():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        num = get_random_number(1, 100)
        answer = ['yes', 'no'][num % 2]
        print(question(num))

        if comparison_answers(get_answer_user(), answer):
            return try_again(name)

    return congratulations(name)

# print(parity_check())
