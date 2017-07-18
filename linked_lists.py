# -*- coding: utf-8 -*-
import sys


class Node(object):
    __slots__ = ('data', 'next_')

    def __init__(self, data=None, next_=None):
        """"""
        self.data = data
        self.next_ = next_

    def __repr__(self):
        return repr(self.data)


class LinkedList(object):
    def __init__(self, data=None):
        """"""
        if data is not None:
            self.head = Node(data)
        else:
            self.head = None

    def __repr__(self):
        nodes = []
        if self.head is not None:
            current = self.head
            while current:
                nodes.append(repr(current.data))
                current = current.next_
        return '[{nodes}]'.format(nodes=', '.join(nodes))

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        self.head = Node(data, next_=self.head)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next_:
            current = current.next_
        current.next_ = Node(data)

    def insert(self, data, index=-1):
        if index == -1:
            self.append(data)
        elif index == 0:
            self.prepend(data)
        else:
            ix = 0
            current = self.head
            while current.next_:
                if ix == index - 1:
                    current.next_ = Node(data, current.next_)
                    return
                ix += 1
                current = current.next_
            raise IndexError(f'"index" {index} out of bounds')

    def delete(self, data):
        current = self.head
        prev_ = None
        while current and current.data != data:
            prev_ = current
            current = current.next_
        if prev_ is None:
            self.head = current.next_
        elif current:
            prev_.next_ = current.next_
            current.next_ = None
        return

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next_

    def traverse(self):
        nodes = []
        count = 0
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next_
            count += 1
        print(f'traversed, found {count} items')

    def reverse(self):
        current = self.head
        prev_ = None
        next_ = None
        while current:
            next_ = current.next_
            current.next_ = prev_
            prev_ = current
            current = next_
        self.head = prev_


def main(argv=None):
    if argv is None:
        argv = sys.argv
    lst = LinkedList()
    while True:
        try:
            n = int(input('How many elements in the list? '))
            break
        except ValueError:
            print('Number of elements to insert must be an integer.')
            continue
    for i in range(n):
        while True:
            try:
                data = int(input('Enter data to store in the list: '))
                break
            except ValueError:
                print('Data to insert must be an integer.')
                continue
        lst.prepend(data)
        print(f'List -> {lst}')

if __name__ == "__main__":
    main()
