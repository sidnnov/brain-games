from brain_games.functions import welcome_user, is_comparison_answers
from prompt import string


def start_game(game):
    name = welcome_user()
    print(game.rules_of_the_game)

    for _ in range(3):
        task, correct_answer = game.get_task_and_answer()
        print(f'Question: {task}')
        answer_user = string('Your answer: ')

        if is_comparison_answers(answer_user, correct_answer):
            return f"Let's try again, {name}!"

    return f'Congratulations, {name}!'
