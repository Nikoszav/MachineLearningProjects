import numpy as np

def reluDerivative(x):
    x[x<=0] = 0.01
    x[x>0] = 1
    return x


def relu(x):
  return np.where(x > 0, x, x * 0.01)


    
def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # only difference

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivativeSigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))
