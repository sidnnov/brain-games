from prompt import string


REPEAT = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES_OF_THE_GAME)

    for _ in range(REPEAT):
        task, correct_answer = game.get_task_and_answer()
        print(f'Question: {task}')
        answer_user = string('Your answer: ')

        if answer_user == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer_user}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
    return
