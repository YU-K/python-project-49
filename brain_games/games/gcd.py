from random import randint
from math import gcd


task = "Find the greatest common divisor of given numbers."


def get_game_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    qestion = f'{number1} {number2}'
    right_answer = gcd(number1, number2)

    return (right_answer, qestion)
