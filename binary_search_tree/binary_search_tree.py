import sys
import io
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        if self.right:
            return self.right.get_max()
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left and self.right:
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.left:
            self.left.for_each(cb)
        elif self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left and self.right:
            return self.left.in_order_print(self.left), print(self.value), self.right.in_order_print(self.right)
        elif self.left:
            return self.left.in_order_print(self.left), print(self.value)
        elif self.right:
            return print(self.value), self.right.in_order_print(self.right)
        else:
            print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        nodes = [node]
        for tree_node in nodes:
            print(tree_node.value)
            if tree_node.left:
                nodes += [tree_node.left]
            if tree_node.right:
                nodes += [tree_node.right]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        nodes = [node]
        skipped_nodes = []
        for tree_node in nodes:
            print(tree_node.value)
            if tree_node.left and tree_node.right:
                nodes += [tree_node.left]
                skipped_nodes += [tree_node.right]
            elif tree_node.left:
                nodes += [tree_node.left]
            elif tree_node.right:
                nodes += [tree_node.right]
            else:
                if len(skipped_nodes) > 0:
                    nodes += [skipped_nodes.pop()]

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

testing = BinarySearchTree(1)
testing.insert(8)
testing.insert(5)
testing.insert(7)
testing.insert(6)
testing.insert(3)
testing.insert(4)
testing.insert(2)

testing.dft_print(testing)
