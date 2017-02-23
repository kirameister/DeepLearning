"""
This script builds and runs a graph with miniflow.

There is no need to change anything to solve this quiz!

However, feel free to play with the network! Can you also
build a network that solves the equation below?

(x + y) + y
"""

import numpy as np
from MiniFlow import *

X = Input()
W = Input()
b = Input()

#f = Linear(X, W, b)
f = Linear(X)

X_ = np.array([[-1., -2.], [-1., -2.]])
Y_ = np.array([[2., -3], [2., -3]])
b_ = np.array([-3., -5])

feed_dict = {X: X_, Y: Y_, b: b_}

graph = topological_sort(feed_dict)
output = forward_pass(f, graph)

# NOTE: because topological_sort set the values for the `Input` nodes we could also access
# the value for x with x.value (same goes for y).
print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))

