#!/bin/ruby -w
# -*- coding: utf-8 -*-

a = [1, 2, 3]  # An array that holds threee Fixnum objects
b = [-10...0, 0..10, ]  # An array of two ranges; trailing commas are allowed
c = [ [1, 2], [3, 4], [5] ]  # An array of nested arrays
p a
p b
p c

words = %W[this is a test]  # same as: ['this', 'is', 'a', 'test']
open = %w| ( [ { |  # same as: ['(', '[', '{', '<']
white = %W(\s \t \r \n)  # same as: ["\s", "\t", "\n"]

=begin
same as %q and %Q can get a string, %w and %W can get a array
=end

empty = Array.new
nils = Array.new(3)  # [nil, nil, nil]
zeros = Array.new(4, 0)  # [0, 0, 0, 0]
copy = Array.new(nils)
count = Array.new(3) { |i| i + 1 } # [1, 2, 3]: elements computed from index

[1, 2, 3] + [4, 5]

['a', 'b', 'c', 'd', 'a'] - ['b', 'c', 'd']  #  ['a', 'a']

a = []
a << 1  # a is [1]
a << 2 << 3  # a is [1, 2, 3]
a << [4, 5, 6]  # a is [1, 2, 3, [4, 5, 6]]

a = [0] * 3  # [0, 0, 0]

a = [1, 1, 2, 2, 3, 3, 4]
b = [5, 5, 4, 4, 3, 3, 2]
a | b  # [1, 2, 3, 4, 5]
b | a  # [5, 4, 3, 2, 1]
a & b  # [2, 3, 4] 
b & a  # [4, 3, 2]
=begin
  ruby does not grantee the order of the resutl of | and &
=end
