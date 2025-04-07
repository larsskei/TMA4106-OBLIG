import numpy as np

def f(x):
    return np.exp(x)

def derivate_f(x,h):
    return (f(x - 2*h) - 8*f(x-h) + 8*f(x+h) - f(x + 2*h)) / (12*h)

print(derivate_f(1.5, 0.000001))
print(np.exp(1.5))