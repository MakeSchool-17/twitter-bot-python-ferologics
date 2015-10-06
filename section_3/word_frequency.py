import sys
import re


def histogram(source_text):
    file = open(source_text)
    string = file.read()

    compiled_rgx = re.compile(r"[^a-zA-Z0-9]*")

    list = re.split(compiled_rgx, string.lower())
    histogram = {}

    for word in list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def unique_words(histogram):
    uniques = 0
    for key in histogram:
        uniques += 1
    return uniques


def frequency(histogram, word):
    return histogram.get(word, 0)


if __name__ == "__main__":
    path = str(sys.argv[1])
    hist = histogram(path)
    uniques = unique_words(hist)
    frequency_of_word_are = frequency(hist, "are")

    print(path)
    print(hist)
    print(uniques)
    print(frequency_of_word_are)
