#!/bin/ruby -w
# -*- coding: utf-8 -*-

str = <<HERE + <<THERE + "World"
Hello
HERE
There
THERE

p str

p `ls`
# eq: %x[ls]
# Kernel.`(ls)
