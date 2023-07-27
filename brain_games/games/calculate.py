from random import randint, choice

task = 'What is the result of the expression?'
operators = ['+', '-', '*']


def get_game_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = choice(operators)
    question = f"{number1} {operator} {number2}"
    right_answer = None

    if (operator == '+'):
        right_answer = number1 + number2
    if (operator == '-'):
        right_answer = number1 - number2
    if (operator == '*'):
        right_answer = number1 * number2

    return (right_answer, question)
