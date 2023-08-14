from math import sqrt
from random import randint


task = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def isPrime(num):
    if num < 2:
        return False
    delimeter = 2

    while delimeter <= sqrt(num):
        if num % delimeter == 0:
            return False
        delimeter += 1

    return True


def get_game_data():
    number = randint(1, 100)
    question = f"Question: {number}"
    right_answer = "yes" if isPrime(number) else "no"
    return (right_answer, question)
