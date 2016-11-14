
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.parent = None
        pass

    def insert(self, data):
        if self.parent is None:
            self.parent = Node(data)
        else:
            self._insert(data, self.parent)

    def _insert(self, data, current):
        if current.left is not None and data < current:
            self._insert(data, current.left)
        elif current.right is  not None and data > current:
            self._insert(data, current.right)
        else:
            print 'done'

    def printer(self):
        current = self.parent
        while current is not None:
            print current.data
            current = current.left

def main():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(4)
    bt.printer()

main()
