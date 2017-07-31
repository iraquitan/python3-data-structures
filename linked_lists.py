# -*- coding: utf-8 -*-
"""
Script to demonstrate Python implementation of Linked-Lists.
"""
import cmd
import sys
from abc import ABCMeta, abstractmethod
from enum import Enum


class Node(object):
    """Singly linked-list node."""
    __slots__ = ('data', 'next_')

    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_

    def __repr__(self):
        return repr((self.data, id(self.next_)))


class DoublyNode(Node):
    """Doubly linked-list node."""
    def __init__(self, data=None, next_=None, previous_=None):
        """"""
        super(DoublyNode, self).__init__(data, next_)
        self.previous_ = previous_

    def __repr__(self):
        return repr((id(self.previous_), self.data, id(self.next_)))


class NodeType(Enum):
    """Node type enumeration class."""
    SINGLY = 1
    DOUBLY = 2


class BaseLinkedList(metaclass=ABCMeta):
    """Abstract class defining a base linked-list."""
    type_ = 0

    def __init__(self, data=None):
        """"""
        if data is not None:
            self.head = self.new_node(data=data)
        else:
            self.head = None

    def __repr__(self):
        nodes = []
        if self.head is not None:
            current = self.head
            while current:
                # nodes.append(repr(current.data))
                nodes.append(repr(current))
                current = current.next_
        return '[{nodes}]'.format(nodes=', '.join(nodes))

    def new_node(self, data):
        """Return a new node depending of list node type."""
        if self.type_ == NodeType.SINGLY:
            return Node(data=data, next_=None)
        elif self.type_ == NodeType.DOUBLY:
            return DoublyNode(data=data, next_=None, previous_=None)

    def append(self, data):
        """Insert data at tail of linked-list. This operation takes O(n) time
        to run, as we only have the pointer to the head of the list, we must
        traverse the entire list to insert in the last index.
        """
        self.insert(data, -1)

    def prepend(self, data):
        """Insert data at head of linked-list. This operation takes O(1) time
        to run, as we don't need to shift all the elements to the right as in
        an array, we just need to add a node before head and update head.
        """
        self.insert(data, 0)

    @abstractmethod
    def insert(self, data, index):
        """Insert data at index of linked-list. This operation takes O(n) time
        to run, as we must traverse to the index.
        """
        return

    @abstractmethod
    def delete(self, data):
        """Remove first occurrence of data in linked-list. This operation
        takes O(n) time to run, as we must traverse until we find a match to
        remove.
        """
        return

    @abstractmethod
    def reverse(self):
        """Reverse the linked-list in-place. This operation takes O(n) time to
        run, as we must traverse all the elements to change their links.
        """
        return

    def find(self, data):
        """Find data in the linked-list. This operation takes O(n) time to
        run, as we must traverse until we find a match.
        """
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next_

    def traverse(self):
        """Traverse the linked-list."""
        nodes = []
        count = 0
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next_
            count += 1
        print(f'traversed, found {count} items')


class SinglyLinkedList(BaseLinkedList):
    """Class defining a singly linked-list."""
    type_ = NodeType.SINGLY

    def print(self, node):
        """Print the linked-list using recursion."""
        if node is None:
            print('', flush=True)
            return
        print(node.data, end=' ')
        self.print(node.next_)

    def reverse_print(self, node):
        """Print the linked-list in reverse order using recursion."""
        if node is None:
            return
        self.reverse_print(node.next_)
        print(node.data, end=' ', flush=True)

    def rec_reverse(self, current):
        """Reverse linked-list using recursion."""
        if current.next_ is None:
            self.head = current
            return
        self.rec_reverse(current.next_)
        # next_ = current.next_
        # next_.next_ = current
        # current.next_ = None
        current.next_.next_ = current
        current.next_ = None
        del current

    def insert(self, data, index=-1):
        # If list is empty set head to new data node
        if self.head is None:
            self.head = self.new_node(data)
            return
        if index == 0:
            new_node = self.new_node(data)
            new_node.next_ = self.head
            self.head = new_node
            return
        idx = 0
        current = self.head
        while current.next_:
            if idx == index - 1:
                break
            idx += 1
            current = current.next_
        if index != -1 and current.next_ is None:
            raise IndexError(f'"index" {index} out of bounds')
        new_node = self.new_node(data)
        new_node.next_ = current.next_
        current.next_ = new_node

    def delete(self, data):
        current = self.head
        prev_ = None
        while current and current.data != data:
            prev_ = current
            current = current.next_
        if prev_ is None and current is not None:
            self.head = current.next_
        elif current:
            prev_.next_ = current.next_
            del current
        return

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


