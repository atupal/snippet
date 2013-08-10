#!/bin/ruby -w
# -*- coding: utf-8 -*-

s = "hello"


# the first index is begin of substring and the second index is the length of substring
p s[0, 2]  # he
p s[-1, 1]  # o

p s[2, 3]  # llo
# the first indexi is begin(include) of substring and the second indexi is end(include) of substring
p s[2..3]  # ll
p s[-3..-1]  # llo
