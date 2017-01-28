#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" A bunch of tests for the BT class """

import unittest
from bt.bt import BT, Node
from random import choice

MAX = 30
values = list(range(1, MAX+1))


class TestBT(unittest.TestCase):
    """ Test methods of the BT """
    def test_tree_creation(self) -> None:
        _tree = BT(choice(values))
        self.assertIn(_tree.get_root_value(), values)
        self.assertEqual(_tree.get_size(), 1)

    def test_insertions(self) -> None:
        _tree = BT(choice(values))
        _tree.insert_iteratively(choice(values))
        self.assertEqual(_tree.get_size(), 2)
        _tree.insert_recursively(choice(values))
        self.assertEqual(_tree.get_size(), 3)

    def test_value_lookup(self) -> None:
        base = choice(values)
        _tree = BT(base)
        for val in values:
            if val != base:
                _tree.insert_iteratively(val)

        for val in values:
            assert(type(_tree.lookup(val)[0]) is Node), '{} not in tree'.format(val)


if __name__ == '__main__':
    unittest.main()