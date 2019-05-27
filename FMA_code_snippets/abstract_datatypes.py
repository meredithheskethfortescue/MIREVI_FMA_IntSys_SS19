#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Demonstrate several abstract data types
@author: Raphael Stascheit at MIREVI
"""

import traceback


def demonstrate_stack_as_object():
    class Stack:
        def __init__(self):
            self.items = []

        def __repr__(self):
            # this is advanced code and only syntactic sugar - simply don't mind it... ;)
            # override objects representation with the stack content
            # this way the items can be accessed directly instead of calling stack.items
            return repr(self.items)

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
            return self.items[len(self.items) - 1]

        def size(self):
            return len(self.items)

    # create stack object
    stack = Stack()

    # add some values
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # pop last element from stack
    last_element = stack.pop()
    print("popped element is", last_element)

    # show its content
    print(stack)


def demonstrate_stack_as_list():
    """Abstract data type: Stack --> Python list"""
    stack = [0, 1, 2, 3]

    # pop last element from stack
    last_element = stack.pop()
    print("popped element is", last_element)

    # pushing is called append in python lists
    stack.append(4)
    stack += [5]  # adding is short hand for appending in python lists (Attention: This is NOT true for numpy arrays!)

    # show its content
    print("stack contains", stack)


def demonstrate_set():
    """Abstract data type: Set --> Python dictionary"""
    set = {'setosa': 2.5,
           'virginica': 1.2,
           'versicolor': 3.1}

    # add a new entry to the dictionary
    set['new entry'] = 0.5

    try:
        # A set is an unsorted data type. Thus you can't get an entry in it by an index.
        print("set[0] is", set[0])  # this will fail

    except:
        # print the error message
        traceback.print_exc()

        # instead get entry by it's key
        print("set['new entry'] is", set['new entry'])


def demonstrate_tree():
    """Abstract data type: Tree
    The shown tree is of the following shape:
            0
          /   \
        1       2
       / \     / \
      3   4   5   6
     /
    7
    """

    class Node(object):
        def __init__(self, value):
            self.left = None
            self.right = None
            self.data = value

        def __repr__(self):
            # this is advanced code and only syntactic sugar - simply don't mind it... ;)
            return repr(self.data)

        def plot(self):
            """Build string representation of the tree by recursion"""
            string = ''
            string += str(self.data)

            if self.left is not None and self.right is not None:
                string += '[' + self.left.plot() + self.right.plot() + ']'

            elif self.left is not None:
                string += '[' + self.left.plot() + ']'

            elif self.right is not None:
                string += '[' + self.right.plot() + ']'

            return string

    # fill the tree
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)

    print(root.plot())


def demonstrate_heap():
    # todo: heap not yet implemented
    import heapq

    heap = [0, 1, 2, 3]
    heapq.heapify(heap)


if __name__ == '__main__':
    demonstrate_stack_as_list()
    # demonstrate_stack_as_object()
    demonstrate_set()
    demonstrate_tree()
