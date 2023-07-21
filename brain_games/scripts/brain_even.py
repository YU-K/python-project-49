#!/usr/bin/venv python3
from random import randint
import prompt


start = 0
finish = 100


def guess_a_number():
    shot = 3
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    while shot > 0:
        number = randint(start, finish)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        right_answer = "yes" if number % 2 == 0 else "no"
        if (user_answer != right_answer):
            print(f"'{user_answer}' is wrong answer ;(. \
                  Correct answer was '{right_answer}'.  \
                  Let's try again, {name}!")
            return
        print("Correct!")
        shot -= 1
    print(f"Congratulations, {name}!")


def greeting():
    print("Welcome to the Brain Games!")


def main():
    greeting()
    guess_a_number()


if __name__ == '__main__':
    main()
