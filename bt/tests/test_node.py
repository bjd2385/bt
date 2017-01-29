#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" A bunch of tests for the Node class """

import unittest
from random import choice

from bt.bt import Node

MAX = 10

# Create some values to choose from throughout the course of these tests
values = list(range(1, MAX+1))


class TestNode(unittest.TestCase):
    """ Test the bt.Node class """

    def test_node_creation(self) -> None:
        node = Node(choice(values))
        self.assertIsNotNone(node.get_value())

        # Trivial base case
        node = Node(None)
        self.assertIsNone(node.get_value())
        self.assertFalse(node.has_rvalue())
        self.assertFalse(node.has_lvalue())
        self.assertIsNone(node.get_l())
        self.assertIsNone(node.get_r())

        # Test both
        node = Node(*(choice(values) for _ in range(3)))
        self.assertTrue(node.has_lvalue())
        self.assertTrue(node.has_rvalue())

        # Test left
        node = Node(value=choice(values), lvalue=choice(values))
        self.assertTrue(node.has_lvalue())
        self.assertFalse(node.has_rvalue())
        self.assertIsNone(node.get_r())
        self.assertIsNotNone(node.get_l())

        # Test right
        node = Node(value=choice(values), rvalue=choice(values))
        self.assertTrue(node.has_rvalue())
        self.assertFalse(node.has_lvalue())
        self.assertIsNone(node.get_l())
        self.assertIsNotNone(node.get_r())

    # Possibly test Node setters, but it's currently immutable if they're already
    # set, which probably isn't the best idea

    def test_node_conditionals(self) -> None:
        node = Node(*(choice(values) for _ in range(3)))

        # Test left
        self.assertTrue(node.has_lvalue())
        self.assertTrue(node.has_rvalue())
        del node

        # Test left & right
        node = Node(value=choice(values))
        self.assertFalse(node.has_lvalue())
        self.assertFalse(node.has_rvalue())


if __name__ == '__main__':
    unittest.main()