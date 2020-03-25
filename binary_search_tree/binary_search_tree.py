import sys
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

        # if the value is less than the current node, go left
        if value < self.value:
            # check if we can go left
            if self.left is None:
                # there is no value to the left, so we insert the new value
                self.left = BinarySearchTree(value)
            else:
                # we continue down the tree
                self.left.insert(value)

        # if the value is greater than the current node or a duplicate, go right
        elif value >= self.value:
            # we check if we can go right
            if self.right is None:
                # if there is no value on the right we insert the new value
                self.right = BinarySearchTree(value)
            else:
                # we continue down the tree
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # if target is smaller than current node, go left
        if target < self.value:
            # if there is no left, the target DNE, return false
            if self.left is None:
                return False
            # Go left
            else:
                return self.left.contains(target)
        # if target is greater than current node, go right
        elif target > self.value:
            # if there is no right, the target DNE, return false
            if self.right is None:
                return False
            # Go right
            else:
                return self.right.contains(target)
        # else, the target is equal to the current node, return true
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        # we check if there is a bigger value
        if self.right is None:
            # if there is no bigger value, we return the current value
            return self.value
        else:
            # if there is a bigger value, we continue down the tree
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # we check if there is a way to go on both the left and right sides
        if self.left is not None:
            # if there is a branch to the left we call cb on it
            self.left.for_each(cb)
        if self.right is not None:
            # if there is a branch to the right we call cb on it
            self.right.for_each(cb)
        # we call cb on every leaf that isn't None
        cb(self.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
