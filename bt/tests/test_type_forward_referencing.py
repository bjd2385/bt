#! /usr/bin/env python3.4
# -*- coding: utf-8 -8-

""" Test type forward referencing """

from typing import Union


class Node:
    def __init__(self, value: int, other: Union[int, None] =None) -> None:
        self.value = value
        self.l = Node(other) if type(other) is int else other

    def get_l(self) -> 'Node':
        return self.l


if __name__ == '__main__':
    X = Node(15, 16)
    print(X.get_l())

    N(5, 6)