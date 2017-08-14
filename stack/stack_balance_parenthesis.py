# -*- coding: utf-8 -*-
import sys
from queue import LifoQueue


def is_balanced(sentence_input):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = LifoQueue(len(sentence_input))
    for char in sentence_input:
        if char in pairs.values():  # Openings
            stack.put(char)
        if char in pairs.keys():  # Closings
            if stack.empty() or pairs.get(char) != stack.get():
                return False
    if stack.empty():
        return True
    else:
        return False


def main(argv):
    if argv is None:
        argv = sys.argv
    user_input = input('Enter sequence with (), [], {} to check: ')
    answer = is_balanced(user_input)
    if answer:
        print('Balanced')
    else:
        print('Not balanced.')

if __name__ == "__main__":
    main(sys.argv[1:])
