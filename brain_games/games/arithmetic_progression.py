from random import randint


def get_task_and_answer():
    step = randint(2, 30)
    start_progression = randint(1, 50)
    index_answer = randint(0, 9)
    progression = [i for i in range(10)]

    for i in range(10):
        progression[i] = str(progression[i] + start_progression)
        start_progression += step

    correct_answer = progression[index_answer]
    progression[index_answer] = '..'

    return ' '.join(progression), correct_answer


rules_of_the_game = 'What number is missing in the progression?'
