from random import randint
from random import randrange
from random import choice


task = "What number is missing in the progression?"


def get_game_data():
    progression = []
    progression_lehgth = randint(5, 10)
    start = randrange(1, 100)
    step = randrange(2, 5)

    for i in range(1, progression_lehgth + 1):
        element = str(start + (i-1) * step)
        progression.append(element)

    right_answer = choice(progression)
    right_answer_index = progression.index(right_answer)
    progression[right_answer_index] = '..'
    question = ' '.join(progression)

    return (right_answer, question)
