#!/bin/env python2.7
# -*- coding: utf-8 -*-

funcs = {}

def fa():
  print 'I am fa'


def fb():
  print "I am fb"


def fc():
  print "I am fc"


names = ["fa", "fb", "fc"]
for name in names:
  funcs.setdefault(name, locals().get(name))

arg = "fb"

if arg in funcs.keys():
  funcs[arg]()
