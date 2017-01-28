#! /usr/bin/env python3.4
# -*- coding: utf-8 -*-

""" A binary tree implementation to store data. I like splitting the BT data
structure into two classes: one for the nodes, and one for the actual BT.
"""

from typing import Union, Tuple

__all__ = ['BT', 'Node']


class Node:
    """ A node type for the BT """

    def __init__(self, value: Union[int, None], lvalue: Union[int, None] =None,
                 rvalue: Union[int, None] =None) -> None:
        self.value = value

        if lvalue:
            # lvalue != None
            self.lvalue = Node(lvalue)
        else:
            self.lvalue = None

        if rvalue:
            # rvalue != None
            self.rvalue = Node(rvalue)
        else:
            self.rvalue = None

    def get_value(self) -> Union[int, None]:
        return self.value

    def get_l(self) -> Union[None, 'Node']:
        """ Get the actual _object_ node """
        return self.lvalue

    def get_r(self) -> Union[None, 'Node']:
        """ Again, get the actual node """
        return self.rvalue

    def get_lvalue(self) -> Union[int, None]:
        """ Every node points to another node or None """
        if self.lvalue:
            return self.lvalue.get_value()
        else:
            return None

    def get_rvalue(self) -> Union[int, None]:
        """ Again, every node points to another node or None """
        if self.rvalue:
            return self.rvalue.get_value()
        else:
            return None

    def set_lvalue(self, val: Union[int, 'Node', None]) -> None:
        """ Set the left child of the current node to a value """
        if self.has_lvalue():
            # Update what it points to
            raise ValueError('** Cannot update at the node level if already set')
        else:
            self.lvalue = Node(val) if type(val) is int or type(val) is None \
                                    else val

    def set_rvalue(self, val: Union[int, 'Node', None]) -> None:
        """ Set the right child of the current node to a value """
        if self.has_rvalue():
            # Update it
            raise ValueError('** Cannot update at the node level if already set')
        else:
            self.rvalue = Node(val) if type(val) is int or type(val) is None \
                                    else val

    # If you'd like to check if it points to an actual node and not None:

    def has_lvalue(self) -> bool:
        if self.lvalue is not None:
            return True
        return False

    def has_rvalue(self) -> bool:
        if self.rvalue is not None:
            return True
        return False


class BT:
    """ A binary tree structure. """

    def __init__(self, root: int) -> None:
        self.root = Node(root)  # (association relationship)
        self._size = 1

    def get_root_value(self) -> int:
        return self.root.get_value()

    def get_size(self) -> int:
        return self._size

    def insert_iteratively(self, i: int) -> None:
        """ Creates a new node in the BT """
        current_node = self.root # != None

        while True:
            # This will terminate for any finite tree
            if i <= current_node.get_value():
                if current_node.has_lvalue():
                    current_node = current_node.get_l()
                else:
                    current_node.set_lvalue(i)
                    self._size += 1
                    break
            else:
                if current_node.has_rvalue():
                    current_node = current_node.get_r()
                else:
                    current_node.set_rvalue(i)
                    self._size += 1
                    break

    def insert_recursively(self, i: int, parent: Union[Node, None] =None) -> None:
        """ Insert a value in the BT recursively """
        if not parent:
            parent = self.root

        if i <= parent.get_value():
            if parent.has_lvalue():
                self.insert_recursively(i, parent.get_l())
            else:
                parent.set_lvalue(i)
                self._size += 1
        else:
            if parent.has_rvalue():
                self.insert_recursively(i, parent.get_r())
            else:
                parent.set_rvalue(i)
                self._size += 1

    def lookup_from_node(self, i: int, n: Node) \
            -> Union[Tuple[Node, None], Tuple[Node, Node], Tuple[None, Node]]:
        """ Make it easier to look up a value starting at some node """
        return self.lookup(i, n)

    def lookup(self, i: int, n: Union[Node, None] =None, parent: Union[Node, None] =None) \
            -> Union[Tuple[Node, None], Tuple[Node, Node], Tuple[None, Node]]:
        """ Return the instance of Node that contains a value """
        if n is None:
            n = self.root   # self.root cannot be None and has no parent
            parent = None

        nval = n.get_value()

        if i < nval:
            if n.has_lvalue():
                return self.lookup(i, n.get_l(), n)
            else:
                return None, parent
        elif i > nval:
            if n.has_rvalue():
                return self.lookup(i, n.get_r(), n)
            else:
                return None, parent
        else:
            return n, parent

    def __str__(self) -> None:
        """ Represent tree as a string """
        raise NotImplementedError