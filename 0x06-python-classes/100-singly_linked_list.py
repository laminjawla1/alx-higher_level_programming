#!/usr/bin/python3
"""
Module representing a singly linked list
"""


class Node:
    """
    Node - The blueprint
    """

    def __init__(self, data, next_node=None):
        """
        __init__ - The initializer
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data - Gets data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data - Sets data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node - returns the next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node - Sets the next node in the list
        """
        # if not isinstance(value, Node) or value != None:
        # 	raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList - The Blueprint
    """

    def __init__(self):
        """
        __init__ The initializer
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        sorted_insert - Inserts nodes in a sorted order
        """
        tmp = self.__head
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif tmp.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """
        Printing the linked list elements
        """
        tmp = self.__head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next_node
        return ""
