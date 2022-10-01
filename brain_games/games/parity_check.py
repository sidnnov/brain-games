from brain_games.logics import try_again, welcome_user, comparison, question
from brain_games.logics import congratulations, get_answer, get_random_number


def parity_check():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        num = get_random_number(1, 100)
        answer = ['yes', 'no'][num % 2]
        print(question(num))

        if comparison(get_answer(), answer):
            return try_again(name)

    return congratulations(name)

# print(parity_check())
