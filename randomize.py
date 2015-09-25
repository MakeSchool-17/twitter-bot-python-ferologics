import random
import sys


def new_string():
    words = sys.argv[1:]

    i = 0
    lenght = len(words)
    new_str = ""

    while i < lenght:
        rand_index = random.randint(0, len(words) - 1)
        rand_word = words[rand_index]

        words.pop(rand_index)
        new_str += rand_word + " "

        i += 1

    return new_str

if __name__ == "__main__":
    for x in range(0, 10):
        randomized = new_string()
        print(randomized)
