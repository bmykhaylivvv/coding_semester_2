"""
Queue to stack converter.
"""

from copy import deepcopy
from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


# stack1 = ArrayStack() #peek, push, pop
# queue1 = ArrayQueue() #peek, add, pop


def queue_to_stack(queue: ArrayQueue):
    '''
    Convert stack to queue.
    '''
    queue_copy = deepcopy(queue)
    stack_reversed = ArrayStack()
    stack = ArrayStack()
    for _ in range(len(queue_copy)):
        value = queue_copy.pop()
        stack_reversed.push(value)

    for _ in range(len(stack_reversed)):
        value = stack_reversed.pop()
        stack.push(value)
    return stack
