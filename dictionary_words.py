import sys
import random
import cProfile
import re

# profiling the script for speed
cProfile.run('re.compile("foo|bar")')


def few_words(n):

    path = "words.txt"  # path to the file
    file = open(path, encoding='utf-8')  # file variable from path
    string = file.read()  # read text from file
    list = string.split()  # create a dict or with each word as object

    str = ""  # result string

    for i in range(n):
        random_num = random.randint(0, (len(list) - 1))
        str += list[random_num] + " "
        list.pop(random_num)
    return str

if __name__ == "__main__":
    n = int(sys.argv[1])

    for i in range(5):
        random_words = few_words(n)
        print(random_words)
