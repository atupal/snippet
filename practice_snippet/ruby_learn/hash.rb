#!/bin/ruby -w
# -*- coding: utf-8 -*-

numbers = Hash.new
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

numbers = { "one" => 1, "two" => 2, "three" => 3 }

# normally Symbol can be efficail than "string", A symbol is a unchange and starts with ":" 
numbers = { :one => 1, :two => 2, :three => 3 }
# or just in ruby 1.9
numbers = { one: 1, two: 2, three: 3 }
