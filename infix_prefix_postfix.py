# -*- coding: utf-8 -*-
from queue import LifoQueue

import sys


OPERATORS = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             '**': lambda x, y: x ** y}


def evaluate_postfix(exp):
    stack = LifoQueue(len(exp))
    token = ''
    for char in exp + ' ':
        if char != ' ':
            token += char
        else:
            if token in OPERATORS.keys():
                var2 = float(stack.get())
                var1 = float(stack.get())
                res = OPERATORS[token](var1, var2)
                stack.put(res)
            else:
                stack.put(token)
            token = ''

    if stack.empty() or stack.qsize() > 1:
        raise ValueError('Invalid postfix expression')
    return stack.get()


def evaluate_prefix(exp):
    stack = LifoQueue(len(exp))
    token = ''
    for char in exp:
        if char != ' ':
            token += char
            continue
        else:
            if token in OPERATORS.keys():
                var2 = float(stack.get())
                var1 = float(stack.get())
                res = OPERATORS[char](var1, var2)
                stack.put(res)
            else:
                stack.put(token)
            token = ''
    if stack.empty() or stack.qsize() > 1:
        raise ValueError('Invalid postfix expression')
    return stack.get()


def main(argv):
    if argv is None:
        argv = sys.argv
    user_input = input('Enter expression: ')
    print(evaluate_postfix(user_input))

if __name__ == "__main__":
    main(sys.argv[1:])
