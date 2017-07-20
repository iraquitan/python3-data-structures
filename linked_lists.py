# -*- coding: utf-8 -*-
import sys
import cmd


class Node(object):
    __slots__ = ('data', 'next_')

    def __init__(self, data=None, next_=None):
        """"""
        self.data = data
        self.next_ = next_

    def __repr__(self):
        return repr((self.data, id(self.next_)))


class DNode(Node):
    def __init__(self, data=None, next_=None, previous_=None):
        """"""
        super(DNode, self).__init__(data, next_)
        self.previous_ = previous_

    def __repr__(self):
        return repr((id(self.previous_), self.data, id(self.next_)))


class SinglyLinkedList(object):
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
                # nodes.append(repr(current.data))
                nodes.append(repr(current))
                current = current.next_
        return '[{nodes}]'.format(nodes=', '.join(nodes))

    def print(self, p):
        """Print the Linked-List using recursion."""
        if p is None:
            print('', flush=True)
            return
        print(p.data, end=' ')
        self.print(p.next_)

    def reverse_print(self, p):
        """Print the Linked-List in reverse order using recursion."""
        if p is None:
            return
        self.reverse_print(p.next_)
        print(p.data, end=' ', flush=True)

    def rec_reverse(self, current):
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

    def prepend(self, data):
        """Special case of insert data with index equal to 0."""
        self.insert(data, 0)

    def append(self, data):
        """Special case of insert data with index equal to -1."""
        self.insert(data, -1)

    def insert(self, data, index=-1):
        """Insert data in index."""
        # If list is empty set head to new data node
        if self.head is None:
            self.head = Node(data)
            return
        if index == 0:
            self.head = Node(data, next_=self.head)
            return
        ix = 0
        current = self.head
        while current.next_:
            if ix == index - 1:
                break
            ix += 1
            current = current.next_
        if index != -1:
            raise IndexError(f'"index" {index} out of bounds')
        current.next_ = Node(data, current.next_)

    def delete(self, data):
        """Remove first match of data"""
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

    def find(self, data):
        """Find data"""
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next_

    def traverse(self):
        """Traverse Linked-List"""
        nodes = []
        count = 0
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next_
            count += 1
        print(f'traversed, found {count} items')

    def reverse(self):
        """Reverse the Linked-List"""
        current = self.head
        prev_ = None
        next_ = None
        while current:
            next_ = current.next_
            current.next_ = prev_
            prev_ = current
            current = next_
        self.head = prev_


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self, data=None):
        """"""
        super(DoublyLinkedList, self).__init__(data)
        if data is not None:
            self.head = DNode(data)
        else:
            self.head = None

    def insert(self, data, index=-1):
        if self.head is None:
            self.head = DNode(data)
            return
        if index == 0:
            next_ = self.head
            self.head = DNode(data, next_=self.head)
            next_.previous_ = self.head
            return
        ix = 0
        current = self.head
        while current.next_:
            if ix == index - 1:
                break
            ix += 1
            current = current.next_
        if index != -1:
            raise IndexError(f'"index" {index} out of bounds')
        next_ = current.next_
        current.next_ = DNode(data, next_=next_, previous_=current)
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
    prompt = '\n(linked-list)> '

    def __init__(self, ):
        """"""
        super(LinkedListCMD, self).__init__()
        self.list = None

    # The default() method is called when none of the other do_*() command
    # methods match.
    def default(self, arg):
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
            for a in parse(line):
                self.list.append(a)

    def do_prepend(self, line):
        """Prepend value(s) to Linked-List"""
        if self.list:
            for a in parse(line):
                self.list.prepend(a)

    def do_insert(self, line):
        """Insert value(s) to Linked-List"""
        if self.list:
            for a in parse(line):
                while True:
                    try:
                        i = int(input(f'Enter index to store data {a}: '))
                        self.list.insert(a, i)
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
            for a in parse(line):
                self.list.find(a)

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
            for a in parse(line):
                self.list.delete(a)

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
