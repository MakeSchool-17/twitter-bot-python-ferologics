import random

class Node(object):

    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleList(object):

    head = None
    tail = None

    def append(self, data):
        new_node = Node(data, None, None)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        current_node = self.head

        while current_node is not None:

            if current_node.data == node_value:
                # if not first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                # else current node is head
                else:
                    self.head = current_node.next
                    current_node.next.prev = None
            current_node = current_node.next

    def show(self):
        print("Printing the data")
        current_node = self.head

        while current_node is not None:
            print(current_node.prev.data if hasattr(current_node.prev, "data") else None)
            print(current_node.data)
            print(current_node.next.data if hasattr(current_node.next, "data") else None)

            current_node = current_node.next
        print("*" * 50)

if __name__ == "__main__":
    d = DoubleList()

    d.append(("meh", 5))
    d.append((6, 5))
    d.append((50, 55))
    d.append((30, 13))

    d.show()

    d.remove((50, 55))
    d.remove(("meh", 5))

    d.show()
