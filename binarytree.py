
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        pass

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return True
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):

        print 'current: {}, data: {}'.format(current.data, data)

        if data < current.data:
            print 'data less than current'
            if current.left is not None:
                self._insert(current.left, data)
            else:
                current.left = Node(data)
                return True

        if current.data < data:
            print 'current less than data'
            if current.right is not None:
                self._insert(current.right, data)
            else:
                current.right = Node(data)
                return True

        else:
            return False

    def find(self, data):
        self._find(self.root, data)

    def _find(self, current, data):

        if current is None:
            return False
        elif current.data is data:
            return True
        elif data < current.data:
            self._find(current.left, data)
        elif current.data < data:
            self._find(current.right, data)

    # def printer(self):
    #     if self.root is None:
    #         return
    #     else:
    #         print self.root.data
    #         self._printer(self.root.data)
    #
    # def _printer(self, current):
    #     print '===> ' + str(current)
    #     if current.left is not None:
    #         print 'going left'
    #         print current.left.data
    #         self._printer(current.left.left)
    #
    #     if current.right is not None:
    #         print 'going right'
    #         print current.right.data
    #         self._printer(current.right.right)

def main():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(4)
    bt.insert(3)
    bt.insert(2)
    bt.insert(6)
    bt.insert(7)

main()
