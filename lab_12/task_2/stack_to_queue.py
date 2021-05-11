"""
Stack to queue converter.
"""

from copy import deepcopy
from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


# stack1 = ArrayStack() #peek, push, pop
# queue1 = ArrayQueue() #peek, add, pop


def stack_to_queue(stack: ArrayStack):
    '''
    Convert stack to queue.
    '''
    stack_copy = deepcopy(stack)
    # stack_copy = [char for char in stack]
    queue = ArrayQueue()
    for _ in range(len(stack_copy)):
        value = stack_copy.pop()
        queue.add(value)

    return queue
