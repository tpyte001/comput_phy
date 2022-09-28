# finite difference for second derivative
import numpy as np

x = np.pi/3
def finite_difference_two(x,h=0.01):
    return sin(x + h) - 2 * sin(x) + sin(x - h) / 2 * h 
    
