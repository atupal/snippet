#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import re

meta_char = ['*', '?', '+', '|', '(', ')']

class State(object):

    class _dict(dict):
        def __missing__(self, key):
            self[key] = []
            return self[key]

    def __init__(self):
        self.state_sets = _dict()
        self.dangling = []

    def add_edge(self, char, state):
        self.state_sets[char].append(state)


class NFA(object):

    def __init__(self, state=None, tail=None):
        self.head = state
        self.tail = []
        if tail:
            self.tail = tail

    def concat(self, b_nfa):
        for state in self.tail:
            for char in state.dangling:
                state.add_edge(char, b_nfa.head)
            state.dangling = []


def infix2postfix(source):
    ret = [source[0]]
    for i in source[1:]:
        if i not in meta_char:
            ret.append('.')
        ret.append(i)

    higher_order_ops = {
            '?': ['?', '+', '*'],
            '+': ['?', '+', '*'],
            '*': ['?', '+', '*'],
            '.': ['?', '+', '*', '.'],
            '|': ['?', '+', '*', '.', '|'],
            }

    output = []
    ops = []

    for c in ret:
        if c not in meta_char:
            output.append(c)
        elif c == '(':
            pass
        elif c == ')':
            pass
        else:
            while ops and ops[-1] in higher_order_ops[c]:
                output.append(ops.pop())
            ops.append(c)

def compile(postfix_source):

    stack = []
    ops = []
    pos = 0
    while 1:
        char = source[pos]
        if   char == '?':
            state = State()
            e = stack.pop()
            state.add_edge('epsilon', e.head)
            state.dangling = ['epsilon']
            nfa = NFA(state)
            nfa.tail = [state] + e.tail
            stack.push(nfa)
        elif char == '*':
            e = stack.pop()
            state = State()
            state.add_edge('epsilon', e.head)
            state.dangling = ['epsilon']
            nfa = NFA(state)
            e.concat(nfa)
            nfa.dangling = [state]
            stack.push(nfa)
        elif char == '+':
            e = stack.pop()
            state = State()
            state.add_edge('epsilon', e.head)
            state.dangling = ['epsilon']
            nfa = NFA(state, [state])
            e.concat(nfa)
            stack.push(e)
        elif char == '(':
            pass
        elif char == ')':
            pass
        elif char == '|':
            e2 = stack.pop()
            e1 = stack.pop()
            state = State()
            state.add_edge('epsilon', e1.head)
            state.add_edge('epsilon', e2.head)
            nfa = NFA(state)
            nfa.tail = e1.tail + e2.tail
            stack.push(nfa)
        else:
            state = State()
            state.dangling = [source]
            nfa = NFA(state)
            stack.push(nfa)
            # inplicit concat '.'
            ops.push('.')


def match(regex, source):

    pass

def main():
    test_set = [
            ('a', 'a'),
            ('e1e2', 'e1e2'),
            ('e1|e2', 'e1'),
            ('e1|e2', 'e2'),
            ('e?', 'e'),
            ('e?', ''),
            ('e*', ''),
            ('e*', 'e'),
            ('e*', 'ee'),
            ('e*', 'eee'),
            ('e+', 'e'),
            ('e+', 'ee'),
            ('e+', 'eee'),
        ]
    for pattern, string in test_set:
        print (re.findall(pattern, string))


if __name__ == '__main__':
    main()
