#!/usr/bin/python3

""" Singly Linked List

This module contains classes for a singly linked list, including Node and
11;rgb:0000/0000/0000SinglyLinkedList.

"""


class Node:
    """Node class for a singly linked list

    This class represents a node in a singly linked list. It contains data
    and a reference to the next node in the list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node in the list.

    """

    def __init__(self, data, next_node=None):
        """Initialize a new node instance with data and an optional next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference to the next node in list.
                Default is None.

        Raises:
            TypeError: If data isn't an integer or next_node isn't Node object.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        elif next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get the reference to the next node in the list.

        Returns:
            Node: The reference to the next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node in the list.

        Args:
            value (Node): The new reference to the next node in the list.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class

    This class represents a singly linked list, which is a collection of nodes.

    Attributes:
        head (Node): The head node of the list.

    """

    def __init__(self):
        """Initialize an empty singly linked list with no head node."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node with data into the list in the correct sorted
        position (increasing order).

        Args:
            value (int): The data to be inserted into the list as a new Node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Represent the list as a string for printing.

        Returns:
            str: A string representation of the list, one node number per line.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")
