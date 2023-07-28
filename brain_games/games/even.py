from random import randint


task = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_game_data():
    number = randint(1, 100)
    question = f"Question: {number}"
    right_answer = "yes" if number % 2 == 0 else "no"
    return (right_answer, question)
