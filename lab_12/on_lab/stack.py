class Node(object):
    '''
    Node for (one way) linked list.
    '''

    def __init__(self, data, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self._size = 0
        self._items = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        self._items = Node(item, None)
        self._size += 1

    def peek(self):
        return self._items.data

    def pop(self):
        pop_element = self._items.data
        self._items = self._items.next
        self._size -= 1

        return pop_element

    def clear(self):
        self._items = None
        self._size = 0
        


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(len(stack))
stack.clear()
print(len(stack))
