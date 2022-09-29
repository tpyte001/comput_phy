import numpy as np
   
def trapezoid(a=-1,b=1,N=100):
    #correct result, prints 1.57 = pi/2
    h = (b-a)/N
    sigma = h * (np.sum(np.array([np.sqrt(1-((a+i*h)**2)) for i in range(1,N)])))
    return h * (0.5 * np.sqrt(1.0 - (a**2.0)) + (0.5 * np.sqrt(1.0 - (b**2.0)))) + sigma

print(trapezoid())

def adap(i=1,a=-1,b=1,N=10):
    # index 1, a = lower bound, b = upper bound, h = delta
    # check against estimated error/numerical error
    # use np arrays
    epsilon = 1.0/3.0 * (I_next - I_prev)
    h = (a-b)/2
    i = 1
    while (np.abs(0) > delta_h):
                  # recalculation of new Ni and Hi
                  # calculate Ii using 1/2 I_{i-1} + 1 to Ni 
                  # calculate episolon error delta_h
                  
    
'''    
# print(integration_sin(i,a,v,N))
