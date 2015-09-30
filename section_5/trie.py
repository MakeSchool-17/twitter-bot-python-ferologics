import random


class Node(object):

    def __init__(self, key, child, value):
        self.key = key
        self.child = child
        self.value = value


class Trie(object):

    head = None
    tail = None

    def append(self, *words):

        if type(data) != str:
            raise TypeError("This 'trie' only works with strings")
        else:
            if self.head is None:
                for word in words:


                    for letter in word:


                    # new_node = Node(data, None, None, None)
            # else:
