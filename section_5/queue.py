class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class Queue(object):

    head = None
    tail = None
    length = 0

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def enque(self, data):
        new_node = Node(data, None, None)

        if self.is_empty() is True:
            self.head = self.tail = new_node  # set tail, head to be new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def deque(self):
        if self.is_empty() is not True:
            temp_node = self.head

            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head.next.prev = None
                self.head = self.head.next

            self.length -= 1
            return temp_node.data
        return None

if __name__ == "__main__":
    q = Queue()
    q.enque(5)
    q.enque(4)
    q.enque(3)

    print("Removing elements huehuehue ~~~~>")
    for i in range(3):
        print(q.deque())
    print("*" * 50)
