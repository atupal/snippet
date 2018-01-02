#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import tensorflow as tf

node1 = tf.constant(3.0, dtype = tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)

session = tf.Session()
print(session.run([node1, node2]))

node3 = tf.add(node1, node2)

print(node3)

print(session.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print(session.run(adder_node, {a: 3, b: 4.5}))
print(session.run(adder_node, {a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3
print(session.run(add_and_triple, {a: 3, b: 4.5}))

W = tf.Variable([.3], dtype = tf.float32)
b = tf.Variable([-.3], dtype = tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x + b

init = tf.global_variables_initializer()
session.run(init)
print(session.run(linear_model, {x: [1, 2, 3, 4]}))

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(session.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
session.run([fixW, fixb])
print(session.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

session.run(init) # reset the values to incorrect defaults
for i in range(1000):
    session.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
print(session.run([W, b]))
