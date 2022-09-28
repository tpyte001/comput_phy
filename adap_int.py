 
def trapezoid():
    trapezoid_rule = np.sum(np.array([2*np.sqrt(1-(x**2)) for i in range(i,N)]))
    return ((b-a)/2) * np.sqrt(1-(a**2)) + np.sqrt(1-(b**2)) + trapezoid_rule

trapezoid

def adap(i=1,a=-1,b=1,N=10):
    import numpy as np
    # calculate f(x) = 2 * sqrt(1 - (x ** 2)) = pi
    # index 1, a = lower bound, b = upper bound, h = delta
    # check against estimated error/numerical error
    # use np arrays
    
    epsilon = 1.0/3.0 * (I_next - I_previous)
    #step1 calculate I_next
    h = (a-b)/2
    i = 1
    while (np.abs(0) > delta_h):
                  # recalculation of new Ni and Hi
                  # calculate Ii using 1/2 I_{i-1} + 1 to Ni 
                  # calculate episolon error delta_h
                  
    
    return ((b-a)/2) * (np.sin(a) + np.sin(b)) + trapezoid_rule

print(integration_sin(i,a,v,N))