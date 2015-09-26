import sys
import random
import cProfile
import re

# profiling the script for speed
cProfile.run('re.compile("foo|bar")')


def histogram(source_text):
    file = open(source_text, encoding="utf-8")
    string = file.read()

    list = re.split("[^a-zA-Z0-9]*", string.lower())
    histogram = {}

    for word in list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    print(list[:250])
    print(histogram)

# def unique_words(histogram):
#
#
# def frequency(histogram, word):


if __name__ == "__main__":
    path = str(sys.argv[1])
    print(path)
    histogram(path)
