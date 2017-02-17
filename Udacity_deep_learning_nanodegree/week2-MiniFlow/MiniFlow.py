#!/usr/env python

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
    def __init__(self):
        Node.__init__(self)

    def forward(self, value=None):
        if(value is not None):
            self.value = value

class Add(Node):
    def __init__(self, x, y):
        Node.__init__(self, [x, y])

    def forward(self):
        pass


def toplogical_sort(feed_dict):
    input_nodes = [n for n in feed_dict.keys()]
    G = {}
    nodes = [n for n in input_nodes]
    while(len(nodes) > 0):
        n = nodes.pop(0)
        if(n not in G):
            G[n] = {'in': set(), 'out': set()}


