class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, item):
        """
        Insert a new item into the list.
        :param item: Item to insert
        :return: 
        """
        # Create a new node
        node = Node(item)
        # Modify nodes pointer to the previous Node in the list
        node.next = self.head
        # Modify the lists pointer to the new node
        self.head = node
        
    def remove(self, item):
        """
        Remove the item from the list.
        :param item: Item to remove
        :return: <bool> True if item removed, else False
        """
        current = self.head
        previous = None
        while current is not None:
            if current.item == item:
                if previous is None:
                    self.head = current.next
                    return True
                else:
                    previous.next = current.next
                    return True
            else:
                previous = current
                current = current.next
        return False

    def contains(self, item):
        """
        Checks to determine is list contains item.
        :param item: Item to search
        :return: <bool> True if list contains item, else False
        """
        current = self.head
        while current is not None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False

    def __repr__(self):
        current = self.head
        s = ''
        while current is not None:
            s += str(current.item) + ', '
            current = current.next
        if s[-2:] == ', ':
            s = s[0:-2]
        return s
