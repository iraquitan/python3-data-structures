# -*- coding: utf-8 -*-
import sys
from queue import LifoQueue


def main(argv):
    if argv is None:
        argv = sys.argv
    user_input = input('Enter name to reverse: ')

    stack = LifoQueue(len(user_input))

    for char in user_input:
        stack.put(char)

    rev_stack = []
    while not stack.empty():
        rev_stack.append(stack.get())

    print('\nReversed: {}'.format(''.join(rev_stack)))

if __name__ == "__main__":
    main(sys.argv[1:])
