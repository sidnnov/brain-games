from brain_games.logics import try_again, welcome_user, comparison_answers
from brain_games.logics import congratulations, get_answer_user
from brain_games.logics import get_random_number, question


def get_progression_and_answer():
    step = get_random_number(2, 30)
    start_progression = get_random_number(1, 50)
    index_answer = get_random_number(0, 9)
    progression = [i for i in range(10)]

    for i in range(10):
        progression[i] = str(progression[i] + start_progression)
        start_progression += step

    answer = progression[index_answer]
    progression[index_answer] = '..'

    return ' '.join(progression), answer


def game_arith_progress():
    name = welcome_user()
    print('What number is missing in the progression?')

    for _ in range(3):
        progression, answer = get_progression_and_answer()
        print(question(progression))

        if comparison_answers(get_answer_user(), answer):
            return try_again(name)

    return congratulations(name)

# print(game_arith_progress())
# print(get_progression_and_answer())
