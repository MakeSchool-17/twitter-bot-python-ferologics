import sys
import random
import word_frequency


def random_word(histogram):
    return random.choice(list(histogram.keys()))

if __name__ == "__main__":
    path = sys.argv[1]
    hist = word_frequency.histogram(path)
    rand_word = random_word(hist)
    print(rand_word)
