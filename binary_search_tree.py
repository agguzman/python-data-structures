class Node(object):
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, item):
        def _insert(current, item):
            if item <= current.item:
                if current.left_child is None:
                    current.left_child = Node(item)
                else:
                    _insert(current.left_child, item)
            elif item > current.item:
                if current.right_child is None:
                    current.right_child = Node(item)
                else:
                    _insert(current.right_child, item)
        if self.root is None:
            self.root = Node(item)
        else:
            _insert(self.root, item)
    
    def remove(self, item):
        def _remove(current, item):
            if current is None:
                return False
            elif current.item == item:
                # TODO
                pass
            elif item < current.item:
                _remove(current.left_child, item)
            elif item > current.item:
                _remove(current.right_child, item)
        return _remove(self.root, item)

    def contains(self, item):
        def _contains(current, item):
            if current is None:
                return False
            elif current.item == item:
                return True
            elif item < current.item:
                _contains(current.left_child, item)
            elif item > current.item:
                _contains(current.right_child, item)
        return _contains(self.root, item)
    
    def preorder(self):
        def _preorder(current):
            if current is not None:
                print(current.item)
                _preorder(current.left_child)
                _preorder(current.right_child)
        _preorder(self.root)

    def postorder(self):
        def _postorder(current):
            if current is not None:
                _postorder(current.left_child)
                _postorder(current.right_child)
                print(current.item)
        _postorder(self.root)

    def inorder(self):
        def _inorder(current):
            if current is not None:
                _inorder(current.left_child)
                print(current.item)
                _inorder(current.right_child)
        _inorder(self.root)
