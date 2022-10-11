from random import randint


LENGTH = 10
MIN_STEP = 2
MAX_STEP = 30
MIN_START = 1
MAX_START = 50
MIN_INDEX_ANSWER = 0
MAX_INDEX_ANSWER = 9
RULES_OF_THE_GAME = 'What number is missing in the progression?'


def get_progression():
    step = randint(MIN_STEP, MAX_STEP)
    start = randint(MIN_START, MAX_START)
    stop = start + (LENGTH * step)
    progression = [str(i) for i in range(start, stop, step)]
    return progression


def get_task_and_answer():
    progression = get_progression()
    index_correct_answer = randint(MIN_INDEX_ANSWER, MAX_INDEX_ANSWER)
    correct_answer = progression[index_correct_answer]
    progression[index_correct_answer] = '..'
    task = ' '.join(progression)

    return task, correct_answer
