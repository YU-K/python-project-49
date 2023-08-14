#!/usr/bin/venv python3
import prompt


def game_engine(get_game_data, task):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    rounds_count = 3
    while rounds_count > 0:
        right_answer, question = get_game_data()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(right_answer):
            print("Correct!")
            rounds_count -= 1
        else:
            print(f"""'{user_answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.\n \
Let's try again, {name}!""")
            return
    print(f"Congratulations, {name}!")