class DoublyLinkedList(BaseLinkedList):
    """Class defining a doubly linked-list."""
    type_ = NodeType.DOUBLY

    def insert(self, data, index=-1):
        if self.head is None:
            self.head = self.new_node(data)
            return
        if index == 0:
            new_node = self.new_node(data)
            new_node.next_ = self.head
            self.head.previous_ = new_node
            self.head = new_node
            return
        idx = 0
        current = self.head
        while current.next_:
            if idx == index - 1:
                break
            idx += 1
            current = current.next_
        if index != -1 and current.next_ is None:
            raise IndexError(f'"index" {index} out of bounds')
        next_ = current.next_
        new_node = self.new_node(data)
        new_node.next_ = next_
        new_node.previous_ = current
        current.next_ = new_node
        if next_:
            next_.previous_ = current.next_

    def delete(self, data):
        current = self.head
        prev_ = None
        while current and current.data != data:
            prev_ = current
            current = current.next_
        if prev_ is None and current is not None:
            self.head = current.next_
            if self.head:
                self.head.previous_ = None
        elif current:
            next_ = current.next_
            prev_.next_ = next_
            if next_:
                next_.previous_ = prev_
            del current
        return

    def reverse(self):
        current = self.head
        prev_ = None
        while current:
            next_ = current.next_
            prev_ = current
            current.next_, current.previous_ = current.previous_, current.next_
            current = next_
        self.head = prev_


class LinkedListCMD(cmd.Cmd):
    """Command line interface for using linked-lists."""
    prompt = '\n(linked-list)> '

    def __init__(self, ):
        """"""
        super(LinkedListCMD, self).__init__()
        self.list = None

    # The default() method is called when none of the other do_*() command
    # methods match.
    def default(self, line):
        self.stdout.write('I do not understand that command. '
                          'Type "help" for a list of commands.')

    def emptyline(self):
        pass

    def do_create_list(self, line):
        """Creates a Linked-List"""
        opt = None
        while True and opt not in (1, 2):
            try:
                opt = int(input("[1] Singly or [2] Doubly Linked-List? "))
            except ValueError:
                continue
        if opt == 1:
            self.list = SinglyLinkedList()
        else:
            self.list = DoublyLinkedList()

    def do_delete_list(self, line):
        """Deletes the current Linked-List"""
        self.list = None

    def do_view_list(self, line):
        """View the current Linked-List if it exists"""
        if self.list:
            print(f'List -> {self.list}')
        else:
            print('No Linked-List created. Use "create_list" to create '
                  'one.')

    def do_append(self, line):
        """Append value(s) to Linked-List"""
        if self.list:
            for data in parse(line):
                self.list.append(data)

    def do_prepend(self, line):
        """Prepend value(s) to Linked-List"""
        if self.list:
            for data in parse(line):
                self.list.prepend(data)

    def do_insert(self, line):
        """Insert value(s) to Linked-List"""
        if self.list:
            for data in parse(line):
                while True:
                    try:
                        i = int(input(f'Enter index to store data {data}: '))
                        self.list.insert(data, i)
                        break
                    except ValueError:
                        print("Could not convert data to an integer.")
                        continue
                    except IndexError:
                        print("Index out of bounds in the list.")
                        continue

    def do_find(self, line):
        """Find value(s) in Linked-List"""
        if self.list:
            for data in parse(line):
                if self.list.find(data):
                    print(f"Found {data}.")
                else:
                    print(f"Not found.")

    def do_reverse(self, line):
        """Reverse the current Linked-List"""
        if self.list:
            self.list.reverse()

    def do_traverse(self, line):
        """Traverse the current Linked-List"""
        if self.list:
            self.list.traverse()

    def do_remove(self, line):
        """Remove value(s) from Linked-List"""
        if self.list:
            for data in parse(line):
                self.list.delete(data)

    def postcmd(self, stop, line):
        command, _, _ = self.parseline(line)
        if command in ('append', 'prepend', 'insert', 'remove', 'find',
                       'create_list', 'reverse'):
            self.do_view_list(line)
        return stop

    def do_quit(self, line):
        """Quit the program."""
        return True  # this exits the Cmd application loop

    def do_EOF(self, line):
        return True


def parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    return tuple(map(int, arg.split()))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) > 1:
        LinkedListCMD().onecmd(' '.join(sys.argv[1:]))
        print(' '.join(sys.argv[1:]))
    else:
        LinkedListCMD().cmdloop('Linked List Command Demo!\n'
                                '=========================\n\n'
                                '(Type "help" for commands.)')

if __name__ == "__main__":
    main()
