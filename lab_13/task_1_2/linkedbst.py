"""
File: linkedbst.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from math import log
import random
from copy import deepcopy
from time import time


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            symb = ""
            if node != None:
                symb += recurse(node.right, level + 1)
                symb += "| " * level
                symb += str(node.data) + "\n"
                symb += recurse(node.left, level + 1)
            return symb

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def lift_max_in_left_subtree_to_top(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            current_node = top.left
            while not current_node.right == None:
                parent = current_node
                current_node = current_node.right
            top.data = current_node.data
            if parent == top:
                top.left = current_node.left
            else:
                parent.right = current_node.left

        # Begin main part of the method
        if self.isEmpty():
            return None

        # Attempt to locate the node containing the item
        item_removed = None
        pre_root = BSTNode(None)
        pre_root.left = self._root
        parent = pre_root
        direction = 'L'
        current_node = self._root
        while not current_node == None:
            if current_node.data == item:
                item_removed = current_node.data
                break
            parent = current_node
            if current_node.data > item:
                direction = 'L'
                current_node = current_node.left
            else:
                direction = 'R'
                current_node = current_node.right

        # Return None if the item is absent
        if item_removed == None:
            return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not current_node.left == None \
                and not current_node.right == None:
            lift_max_in_left_subtree_to_top(current_node)
        else:

            # Case 2: The node has no left child
            if current_node.left == None:
                new_child = current_node.right

                # Case 3: The node has no right child
            else:
                new_child = current_node.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = new_child
            else:
                parent.right = new_child

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = pre_root.left
        return item_removed

    def replace(self, item, new_item):
        """
        If item is in self, replaces it with new_item and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                old_data = probe.data
                probe.data = new_item
                return old_data
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    @property
    def vertex_num(self):
        '''
        Return number of vertex in the tree.
        '''
        return len(self)

    def height(self):
        '''
        Return the height of tree
        :return: int
        '''

        def height1(node):
            '''
            Helper function
            :param top:
            :return:
            '''
            # Base case:
            if node is None:
                return -1

            return max(height1(node.left), height1(node.right)) + 1

        return height1(self._root)

    def is_balanced(self):
        '''
        Return True if tree is balanced
        :return:
        '''

        tree_height = self.height()
        return tree_height < 2*log(self.vertex_num+1, 2)-1

    def range_find(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        :param low:
        :param high:
        :return:
        '''

        all_value = list(self.inorder())
        low_high_range = []
        for value in all_value:
            if low <= value <= high:
                low_high_range.append(value)

        return low_high_range

    def rebalance(self):
        '''
        Rebalances the tree.
        :return:
        '''

        all_nodes = list(self.inorder())

        def create_node(nodes_lst):
            if len(nodes_lst) == 0:  # if list contains only last leaf
                return None
            mid = len(nodes_lst) // 2

            mid_value = nodes_lst[mid]
            left_part = nodes_lst[:mid]
            right_part = nodes_lst[mid+1:]

            return BSTNode(mid_value, create_node(left_part), create_node(right_part))
        self._root = create_node(all_nodes)

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        more_list = []
        for value in list(self.inorder()):
            if value > item:
                more_list.append(value)
        try:
            return sorted(more_list)[0]
        except IndexError:
            return None

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        less_list = []
        for value in list(self.inorder()):
            if value < item:
                less_list.append(value)
        try:
            return sorted(less_list)[-1]
        except IndexError:
            return None

    def find_height(self, root):
        '''
        Return height of the tree.
        '''
        # Base case:
        if root is None:
            return 0

        return max(self.find_height(root.left), self.find_height(root.right)) + 1

    def demo_bst(self, path):
        """
        Demonstration of efficiency binary search tree for the search tasks.
        :param path:
        :type path:
        :return:
        :rtype:
        """


print('File is reading')
with open('words.txt') as f:
    all_words = f.read().splitlines()

random_words = [random.choice(all_words) for _ in all_words][:10000]


print('Loading (1/5)')
# time into ordinary Python list

start_time = time()
# finding
for r_word in random_words:
    if r_word in all_words:
        word = r_word

ordinary_python_list_time = time() - start_time
print(ordinary_python_list_time)

print('Loading (2/5)')
# time into linked BST with alphabet order words
alphabet_order_tree = LinkedBST()
for word in all_words[:900]:
    alphabet_order_tree.add(word)

start_time = time()
# finding
for r_word in random_words:
    alphabet_order_tree.find(r_word)

alphabet_order_tree_time = time() - start_time
print(alphabet_order_tree_time)

print('Loading (3/5)')
# time into disbalanced linked BST with random order words
random_order_disbalanced_tree = LinkedBST()

for word in random.sample(all_words, len(all_words)):
    random_order_disbalanced_tree.add(word)

start_time = time()
# finding
for r_word in random_words:
    random_order_disbalanced_tree.find(r_word)

random_order_disbalanced_tree_time = time() - start_time
print(random_order_disbalanced_tree_time)

print('Loading (4/5)')
# time into balanced linked BST with random order words
random_order_balanced_tree = deepcopy(random_order_disbalanced_tree)
random_order_balanced_tree.rebalance()
start_time = time()
# finding
for r_word in random_words:
    random_order_balanced_tree.find(r_word)

random_order_balanced_tree_time = time() - start_time
print(random_order_balanced_tree_time)

print('Loading (5/5)')
print('Results below')

