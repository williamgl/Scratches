# Author: Gan Li
# Date: 10/28/21 9:46 下午
# Description: My project work regarding linked list.
class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        """method to get _data"""
        return self._data

    def set_data(self, new_data):
        """method to set _data"""
        self._data = new_data

    def get_next(self):
        """method to get the value of _next"""
        return self._next

    def set_next(self, new_next):
        """method to set the new value to _next"""
        self._next = new_next


class LinkedList:
    """
    Represents a linked list implementation of the list abstract data type
    """
    def __init__(self):
        self._head = None

    def get_head(self):
        """method to get _head"""
        return self._head

    def set_head(self, new_head):
        """method to set the new value to _head"""
        self._head = new_head

    def add(self, val):
        """
        Here is the example using while loop
        to add a node containing val to the linked list
        # if the list is empty
        if self._head is None:
            self._head = Node(val)
        # if the list is not empty
        else:
            # set current to the next node
            current = self._head
            # find the last node
            while current.next is not None:
                current = current.next
            # the .next of the last node is None
            # set it to the new linked list element
            current.next = Node(val)
        """
        if self.get_head() is None:
            self.set_head(Node(val))
        else:
            self.rec_add(val, self.get_head())

    def rec_add(self, val, node=None):
        """recursive add method"""
        if node is None:
            return
        elif node.get_next() is None:
            node.set_next(Node(val))
        else:
            self.rec_add(val, node.get_next())

    def remove(self, val):
        """
        Removes the node containing from the linked list
        """
        if self.get_head() is None:
            return
        elif self.get_head().get_data() == val:
            self.set_head(self.get_head().get_next())
        else:
            self.rec_remove(val, self.get_head())

    def rec_remove(self, val, node=None):
        """recursive remove method"""
        if node is None:
            return
        elif node.get_next().get_data() == val:
            node.set_next(node.get_next().get_next())
        else:
            self.rec_remove(val, node.get_next())

    def contains(self, key):
        """
        returns True if the list contains a Node with the value key
        otherwise returns False
        :param key: the target value
        :return: True or False
        """
        if self.get_head() is None:
            return False
        else:
            return self.rec_contains(key, self.get_head())

    def rec_contains(self, key, node):
        """recursively check if the node's value equals to key"""
        if node.get_data() == key:
            return True
        # if we reach the end of the list
        elif node.get_next() is None:
            return False
        else:
            return self.rec_contains(key, node.get_next())

    def length(self):
        """method to get the length of the linked list"""
        if self.get_head() is None:
            return 0
        else:
            return self.rec_length(self.get_head())

    def rec_length(self, node):
        """recursively count each node with a data"""
        if node is None:
            return 0
        else:
            return self.rec_length(node.get_next()) + 1

    def insert(self, val, pos):
        """inserts a node containing val into the linked list at position pos"""
        # if the position pos is larger than the length of the linked list:
        if pos > self.length():
            print('This cannot be done.')
            print('Please change the position to a valid number within the length of the linked list.')
            return
        # if the list is empty
        if self.get_head() is None:
            self.add(val)
            return
        # if position pos is 0, we inset this value to _head's node:
        elif pos == 0:
            temp = self.get_head()
            self.set_head(Node(val))
            self.get_head().set_next(temp)
        else:
            self.rec_insert(val, pos, self.get_head())

    def rec_insert(self, val, pos, node):
        """
        recursively check if this node is the target position
        if so, set current node's value to val
        and move current code and following nodes to the next position
        """
        if pos == 1:
            temp = node.get_next()
            node.set_next(Node(val))
            node.get_next().set_next(temp)
        else:
            self.rec_insert(val, pos - 1, node.get_next())

    def previous(self, node):
        """find the previous node"""
        if self.get_head() is None:
            return None
        else:
            return self.rec_previous(node, self.get_head())

    def rec_previous(self, target, node):
        """recursively check whether this note is the previous node of the target"""
        if node.get_next() is None:
            return None
        elif node.get_next() == target:
            return node
        else:
            self.rec_previous(target, node.get_next())

    def get_last(self):
        """get the last element"""
        if self.get_head() is None:
            return None
        return self.rec_get_last(self.get_head())

    def rec_get_last(self, node):
        """check if this node is the last element"""
        if node.get_next() is None:
            return node
        else:
            return self.rec_get_last(node.get_next())

    def reverse(self):
        """method to reverse the linked list"""
        if self.get_head() is None:
            return None
        elif self.get_head().get_next() is None:
            return
        else:
            previous = None
            current = self.get_head()
            node = current.get_next()
            current.set_next(previous)
            previous = current
            current = node
            self.set_head(self.rec_reverse(previous, current))

    def rec_reverse(self, previous, current):
        """recursively reverse the current node position"""
        if current is None:
            return previous
        else:
            following = current.get_next()
            current.set_next(previous)
            previous = current
            current = following
            return self.rec_reverse(previous, current)

    def display(self):
        """recursive display helper method"""
        if self.get_head() is None:
            return
        self.rec_display(self.get_head())
        print()

    def rec_display(self, node):
        """recursive display method"""
        if node is None:
            return
        print(node.get_data(), end=" ")
        self.rec_display(node.get_next())

    def to_plain_list(self):
        """return the linked list as a normal Python list"""
        result = []
        if self.get_head() is None:
            return []
        else:
            return self.rec_to_plain_list(result, self.get_head())

    def rec_to_plain_list(self, result, node):
        """recursively add the data to the list"""
        result.append(node.get_data())
        # if we reach the end of the list
        if node.get_next() is None:
            return result
        else:
            return self.rec_to_plain_list(result, node.get_next())
