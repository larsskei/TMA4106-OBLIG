import numpy as np

def f(x):
    return np.exp(x)

def derivate_f(x,h):
    return (f(x+h) - f(x)) / h

print(derivate_f(1.5, 0.000000001))
print(np.exp(1.5))