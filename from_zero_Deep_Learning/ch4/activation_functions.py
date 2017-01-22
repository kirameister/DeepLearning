#!/usr/bin/env python

import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return(np.array(x>0, dtype=np.int))


def sigmoid(x):
    return(1 / (1 + np.exp(-1)))


def relu(x):
    return(np.maximize(0,x))

