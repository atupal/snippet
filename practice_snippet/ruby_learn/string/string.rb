#!/bin/ruby -w
# -*- coding: utf-8 -*-

planet = "Earth"

p "Hello" + " " + planet

planet_number = 1

puts "Hello planet #{planet_number}"

greeting = "Hello"
greeting << " " << "World"
puts greeting

alphabet = "A"
alphabet << ?B
p alphabet
alphabet << 67
p alphabet
alphabet << 256  # erro in Ryby 1.8: codes must be >= 0 and < 256
p alphabet

p "p" * 3
a = 0
p "#{a=a+1}" * 3  # return "111", not "123"
