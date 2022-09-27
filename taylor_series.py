# taylor series to approximate order of error
# adapted integration (one step higher than brute force)
#central difference method
import numpy as np
import math as mt

def deriv_sin(x,h=0.01):
    return (np.sin(x+h) - np.sin(x-h)) / (2 * h)

def taylor_series_sin(x=np.pi/3,c=0):
    return (np.sin(x) + deriv_sin(x) * (x-c) + (deriv_sin(x) * (x-c) ** 2) / mt.factorial(2))

print(taylor_series_sin(np.pi/3,0))
    
    
x = np.pi/2
y = 0

for n in range(4):
    y = y + ((-1)**n * (x)**(2*n+1)) / np.math.factorial(2*n+1)
    
print(y)