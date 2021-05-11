'''
Module for Big Integer ADT.
'''

VARIANT = 77
# Михайлів Богдан Ігорович
#     [
#     '>=', DONE
#     '<' DONE
#     ]
#     [
#     '-',
#     '*'
#     ]
#     [
#     '>>', DONE
#     '<<' DONE
#     ]


class Node(object):
    '''
    Node for (one way) linked list.
    '''

    def __init__(self, data, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class TwoWayNode(Node):
    '''
    Node for (two way) linked list.
    '''

    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


class BigInteger:
    '''
    Represents Big Integer.
    '''

    def __init__(self, value='0'):
        self.value = value

        self.head = TwoWayNode(value[0])
        self.tail = self.head
        self.previous = self.head

        for char in value[1:]:
            node = TwoWayNode(char, self.previous)
            self.previous.next = node
            self.previous = self.previous.next

    def __str__(self):
        bigint_string = ''
        char = self.head

        while char is not None:
            bigint_string += char.data
            char = char.next

        return bigint_string

    def to_string(self):
        '''
        Converts linked list BigInteger into string view.
        '''
        bigint_string = ''
        char = self.head

        while char is not None:
            bigint_string += char.data
            char = char.next

        return bigint_string

    @property
    def length(self):
        length = 0

        position = self.head

        while position:
            length += 1
            position = position.next

        return length

    def insert_at_start(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def __lt__(self, other):
        '''
        <
        '''

        if self.head.data == '-' and other.head.data != '-':
            return True

        if self.head.data != '-' and other.head.data == '-':
            return False

        if self.length < other.length and self.head.data != '-' and other.head.data != '-':
            return True
        if self.length > other.length and self.head.data != '-' and other.head.data != '-':
            return False

        if self.length < other.length and self.head.data == '-' and other.head.data == '-':
            return False
        if self.length > other.length and self.head.data == '-' and other.head.data == '-':
            return True

        if self.head.data == '-' and other.head.data == '-':
            char1 = self.head
            char2 = other.head
            for _ in range(self.length):  # self.length == other.length
                if char1.data == char2.data:
                    pass
                if char1.data > char2.data:
                    return True
                char1 = char1.next
                char2 = char2.next

        if self.head.data != '-' and other.head.data != '-':
            char1 = self.head
            char2 = other.head
            for _ in range(self.length):  # self.length == other.length
                if char1.data == char2.data:
                    pass
                if char1.data < char2.data:
                    return True
                char1 = char1.next
                char2 = char2.next

        return False

    def __ge__(self, other):
        '''
        >=
        '''

        if self.head.data == '-' and other.head.data != '-':
            return False

        if self.head.data != '-' and other.head.data == '-':
            return True

        if self.length < other.length and self.head.data != '-' and other.head.data != '-':
            return False
        if self.length > other.length and self.head.data != '-' and other.head.data != '-':
            return True

        if self.length < other.length and self.head.data == '-' and other.head.data == '-':
            return True
        if self.length > other.length and self.head.data == '-' and other.head.data == '-':
            return False

        if self.head.data == '-' and other.head.data == '-':
            char1 = self.head
            char2 = other.head
            for _ in range(self.length):  # self.length == other.length
                if char1.data == char2.data:
                    pass
                if char1.data > char2.data:
                    return False
                char1 = char1.next
                char2 = char2.next

        if self.head.data != '-' and other.head.data != '-':
            char1 = self.head
            char2 = other.head
            for _ in range(self.length):  # self.length == other.length
                if char1.data == char2.data:
                    pass
                if char1.data < char2.data:
                    return False
                char1 = char1.next
                char2 = char2.next

        return True

    def __lshift__(self, other):
        '''
        '<<',
        '''
        self_string = self.to_string()
        other_string = other.to_string()

        bin_self = bin(int(self_string))[2:]
        shift = int(other_string)

        value = bin_self

        head = TwoWayNode(value[0])
        previous = head

        for char in value[1:]:
            node = TwoWayNode(char, previous)
            previous.next = node
            previous = previous.next

        for _ in range(shift):
            node = TwoWayNode('0', previous)
            previous.next = node
            previous = previous.next

        current = head
        res_str = ''
        while current:
            res_str += current.data
            current = current.next

        return BigInteger(res_str)

    def __rshift__(self, other):
        '''
        '>>',
        '''
        self_string = self.to_string()
        other_string = other.to_string()

        bin_self = bin(int(self_string))[2:]
        shift = int(other_string)

        value = bin_self

        head = TwoWayNode(value[0])
        previous = head

        for char in value[1:]:
            node = TwoWayNode(char, previous)
            previous.next = node
            previous = previous.next

        tail = None
        current = head
        while current:
            tail = current
            current = current.next

        for _ in range(shift):
            tail = tail.previous
            tail.next = None

        current = head
        res_str = ''
        while current:
            res_str += current.data
            current = current.next

        return BigInteger(res_str)

    def __add__(self, other):
        '''
        +
        '''

        return BigInteger(str((int(self.to_string()) + int(other.to_string()))))

        res = BigInteger()
        # if self.to_string()[0] == '-' and other.to_string()[0] == '-':
        #     remaider = 0
        #     integer = 0

        #     self_tail = self.tail
        #     other_tail = other.tail

        #     while self_tail or other_tail:
        #         integer = 0
        #         if self_tail is not None:
        #             integer += self_tail.data
        #             self_tail = self_tail.previous
        #         if other_tail is not None:
        #             integer += other_tail.data
        #             other_tail = other_tail.previous
        #         integer += remaider
        #         digit = digit % 10
        #         remainder = digit // 10
        #         res.insert_at_start(digit)

        #     if remainder != 0:
        #         res.insert_at_start(remainder)

        #     res.insert_at_start('-')

        # return res

    def __pow__(self, other):
        '''
        **
        '''

        return BigInteger(str((int(self.to_string()) ** int(other.to_string()))))
