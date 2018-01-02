#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import itertools

meta_char = ['*', '?', '+', '|', '(', ')', '.']
[SUCCEED, FAIL, SYNTAX_ERROR] = range(3)
debug = 0


class State(object):

    class _dict(dict):
        def __missing__(self, key):
            self[key] = []
            return self[key]

    cnt = 0

    def __init__(self, dangling=None):
        self._state_sets = self._dict()
        self.dangling = []
        if dangling:
            self.dangling = dangling
        State.cnt += 1
        self.idx = State.cnt

    def add_edge(self, char, states):
        for state in states:
            self._state_sets[char].append(state)

    def next(self, char):
        return self._state_sets[char]

    def empty(self):
        if self.dangling: return False
        for val in self._state_sets.values():
            if val: return False
        return True

    def __str__(self):
        return '%r'%self

    def __repr__(self):
        return '<state: %d>'%(self.idx)


class NFA(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = []
        if tail:
            self.tail = tail

    def concat(self, b_nfa):
        for state in self.tail:
            for char in state.dangling:
                state.add_edge(char, [b_nfa.head])
            state.dangling = []
        self.tail = []
        return self

    def match(self, source, findall=False):

        next_states = set()

        def add_state(state):
            for s in state.next('epsilon'):
                add_state(s)
            else:
                next_states.add(state)

        add_state(self.head)
        current_states = next_states
        next_states = set()

        def step_next_state(state, char):
            for s in state.next(char):
                add_state(s)

        def is_match(current_states):
            for state in current_states:
                if state.empty():
                    return SUCCEED

            return FAIL

        for pos in xrange(len(source)):
            char = source[pos]
            for state in current_states:
                step_next_state(state, char)
            current_states = next_states
            next_states = set()


            if findall:
                if is_match(current_states) == SUCCEED:
                    return SUCCEED, pos
                if not current_states:
                    return FAIL, pos

        if findall:
            return FAIL, pos

        return is_match(current_states)


    def findall(self, source):
        ret = []
        pos = 0
        while pos < len(source):
            sub = source[pos:]
            c, newpos = self.match(sub, findall=1)
            if c == SUCCEED:
                ret.append(source[pos:pos+newpos+1])
            pos += newpos+1

        return ret


def compile_postfix(postfix_arr):

    stack = []

    if debug:
        states = []

    for char in postfix_arr:

        state = State()  # indicate that every char map to a state

        if debug:
            states.append(state)

        if   char == '?':
            e = stack.pop()
            state.add_edge('epsilon', [e.head])
            state.dangling = ['epsilon']
            stack.append(NFA(state, [state]+e.tail))
        elif char == '*':
            e = stack.pop()
            state.add_edge('epsilon', [e.head])
            state.dangling = ['epsilon']
            nfa = NFA(state, [state])
            e.concat(nfa)
            stack.append(nfa)
        elif char == '+':
            e = stack.pop()
            state.add_edge('epsilon', [e.head])
            state.dangling = ['epsilon']
            nfa = NFA(state, [state])
            e.concat(nfa)
            e.tail = nfa.tail
            stack.append(e)
        elif char == '|':
            e2 = stack.pop()
            e1 = stack.pop()
            state.add_edge('epsilon', [e1.head, e2.head])
            stack.append(NFA(state, e1.tail+e2.tail))
        elif char == '.':
            e2 = stack.pop()
            e1 = stack.pop()
            e1.concat(e2)
            e1.tail = e2.tail
            stack.append(e1)
        else:
            state.dangling = [char]
            stack.append(NFA(state, [state]))

    assert(len(stack) == 1)
    nfa = stack[0].concat(NFA(State(), []))

    if debug:
        print '-' * 57
        print 'NFA info:'
        print 'start state : %d, match state : %d' % (nfa.head.idx, State.cnt)
        for state in states:
            print (state.idx), ':',
            for key, val in state._state_sets.items():
                for ns in val:
                    print '%s -> %d' % (key, ns.idx),
            print
        print '-' * 57

    return nfa


def infix2postfix(source):
    ret = []
    for i, j in zip(source[:-1], source[1:]):
        ret.append(i)
        if i != '(' and i != '|' and j not in ['+', '*', '?', ')', '|']:
            ret.append('.')
    ret.append(source[-1])

    higher_order_ops = {
            '.': ['.'],
            '|': ['.', '|'],
            }

    output = []
    ops = []

    if debug: print 'infix:', ''.join(ret)

    for c in ret:
        if c not in meta_char:
            output.append(c)
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops[-1] != '(':
                output.append(ops.pop())
            ops.pop()
        elif c in ['?', '+', '*']:
            output.append(c)
        else:
            while ops and ops[-1] in higher_order_ops[c]:
                output.append(ops.pop())
            ops.append(c)

    while ops:
        output.append(ops.pop())

    if debug:
        print 'postfix:', ''.join(output)

    return output


def compile(source):
    postfix_arr = infix2postfix(source)
    return compile_postfix(postfix_arr)

def match(pattern, source):
    regex = compile(pattern)
    return regex.match(source)

def findall(pattern, source):
    regex = compile(pattern)
    return regex.findall(source)

def test():

    tests = [
                ('abc', 'abc', SUCCEED),
                ('abc', 'xbc', FAIL),
                ('abc', 'axc', FAIL),
                ('abc', 'abx', FAIL),
                ('ab+bc', 'abc', FAIL),
                ('ab+bc', 'abq', FAIL),
                ('ab?bc', 'abc', SUCCEED),
                ('ab?bc', 'abbbbc', FAIL),
            ]

    for pattern, string, ret in tests:
        print ('%s %s -> %d %d'% (pattern, string, match(pattern, string), ret))

def main():
    tests = [
            ('a', 'a', SUCCEED),
            ('e1e2', 'e1e2', SUCCEED),
            ('e1|e2', 'e1', SUCCEED),
            ('e1|e2', 'e2', SUCCEED),
            ('e?', 'e', SUCCEED),
            ('e?', '', SUCCEED),
            ('e*', '', SUCCEED),
            ('e*', 'e', SUCCEED),
            ('e*', 'ee', SUCCEED),
            ('e*', 'eee', SUCCEED),
            ('e*', 'eeee', SUCCEED),
            ('e*', 'eeeee', SUCCEED),
            ('e+', 'e', SUCCEED),
            ('e+', 'ee', SUCCEED),
            ('e+', 'eee', SUCCEED),
            ('e+', 'eeee', SUCCEED),
            ('e+', 'eeeee', SUCCEED),
        ]
    for pattern, string, ret in tests:
        print ('%s %s -> %d %d'% (pattern, string, match(pattern, string), ret))

    print


if __name__ == '__main__':
    main()
    test()
    #debug = 1
    #print (match('ab+bc', 'abbccccccccccccccccccccccccccccc'))
    #print (findall('ab+bc', 'abbbcdefghiabbcdabbbbbbbbc'))
