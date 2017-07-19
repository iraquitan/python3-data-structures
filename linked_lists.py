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
            del current
            # current.next_ = None
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


def create_list():
    return LinkedList()


def get_list_size():
    while True:
        try:
            n = int(input('How many elements in the list? '))
            return n
        except ValueError:
            print('Number of elements to insert must be an integer.')
            continue


def append_data(lst):
    while True:
        try:
            data = int(input('Enter data to store in the list: '))
            break
        except ValueError:
            print('Data to insert must be an integer.')
            continue
    lst.append(data)


def prepend_data(lst):
    while True:
        try:
            data = int(input('Enter data to store in the list: '))
            break
        except ValueError:
            print('Data to insert must be an integer.')
            continue
    lst.prepend(data)


def insert_data(lst):
    while True:
        try:
            data = int(input('Enter data to store in the list: '))
            index = int(input('Enter index to store data: '))
            lst.insert(data, index)
            break
        except ValueError:
            print("Could not convert data to an integer.")
            continue
        except IndexError:
            print("Index out of bounds in the list.")
            continue


def delete_data(lst):
    while True:
        try:
            data = int(input('Enter data to delete in the list: '))
            break
        except ValueError:
            print('Data to insert must be an integer.')
            continue
    lst.delete(data)


def find_data(lst):
    while True:
        try:
            data = int(input('Enter data to find in the list: '))
            break
        except ValueError:
            print('Data to insert must be an integer.')
            continue
    return lst.find(data)


def options():
    while True:
        try:
            opt = int(input("1: Create Linked-List\n2: Exit\n"))
            if opt == 1:
                return create_list()
                break
            elif opt == 2:
                sys.exit()
        except ValueError:
            continue


def list_options(lst):
    while True:
        try:
            opt = int(input("1: Append\n2: Prepend\n3: Insert\n4: Find\n"
                            "5: Delete\n6: Exit\n"))
            if opt == 1:
                append_data(lst)
                print(f'List -> {lst}')
                break
            elif opt == 2:
                prepend_data(lst)
                print(f'List -> {lst}')
                break
            elif opt == 3:
                insert_data(lst)
                print(f'List -> {lst}')
                break
            elif opt == 4:
                data_node = find_data(lst)
                if data_node:
                    print(f'{data_node} found!')
                else:
                    print('not found!')
                break
            elif opt == 5:
                delete_data(lst)
                print(f'List -> {lst}')
                break
            elif opt == 6:
                sys.exit()
        except ValueError:
            continue


def main(argv=None):
    while True:
        if argv is None:
            argv = sys.argv
        lst = options()
        while lst:
            list_options(lst)
        # n = get_list_size()
        # for i in range(n):
        #     prepend_data(lst)
        #     print(f'List -> {lst}')

if __name__ == "__main__":
    main()
