class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev


class Stack(object):

    top = None
    lenght = 0

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):
        new_node = Node(data, None, None)  # initialize empty node
        self.lenght += 1

        if self.is_empty() is True:  # if stack empty make new_node the top
            self.top = new_node
        else:  # otherwise handle the prev, next and top ...
            new_node.prev = self.top
            self.top.next = new_node
            self.top = new_node

    def pop(self):
        if self.is_empty() is False:  # if list not empty
            temp_node = self.top

            if self.lenght == 1:
                self.lenght = 0
                self.top = None
            else:
                self.lenght -= 1
                self.top = None
                self.top = temp_node.prev

            return temp_node.data
        else:
            return None

if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(7)

    for i in range(3):
        print(s.pop())
