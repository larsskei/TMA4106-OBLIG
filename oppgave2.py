import numpy as np

def f(x):
    return np.exp(x)

def derivate_f(x,h):
    return (f(x+h) - f(x-h)) / (2*h)

h = 0.00000001

print(derivate_f(1.5, h))
print(np.exp(1.5))