import sys
import random
import word_frequency


def stochastic_list(histogram):
    new_list = []

    for word in histogram.keys():

        for i in range(0, histogram[word]):
            new_list.append(word)

    return new_list


def random_word(list):
    return random.choice(list)


def randomnes_check(hist):
    n_of_times = word_frequency.unique_words(hist)
    list = stochastic_list(hist)
    chosen = {}

    for i in range(n_of_times * 100):
        word = random_word(list)

        if chosen.get(word, 0) != 0:
            chosen[word] += 1
        else:
            chosen[word] = 1

    return chosen

if __name__ == "__main__":
    path = sys.argv[1]
    hist = word_frequency.histogram(path)
    check = randomnes_check(hist)

    for key, value in check.items():
        print(key + "\t" + str(value))
    print(len(check.keys()))
