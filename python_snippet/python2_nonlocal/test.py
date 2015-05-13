#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

from nonlocals import *

def outer():
    var = 0
    @nonlocals('var')
    def inner():
        print (var)
        var = 1
        print (var)
    inner()

outer()

print ('---' * 10)

'''
How it works:

export_nonlocals changes all local variable references in a way so that they modified by other scopes by replacing LOAD_FAST and STORE_FAST codes that modify the given variables to LOAD_NAME and STORE_NAME, moving the variable reference to external names, and using bitwise NOT to change the compile flags. nonlocals works by changing LOAD_FAST and STORE_FAST codes that modify the given variables with LOAD_DEREF and STORE_DEREF and modifying outer's locals if export_nonlocals was used.

This is very hackish and plays with CPython internal implementation stuff that PyPy just happens to be compatible with. YOU WERE WARNED!!!
'''

@export_nonlocals('var')
def outer():
    var = 0
    @nonlocals('var')
    def inner():
        print (var)
        var = 1
        print (var)
    inner()
    print (var)

outer()
