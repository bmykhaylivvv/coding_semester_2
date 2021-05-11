class Node(object):
    '''
    Node for (one way) linked list.
    '''

    def __init__(self, data, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

# front / rear

class Queue:
    def __init__(self):
        self._size = 0
        self._head = self._tail = None  

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0
    
    def add(self, item):
        new_node = Node(item, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise KeyError('Queue is empty')
        pop_element = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return pop_element

    def peek(self):
        if self.is_empty():
            raise KeyError('Queue is empty')
        peek_element = self._head.data

        return peek_element
        



queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.peek())
# print(len(queue))

queue.pop()
# print(len(queue))
print(queue.peek())
