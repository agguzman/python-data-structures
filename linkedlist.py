class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def contains(self, data):
        current = self.head
        while(current is not None):
            if current.data is data:
                return True
            else:
                current = current.next
        return False

    def printer(self):
        current = self.head
        s = 'HEAD ==> '
        while(current is not None):
            s += current.data + ' ==> '
            current = current.next
        s += 'TAIL'
        return s


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
