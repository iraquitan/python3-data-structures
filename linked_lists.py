# -*- coding: utf-8 -*-
import sys


class Node(object):
    def __init__(self, value, next_=None):
        """"""
        self.value = value
        self.next_ = next_

    def __repr__(self):
        return repr(self.value)


class LinkedList(object):
    def __init__(self, value=None):
        """"""
        if value is not None:
            self.head = Node(value)
        else:
            self.head = value

    def __repr__(self):
        nodes = []
        if self.head is not None:
            current = self.head
            while current.next_:
                nodes.append(repr(current.value))
                current = current.next_
        return '[' + ','.join(nodes) + ']'

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        self.head = Node(value, next_=self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next_:
            current = current.next_
        current.next_ = Node(value)

    # def insert(self, value, index):
    #     current = self.head
    #     while current.next_:
    #         if
    #         current = current.next_
    #     current.next_ = Node(value)

    def traverse(self):
        nodes = []
        current = self.head
        while current.next_:
            nodes.append(current.value)
            current = current.next_
        print(nodes)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    ll = LinkedList(0)
    ll.append(10)
    ll.append(13)
    ll.prepend(16)
    # ll.traverse()
    ll

if __name__ == "__main__":
    main()
