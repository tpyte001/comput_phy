# brute force taylor series calculation
import numpy as np

def cen_dif_sin(x,h=0.1):
    # returns derivative via central difference method
    return (np.sin(x+h) - np.sin(x-h)) / (2 * h)


print(cen_dif_sin(np.pi/3))

def taylor_series_sin(x,h=0.1):
    # returns taylor series representation of sinx
    return np.sin(x) + cen_dif_sin(x)
    


    # temporary check
    print(cen_dif_sin(np.pi/3))

print(taylor_series_sin(np.pi/3,h=0.1))

