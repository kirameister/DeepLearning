#!/usr/env python

import numpy as np

class Node(object):
    def __init__(self, inbound_nodes=[]):
        # Nodes from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Nodes to which this Node passes values
        self.outbound_nodes = []
        # For each inbound Node here, add this Node as an outbound Node to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        # A calculated value
        self.value = None

    def forward(self):
        """
        Forward propagation.
        Compute the output value based on inbound_nodes and 
        store the results in self.value
        """
        pass

class Input(Node):
    # An Input node has no inbound nodes. 
    # so no need to pass anything to that Node instantiator. 
    def __init__(self):
        Node.__init__(self)

    # NOTE: Input node is the only node where the value 
    # may be passed to an argument to forward().
    # All other node implementation should get values 
    # of the previous node from self.inbound_nodes
    # Examle:
    #   val0 = self.inbound_nodes[0].value
    def forward(self, value=None):
        # Overwrite the value if it exists. 
        #if(value is not None):
        #    self.value = value
        pass

class Linear(Node):
    def __inint__(self, X, W, b):
        Node.__init__(self, [X, W, b])
        # NOTE: The weights and bias properties here are not
        # numbers, but rather reference to other nodes. 
        # The weight and bias values are stored within the
        # respective nodes. 

    def forward(self):
        """
        Set self.value to the value of the linear function output.
        """
        X = self.inbound_nodes[0].value
        W = self.inbound_nodes[1].value
        b = self.inbound_nodes[2].value
        self.value = np.dot(X, W) + b
        return(self.value)

class Add(Node):
    def __init__(self, x, y):
        Node.__init__(self, [x, y])

    def forward(self):
        self.value = self.inbound_nodes[0].value + self.inbound_nodes[1].value


def topological_sort(feed_dict):
    input_nodes = [n for n in feed_dict.keys()]
    G = {}
    nodes = [n for n in input_nodes]
    while(len(nodes) > 0):
        n = nodes.pop(0)
        if(n not in G):
            G[n] = {'in': set(), 'out': set()}

def forward_pass(output_node, sorted_nodes):
    """
    Performs a forward pass through a list of sorted nodes. 

    Argument: 
        `output_node`: The output node of the graph (no outgoing edges).
        `sorted_nodes`: a topologically sorted list of nodes. 

    returns the output node's value
    """
    for n in sorted_nodes:
        n.forward
    return(output_node.value)

def Sigmoid(Node):
    """
    Represents a node that performs the sigmoid activation function. 
    """
    def __init__(self, node):
        Node.__init__(self, [node])

    def _sigmoid(self, x):
        return(1. / (1. + np.exp(-x)))

    def forward(self):
        input_value = self.inbound_nodes[0].value
        self.value = self._sigmoid(input_value)

    def backward(self):
        self.gradients = {n: np.zeros_like(n.value) for n in self.inbound_nodes}
        for n in self.outbound_nodes:
            grad_cost = n.gradients[self]
            sigmoid = self.value
            self.gradients[self.inbound_nodes[0]] += sigmoid * (1 - sigmoid) * grad_cost
